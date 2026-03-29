import google.generativeai as genai

genai.configure(api_key="AIzaSyBH18rMD3jSYRQjYn8WYbvtlvN262AIN5k")

models = genai.list_models()

for m in models:
    if "generateContent" in m.supported_generation_methods:
        print(m.name)