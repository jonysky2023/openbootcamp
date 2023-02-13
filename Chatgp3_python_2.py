import openai

openai.api_key = "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"
model_engine = "text-davinci-002"

prompt = "Que es chatGP3"

completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=2048, n=1, stop=None, temperature=0.5)

response = completions.choices[0].text

print(response)