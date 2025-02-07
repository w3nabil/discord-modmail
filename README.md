# Discord Mod Mail Bot

A Discord bot built with Python and `discord.py`, designed for handling direct messages, and enabling moderators to reply to users through a dedicated channel.

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8.x-green?style=for-the-badge&logo=python" alt="Python Version 3.8.x">
  <img src="https://img.shields.io/badge/DiscordPy-2.3.2-green?style=for-the-badge&logo=python" alt="DiscordPy Version 2.3.2">
  <img src="https://img.shields.io/github/license/w3nabil/discord-modmail?style=for-the-badge&logo=github&label=License" alt="License">
</div>

## Features

- Listens for direct messages and forwards them to a moderation channel.
- Allows moderators to reply to users from a specific channel.

## Installation

### Prerequisites
- Python 3.8+
- `discord.py` library
- `python-dotenv` for environment variable management
- `json` for configuration management

### Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/w3nabil/discord-modmail.git
   cd discord-modmail
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Rename `.env.EXAMPLE` to `.env` in the project root and add the following:
     ```ini
     BOT_TOKEN=your_discord_bot_token
     ```
     - [Learn more about Discord Bot Token](https://discord.com/developers)

4. **Configure `config.json`:**
   - Modify the `config.json` file in the project root and structure it like this:
     ```json
     {
       "server_id": 123456789012345678, // This is your SERVER ID
       "mod_channel_id": 123456789012345678, // This is the channel where dms messages will be forwarded
       "mod_role_id": 123456789012345678 // Moderator Role, so that they can send messages
     }
     ```

5. **Run the bot:**
   ```sh
   python bot.py
   ```

## Usage

- **Listening to DMs:** Any DM sent to the bot will be forwarded to the moderation channel.
- **Moderator Replies:** Mods can reply using:
  ```sh
  reply <user_id> <message>
  ```
- **Bot Presence:** The bot will display "Listening to People!" as its status.

## Error Handling
- If `config.json` is missing or has incorrect values, the bot will print an error message and exit.
- If the bot lacks permissions to message a user, it will notify the moderator in the channel.

## Limitations 
- Uses lower python and discord.py version (Maybe it will be outdated soon).
- Things need to be monitored manually, for example, you need to find the text. 
- Not good for servers which planning to serve 20+ users using my modmail.
- Poor Error handling, and I did not effort much for this project. 
- Can not send direct images, use image cdn instead with vanity.  

## License
This project is licensed under the MIT License. See [LICENSE](License) for details.

## Contact
For questions, feedback, or collaboration opportunities, feel free to reach out at w3nabil@gmail.com.

---



