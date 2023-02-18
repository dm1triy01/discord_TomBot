# V2.0
Working with mysql database. 

### Deploy Tom-Bot with webui:
1. #### Edit docker-compose.yml
```yaml
version: "3"
services:
  tom_bot:
    container_name: "tom_bot"
    networks:
      - tomnet
    depends_on:
      - tom_database
    environment:
      TOM_DB_URL: postgresql://example/tom_bot
#      TOM_DB_USERNAME: admin
#      TOM_DB_PASSWORD: Tom123456
#      TOM_BOT_TOKEN:
#      TOM_BOT_OWNER_ID:
    build: bot
    volumes:
      - /srv/bot/config:/root/bot/config
      - /srv/bot/logs:/root/bot/logs
      - /srv/bot/files:/root/bot/files

  tom_database:
    image: postgres:13
    container_name: "tom_db"
    networks:
      - tomnet
    environment:
      - POSTGRES_USER=tom
      - POSTGRES_PASSWORD=tom123456
      - POSTGRES_DB=tom
    volumes:
      - /srv/postgresql:/var/lib/postgresql:z
      - /srv/postgresql/data:/var/lib/postgresql/data:z

#  tom_webui:
#    container_name: "tom_webui"
#    environment: []
#    build: webui
#    volumes: []
#    ports:
#      - "80:80"

networks:
  tomnet:
    driver: bridge
```

2. #### Create /srv/bot/...
```
mkdir -p /srv/bot/config \
      /srv/bot/logs \
      /srv/bot/files \
      /srv/postgresql \
      /srv/postgresql/data 
```

3. #### Create and edit /srv/bot/config/cfg.py
```python
# kv
token_id = 'TOKEN_HERE'  # bot token
owner_id = 123456  # your id (for use pm of bot)

# Systems paths
ffmpeg = "/usr/bin/ffmpeg"
```

4. #### Build and run containers:
```docker-compose up -d```