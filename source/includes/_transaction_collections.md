# Transaction Collections

Transaction collections are a way to group multiple transactions under a single identifier. Every transaction is part of a single transaction collection. A transaction collection can contain multiple different transactions, with different types, subtypes and accounts. In simple terms transaction collections are used to “organize” transactions.

## List Transactions Collections

> User transaction collections request

```shell
curl https://api.rehive.com/3/transaction-collections/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
```

```python
rehive.transaction_collections.get(
    filters=filters
)
```

> User transaction collections response

```shell
 {
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": "00000000-0000-0000-0000-000000000000",
                "transactions": [
                    "id": "00000000-0000-0000-0000-000000000000",
                    "parent": null,
                    "partner": null,
                    "inferred": false,
                    "tx_type": "credit",
                    "subtype": null,
                    "note": "",
                    "metadata": {},
                    "status": "Pending",
                    "reference": "",
                    "amount": 500,
                    "balance": 0,
                    "account": "0000000000",
                    "label": "Credit",
                    "company": "rehive",
                    "total_amount":100,
                    "currency": {
                        "description": "Rand",
                        "code": "ZAR",
                        "symbol": "R",
                        "unit": "rand",
                        "divisibility": 2
                    },
                    "created": 1496135465218,
                    "updated": 1496135465287
                ],
                "created": 1496135465218,
                "updated": 1496135465287
            }
        ]
    }
}
```

```javascript
```

```python
 [
    {
        "id": "00000000-0000-0000-0000-000000000000",
        "transactions": [
            "id": "00000000-0000-0000-0000-000000000000",
            "parent": null,
            "partner": null,
            "inferred": false,
            "tx_type": "credit",
            "subtype": null,
            "note": "",
            "metadata": {},
            "status": "Pending",
            "reference": "",
            "amount": 500,
            "balance": 0,
            "account": "0000000000",
            "label": "Credit",
            "company": "rehive",
            "total_amount":100,
            "currency": {
                "description": "Rand",
                "code": "ZAR",
                "symbol": "R",
                "unit": "rand",
                "divisibility": 2
            },
            "created": 1496135465218,
            "updated": 1496135465287
        ],
        "created": 1496135465218,
        "updated": 1496135465287
    }
]
```

Get a a user's transaction collections list.

#### Filtering

Field | Type
--- | ---
`id` | string

#### Endpoint

`https://api.rehive.com/3/transaction-collections/`


## Create Transaction Collection

> User create transaction collections request

```shell
curl https://api.rehive.com/3/transaction-collections/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"transactions": [
        {"amount": 500, "currency": "ZAR", "tx_type": "credit"},
        {"amount": 500, "currency": "ZAR", "tx_type": "credit"}]}'
```

```javascript
```

```python
```

> User create transaction collections response

```shell
{
    "status": "success",
    "data": {
        "id": "00000000-0000-0000-0000-000000000000",
        "transactions": [
            {
                "id": "00000000-0000-0000-0000-000000000000",
                "parent": null,
                "partner": null,
                "tx_type": "credit",
                "subtype": null,
                "note": "",
                "metadata": {},
                "status": "Pending",
                "reference": null,
                "amount": 500,
                "total_amount": 500,
                "balance": 0,
                "account": "0000000000",
                "label": "Credit",
                "company": "rehive",
                "currency": {
                    "description": "Rand",
                    "code": "ZAR",
                    "symbol": "R",
                    "unit": "rand",
                    "divisibility": 2
                },
                "messages": [],
                "created": 1476691969394,
                "updated": 1496135465287
            },
            {
                "id": "00000000-0000-0000-0000-000000000000",
                "parent": null,
                "partner": null,
                "tx_type": "credit",
                "subtype": null,
                "note": "",
                "metadata": {},
                "status": "Pending",
                "reference": null,
                "amount": 500,
                "total_amount": 500,
                "balance": 0,
                "account": "0000000000",
                "label": "Credit",
                "company": "rehive",
                "currency": {
                    "description": "Rand",
                    "code": "ZAR",
                    "symbol": "R",
                    "unit": "rand",
                    "divisibility": 2
                },
                "messages": [],
                "created": 1476691969394,
                "updated": 1496135465287
            }
        ],
        "created": 1476691969394,
        "updated": 1496135465287
    }
}
```

```javascript
```

```python
```

Create a transaction collection with one or more transactions.

#### Endpoint

`https://api.rehive.com/3/transaction-collections/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`transactions` | object | null


## Retrieve Transaction Collection

> Retrieve transaction collection request

```shell
curl https://api.rehive.com/3/transaction-collections/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
```

```python
rehive.transaction_collections.get(
   "{id}"
)
```

> Retrieve transaction collection response

```shell
{
    "status": "success",
    "data":  {
        "id": "00000000-0000-0000-0000-000000000000",
        "transactions": [
            "id": "00000000-0000-0000-0000-000000000000",
            "parent": null,
            "partner": null,
            "inferred": false,
            "tx_type": "credit",
            "subtype": null,
            "note": "",
            "metadata": {},
            "status": "Pending",
            "reference": "",
            "amount": 500,
            "balance": 0,
            "account": "0000000000",
            "label": "Credit",
            "company": "rehive",
            "total_amount":100,
            "currency": {
                "description": "Rand",
                "code": "ZAR",
                "symbol": "R",
                "unit": "rand",
                "divisibility": 2
            },
            "created": 1496135465218,
            "updated": 1496135465287
        ],
        "created": 1496135465218,
        "updated": 1496135465287
    }
}
```

```javascript
```

```python
{
    "id": "00000000-0000-0000-0000-000000000000",
    "transactions": [
        "id": "00000000-0000-0000-0000-000000000000",
        "parent": null,
        "partner": null,
        "inferred": false,
        "tx_type": "credit",
        "subtype": null,
        "note": "",
        "metadata": {},
        "status": "Pending",
        "reference": "",
        "amount": 500,
        "balance": 0,
        "account": "0000000000",
        "label": "Credit",
        "company": "rehive",
        "total_amount":100,
        "currency": {
            "description": "Rand",
            "code": "ZAR",
            "symbol": "R",
            "unit": "rand",
            "divisibility": 2
        },
        "created": 1496135465218,
        "updated": 1496135465287
    ],
    "created": 1496135465218,
    "updated": 1496135465287
}
```

Get transaction details for a spcific transaction collection.

#### Endpoint

`https://api.rehive.com/3/transaction-collections/{id}/`


