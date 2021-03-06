# spaCy Model

This is an API service for `ModelSpacy` of `coeus`

## API Documentation
### `GET /heathcheck`
Request: `None`

Response: `'OK'` with HTTP Status `200`

### `POST /predict/sentences/count`
Request:
`"data"` is a string of text to process.
```json
{
  "data": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
}
```

Response:
`"result"` is a number represents amount of sentences in text.
```json
{
  "result": 1
}
```

### `POST /predict/sentences`
Request:
`"data"` is a string of text to process.
```json
{
  "data": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. hello i am new."
}
```

Response:
`"result"` is a array of text sentence.
```json
{
    "result": [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "hello i am new."
    ]
}
```

### `POST /predict/pos`
Request:
`"data"` is a string of text to process.
```json
{
  "data": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
}
```
Response:
`"result"` is an object which key is token and value is part of speech tag.
```json
{
  "result": {
    "word1": "NOUN",
    "word2": "VERB"
  }
}
```

### `POST /predict/noun-chunks-with-entity-type`
Request:
`"data"` is a string of text to process.
```json
{
  "data": "Thailand is a country in southeast Asia."
}
```
Response:
`"result"` is an array of noun chunks with its own entity type.
```json
{
    "result": [
        [
            "Thailand",
            "GPE"
        ],
        [
            "a country",
            ""
        ],
        [
            "southeast Asia",
            "LOC"
        ]
    ]
}
```

## Run
1. Copy file `.env.example` into `.env` and fill in all necessary values
2. Make sure you have Docker installed on your system and running
3. Build Docker image with a name of your choice if you haven't
```shell
docker build --tag spacy-api .
```
5. Spin up a server
```shell
docker run -d -p 5000:5000 --name spacy-api spacy-api
```
6. Try accessing [http://127.0.0.1:5000](http://127.0.0.1:5000) with a valid route