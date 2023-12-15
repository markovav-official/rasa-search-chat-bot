# Conversational chat bot for searching using RASA

## Functionality

1. Search for images for example: find image of cat, show me picture of dogs, etc.
2. Search for videos for example: video with Earth, find video with funny cats, etc.
3. Search for answers for example: what is stock, who is Elon Musk, etc.
4. Translate text for example: translate hello to Spanish, translate how are you to Finnish, etc. *Supported languages: Russian, English, Spanish, Swedish, Finnish*
5. Get conversion rate between currencies
   for example: what is the conversion rate between USD and EUR, convert USD to RUB, etc.

## Author

- Name: Andrei Markov
- Email: `a.markov@innopolis.university`
- Group Number: B21-AAI-01

## Repository Structure

- `actions` - folder with custom actions
- `data` - folder with training data (nlu, stories, rules)
- `models` - folder with trained models (the model is already trained and saved in the repository)
- `results` - folder with results of benchmark
- `tests` - folder with tests
- `config.yml` - file with configuration of the model
- `credentials.yml` - file with credentials for connecting to services (this file is not in the repository, but there is `example.credentials.yml` file, which you can copy and fill with your credentials)
- `domain.yml` - file with domain (intents, entities, actions, slots, responses, etc.)
- `endpoints.yml` - file with endpoints (for example, for connecting to custom actions server)
- `graph.html` - image with graph of the model behavior

## Running the bot

- Install Python 3.8, 3.9 or 3.10
- Clone the repository: `git clone https://github.com/markovav-official/rasa-search-chat-bot.git`
- Install dependencies: `pip install -r requirements.txt`
- For running the bot with command line interface: `rasa shell` (but it will not support image and video search)
- For running the bot with web interface:
  - Copy `example.credentials.yml` to `credentials.yml` and fill it with your credentials
  - Run `rasa run actions` in one terminal (it will start the server with custom actions)
  - Run `rasa run` in another terminal (it will start the server with bot)
- For running the tests: `rasa test` (it will run tests from `tests` folder, and will save results to `results` folder)
- If you want to train the model: `rasa train` (it will train the model and save it to `models` folder, but it is not necessary, because the model is already trained and saved in the repository)
