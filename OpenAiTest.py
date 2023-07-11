import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to HR of XYZ company for interview opportunity of full-time job?",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

'''
{
  "id": "cmpl-7RFZT5iSBzfXbsvOKjEqfwN0Wf2W0",
  "object": "text_completion",
  "created": 1686729067,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nSubject: Request for Interview Opportunity\n\nDear HR Team, \n\nI am writing to express my interest in a full-time position at XYZ Company. I recently came across your job posting online and believe I possess the necessary qualifications to excel in the role. \n\nI have a Bachelor's degree in accounting and three years of experience in accounting and financial analysis. I am highly organized, detail-oriented, and capable of managing multiple tasks with ease. In addition, I have an extensive knowledge of accounting principles and standards, as well as excellent problem-solving and communication skills. \n\nGiven my credentials, I am confident I would make a great addition to the team. I am eager to learn more and discuss how my experience can be leveraged in this role. \n\nI look forward to hearing from you, and thank you for your consideration.\n\nSincerely, \n[Your Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 208,
    "total_tokens": 208
  }
}
'''