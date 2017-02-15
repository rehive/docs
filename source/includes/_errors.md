# Errors

> Basic error response:

```json
{
    "status": "error",
    "message": "Error message."
}
```

> Multiple errors response:

```json
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

Rehive errors result in an API response message (formatted in JSON) as well as an HTTP response code.

The Rehive API uses the following error codes:

Error Code | Meaning
---------- | -------
400 | Bad Request
401 | Unauthorized
403 | Forbidden
404 | Not Found
405 | Method Not Allowed
406 | Not Acceptable
410 | Gone
429 | Too Many Requests
500 | Internal Server Error
503 | Service Unavailable
