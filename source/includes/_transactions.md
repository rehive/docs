# Transactions

Transaction currency values are always inputted/outputted in their lowest currency unit. For most currencies this will be the cents values, so a $ 1.00 transaction will output an amount of 100.

<aside class="notice">
Transactions are run as asynchronous processes within Rehive, so the latest state of the transaction will not necessarily be available immediately after a request has been completed. To get the latest transaction details you will have to make a follow up request using its `tx_code`.
</aside>

## List Transactions

> User transactions request

```shell
curl https://www.rehive.com/api/3/transactions/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> User transactions response

```json
 {
    "status": "success",
    "data": {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "tx_code": "000000000000000000000",
                "tx_type": "transfer",
                "subtype": null,
                "external": false,
                "note": "",
                "metadata": {},
                "external_response": {},
                "status": "Complete",
                "reference": "sally@rehive.com",
                "amount": -500,
                "fee": 0,
                "balance": 1000,
                "label": "Transfer",
                "account": "default",
                "company": "rehive",
                "currency": {
                    "description": "Rand",
                    "code": "ZAR",
                    "symbol": "R",
                    "unit": "rand",
                    "divisibility": 2
                },
                "created": 1474399284065,
                "updated": 1474399285570
            },
            {
                "tx_code": "000000000000000000000",
                "tx_type": "transfer",
                "subtype": null,
                "external": false,
                "note": "",
                "metadata": {},
                "external_response": {},
                "status": "Complete",
                "reference": "sally@rehive.com",
                "amount": -500,
                "fee": 0,
                "balance": 1500,
                "label": "Transfer",
                "account": "default",
                "company": "rehive",
                "currency": {
                    "description": "Rand",
                    "code": "ZAR",
                    "symbol": "R",
                    "unit": "rand",
                    "divisibility": 2
                },
                "created": 1474399284065,
                "updated": 1474399285570
            }
        ]
    }
}
```

Get a a user's transaction list.

### Pagination

The list is paginated by default and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

### Filtering

The transactions listing offers filtering on the `tx_code`, `tx_type`, `subtype`, `status`, `created` and `metadata` fields. This is done through URL parameters in the request URL:

`/api/3/transactions/?tx_type=transfer`

There is a special format for fitering on metadata (ie. `metadata__{field_name}`):

`/api/3/transactions/?metadata__type=test`

### Sorting

Sorting of the transactions listing can be done on all the "filtering" fields mentioned above via an `orderby` parameter in the request URL:

`/api/3/transactions/?orderby=tx_type`

### Endpoint

`https://rehive.com/api/3/transactions/`

## Total Transactions

> User total transactions request

```shell
curl https://www.rehive.com/api/3/transactions/totals/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> User total transactions response

```json
{
    "status": "success",
    "data": {
        "amount": 1000,
        "fees": 0,
        "count": 2,
        "currency": "ZAR"
    }
}
```

Get a user's total transaction details. This is a summary of transaction details like: amount totals, fee totals, and the total number of transactions.

### Filtering

The transactions listing offers filtering on the `tx_code`, `tx_type`, `subtype`, `status`, `created` and `metadata` fields. This is done through URL parameters in the request URL:

`/api/3/transactions/?tx_type=transfer`

There is a special format for fitering on metadata (ie. `metadata__{field_name}`):

`/api/3/transactions/?metadata__type=test`

### Sorting

Sorting of the transactions listing can be done on all the "filtering" fields mentioned above via an `orderby` parameter in the request URL:

`/api/3/transactions/?orderby=tx_type`

### Endpoint

`https://rehive.com/api/3/transactions/totals/`

## Retrieve Transaction

> Retrieve transaction request

```shell
curl https://www.rehive.com/api/3/transactions/{tx_code}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve transaction response

```json
{
    "status": "success",
    "data": {
        "tx_code": "000000000000000000000",
        "tx_type": "transfer",
        "subtype": null,
        "external": false,
        "note": "",
        "metadata": {},
        "external_response": {},
        "status": "Complete",
        "reference": "sally@rehive.com",
        "amount": -500,
        "fee": 0,
        "balance": 1000,
        "label": "Transfer",
        "account": "default",
        "company": "rehive",
        "currency": {
            "description": "Rand",
            "code": "ZAR",
            "symbol": "R",
            "unit": "rand",
            "divisibility": 2
        },
        "messages": [
            {
                "level": "info",
                "message": "Info message.",
                "created": 1493729659821
            }
        ],
        "created": 1474399284065,
        "updated": 1474399285570
    }
}
```

Get transaction details for a spcific transactions.

### Endpoint

`https://rehive.com/api/3/transactions/{tx_code}/`

## Create Transfer

> User transfer request

```shell
curl https://www.rehive.com/api/3/transactions/transfer/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"amount": 500,
       "reference": "sally@rehive.com"}'
```

> User transfer response

```json
{
    "status": "success",
    "data": {
        "tx_code": "00000000000000000000",
        "metadata": {}
    }
}
```

Create a transfer transaction. This will transfer currency from one user to another. If the recipient reference does not exist as a user in Rehive and the reference is an email address or mobile number then an invitation message will be sent to the recipient informing them thay have an unclaimed transaction.

### Endpoint

`https://rehive.com/api/3/transactions/transfer/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`amount` | amount | 0 | true
`reference` | email, mobile number, unique identifier | null | true
`subtype` | a custom defined subtype | null | false
`account` | account reference code | null | false
`note` | user's note or message | blank | false
`metadata` | custom metadata | {} | false

<aside class="notice">
Bear in mind that the <code>amount</code> should always be in the lowest currency unit available (ie, cents).
</aside>

<aside class="notice">
<code>subtype</code>s can be set in the admin dashboard by an admin user. A blank <code>subtype</code> can be sent without errors, but if a subtype is sent in the request it must match an existing <code>subtype</code> and it's related <code>tx_type</code> in Rehive.
</aside>

## Create Deposit

> User deposit request

```shell
curl https://www.rehive.com/api/3/transactions/deposit/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"amount": 500}'
```

> User deposit response

```json
{
    "status": "success",
    "data": {
        "tx_code": "00000000000000000000",
        "metadata": {}
    }
}
```

Create a deposit transaction.

### Endpoint

`https://rehive.com/api/3/transactions/deposit/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`amount` | amount | 0 | true
`reference` | optional deposit reference | blank | false
`subtype` | a custom defined subtype | null | false
`account` | account reference code | null | false
`note` | user's note or message | blank | false
`metadata` | custom metadata | {} | false

## Create Withdraw

> User withdraw request

```shell
curl https://www.rehive.com/api/3/transactions/withdraw/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"amount": 500}'
```

> User withdraw response

```json
{
    "status": "success",
    "data": {
        "tx_code": "00000000000000000000",
        "metadata": {}
    }
}
```

Create a withdraw transaction.

### Endpoint

`https://rehive.com/api/3/transactions/withdraw/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`amount` | amount | 0 | true
`reference` | optional withdraw reference | blank | false
`subtype` | a custom defined subtype | null | false
`account` | account reference code | null | false
`note` | user's note or message | blank | false
`metadata` | custom metadata | {} | false