import configparser
from pathlib import Path

from telethon import TelegramClient

KEYWORDS = ['https://t.me/']


def config_input(prompt=None):
    """Removes any extra quotes that might be added around values that will be added to a config file."""
    value = input(prompt).strip('\'').strip('"')
    return value


config_file = Path('config.ini')
config = configparser.ConfigParser()

if not config_file.exists():
    config.add_section('AUTH')
    config.add_section('DEFAULTS')
    print('\n\nFirst use detected.\n\n', 
          'Enter your auth details below. (You\'ll only need to do this once)\n',
          'If you don\'t already have them, you can visit this link to get them: https://my.telegram.org/auth', 
          sep='\n', end='\n\n')
    api_id = config_input('api_id: ')
    api_hash = config_input('api_hash: ')
    config['AUTH']['api_id'] = api_id
    config['AUTH']['api_hash'] = api_hash
    config.set('DEFAULTS', 'chat_id', '')
    with config_file.open('w') as file:
        config.write(file)
else:
    config.read(config_file)

API_ID = config['AUTH']['API_ID']
API_HASH = config['AUTH']['API_HASH'] 
CHAT_ID = config_input('Chat or Group ID (where you or your bot has Admin access): ') if not config['DEFAULTS']['chat_id'] else config['DEFAULTS']['chat_id']

client = TelegramClient('anon', API_ID, API_HASH)


async def main():
    messages_deleted = False
    async for message in client.iter_messages(int(CHAT_ID)):
        if message.text:
            if any(keyword in message.text for keyword in KEYWORDS):
                print('Deleting message: ', message.text)
                await message.delete()
                messages_deleted = True
    if not messages_deleted:
        print('No messages deleted. Nothing to delete.')

with client:
    client.loop.run_until_complete(main())