# discord-a2s-player-count
A simple discord bot that updates a channel name with the current player count of an A2S protocol supported server. This was made for DayZ servers but should work for others as well as long as the `python-a2s` library can connect to them.

# Setup
1. Create a new Discord bot and get the token.
2. Add the bot to your server, and make sure it has permission to manage the channels you want to update. I like to create a voice channels and disallow connection to them for all users.
3. `cp config.py.example config.py` and fill out the variables. Alternatively template the file with whatever deployment orchestration system you use.

An example config file for a server can be seen here:

```python
# Format is server_name, ip, port, channel_id
SERVERS = [("Namalsk", "158.51.123.148", 2303, 1433272621092307004)]
WAIT = 120
BOT_TOKEN = "redacted"
```

You may run into rate limiting if you are updating too many channels too frequently. Feel free to mess around with the values or add aditional waits in between servers.

## Running Manually
1. `pip install -r requirements.txt` to install the dependencies. I recommend using a virtual environment as most distros no longer support globally installing pip packages.
2. `python main.py`

## Using Docker
1. `docker build . --tag discord-a2s-player-count:latest`
2. `docker run -d discord-a2s-player-count:latest` to run in background or `docker run -it discord-a2s-player-count:latest` to run in current terminal.

# Missing Features
1. Players in queue.

# Issues
Feel free to open an issue or a PR to fix or improve the project.
