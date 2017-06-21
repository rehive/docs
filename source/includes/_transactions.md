# Transactions

Rehive offers 2 standard type transactions: Debit and Credit. Debit transactiosn deduct from a user's account and Credit transaction add to a user's account. There is an additional "transfer" endpoint that can be used in order to automtically trigger a debit followed by a credit on the specified accounts.

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

```javascript
var filters = {tx_type: 'credit',currency: 'ZAR'};

rehive.transactions.getTransactionsList(filters).then(function(res){
        // ...
    },function(err){
        // ...
    })
```

> User transactions response

```shell
 {
    "status": "success",
    "data": {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": "000000000000000000000",
                "tx_type": "credit",
                "subtype": null,
                "external": false,
                "note": "",
                "metadata": {},
                "status": "Complete",
                "reference": "",
                "amount": 500,
                "fee": 0,
                "balance": 1000,
                "account": "akC49YT8x4",
                "label": "Credit",
                "company": "rehive",
                "currency": {
                    "description": "Rand",
                    "code": "ZAR",
                    "symbol": "R",
                    "unit": "rand",
                    "divisibility": 2
                },
                "user": {
                    "identifier": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": "",
                    "mobile_number": "+27840000000",
                    "profile": null
                },
                "source_transaction": null,
                "destination_transaction": null,
                "created": 1496135465218,
                "updated": 1496135465287
            },
            {
                "id": "000000000000000000000",
                "tx_type": "credit",
                "subtype": null,
                "external": false,
                "note": "",
                "metadata": {},
                "status": "Complete",
                "reference": "",
                "amount": 500,
                "fee": 0,
                "balance": 500,
                "account": "akC49YT8x4",
                "label": "Credit",
                "company": "rehive",
                "currency": {
                    "description": "Rand",
                    "code": "ZAR",
                    "symbol": "R",
                    "unit": "rand",
                    "divisibility": 2
                },
                "user": {
                    "identifier": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": "",
                    "mobile_number": "+27840000000",
                    "profile": null
                },
                "source_transaction": null,
                "destination_transaction": null,
                "created": 1496135465218,
                "updated": 1496135465287
            }
        ]
    }
}
```

```javascript
 {
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "000000000000000000000",
            "tx_type": "credit",
            "subtype": null,
            "external": false,
            "note": "",
            "metadata": {},
            "status": "Complete",
            "reference": "",
            "amount": 500,
            "fee": 0,
            "balance": 1000,
            "account": "akC49YT8x4",
            "label": "Credit",
            "company": "rehive",
            "currency": {
                "description": "Rand",
                "code": "ZAR",
                "symbol": "R",
                "unit": "rand",
                "divisibility": 2
            },
            "user": {
                "identifier": "00000000-0000-0000-0000-000000000000",
                "first_name": "Joe",
                "last_name": "Soap",
                "email": "joe@rehive.com",
                "username": "",
                "mobile_number": "+27840000000",
                "profile": null
            },
            "source_transaction": null,
            "destination_transaction": null,
            "created": 1496135465218,
            "updated": 1496135465287
        },
        {
            "id": "000000000000000000000",
            "tx_type": "credit",
            "subtype": null,
            "external": false,
            "note": "",
            "metadata": {},
            "status": "Complete",
            "reference": "",
            "amount": 500,
            "fee": 0,
            "balance": 500,
            "account": "akC49YT8x4",
            "label": "Credit",
            "company": "rehive",
            "currency": {
                "description": "Rand",
                "code": "ZAR",
                "symbol": "R",
                "unit": "rand",
                "divisibility": 2
            },
            "user": {
                "identifier": "00000000-0000-0000-0000-000000000000",
                "first_name": "Joe",
                "last_name": "Soap",
                "email": "joe@rehive.com",
                "username": "",
                "mobile_number": "+27840000000",
                "profile": null
            },
            "source_transaction": null,
            "destination_transaction": null,
            "created": 1496135465218,
            "updated": 1496135465287
        }
    ]
 }
```

Get a a user's transaction list.

#### Pagination

The list is paginated by default and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

#### Filtering

The transactions listing offers filtering on the `tx_code`, `tx_type`, `subtype`, `status`, `created` and `metadata` fields. This is done through URL parameters in the request URL:

`/api/3/transactions/?tx_type=debit`

You can also do boolean filtering on `source_transaction` and `destination_transaction` like this:

`/api/3/transactions/?destination_transaction=true`

There is a special format for fitering on metadata (ie. `metadata__{field_name}`):

`/api/3/transactions/?metadata__type=test`

#### Sorting

Sorting of the transactions listing can be done on all the "filtering" fields mentioned above via an `orderby` parameter in the request URL:

`/api/3/transactions/?orderby=tx_type`

#### Endpoint

`https://rehive.com/api/3/transactions/`

## Total Transactions

> User total transactions request

```shell
curl https://www.rehive.com/api/3/transactions/totals/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
var filters = {currency:'ZAR'};

rehive.transactions.getTotalTransactionsList(filters).then(function(res){
        // ...
    },function(err){
        // ...
    })
```

> User total transactions response

```shell
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

```javascript
{
    "amount": 1000,
    "fees": 0,
    "count": 2,
    "currency": "ZAR"
}
```

Get a user's total transaction details. This is a summary of transaction details like: amount totals, fee totals, and the total number of transactions.

#### Filtering

The transaction totals endpoint has identical filtering to the transaction list endpoint.

#### Endpoint

`https://rehive.com/api/3/transactions/totals/`

## Retrieve Transaction

> Retrieve transaction request

```shell
curl https://www.rehive.com/api/3/transactions/{tx_code}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.transactions.getTransaction(txCode).then(function(res){
        // ...
    },function(err){
        // ...
    })
```

> Retrieve transaction response

```shell
{
    "status": "success",
    "data":  {
        "id": "000000000000000000000",
        "tx_type": "credit",
        "subtype": null,
        "external": false,
        "note": "",
        "metadata": {},
        "status": "Complete",
        "reference": "",
        "amount": 500,
        "fee": 0,
        "balance": 500,
        "account": "akC49YT8x4",
        "label": "Credit",
        "company": "rehive",
        "currency": {
            "description": "Rand",
            "code": "ZAR",
            "symbol": "R",
            "unit": "rand",
            "divisibility": 2
        },
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "source_transaction": null,
        "destination_transaction": null,
        "messages": [
            {
                "level": "info",
                "message": "Transaction completed.",
                "created": 1496144568989
            }
        ],
        "created": 1496135465218,
        "updated": 1496135465287
    }
}
```

```javascript
{
    "id": "000000000000000000000",
    "tx_type": "credit",
    "subtype": null,
    "external": false,
    "note": "",
    "metadata": {},
    "status": "Complete",
    "reference": "",
    "amount": 500,
    "fee": 0,
    "balance": 500,
    "account": "akC49YT8x4",
    "label": "Credit",
    "company": "rehive",
    "currency": {
        "description": "Rand",
        "code": "ZAR",
        "symbol": "R",
        "unit": "rand",
        "divisibility": 2
    },
    "user": {
        "identifier": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": "",
        "mobile_number": "+27840000000",
        "profile": null
    },
    "source_transaction": null,
    "destination_transaction": null,
    "messages": [
        {
            "level": "info",
            "message": "Transaction completed.",
            "created": 1496144568989
        }
    ],
    "created": 1496135465218,
    "updated": 1496135465287
}
```

Get transaction details for a spcific transactions.

#### Endpoint

`https://rehive.com/api/3/transactions/{tx_code}/`

## Create Credit

> User credit request

```shell
curl https://www.rehive.com/api/3/transactions/credit/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"amount": 500}'
```

```javascript
rehive.transactions.createCredit(
        {
            amount: 500
        }).then(function(res){
            // ...
        },function(err){
            // ...
        })
```

> User credit response

```shell
{
    "status": "success",
    "data": {
        "tx_code": "00000000000000000000",
        "metadata": {}
    }
}
```

```javascript
{
    "tx_code": "00000000000000000000",
    "metadata": {}
}
```

Create a credit transaction.

#### Endpoint

`https://rehive.com/api/3/transactions/credit/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`amount` | amount | 0 | true
`currency` | currency code | blank | false
`reference` | optional credit reference | blank | false
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

## Create Debit

> User debit request

```shell
curl https://www.rehive.com/api/3/transactions/debit/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"amount": 500}'
```

```javascript
rehive.transactions.createDebit(
        {
            amount: 500
        }).then(function(res){
            // ...
        },function(err){
            // ...
        })
```

> User debit response

```shell
{
    "status": "success",
    "data": {
        "tx_code": "00000000000000000000",
        "metadata": {}
    }
}
```

```javascript
{
    "tx_code": "00000000000000000000",
    "metadata": {}
}
```

Create a debit transaction.

#### Endpoint

`https://rehive.com/api/3/transactions/debit/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`amount` | amount | 0 | true
`currency` | currency code | blank | false
`reference` | optional debit reference | blank | false
`subtype` | a custom defined subtype | null | false
`account` | account reference code | null | false
`note` | user's note or message | blank | false
`metadata` | custom metadata | {} | false

## Create Transfer

> User transfer request

```shell
curl https://www.rehive.com/api/3/transactions/transfer/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"amount": 500,
       "recipient": "joe@rehive.com"}'
```

```javascript
rehive.transactions.createTransfer(
    {
        amount: 500,
        recipient: "joe@rehive.com"
    }).then(function(res){
        // ...
    },function(err){
        // ...
    })
```

> User transfer response

```shell
{
    "status": "success",
    "data": {
        "tx_code": "00000000000000000000",
        "metadata": {}
    }
}
```

```javascript
{
    "tx_code": "00000000000000000000",
    "metadata": {}
}
```

Create a transfer transaction. This will transfer currency from one user to another. If the recipient reference does not exist as a user in Rehive and the reference is an email address or mobile number then an invitation message will be sent to the recipient informing them thay have an unclaimed transaction.

<aside class="notice">
The transfer transaction endpoint is essentially a wrapper for standard debit/credit transactions. If a transfer is completed successfuly it will create 2 transactions: one to debit from the sender and one to credit the receiver. The transactions are otherwise indentical to normal debit/credit transactions. You can view sender/receiver details by accessing the attributes `source_transaction` (indicates who the transfer came from) and `destination_transaction` (indicates who the transfer was sent to).
</aside>

#### Endpoint

`https://rehive.com/api/3/transactions/transfer/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`amount` | amount | 0 | true
`recipient` | email, mobile number, unique identifier | null | true
`currency` | currency code | blank | false
`debit_subtype` | a custom defined subtype | null | false
`debit_account` | account reference code | null | false
`debit_note` | user's note or message | blank | false
`debit_metadata` | custom metadata | {} | false
`debit_reference` | optional debit reference | string | false
`credit_subtype` | a custom defined subtype | null | false
`credit_note` | user's note or message | blank | false
`credit_metadata` | custom metadata | {} | false
`credit_reference` | optional credit reference | string | false