from openai import OpenAI

client = OpenAI(api_key="")

def chatgpt_summarize(comment):
    prompt = "I want you to participate in my project Rate My Course where you have to summarize each review about the course in 3 words. Your 3 words serve a purpose to advise a new student if they should take this course. Here is the review that you have to summarize in 3 words:" + comment 
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
        )
    ans = completion.choices[0].message.content
    return ans 

