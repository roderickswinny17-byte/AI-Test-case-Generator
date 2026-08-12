from prompt import SYSTEM_PROMPT
import ollama
def read_requirement(file_path):
    try:
    
        with open(file_path,"r",encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error :: {file_path} not found")
        return None
    except Exception as e:
        print(f"Unexpeccted Error :: {e}")
        return None

def generate_test_cases(requirement):
    reponse = ollama.chat(
        model = "qwen3",
        messages = [ 
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": requirement
        }
            
        ]
    )
    return reponse ["message"]["content"]