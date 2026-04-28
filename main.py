from typing import Never


import asyncio
import logging
import a2s
from discord.abc import PrivateChannel
import config
from discord import Intents, Client


intents = Intents.default()

client = Client(intents=intents)


async def update_playercounts() -> Never:
    player_counts = {}
    while True:
        for server in config.SERVERS:
            try:
                if server[0] not in player_counts.keys():
                    player_counts[server[0]] = -1
                name = server[0]
                info = a2s.info(
                    address=(server[1], server[2]),
                    timeout=3,
                    encoding="utf-8",
                )
                current = info.player_count
                max = info.max_players
                if current == player_counts[server[0]]:
                    continue
                else:
                    player_counts[server[0]] = current
                channel = client.get_channel(server[3])
                if type(channel) in [None, PrivateChannel]:
                    raise TypeError(
                        f"Channel type {type(channel)} is invalid. Please make sure the channel is a GuildChannel."
                    )

                await channel.edit(name=f"{name}: {current}/{max}")
                logging.info(f"Updated channel {channel.name}")
            except Exception as e:
                logging.error(e)
        await asyncio.sleep(config.WAIT)


@client.event
async def on_ready() -> None:
    logging.info(f"logged in as {client.user}")
    await update_playercounts()


client.run(config.BOT_TOKEN)
