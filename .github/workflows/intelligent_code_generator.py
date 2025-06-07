import openai
import time
import traceback

openai.api_key = 'YOUR_OPENAI_API_KEY'

def get_code_from_prompt(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            {"role": "system", "content": "You are a helpful Python coding assistant. Only generate code, no explanations."},
            {"role": "user", "content": f"Generate an efficient Python program for: {prompt}"}
        ],
        temperature=0.3
    )
    return response['choices'][0]['message']['content']

def execute_code(code):
    start = time.time()
    local_vars = {}
    try:
        exec(code, {}, local_vars)
        end = time.time()
        return True, local_vars, end - start, None
    except Exception as e:
        return False, None, None, traceback.format_exc()

def code_optimizer(prompt, max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt}:\n{'-'*30}")
        code = get_code_from_prompt(prompt)
        print("Generated Code:\n", code)

        success, output, exec_time, error = execute_code(code)

        if success:
            print("\n✅ Execution Status: Success")
            print(f"⏱️ Execution Time: {exec_time:.4f} seconds")
            print("🖥️ Output Variables:\n", output)
            print("\n🎯 Efficient and working code generated.\n")
            break
        else:
            print("\n❌ Execution Status: Failed")
            print("🔧 Error Traceback:\n", error)

if __name__ == "__main__":
    user_prompt = input("📌 Describe the program you want: ")
    code_optimizer(user_prompt)

