---
title: API Reference

language_tabs:
  - shell
  - javascript

includes:
  - authentication
  - tokens
  - users
  - transactions
  - accounts
  - company
  - permissions
  - administration
  - beta

search: true
---

# Introduction

```javascript
SDK Initialization


window.rehive = new Rehive({apiVersion: 3});
```

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

## Errors

> Basic error response:

```shell
{
    "status": "error",
    "message": "Error message."
}
```

```javascript
{
    "message": "Error message."
}
```

> Multiple errors response:

```shell
 {
    "status": "error",
    "message": "First error message, Second error message",
    "data": {
        "field_name1": [
            "First error message."
        ],
        "field_name2": [
            "Second error message."
        ]
    }
}
```

```javascript
 {
    "field_name1": [
        "First error message."
    ],
    "field_name2": [
        "Second error message."
    ]
}
```

Rehive errors return an API response message (formatted in JSON) as well as a standard HTTP response code.

The JSON error respone generally includes a `message` string. If an error occurred on a specific attribute or
key they will be outputted in the `data` object.