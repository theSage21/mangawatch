# MangaWatch

Notifies you on telegram about new chapters for manga that you've listed for watching.

Create a `watch.json` file after looking at `example.json` file and then run `python -m mangawatch`. To run as a service:

```bash
docker build -t mangawatch .
docker run  -d -it --restart unless-stopped -v $PWD:/src mangawatch python -m mangawatch
```
