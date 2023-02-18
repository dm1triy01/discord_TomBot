# V2.0
Working with mysql database. 

### Deploy Tom-Bot with webui:
1. Edit docker-compose.yml
```yaml
version: "3"
services:
  tom_bot:
    environment:
      TOM_DB_URL: PASTE_YOUR_DB_URL_HERE
      TOM_DB_USERNAME: PASTE_YOUR_DB_USERNAME_HERE
      TOM_DB_PASSWORD: PASTE_YOUR_DB_PASSWORD_HERE
      
      TOM_BOT_TOKEN: PASTE_YOUR_BOT_TOKEN_HERE
      TOM_BOT_OWNER_ID: PASTE_YOUR_DISCORD_ID_HERE
    build: bot
    volumes:
      - /srv/bot/config:/root/bot/config
      - /srv/bot/logs:/root/bot/logs
      - /srv/bot/files:/root/bot/files
    container_name: "tom_bot"

  tom_webui:
    environment: []
    build: webui
    volumes: []
    ports:
      - "80:80"
    container_name: "tom_webui"
```


2. Build and run containers: \
```docker-compose up -d```