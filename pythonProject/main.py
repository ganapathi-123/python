# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from openai import OpenAI

client = OpenAI(api_key= "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")

def chat_with_gpt(prompt):
    response =  client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role" : "user" , "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__" :
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            break
        response = chat_with_gpt(user_input)
        print("chatbot: ", response)
