from google.colab import ai
memory = []

rules = [
"Be useful"
]

while True:
    user = input("You: ")
    r = ai.generate_text(f"rules: {rules}, memory: {memory}, Prompt: {user}")
    memory.append(f"User: {user}, you: {r}")
    
    print("AI: ", r)
