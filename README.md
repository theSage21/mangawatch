# MangaWatch

Notifies you on telegram about new chapters for manga that you've listed for watching.

1. Get a bot token from bofather on telegram.
2. Find your own user ID using userinfobot on telegram.
3. `cp example.json watch.json`
4. Edit `watch.json` with the info obtained in step 1 and 2.
5. Run the program with `python -m mangawatch`

I usually run it as a permanent service with docker.

```bash
docker build -t mangawatch .
docker run  -d -it --restart unless-stopped -v $PWD:/src mangawatch python -m mangawatch
```
