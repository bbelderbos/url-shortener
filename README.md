# A simple URL shortener using Redis

In this repo I built a quick and simple URL shortener showing random vs deterministic url code (or slug) generation (I prefer the latter), storing the key (code), value (full URL) pairs in Redis. 

Lastly I used Typer and rich (`pip install typer[all]`) for a quick and nice command line interface to shorten and go to URLs. 

TODO: build a simple GUI as an alternative interface ...

## Redis setup

I used [Antonio Mele's Django 4 book](https://www.amazon.es/Django-Example-powerful-reliable-applications-ebook/dp/B09YS5NHX9/) (chapter 7 / page 324) to quickly spin up a Docker container for Redis, super convenient and just takes a few steps:

```
# pull the image
docker pull redis

# run in container
docker run -it --rm --name redis -p 6379:6379 redis

# play with redis-cli
docker exec -it redis bash

root@e29fa2376c66:/data# redis-cli
127.0.0.1:6379> set key value
OK
127.0.0.1:6379> get key
"value"
```
