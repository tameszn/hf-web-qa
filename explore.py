import requests 
response=requests.get("https://agents-course-unit4-scoring.hf.space/questions")
questions=response.json()

print(questions[0].keys())


for i, question in enumerate(questions, start=1):
    print(i, question["question"])

