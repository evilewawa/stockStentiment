import google.generativeai as genai
genAiApiKey = # hidden
genai.configure(api_key=genAiApiKey)
model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("What stock is this post talking about '$HIVE go boom to the moon'. answer only with the ticker symbol")
# print(response.text)

def askGemini(prompt):
    response = model.generate_content(prompt)
    return response.text
