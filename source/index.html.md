---
title: API Reference

language_tabs:
  - shell

includes:
  - authentication
  - tokens
  - users
  - transactions
  - accounts
  - company
  - administration
  - errors

search: true
---

# Introduction

> API Endpoint

```
https://rehive.com/api/3/
```

The Rehive API is the core interface for communicating with Rehive. The API is 
organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) 
with predictable resource oriented URLs. Standard HTTP verbs, codes and authentication 
methods are used alongside JSON to ensure ease of implementation.

JSON is returned by all API responses. API errors will result in a JSON response 
as well as a corresponding HTTP response code. For more on errors take a look at [errors](/#errors).

## Browsable API

To ensure the API is easily explorable Rehive has implemented a browsable API. 
In addition to ease of navigation, you can experiment with different request 
formats and methods straight from within your browser:

[Browsable API](https://rehive.com/api/3/)

<aside class="notice">
It is important to remember that the browsable API uses cookie based sessions 
for authentication and therefore differs from the documented method of 
authentication. See <a href="/#authorization">Authentication</a> for 3rd party authentication.
</aside>

## Idempotent Requests

> Idempotent Request

```shell
curl {url}
  -X GET
  -H "Idempotency-Key: {key}"
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

The Rehive API supports idempotent requests for ensuring the same operations never occur twice.

To perform an idempotent request, attach a unique key to any `POST`, `PUT` or `PATCH` request made to the API: via the `Idempotency-Key: {key}` header.

Requests made with the same key will allows return the same response (As long as the request has the same HTTP method and URL path). The keys (and their associated saved responses) expire after 24 hours.

<aside class="notice">
Idempotent requests will not work for anonymous users and/or any endpoints found under <a href="/#authorization">Authentication</a> (eg. URL paths beginning with `/api/3/auth/`)
</aside>