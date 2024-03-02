# Discord Basic Modmail 

# About Basic Modmail 
This project is a Discord bot that performs modmail tasks. It listens to messages in a server and sends notifications to a designated moderation channel. It also allows moderators to reply to messages and send direct messages to users.

# Installation
1. Clone the repository: `git clone https://github.com/w3nabil/discord-modmail.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Create a `.env` file in the root directory and add the following variables:
    - `BOT_TOKEN`: Your Discord bot token
4. Update the `config.json` file with the necessary server and channel IDs.
5. Run the bot: `python app.py`

# Usage
- Once the bot is running, it will listen to messages in the specified server and channel.
- When a message is received, it will check if it's a direct message or from the server.
- If it's a direct message, it will send a notification to the moderation channel with the message content and author details.
- If it's a message from the server, it will check if the message starts with the command "reply".
  - If it does, and the message is from the moderation channel and sent by a moderator, it will send a direct message to the specified user with the provided reply.
  - It will also send a confirmation message in the moderation channel with the reply details.
- The bot will continue running until terminated manually.

# Contributing
- Fork the repository.
- Create a new branch: `git checkout -b my-feature`
- Make your changes and commit them: `git commit -m "Add my feature"`
- Push to the branch: `git push origin my-feature`
- Submit a pull request.

# License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
