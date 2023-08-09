# Discord Bot - Sherpuk

Shlepuk is a Discord bot designed to assist and track interactions between mentors (sherpas) and mentees (sherpaling) in your Discord server. It enables tracking and logging of support sessions, helping you keep organized records of time spent, descriptions, and more.

## Features

- **Support Session Logging**: The bot allows mentors to log support sessions with their mentees. Each session includes information like the time spent, description, and relevant details.

- **Google Sheets Integration**: Shlepuk integrates with Google Sheets to record and store session data. This provides an organized and easily accessible way to manage and review past sessions.

- **Automated Record Keeping**: The bot automates the process of updating Google Sheets with session data, reducing the need for manual data entry.

## Getting Started

To use Shlepuk in your Discord server, follow these steps:

1. Clone this repository to your local machine or your preferred server.

2. Install the required dependencies using `pip`:

   ```
   pip install -r requirements.txt
   ```

   The required dependencies for Shlepuk are listed in the `requirements.txt` file:

   ```
   pandas~=2.0.3
   requests~=2.31.0
   gspread~=5.10.0
   ```

3. Create a Discord bot in the [Discord Developer Portal](https://discord.com/developers/applications) and copy its token.

4. Replace `'YOUR_BOT_TOKEN'` in `bot.py` with your actual bot token.

5. Update `csv_file_link` in `bot.py` with the publicly accessible Google Drive link to your CSV file for data storage.

6. Make sure to have the `xxx-xxx.json` service account JSON file for Google Sheets integration. Replace the existing filename in `writeToDrive.py` if needed.

7. Run the bot using the following command:

   ```
   python bot.py
   ```

## Usage

- To log a support session, use the command:

  ```
  /drive <time_spend> <description>
  ```

  For example:

  ```
  /drive [1 hour] [Helped with basics]
  ```

  ![image](https://github.com/OfficalOffical/discordBot/assets/18538179/a55c35b1-797c-4b27-a37a-cfe0a4ac9e29)


- To greet the bot, use the command:

  ```
  !hello <your_input>
  ```


## Contributing

Contributions to Shlepuk are welcome! If you find a bug or want to suggest improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
