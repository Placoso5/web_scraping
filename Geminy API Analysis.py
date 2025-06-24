from google import genai
from google.genai import types
import pandas as pd
import time

#Retrieve API key as undisclosed string and put it in place
file_object = open("Geminy API Key.txt", "r")
key = file_object.read()
print(key)
file_object.close()
client = genai.Client(api_key=key)

#Cargamos el csv original como dataframe
df = pd.read_csv("analysis_summary.csv", sep = ",")

#Definimos listas para poner lo que vayamos sacando
summary_list = []
topics_list = []



for i in range(10):
    summary_response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="Don't use any commas. Make sure your answer is won't cause any issues when written on a .csv file."),
        contents="Generate a concise, one-sentence summary of the following article's main point:" + df.iloc[i,3]
    )
    print(summary_response.text)
    summary_list.append(summary_response.text)
    time.sleep(10)


    tags_response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="Don't use any commas. Make sure your answer is won't cause any issues when written on a .csv file."),
        contents="Identify and separate by parentheses 3-5 primary topics or keywords from the text of the following article:" + df.iloc[i,3]
    )
    print(tags_response.text)
    topics_list.append(tags_response.text)
    time.sleep(10)


#Agregamos las respuestas como columnas
df['Summary'] = summary_list
df['Topics'] = topics_list
# Fill missing values por si acaso
df.fillna("NA") 

df.to_csv('finished_sumary.csv', index=True)

