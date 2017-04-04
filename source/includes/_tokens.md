# Tokens

The tokens endpoints provide some basic access to managing user and admin tokens.
The ability to create infinite lifespan tokens as well as viewing active tokens and 
deleting unused tokens.

<aside class="notice">
    For security purposes Rehive does not store the authentication tokens.
</aside>

## List Tokens

> List tokens request

```shell
curl https://www.rehive.com/api/3/auth/tokens/
  -X GET
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
```

> List user tokens response

```json
{
  "status": "success",
  "data": [
    {
      "token_key": "{token_key}",
      "expires": null
    },
    {
      "token_key": "{token_key}",
      "expires": "2001-01-01T01:01:01.000001Z"
    },
    {
      "token_key": "{token_key}",
      "expires": "2001-01-01T01:01:01.000002Z"
    }
  ]
}
```

Retrieve a list of the current active tokens for the authenticated user. 
Notice that only the `token_key` is exposed here and not the whole token, in case
user tokens need to be managed on the client side.

## Create Token

> Create token request

```shell
curl https://www.rehive.com/api/3/auth/tokens/
  -X POST
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
  -D "{"password": "joe1234"}"
```

> Create token response

```json
{
  "status": "success",
  "data": {
    "token": "{token}",
    "user": {
      "identifier": "00000000-0000-0000-0000-000000000000",
      "email": "joe@rehive.com",
      "mobile_number": "+00000000000",
      "first_name": "Joe",
      "last_name": "Soap",
      "company": "rehive",
      "profile": null,
      "language": "en"
    }
  }
}
```

Creating a token here will remove the expiration time on the token, thus giving it an infinite lifespan.

### Endpoint

`https://rehive.com/api/3/auth/tokens/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`password` | password | null | true

## Delete Token

> Delete token request

```shell
curl https://www.rehive.com/api/3/auth/tokens/{token_key}
  -X DELETE
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
```

> Delete token response

```json
{
  "status": "success"
}
```

### Endpoint

`https://rehive.com/api/3/auth/tokens/{token_key}`

