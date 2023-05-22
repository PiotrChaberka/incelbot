import requests
from bs4 import BeautifulSoup
import random
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import re
import sys

# Set up the GPT-2 model and tokenizer
model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Scrape data from 4chan /b/ board
# If you want to edit it just change the url variable. It SHOULD work
url = 'https://boards.4chan.org/b/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
threads = soup.find_all('div', class_='thread')

sentences = []

# Extract sentences from each thread
for thread in threads:
    posts = thread.find_all('blockquote')
    for post in posts:
        text = post.get_text().strip()
        text = re.sub('>[^<]+', '', text)
        text = re.sub(r'[^\x00-\x7F]+', '', text)
        if text:
            sentences.append(text)

# Choose a random completion from the scraped sentences
completion = random.choice(sentences)

# Set the device to CPU or GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Generate completion using GPT-2 model
print("Write a sentence you want completed :)")
input_text = input("") + " " + completion
input_ids = tokenizer.encode(input_text, return_tensors='pt').to(device)
output = model.generate(input_ids, max_length=35, num_return_sequences=1)

# Decode the generated completion
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

# Print the generated completion
print("Generated completion:")
print(generated_text)

print("\n ")
print("press any key to quit the program :D")
a = input("")