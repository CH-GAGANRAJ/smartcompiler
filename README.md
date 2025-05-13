# smartcompiler
## 🔍 Overview:
SmartCompiler is an intelligent Python code compiler built in Python that automatically detects syntax errors in source code, corrects them using Gemini 1.5 Flash, and executes the fixed code — all seamlessly from the command line.

## 🎯 Key Features:
  ✅ Lexing & Parsing using Python's built-in ast module
  
  🧠 AI-Powered Syntax Correction using Google’s Gemini API
  
  🛠️ Interpreter to run valid Python Abstract Syntax Trees (AST)
  
  💾 Automatically overwrites original files with corrected code if execution succeeds
  
  📂 Organizes test files in an examples/ directory for easy testing

## 📁 Project Structure:
![Screenshot 2025-05-13 152720](https://github.com/user-attachments/assets/70f0e6ca-5fcd-451d-b81f-ae2696268988)

## ⚙️ How It Works:
Run main.py with a file path:

bash
Copy
Edit
python main.py examples/hello.mylang
If syntax is valid → code is executed directly.

If there's a syntax error:

Code is passed to ai_editor.py

Gemini API fixes the code

If the fixed code runs successfully:

It is saved back to the original file

## 🤖 Tech Stack:
Language: Python 3

AI Engine: Gemini 1.5 Flash (via google.generativeai)

Modules Used: ast, tokenize, sys, os, openai/google.generativeai

## 💡 Future Improvements:
Add runtime error correction

Build a GUI using Streamlit

Track and show AI diff logs or explanations

Support for custom programming languages in future versions
