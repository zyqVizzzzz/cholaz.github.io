import openai
openai.api_key = "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"

def get_completion(prompt, model = "gpt-3.5-turbo"):
  message = [{"role": "user", "content": prompt}]
  response = openai.ChatCompletion.create(
    model=model,
    message=message,
    temperature=0,
  )
  return response['choices'][0]['message']['content']

text = f"""
You should be able to: brush your teeth
"""
prompt = get_completion(text)
print(prompt)