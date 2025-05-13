import tokenize
from io import BytesIO

def tokenize_code(code):
    res = []
    g = tokenize.tokenize(BytesIO(code.encode('utf-8')).readline)
    for toknum,tokval,_,_,_ in g:
        if toknum==tokenize.ENDMARKER:
            break
        elif toknum in (tokenize.ENCODING,tokenize.NL,tokenize.NEWLINE):
            continue
        else:
            res.append((tokenize.tok_name[toknum],tokval))
    return res

sample_code = '''
x = 10
def greet():
    print("Hello")
'''
a=tokenize_code(sample_code)
print(a)
