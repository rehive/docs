# Accounts

## List Accounts

> User list accounts request

```shell
curl https://www.rehive.com/api/3/accounts/
  -X GET
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
```

> User list accounts response

```json
{
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "name": "default",
                "reference": "0000000000",
                "balances": [
                    {
                        "balance": 10000,
                        "currency": {
                            "code": "XBT",
                            "description": "bitcoin",
                            "symbol": "฿",
                            "unit": "bitcoin",
                            "divisibility": 8
                        },
                        "active": true
                    }
                ],
                "created": 1464858068745,
                "updated": 1464858068745
            }
        ]
    }
}
```

Get a list of accounts belonging to a user.

### Endpoint

`https://rehive.com/api/3/accounts/`

## Retrieve Account

> User retrieve account request

```shell
curl https://www.rehive.com/api/3/accounts/{reference}/
  -X GET
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
```

> User retrieve account response

```json
{
    "status": "success",
    "data": {
        "name": "default",
        "reference": "0000000000",
        "balances": [
            {
                "balance": 10000,
                "currency": {
                    "code": "XBT",
                    "description": "bitcoin",
                    "symbol": "฿",
                    "unit": "bitcoin",
                    "divisibility": 8
                },
                "active": true
            }
        ],
        "created": 1464858068745,
        "updated": 1464858068745
    }
}
```

Retrieve an account belonging to a user.

### Endpoint

`https://rehive.com/api/3/accounts/{reference}/`

## List Account Currencies

> User list account currencies request

```shell
curl https://www.rehive.com/api/3/accounts/{reference}/currencies/
  -X GET
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
```

> User list account currencies response

```json
{
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "balance": 10000,
                "currency": {
                    "code": "XBT",
                    "description": "bitcoin",
                    "symbol": "฿",
                    "unit": "bitcoin",
                    "divisibility": 8
                },
                "active": true
            }
        ]
    }
}
```

Get a list of currencies for an account belonging to a user.

### Endpoint

`https://rehive.com/api/3/accounts/{reference}/currencies/`

## Retrieve Account Currency

> User retrieve account currency request

```shell
curl https://www.rehive.com/api/3/accounts/{reference}/currencies/{code}
  -X GET
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
```

> User retrieve account currency response

```json
{
    "status": "success",
    "data": {
        "balance": 10000,
        "currency": {
            "code": "XBT",
            "description": "bitcoin",
            "symbol": "฿",
            "unit": "bitcoin",
            "divisibility": 8
        },
        "active": true
    }
}
```

Retrieve an account's currency belonging to a user.

### Endpoint

`https://rehive.com/api/3/accounts/{reference}/currencies/{code}`

## Update Account Currency

> User retrieve account currency request

```shell
curl https://www.rehive.com/api/3/accounts/{reference}/currencies/{code}
  -X PUT
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
  -d '{"active": true}'
```

> User retrieve account currency response

```json
{
    "status": "success",
    "data": {
        "balance": 10000,
        "currency": {
            "code": "XBT",
            "description": "bitcoin",
            "symbol": "฿",
            "unit": "bitcoin",
            "divisibility": 8
        },
        "active": true
    }
}
```

Update the active status of an account currency. Activating an account's currency will result in that currency getting used by default for all transactions if no other account/currency is specified.

### Endpoint

`https://rehive.com/api/3/accounts/{reference}/currencies/{code}`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`active` | is active currency | false | false
