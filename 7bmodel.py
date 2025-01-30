import ollama

def chat_with_model(model_name, messages):
    """
    Send a list of messages (conversation history) to the model and get a response.
    """
    response = ollama.chat(model=model_name, messages=messages)
    return response['message']['content']

# Main function for user interaction
def main():
    model_name = 'deepseek-r1:7b'
    print(f"Chat system using model: {model_name}")
    print("Press Ctrl+C to exit the chat.\n")

    # Initialize the conversation history
    conversation_history = []

    try:
        while True:
            # Get user input
            user_message = input("You: ")

            # Add the user's message to the conversation history
            conversation_history.append({'role': 'user', 'content': user_message})

            # Generate a response while maintaining context
            try:
                response_content = chat_with_model(model_name, conversation_history)
                # Add the model's response to the conversation history
                conversation_history.append({'role': 'assistant', 'content': response_content})

                # Display the model's response
                print(f"Model: {response_content}\n")
            except Exception as e:
                print(f"An error occurred: {e}\n")
    except KeyboardInterrupt:
        print("\nExiting the chat. Goodbye!")

# Run the chat system
if __name__ == "__main__":
    main()
