from openai import OpenAI

# Initialize the client pointing to your local Ollama instance
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama'  # Required by the SDK, but ignored by Ollama
)

# Call the standard Chat Completions endpoint
response = client.chat.completions.create(
    model='gemma4:e2b',  # Match the exact model name pulled via Ollama
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain the meaning of name atharv"}
    ],
    temperature=0.7,
    stream=True  # Enable streaming responses
)

# Print the model's text response
# print(response.choices[0].message.content)
for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
