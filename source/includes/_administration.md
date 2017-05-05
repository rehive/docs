# Administration

Rehive includes a set of admin-only endpoints that can make working with users and their transactions extremely easy.

## List Transactions

> Admin transactions request

```shell
curl https://www.rehive.com/api/3/admin/transactions/
  -X GET
  -H "Authorization: Token {token}"
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

The transactions listing offers filtering on the `tx_code`, `tx_type`, 
`subtype`, `status`, `user`, `from_reference`, `to_reference`, `currency`, 
`created` and `metadata` fields. This is done through URL parameters in the request URL:

`/api/3/admin/transactions/?tx_type=transfer`

Filtering on a timestamp range using 
`created__gt` and `created__lt` for greater than and less than a timestamp.
 
 `/api/3/admin/transactions/?created__gt=1490033384080&created__lt=1490033384089`

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
  -H "Authorization: Token {token}"
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

`https://rehive.com/api/3/admin/transactions/{tx_code}/`

## Update Transaction

> Admin update transaction request

```shell
curl https://rehive.com/api/3/admin/transactions/{tx_code}/
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"status": "Complete"}'
```

> Admin update transaction response

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

Update a transaction's status and metadata. This endpoint can be used to move transactions from pending to complete/failed/deleted and updated the corresponding user's balance accordingly.

### Messsage

Custom messages can be attached to transactions by including a `message` attribute in an update request. The `message`
attribute should be a JSOn object with 2 attributes `level` and `message`.

1. `level` : message log level, can be `info`, `warning`, `error`.
2. `message`: A text message.

Each message added to a transaction will be stored in a list. 

### Endpoint

`https://rehive.com/api/3/admin/transactions/{tx_code}/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`status` | update action/status (`Complete`, `Failed`, `Deleted`) | null | true
`metadata` | custom metadata | {} | false
`message` | message object | [] | false
## Create Transfer

> Admin transfer request

```shell
curl https://www.rehive.com/api/3/admin/transactions/transfer/
  -X POST
  -H "Authorization: Token {token}"
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
`currency` | currency code | blank | false
`metadata` | custom metadata | {} | false

<aside class="notice">
For all admin "create transaction" endpoints a <code>user</code> should always be specified in the request.
</aside>

## Create Deposit

> Admin deposit request

```shell
curl https://www.rehive.com/api/3/admin/transactions/deposit/
  -X POST
  -H "Authorization: Token {token}"
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
`currency` | currency code | blank | false
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
  -H "Authorization: Token {token}"
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
`currency` | currency code | blank | false
`metadata` | custom metadata | {} | false
`confirm_on_create` | complete immediately after creation | false | false

## List Accounts

> Admin list accounts request

```shell
curl https://www.rehive.com/api/3/admin/accounts/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin list accounts response

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
                "user": "joe@rehive.com",
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

Get a list of accounts belonging to users in a company.

### Pagination

The list is paginated and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

### Filtering

The account listing offers filtering on the `active` and `user` attributes. This is done through URL parameters in the request URL:

`/api/3/admin/accounts/?active=true`

### Endpoint

`https://rehive.com/api/3/admin/accounts/`

## Retrieve Account

> Admin retrieve account request

```shell
curl https://www.rehive.com/api/3/admin/accounts/{reference}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin retrieve account response

```json
{
    "status": "success",
    "data": {
        "name": "default",
        "reference": "0000000000",
        "user": "joe@rehive.com",
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

Retrieve an account belonging to a company.

### Filtering

The account view offers filtering of currencies based on the `active` attribute. This is done through a URL parameter in the request URL:

`/api/3/admin/accounts/{reference}/?active=true`

### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/`

## List Account Currencies

> Admin list account currencies request

```shell
curl https://www.rehive.com/admin/api/3/accounts/{reference}/currencies/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin list account currencies response

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

Get a list of currencies for an account belonging to a company.

### Pagination

The list is paginated and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

### Filtering

The account currency listing offers filtering on the `active` attribute. This is done through a URL parameter in the request URL:

`/api/3/admin/accounts/{reference}/currencies/?active=true`

### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/`

## Retrieve Account Currency

> Admin retrieve account currency request

```shell
curl https://www.rehive.com/api/3/admin/accounts/{reference}/currencies/{code}
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin retrieve account currency response

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

Retrieve an account's currency belonging to a company.

### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}`

## Update Account Currency

> Admin retrieve account currency request

```shell
curl https://www.rehive.com/api/3/admin/accounts/{reference}/currencies/{code}
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"active": true}'
```

> Admin retrieve account currency response

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

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`active` | is active currency | false | false







## List Currencies

> Admin list currencies request

```shell
curl https://www.rehive.com/api/3/company/currencies/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin list currencies response

```json
{
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "code": "XBT",
                "description": "bitcoin",
                "symbol": "฿",
                "unit": "bitcoin",
                "divisibility": 8
            }
        ]
    }
}
```

Get a list of all existing currencies. This includes default Rehive currencies as well as any currencies added by the company.

### Endpoint

`https://rehive.com/api/3/admin/currencies/`

## List Currencies

> Admin list currencies request

```shell
curl https://www.rehive.com/api/3/admin/currencies/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin list currencies response

```json
{
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "code": "XBT",
                "description": "bitcoin",
                "symbol": "฿",
                "unit": "bitcoin",
                "divisibility": 8
            }
        ]
    }
}
```

Get a list of all existing currencies. This includes default Rehive currencies as well as any currencies added by the company.

### Endpoint

`https://rehive.com/api/3/admin/currencies/`

## Create Currency

> Admin create currency request

```shell
curl https://www.rehive.com/api/3/admin/currencies/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"code": "XBT",
        "description": "bitcoin",
        "symbol": "฿",
        "unit": "bitcoin",
        "divisibility": 8}'
```

> Admin create currency response

```json
 {
    "status": "success",
    "data": {
        "code": "XBT",
        "description": "bitcoin",
        "symbol": "฿",
        "unit": "bitcoin",
        "divisibility": 8,
        "enabled": false
    }
}
```

Create a custom currency. This currency will be unique to the company that created it.

### Endpoint

`https://rehive.com/api/3/admin/currencies/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`code` | currency code | null | true
`description` | name of currency | null | true
`symbol` | currency symbol | null | true
`unit` | unit, like `dollar` | null | true
`divisibility` | number of decimal places | 0 | true


## Retrieve Currency

> Admin retrieve currency request

```shell
curl https://www.rehive.com/api/3/admin/currencies/{code}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin retrieve currency response

```json
{
    "status": "success",
    "data": {
        "code": "XBT",
        "description": "bitcoin",
        "symbol": "฿",
        "unit": "bitcoin",
        "divisibility": 8,
        "enabled": true
    }
}
```

Retrieve a currencies details.

### Endpoint

`https://rehive.com/api/3/admin/currencies/{code}/`

## Update Currency

> Admin update currency request

```shell
curl https://www.rehive.com/api/3/admin/currencies/{code}/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"enabled": true}'
```

> Admin update currency response

```json
 {
    "status": "success",
    "data": {
        "code": "XBT",
        "description": "bitcoin",
        "symbol": "฿",
        "unit": "bitcoin",
        "divisibility": 8,
        "enabled": true
    }
}
```

Update a currency. this endpoint can be used to enable an existing currency or if it is a custom currency, edit its details.

### Endpoint

`https://rehive.com/api/3/admin/currencies/{code}/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`code` | currency code | null | true
`description` | name of currency | null | true
`symbol` | currency symbol | null | true
`unit` | unit, like `dollar` | null | true
`divisibility` | number of decimal places | 0 | true
`enabled` | whether active for a company | false | true

## Verify Email Address

> Admin verify email request

```shell
curl https://rehive.com/api/3/admin/users/emails/verify/
  -X POST
  -H "Authorization: Token {token}"
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
  -H "Authorization: Token {token}"
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

## Retrieve Company

> View the company info

```shell
curl https://rehive.com/api/3/admin/company/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Company info response

```json
{
    "status": "success",
    "data": {
        "identifier": "test_company",
        "name": "Test Company 1",
        "description": "A Test Company.",
        "website": "http://www.test_company.com",
        "logo": "https://www.test_company.com/logo.jpg",
        "password_reset_url": null,
        "email_confirmation_url": null,
        "default_currency": "XBT"
    }
}
```

Retrieve the company info.

### Endpoint

`https://rehive.com/api/3/admin/company/`

## Update Company

> Update company info

```shell
curl https://rehive.com/api/3/admin/company/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"description": "A new description"}'
```

> Update company info response

```json
{
    "status": "success",
    "data": {
        "identifier": "test_company",
        "name": "Test Company 1",
        "description": "A new description",
        "website": "http://www.test_company.com",
        "logo": "https://www.test_company.com/logo.jpg",
        "password_reset_url": null,
        "email_confirmation_url": null,
        "default_currency": "XBT"
    }
}
```

Retrieve the company info.

### Endpoint

`https://rehive.com/api/3/admin/company/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | Company Name | blank | false
`description` | Company Description | blank | false
`website` | Company website URL | blank | false
`logo` | Company logo URL | blank | false
`password_reset_url` | Custom company password reset URL | blank | false
`email_confirmation_url` | Custom company email confirmation URL | blank | false
`default_currency` | Default company currency | null | false

## List Webhooks

> List webhooks request

```shell
curl https://rehive.com/api/3/admin/webhooks/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List webhooks response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "url": "http://mysite.com/webhook_endpoint",
            "tx_type": "transfer",
            "secret": "supersecret"
        }
    ]
}
```

### Endpoint

`https://rehive.com/api/3/admin/webhooks/`

## Create Webhooks

> Create webhooks request

```shell
curl https://rehive.com/api/3/admin/webhooks/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"url": "http://mysite.com/webhook_endpoint",
       "tx_type": "transfer",
       "secret": "supersecret"}'
```

> List webhooks response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "url": "http://mysite.com/webhook_endpoint",
            "tx_type": "transfer",
            "secret": "supersecret"
        }
    ]
}
```

### Endpoint

`https://rehive.com/api/3/admin/webhooks/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`url` | Webhook URL | blank | true
`tx_type` | Transaction type | blank | true
`secret` | Webhook secret | blank | false

## Retrieve Webhook

> Retrieve webhook request

```shell
curl https://rehive.com/api/3/admin/webhooks/{id}
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve webhook response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "url": "http://mysite.com/webhook_endpoint",
        "tx_type": "transfer",
        "secret": "supersecret"
    }
}
```

### Endpoint

`https://rehive.com/api/3/admin/webhooks/{id}`

## Update Webhook

> Update webhook request

```shell
curl https://rehive.com/api/3/admin/webhooks/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"url": "http://mysite.com/new_webhook_endpoint"}'
```

> Update webhook response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "url": "http://mysite.com/new_webhook_endpoint",
            "tx_type": "transfer",
            "secret": "supersecret"
        }
    ]
}
```

### Endpoint

`https://rehive.com/api/3/admin/webhooks/{id}`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`url` | Webhook URL | blank | true
`tx_type` | Transaction type | blank | true
`secret` | Webhook secret | blank | false

## List Subtypes

> List subtypes request

```shell
curl https://rehive.com/api/3/admin/subtypes/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List subtypes response

```json
{
    "status": "success",
    "data": [
        {
            "id": 20,
            "name": "deposit_subtype",
            "label": "Our deposit",
            "description": "Description for out deposit",
            "tx_type": "deposit",
            "created": "2017-04-28T11:36:57.396723Z",
            "updated": "2017-04-28T11:36:57.396743Z"
        }
    ]
}
```

### Endpoint

`https://rehive.com/api/3/admin/subtypes/`

## Create subtypes

> Create subtypes request

```shell
curl https://rehive.com/api/3/admin/subtypes/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Create subtypes response

```json
{
    "status": "success",
    "data": {
        "id": 20,
        "name": "deposit_subtype",
        "label": "Our deposit",
        "description": "Description for out deposit",
        "tx_type": "deposit",
        "created": "2017-04-28T11:36:57.396723Z",
        "updated": "2017-04-28T11:36:57.396743Z"
    }
}
```

### Endpoint

`https://rehive.com/api/3/admin/subtypes/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | name | blank | true
`label` | label | blank | false
`description` | description | blank | false
`tx_type` | Transaction type | blank | true

## Retrieve Subtypes

> Retrieve subtypes request

```shell
curl https://rehive.com/api/3/admin/subtypes/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve subtypes response

```json
{
    "status": "success",
    "data": {
        "id": 20,
        "name": "deposit_subtype",
        "label": "Our deposit",
        "description": "Description for out deposit",
        "tx_type": "deposit",
        "created": "2017-04-28T11:36:57.396723Z",
        "updated": "2017-04-28T11:36:57.396743Z"
    }
}
```

### Endpoint

`https://rehive.com/api/3/admin/subtypes/{id}`

## Update subtypes

> Update subtypes request

```shell
curl https://rehive.com/api/3/admin/subtypes/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"description": "New description"}'
```

> Update subtypes response

```json
{
    "status": "success",
    "data": {
        "id": 20,
        "name": "deposit_subtype",
        "label": "Our deposit",
        "description": "New description",
        "tx_type": "deposit",
        "created": "2017-04-28T11:36:57.396723Z",
        "updated": "2017-04-28T11:36:57.396743Z"
    }
}
```

### Endpoint

`https://rehive.com/api/3/admin/subtypes/{id}`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | name | blank | true
`label` | label | blank | false
`description` | description | blank | false
`tx_type` | Transaction type | blank | true

## List Bank Accounts

> List Bank Accounts request

```shell
curl https://rehive.com/api/3/admin/bank-accounts/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List Bank Accounts response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "name": "Bank Account",
            "number": "12341234",
            "type": "Cheque",
            "bank_name": "Barclays",
            "bank_code": "1234",
            "branch_code": "1234",
            "swift": null,
            "iban": null,
            "bic": null
        }
    ]
}
```

### Endpoint

`https://rehive.com/api/3/admin/bank-accounts/`

## Create Bank Account

> Create Bank Account request

```shell
curl https://rehive.com/api/3/admin/bank-accounts/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "Bank Account",
        "number": "12341234",
        "type": "Cheque",
        "bank_name": "Barclays",
        "bank_code": "1234",
        "branch_code": "1234"}'
```

> Create Bank Account response

```json
{
    "status": "success",
    "data": {
        "id": 2,
        "name": "Bank Account",
        "number": "12341234",
        "type": "Cheque",
        "bank_name": "Barclays",
        "bank_code": "1234",
        "branch_code": "1234",
        "swift": null,
        "iban": null,
        "bic": null
    }
}
```

### Endpoint

`https://rehive.com/api/3/admin/bank-accounts/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | Account Name | blank | false
`number` | Account Number | blank | false
`type` | Account Type | blank | false
`bank_name` | Bank Name | blank | false
`bank_code` | Bank Code | blank | false
`branch_code` | Branch Code | blank | false

## Retrieve Bank Account

> Retrieve Bank Account request

```shell
curl https://rehive.com/api/3/admin/bank-accounts/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve Bank Account response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "name": "Bank Account",
        "number": "12341234",
        "type": "Cheque",
        "bank_name": "Barclays",
        "bank_code": "1234",
        "branch_code": "1234",
        "swift": null,
        "iban": null,
        "bic": null
    }
}
```

### Endpoint

`https://rehive.com/api/3/admin/bank-accounts/{id}`

## Update Bank Account

> Update Bank Account request

```shell
curl https://rehive.com/api/3/admin/bank-accounts/{id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "New account name"}'
```

> Update Bank Account response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "name": "New account name",
        "number": "12341234",
        "type": "Cheque",
        "bank_name": "Barclays",
        "bank_code": "1234",
        "branch_code": "1234",
        "swift": null,
        "iban": null,
        "bic": null
    }
}
```

### Endpoint

`https://rehive.com/api/3/admin/bank-accounts/{id}`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | Account Name | blank | false
`number` | Account Number | blank | false
`type` | Account Type | blank | false
`bank_name` | Bank Name | blank | false
`bank_code` | Bank Code | blank | false
`branch_code` | Branch Code | blank | false

## List Notifications

> List Notifications request

```shell
curl https://rehive.com/api/3/admin/notifications/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List Notifications response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "name": "tx_send",
            "description": "Send transaction notifications",
            "enabled": true
        }
    ]
}
```

### Endpoint

`https://rehive.com/api/3/admin/notifications/`

## Retrieve Notifications

> Retrieve Notifications request

```shell
curl https://rehive.com/api/3/admin/notifications/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve Notifications response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "name": "tx_send",
        "description": "Send transaction notifications",
        "enabled": true
    }
}
```

### Endpoint

`https://rehive.com/api/3/admin/notifications/{id}`

## Update Notifications

> Update Notifications request

```shell
curl https://rehive.com/api/3/admin/notifications/{id}
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"enabled": false}'
```

> Update Notifications response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "name": "tx_send",
        "description": "Send transaction notifications",
        "enabled": false
    }
}
```

### Endpoint

`https://rehive.com/api/3/admin/notifications/{id}`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`enabled` | Account Name | false | true

## List Controls

> List Controls request

```shell
curl https://rehive.com/api/3/admin/controls/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List Controls response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "name": "tx_all",
            "description": "Allow transactions",
            "enabled": true
        }
    ]
}
```

### Endpoint

`https://rehive.com/api/3/admin/controls/`

## Retrieve Controls

> Retrieve Controls request

```shell
curl https://rehive.com/api/3/admin/controls/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve Controls response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "name": "tx_all",
        "description": "Allow transactions",
        "enabled": true
    }
}
```

### Endpoint

`https://rehive.com/api/3/admin/controls/{id}`

## Update Controls

> Update Controls request

```shell
curl https://rehive.com/api/3/admin/controls/{id}
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"enabled": false}'
```

> Update Controls response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "name": "tx_all",
        "description": "Allow transactions",
        "enabled": false
    }
}
```

### Endpoint

`https://rehive.com/api/3/admin/controls/{id}`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`enabled` | Account Name | false | true