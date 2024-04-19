def chat(philo, sentence):    

    import random
    import json
    from conversationalBot import chat
    import torch

    from model import NeuralNet
    from nltk_utils import bag_of_words, tokenize

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open('intents.json', 'r') as json_data:
        intents = json.load(json_data)

    FILE = "data.pth"
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    philoChoice = philo
    print("philo choice is ", philoChoice)
    switcher = {
        0: "Aurelius",
        1: "Socrates",
        2: "Shakespeare",
        3: "Angelou",
    }
    bot_name = switcher.get(philoChoice)
    # print("Let's chat! (type 'quit' to exit)")
    while True:
        isEnded = False
        # sentence = "do you use credit cards?"
        # sentence = input("You: ")
        sentence = sentence
        if sentence == "quit":
            break

        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)
        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        # It started as > 75
        if prob.item() > 0.75:
            print(tag, "prob is", prob.item())
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    return(random.choice(intent['responses'][philoChoice]))
                    print(f"{bot_name}: {random.choice(intent['responses'][philoChoice])}")
                    if intent['tag'] == "goodbye":
                        isEnded = True
        else:
            print("goto other conversational bot")
            return("WENT TO FUCKING CHATBOT")
            return(chat(sentence, bot_name))
            print(chat(sentence, bot_name))
        if isEnded:
            break