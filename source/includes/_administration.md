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
    "status": "success"
}
```

Update a transaction's status and metadata. This endpoint can be used to move transactions from pending to complete/failed/deleted and updated the corresponding user's balance accordingly.

### Endpoint

`https://rehive.com/api/3/admin/transactions/{tx_code}/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`status` | update action/status (`Complete`, `Failed`, `Deleted`) | null | true
`metadata` | custom metadata | {} | false

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

`https://rehive.com/api/3/admin/bank-account/`

## Create Bank Account

> Create Bank Account request

```shell
curl https://rehive.com/api/3/admin/bank-account/
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

`https://rehive.com/api/3/admin/bank-account/`

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
curl https://rehive.com/api/3/admin/bank-account/{id}/
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

`https://rehive.com/api/3/admin/bank-account/{id}`

## Update Bank Account

> Update Bank Account request

```shell
curl https://rehive.com/api/3/admin/bank-account/{id}
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

`https://rehive.com/api/3/admin/bank-account/{id}`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | Account Name | blank | false
`number` | Account Number | blank | false
`type` | Account Type | blank | false
`bank_name` | Bank Name | blank | false
`bank_code` | Bank Code | blank | false
`branch_code` | Branch Code | blank | false