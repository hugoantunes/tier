#  ShorterURL

Simple API to make your URLs shorter

## Dependencies:
[redis](http://redis.io/download#installation)


## How To:

### Installation:
```
make setup
make test
```

### Use:
```
make run
```


#### Short an URL
```
curl -i -H "Content-Type: application/json" -X POST -d '{"url":"http://google.com"}' http://localhost:5000/url
```

```
# response
{
  "original": "http://google.com",
  "short": "b'2e32ee40-baaa-52e8-8227-a4ced6c95d14'"
}

```

####
```
# access
curl -i  http://localhost:5000/<short>
```
