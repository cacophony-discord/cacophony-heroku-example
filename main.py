#!/usr/bin/env python3
import os

from cacophony.app import CacophonyApplication

def main():
    """Launch the bot with plugins."""
    plugins = ['reverse', 'chattymarkov']

    bot = CacophonyApplication(
        discord_token=os.environ['CACOPHONY_DISCORD_TOKEN'],
        name='cacophony',
        database=os.environ.get('CACOPHONY_DATABASE', 'sqlite://'),
        plugins=plugins)
    bot.run()

if __name__ == "__main__":
    main()
