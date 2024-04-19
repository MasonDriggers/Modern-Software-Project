Ripped code off from here
https://img.youtube.com/vi/RpWeNzfSUHw/hqdefault.jpg)](https://www.youtube.com/watch?v=RpWeNzfSUHw&list=PLqnslRFeH2UrFW4AUgn-eY37qOAWQpJyg

## What is This?
This project is an implementation of a chatbot using Marcus Aurelius, William Shakespeare, Socrates, and Maya Angelou quotes. The chatbot leverages natural language processing and machine learning to simulate a conversation with a philosopher. It is a slightly more advanced implementation of the Eliza chatbot, as it doesn't require exact matches on inputs.

## Installation

### Create an environment
Whatever you prefer (e.g. `conda` or `venv`)
```console
mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

### Activate it
Mac / Linux:
```console
. venv/bin/activate
```
Windows:
```console
venv\Scripts\activate
```
### Install PyTorch and dependencies

For Installation of PyTorch see [official website](https://pytorch.org/).

You also need `nltk`:
 ```console
pip install nltk
 ```
pip install torch  # Follow the official PyTorch website for the correct command

If you get an error during the first run, you also need to install `nltk.tokenize.punkt`:
Run this once in your terminal:
 ```console
$ python
>>> import nltk
>>> nltk.download('punkt')
```

## Usage
Run
```console
python train.py
```
This will dump `data.pth` file. And then run
```console
python chat.py
```
## Customize
Have a look at [intents.json](intents.json). You can customize it according to your own use case. Just define a new `tag`, possible `patterns`, and possible `responses` for the chatbot. You have to re-run the training whenever this file is modified.
```console
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": [
        "Hi",
        "Hey",
        "How are you",
        "Is anyone there?",
        "Hello",
        "Good day"
      ],
      "responses": [
        "Hey :-)",
        "Hello, thanks for visiting",
        "Hi there, what can I do for you?",
        "Hi there, how can I help?"
      ]
    },
    ...
  ]
}
```

## Git History
You can generate the Git history using the following command:
git log > git_history

## Contributions by Team

We currently have a functional UI that displays all poets and a functional chatbot for each poet. As of this time, only Socrates has been fully integrated with the model. We plan to implement the model with the remaining poets.

### Frontend Team (Esther and Kellen)

The frontend team worked on:

- **User Interface (UI):** Created an intuitive and user-friendly interface for the chatbot.
- **Chat Window:** Designed a responsive chat window for seamless interaction with the bot.
- **Design Elements:** Implemented visual design elements such as colors, fonts, and icons to enhance the user experience.
- **Integration:** Coordinated with the backend team to integrate the frontend UI with the backend API for a smooth and efficient communication flow.

### Backend Team (Austin and Mason)

The backend team worked on:

- **Natural Language Processing (NLP):** Implemented natural language processing using NLTK and PyTorch to handle user input and generate responses.
- **Model Training:** Trained and optimized machine learning models for understanding user input and providing appropriate responses.
- **Data Management:** Managed training data, including `intents.json`, and ensured data quality and accuracy for better model performance.
- **API Development:** Created RESTful APIs for frontend-backend communication and data exchange.
