import parser
from interpreter import interpret
from ai_edit import edit
import sys
import ast

def load_code(file_path):
    with open(file_path, "r") as f:
        return f.read()

def write_code(file_path, code):
    with open(file_path, "w") as f:
        f.write(code)
def try_parse_and_run(code: str):
    try:
        tree = parser.parse_code(code)
        interpreter = interpret()
        interpreter.interpret(tree)
    except SyntaxError as e:
        print("❌ Syntax error detected! Attempting to fix using AI...\n")
        fixed_code = edit(code)

        if not fixed_code:
            print("❌ AI could not fix the code.")
            return

        print("✅ Fixed Code:\n")
        print(fixed_code)
        print("\n▶️ Running corrected code:\n")

        try:
            #print(fixed_code[10:-3])
            tree = parser.parse_code(fixed_code[10:-3])
            interpreter = interpret()
            interpreter.interpret(tree)
            write_code(file_path,fixed_code[10:-3])
        except Exception as e:
            print("❌ Failed to run corrected code:", e)

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename.py>")
        return
    global file_path
    file_path = sys.argv[1]
    code = load_code(file_path)
    #print(code)
    try_parse_and_run(code)

if __name__ == "__main__":
    main()
