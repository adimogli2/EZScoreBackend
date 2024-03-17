import dropbox
import openai
from datetime import datetime

# Set your API keys
openai.api_key = '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'
dbx = dropbox.Dropbox('sl.Bxgxh77OMNJz17mrUZq3Y4QkLy5RMD2LLGP8cvpJWEbp6eQr1Ud_RMHK71VK1wMocpc_VP7etB_yBQZqbktzwM0JU3DK6f5AGvhaAiPflugEiaBgAEhJ8seTBs3PDU7zi87RbfHgitsf7-S8dQroubk')

# Paragraph to be graded
paragraph = "The swing set was there. It was old.  The wind blew. There were shadows.  School ended."

# Rubric for grading
rubric = "Rubric: Strong sensory details, figurative language, and word choice (4 pts), Some descriptive elements and clear grammar (3 pts), Limited description or grammatical errors (2 pts), Lacks description and clarity (1 pt)"

# Combining paragraph and rubric into one prompt
prompt = f"Grade this paragraph on the following rubric: {paragraph} {rubric}"

# Sending the prompt to the OpenAI API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

# Accessing and printing the response
openai_response = response.choices[0].message['content']
# print("OpenAI response:", openai_response)

# Construct the file content
file_content = f"Prompt:\n{prompt}\n\nResponse:\n{openai_response}"

# Dropbox API endpoint for uploading files
upload_endpoint = "/2/files/upload"

# Set the desired filename (replace with your preference)
# filename = "/Tests/response.txt"

current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

# Set the desired filename with the current time
filename = f"/Tests/{current_time}_openai_response.txt"

# Perform the upload
try:
  with dbx.files_upload(file_content.encode('utf-8'), filename, mode=dropbox.files.WriteMode('add')) as result:
    print("File uploaded successfully:", result.name)
except Exception as e:
  #print("Upload failed:", e)
  print()