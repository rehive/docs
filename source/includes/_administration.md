# Administration

Rehive includes a set of admin-only endpoints that can make working with users and their transactions extremely easy.

## List Transactions

> Admin transactions request

```shell
curl https://www.rehive.com/api/3/admin/transactions/
  -X GET
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
```

> Admin transactions response

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
                "status": "Complete",
                "external": false,
                "note": "",
                "metadata": {},
                "external_response": {},
                "amount": 500,
                "fee": 0,
                "from_balance": 1500,
                "to_balance": 500,
                "label": "Transfer",
                "currency": {
                    "description": "Rand",
                    "code": "ZAR",
                    "symbol": "R",
                    "unit": "rand",
                    "divisibility": 2
                },
                "from_account": "default",
                "to_account": "default",
                "from_reference": "joe@rehive.com",
                "to_reference": "sally@rehive.com",
                "created": 1487066686668,
                "updated": 1487066694343
            },
            {
                "tx_code": "000000000000000000000",
                "tx_type": "transfer",
                "subtype": null,
                "status": "Complete",
                "external": false,
                "note": "",
                "metadata": {},
                "external_response": {},
                "amount": 500,
                "fee": 0,
                "from_balance": 1000,
                "to_balance": 1000,
                "label": "Transfer",
                "currency": {
                    "description": "Rand",
                    "code": "ZAR",
                    "symbol": "R",
                    "unit": "rand",
                    "divisibility": 2
                },
                "from_account": "default",
                "to_account": "default",
                "from_reference": "joe@rehive.com",
                "to_reference": "sally@rehive.com",
                "created": 1487066686668,
                "updated": 1487066694343
            }
        ]
    }
}
```

Get a company's transaction list.

### Pagination

The list is paginated by default and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

### Filtering

The transactions listing offers filtering on the `tx_code`, `tx_type`, `subtype`, `status`, `created` and `metadata` fields. This is done through URL parameters in the request URL:

`/api/3/admin/transactions/?tx_type=transfer`

There is a special format for fitering on metadata (ie. `metadata__{field_name}`):

`/api/3/admin/transactions/?metadata__type=test`

### Sorting

Sorting of the transactions listing can be done on all the "filtering" fields mentioned above via an `orderby` parameter in the request URL:

`/api/3/admin/transactions/?orderby=tx_type`

### Endpoint

`https://rehive.com/api/3/admin/transactions/`

## Total Transactions

> Admin total transactions request

```shell
curl https://www.rehive.com/api/3/admin/transactions/totals/
  -X GET
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
```

> Admin total transactions response

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

Get a company's total transaction details. This is a summary of transaction details like: amount totals, fee totals, and the total number of transactions.

### Filtering

The transactions listing offers filtering on the `tx_code`, `tx_type`, `subtype`, `status`, `created` and `metadata` fields. This is done through URL parameters in the request URL:

`/api/3/admin/transactions/?tx_type=transfer`

There is a special format for fitering on metadata (ie. `metadata__{field_name}`):

`/api/3/admin/transactions/?metadata__type=test`

### Sorting

Sorting of the transactions listing can be done on all the "filtering" fields mentioned above via an `orderby` parameter in the request URL:

`/api/3/transactions/?orderby=tx_type`

### Endpoint

`https://rehive.com/api/3/admin/transactions/totals/`

## Retrieve Transaction

> Retrieve transaction request

```shell
curl https://www.rehive.com/api/3/admin/transactions/{tx_code}/
  -X GET
  -H "Authorization: JWT {token}"
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
        "created": 1474399284065,
        "updated": 1474399285570
    }
}
```

Get transaction details for a spcific transactions.

### Endpoint

`https://rehive.com/api/3/admin/transactions/{tx_code}/`

## Update Transaction

> Admin update transaction request

```shell
curl https://rehive.com/api/3/admin/transactions/{tx_code}/
  -X PUT
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
  -d '{"status": "Confirmed"}'
```

> Admin update transaction response

```json
{
    "status": "success"
}
```

Update a transaction's status and metadata. This endpoint can be used to move transactions from pending to complete/failed/deleted and updated the corresponding user's balance accordingly.

### Endpoint

`https://rehive.com/api/3/admin/transactions/{tx_code}/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`status` | update action/status (`Confirmed`, `Failed`, `Deleted`) | null | true
`metadata` | custom metadata | {} | false

## Create Transfer

> Admin transfer request

```shell
curl https://www.rehive.com/api/3/admin/transactions/transfer/
  -X POST
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
  -d '{"user": "joe@rehive.com",
       "amount": 500,
       "reference": "sally@rehive.com"}'
```

> Admin transfer response

```json
{
    "status": "success",
    "data": {
        "tx_code": "00000000000000000000",
        "metadata": {}
    }
}
```

Create a transfer transaction on behalf of a user. This will transfer currency from one user to another. If the recipient reference does not exist as a user in Rehive and the reference is an email address or mobile number then an invitation message will be sent to the recipient informing them they have an unclaimed transaction.

### Endpoint

`https://rehive.com/api/3/admin/transactions/transfer/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`user` | email, mobile number, unique identifier | null | true
`amount` | amount | 0 | true
`reference` | email, mobile number, unique identifier | null | true
`subtype` | a custom defined subtype | null | false
`account` | account reference code | null | false
`note` | user's note or message | blank | false
`metadata` | custom metadata | {} | false

<aside class="notice">
For all admin "create transaction" endpoints a <code>user</code> should always be specified in the request.
</aside>

## Create Deposit

> Admin deposit request

```shell
curl https://www.rehive.com/api/3/admin/transactions/deposit/
  -X POST
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
  -d '{"user": "joe@rehive.com",
       "amount": 500}'
```

> Admin deposit response

```json
{
    "status": "success",
    "data": {
        "tx_code": "00000000000000000000",
        "metadata": {}
    }
}
```

Create a deposit transaction on behalf of a user.

### Endpoint

`https://rehive.com/api/3/admin/transactions/deposit/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`user` | email, mobile number, unique identifier | null | true
`amount` | amount | 0 | true
`reference` | optional deposit reference | blank | false
`subtype` | a custom defined subtype | null | false
`account` | account reference code | null | false
`note` | user's note or message | blank | false
`metadata` | custom metadata | {} | false
`confirm_on_create` | complete immediately after creation | false | false

<aside class="notice">
Admin deposits (and withdrawals) have an additional <code>confirm_on_create</code> boolean that can be used when the deposit/withdraw should be processed and completed at the same time. This will override the normal behaviour of requiring an update or manual "completion" via the dashboard.
</aside>

## Create Withdraw

> Admin withdraw request

```shell
curl https://www.rehive.com/api/3/admin/transactions/withdraw/
  -X POST
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
  -d '{"user": "joe@rehive.com",
       "amount": 500}'
```

> Admin withdraw response

```json
{
    "status": "success",
    "data": {
        "tx_code": "00000000000000000000",
        "metadata": {}
    }
}
```

Create a withdraw transaction on behalf of a user.

### Endpoint

`https://rehive.com/api/3/admin/transactions/withdraw/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`user` | email, mobile number, unique identifier | null | true
`amount` | amount | 0 | true
`reference` | optional withdraw reference | blank | false
`subtype` | a custom defined subtype | null | false
`account` | account reference code | null | false
`note` | user's note or message | blank | false
`metadata` | custom metadata | {} | false
`confirm_on_create` | complete immediately after creation | false | false

## Verify Email Address

> Admin verify email request

```shell
curl https://rehive.com/api/3/admin/users/emails/verify/
  -X POST
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
  -d '{"email": "joe@rehive.com"}'
```

> Admin verify email response

```json
{
    "status": "success",
    "data": {
        "email": "joe@rehive.com",
        "verified": true
    }
}
```

Verify an email address on behalf of a user.

### Endpoint

`https://rehive.com/api/3/admin/users/emails/verify/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`email` | email address | null | true

## Verify Mobile Number

> Admin verify mobile request

```shell
curl https://rehive.com/api/3/admin/users/mobiles/verify/
  -X POST
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
  -d '{"email": "joe@rehive.com"}'
```

> Admin verify mobile response

```json
{
    "status": "success",
    "data": {
        "email": "joe@rehive.com",
        "verified": true
    }
}
```

Verify a mobile number on behalf of a user.

### Endpoint

`https://rehive.com/api/3/admin/users/mobiles/verify/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`number` | mobile number | null | true