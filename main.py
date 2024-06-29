import google.generativeai as genai
from openai import OpenAI


import os
import streamlit as st

client = OpenAI(
    api_key= os.environ['OPENAI_API_KEY'],
)


genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def story_ai(msg,sysprompt):
  story_response = client.chat.completions.create(
      model="gpt-4o",
      messages=[{
          "role": "system",
          "content":sysprompt

      },
       {
          "role": "user",
          "content": msg
      }],

      max_tokens=300

  )
  # print(story_response)
  story = story_response.choices[0].message.content
  return story



def art_ai(msg):
  art_response = client.images.generate(
      model="dall-e-3",
      prompt=msg,
      size="1024x1024",
      n=1,
      quality='hd'
  )

  art = art_response.data[0].url
  return art

def design_ai(msg):
  design_model = genai.GenerativeModel('gemini-1.5-flash')
  design = design_model.generate_content([f"""
    craft a fitting prompt for an AI image generator
    to generate a most fitting cover art for this story:
    {msg}
  """])

  return design.text


def storybook_ai(msg,sysprompt):
  story = story_ai(msg,sysprompt)
  design = design_ai(story)
  art = art_ai(design)
  st.image(art)
  st.write(story)

sysprompt = """
you area bestselling author.
    you will take in a user's requests and create a 100 word short story.
    The story should be suitable for mature ages.
    """

msg = "write a story about wizards in wizard schools"
storybook_ai(msg,sysprompt)