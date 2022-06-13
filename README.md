# Message Delete Bot

## Get Started
0. Install your pip requirements to your Python environemnt. You can do this by running:
```cmd
pip install -r requirements.txt
```
1. Enter the desired `KEYWORDS` that should appear in the messages to be deleted. You can find this variable on line 6 in the `main.py` file. For example:
```python
# This will delete any message that contains a telegram sharing link with the t.me format.
KEYWORDS = ['https://t.me/']

# This would delete any message that contains the adjacent letters of 'h' and 'i', for example: hippo, hipotenuse, hi, etc.
KEYWORDS = ['hi']

# This would delete any messages that contain either of them:
KEYWORDS = ['https://t.me/', 'hi']
``` 
2. Run the script: `python main.py`
3. Get your `API_ID` and `API_HASH` from [this link](https://my.telegram.org/auth). If you need help finding them, follow the items below:
    1. Login by entering your phone number then entering the code it sends you. The code is sent in the telegram app connected to that phone number.
    2. Click on the "API development tools" link.
    3. Copy your api_id and api_hash and paste them in their respective variables in the input when first running the script ***OR*** in the `config.ini` file that's generated after the first time they're entered in.
4. Enter the `CHAT_ID` of the chat you wish to delete messages in the prompt that appears when running the script ***OR*** you can set a default chat in the `config.ini` file generated after the first time you run the script. You can get this (if you don't have it already) by adding the IDBOt (Username: @myidbot) to the group and entering the command `/getgroupid@myidbot`. ***YOU MUST HAVE ADMIN PRIVLEDGES IN THIS GROUP / CHANNEL / CHAT TO DELETE MESSAGES.***
5. If it's your first time running the script it, it will ask you to login. Follow the instructions it provides to run the script and it will generate a file that looks something like `anon.session` in this project's base directory (where requirements.txt and what not is). This is just so you don't have to login every single time you run the script.