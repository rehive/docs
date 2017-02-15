# Accounts

## Balances

> User balance request


```shell
curl https://www.rehive.com/api/3/accounts/balance/
  -X POST
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
```

> User balance response

```json
{
    "status": "success",
    "data": {
        "balance": 1000,
        "account": "default",
        "currency": {
            "description": "Rand",
            "code": "ZAR",
            "symbol": "R",
            "unit": "rand",
            "divisibility": 2
        }
    }
}
```

Get the balance of either the current active currency or a specific currency/account.

### Endpoint

`https://www.rehive.com/api/3/accounts/balance/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`currency` | currency code | null | false
`account` | accound reference code | null | false

## Currencies

> User currencies list request

```shell
curl https://www.rehive.com/api/3/accounts/currencies/
  -X GET
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
```

> User currencies list response

```json
  {
    "status": "success",
    "data": [
        {
            "account": {
                "name": "default",
                "reference": "xxxxxxxxxx",
                "created": "2016-06-02T09:01:08.745000Z"
            },
            "balance": 1000,
            "token": {
                "code": "ZAR",
                "currency": {
                    "code": "ZAR",
                    "description": "Rand",
                    "symbol": "R",
                    "unit": "rand",
                    "divisibility": 2
                },
                "issuer": {
                    "company": {
                        "identifier": "rehive",
                        "name": "Rehive",
                        "description": "Wallets for everyone.",
                        "website": "http://www.rehive.com",
                        "logo": null
                    },
                    "identifier": null,
                    "metadata": {}
                },
                "divisibility": 2,
                "description": "South African Rand for Rehive.",
                "icon": null,
                "metadata": {},
                "created": "2016-05-24T14:11:26.228000Z",
                "updated": "2016-07-29T19:45:40.008208Z"
            },
            "status": "active"
        }
    ]
}
```

Get a list of currencies available to a user.

### Endpoint

`https://rehive.com/api/3/accounts/currencies/`

## Active Currency

> Request description

```shell
curl https://www.rehive.com/api/3/accounts/currency/
  -X GET
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
```

> Response description

```json
{
    "status": "success",
    "data": {
        "code": "ZAR",
        "currency": {
            "code": "ZAR",
            "description": "Rand",
            "symbol": "R",
            "unit": "rand",
            "divisibility": 2
        },
        "issuer": {
            "company": {
                "identifier": "rehive",
                "name": "Rehive",
                "description": "Wallets for everyone.",
                "website": "http://www.rehive.com",
                "logo": null
            },
            "identifier": null,
            "metadata": {}
        },
        "divisibility": 2,
        "description": "South African Rand for Rehive.",
        "icon": null,
        "metadata": {},
        "created": "2016-05-24T14:11:26.228000Z",
        "updated": "2016-07-29T19:45:40.008208Z"
    }
}
```

Get the details for the current active currency.

### Endpoint

`https://rehive.com/api/3/accounts/currency/`

## Set Currency

> Request description

```shell
curl https://www.rehive.com/api/3/accounts/currency/set/
  -X POST
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
  -d '{"currency": "ZAR",
       "account": "xxxxxxxxxx"}'
```

> Response description

```json
{
    "status": "success",
    "data": {
        "balance": 1000,
        "currency": {
            "description": "Rand",
            "code": "ZAR",
            "symbol": "R",
            "unit": "rand",
            "divisibility": 2
        },
        "account": {
            "reference": "xxxxxxxxxx",
            "created": "2016-06-02T09:01:08.745000Z",
            "name": "default"
        }
    }
}
```

Set the active currency for a user. Get the currency code and account reference from the currency list.

### Endpoint

`https://rehive.com/api/3/accounts/currency/set/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`currency` | currency code | null | true
`account` | accound reference code | null | true

## Bank Deposits

> Request description

```shell
curl https://www.rehive.com/api/3/accounts/deposits/bank/
  -X GET
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
```

> Response description

```json
{
    "status": "success",
    "data": [
        {
            "id": 53,
            "token": 1,
            "bank_account": {
                "id": 1,
                "name": "Rehive",
                "number": "xxxxxxxx",
                "type": "Cheque",
                "bank_name": "Barclays",
                "bank_code": "xxxx",
                "branch_code": "xxxxx",
                "swift": "",
                "iban": "",
                "bic": ""
            },
            "reference": "xxxxxxxxxx"
        }
    ]
}
```

Get the bank deposit details for the user's company.

### Endpoint

`https://rehive.com/api/3/accounts/deposits/bank/`
