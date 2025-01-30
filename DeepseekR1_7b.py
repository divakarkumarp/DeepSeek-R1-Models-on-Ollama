import ollama

response = ollama.chat(model='deepseek-r1:7b', messages=[
    {
        'role': 'user',
        'content': 'Explain the concept of recursion in programming.',
    },
])

print(response['message']['content'])