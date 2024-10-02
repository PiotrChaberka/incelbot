GPT-2 Text Generation with Web Scraping

This project is a text generation script using the GPT-2 model, combined with a basic web scraping component to gather data from the /b/ board of 4chan. It utilizes the scraped content as input to generate new text completions using GPT-2.
Features

    Web Scraping: The script scrapes threads from the /b/ board on 4chan to collect random sentences.
    GPT-2 Model Integration: It uses the Hugging Face implementation of the GPT-2 model for text generation.
    User Input Completion: The script takes a user-provided sentence, appends a random scraped sentence, and generates a continuation using the GPT-2 model.
    CUDA Support: Automatically utilizes GPU if available, otherwise defaults to CPU.

Requirements

To run this script, you'll need the following libraries:

    torch
    transformers
    requests
    beautifulsoup4


Code Walkthrough:

    Web Scraping:
        The script starts by sending a request to the 4chan /b/ board and parses the HTML using BeautifulSoup.
        It extracts and cleans up sentences from the posts in each thread.

    Text Generation:
        The user is prompted to provide an initial sentence.
        The script randomly selects a sentence from the scraped data and appends it to the input text.
        GPT-2 generates a continuation, which is printed as output.

    Device Configuration:
        The script automatically checks for CUDA (GPU) availability and sets the device accordingly.