# Discord Bot

## First create .env file or change code manually as you want
```
you need to put host url in https://discord.com/developers/applications/yourid/oauth2/general
```
# steps
## using quart, discord, and other dependencies helps communication between bot and dashboard
first, install packages by running:
```
pip install -r requirements.txt
```

```
then, put theses environment variables for your secrets
BOT_TOKEN = BOTTOKEN
DISCORD_CLIENT_ID = DISCORD_CLIENT_ID
DISCORD_CLIENT_SECRET = DISCORD_CLIENT_SECRET
SECRET_KEY = YOUR SECRET KEY
```
and lastly run
```
prisma db push
```
make sure install uvicorn or something else to excute your web dashbaord and start launch.py for bot
( pushing big update for comments guide and start using HTTP requests and database for bot dashboard )
enjoy :)
oh and any errors or something went wrong don't forget to dm me