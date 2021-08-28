# model-api-template

This is a template for model API wrapper. To make it easier to wrap around any model and deploy model into an API server.

## Run
1. Copy file `.env.example` into `.env` and fill in all necessary values
2. Make sure you have Docker installed on your system and running
3. Build Docker image with a name of your choice if you haven't
```shell
docker build --tag model-api .
```
5. Spin up a server
```shell
docker run -d -p 5000:5000 --name model-api-server model-api
```
6. Try accessing [http://127.0.0.1:5000](http://127.0.0.1:5000) with a valid route