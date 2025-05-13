import google.generativeai as genai

gemini_url='https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=GEMINI_API_KEY'
gemini_api='AIzaSyAAOtkSLsnZAV8Wf2RTfB3N5rDcY0T0CLs'
genai.configure(api_key=gemini_api)
model = genai.GenerativeModel("gemini-2.0-flash")
code='''
def add
    return x+y'''
def edit(code):
    prompt = f"""
    You are an expert Python developer.
    The following code contains syntax errors. Please fix them and return only the corrected code.The result should only contain code because it will be directly written in python file.
    
    Code:
    {code}"""
    res = model.generate_content(prompt)
    return res.text
edit(code)