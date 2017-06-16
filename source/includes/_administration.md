# Administration

Rehive includes a set of admin-only endpoints that can make working with users and their transactions extremely easy.

## User

### List Users

> Admin list users request

```shell
curl https://www.rehive.com/admin/api/3/admin/users/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin list users response

```json
{
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "identifier": "00000000-0000-0000-0000-000000000000",
                "first_name": "Joe",
                "last_name": "Soap",
                "email": "joe@rehive.com",
                "username": "",
                "id_number": "",
                "profile": null,
                "currency": {
                    "description": "Rand",
                    "code": "ZAR",
                    "symbol": "R",
                    "unit": "rand",
                    "divisibility": 2
                },
                "company": "rehive",
                "language": "en",
                "nationality": "ZA",
                "metadata": null,
                "mobile_number": "+27840000000",
                "skype_name": "@skype",
                "timezone": "Asia/Dhaka"
                "date_joined": 1464912953000
            }
        ]
    }
}
```

Get a list of users belonging to a company.

#### Pagination

The list is paginated and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

#### Filtering

The account currency listing offers filtering on the `identifier`, `email`, `mobile_number`, `first_name`, `last_name`, `username`, `id_number`, `date_joined`, and `last_login` attribute. This is done through a URL parameter in the request URL:

`/api/3/admin/users/?first_name=Joe`

#### Endpoint

`https://rehive.com/api/3/admin/users/`

### Create User

> Admin create user reuest

```shell
curl https://www.rehive.com/api/3/admin/users/`
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"first_name": "Joe",
       "last_name": "Soap",
       "mobile_number": "+27840000000",
       "email": "joe@rehive.com"}'
```

> Admin update user response

```json
{
    "status": "success",
    "data": {
        "identifier": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": "",
        "id_number": "",
        "profile": null,
        "currency": {
            "description": "Rand",
            "code": "ZAR",
            "symbol": "R",
            "unit": "rand",
            "divisibility": 2
        },
        "company": "rehive",
        "language": "en",
        "nationality": "ZA",
        "metadata": null,
        "mobile_number": "+27840000000",
        "skype_name": "@skype",
        "timezone": "Asia/Dhaka"
        "date_joined": 1464912953000
    }
}
```

Update a user's details.

#### Endpoint

`https://rehive.com/api/3/admin/users/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`first_name` | first name | "" | false
`last_name` | last name | "" | false
`email` | email address | null| false
`mobile_number` | mobile number | null | false

<aside class="warning">
    A `mobile_number` or `email` is required.
</aside>

### Retrieve User

> Admin retrieve user request

```shell
curl https://www.rehive.com/api/3/admin/users/{identifier}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin retrieve user response

```json
{
    "status": "success",
    "data": {
        "identifier": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": "",
        "id_number": "",
        "profile": null,
        "currency": {
            "description": "Rand",
            "code": "ZAR",
            "symbol": "R",
            "unit": "rand",
            "divisibility": 2
        },
        "company": "rehive",
        "language": "en",
        "nationality": "ZA",
        "metadata": null,
        "mobile_number": "+27840000000",
        "skype_name": "@skype",
        "timezone": "Asia/Dhaka"
        "date_joined": 1464912953000
    }
}
```

Retrieve a company's user.

#### Endpoint

`https://rehive.com/api/3/admin/users/{identifier}/`

### Update User

> Admin update user request

```shell
curl https://www.rehive.com/api/3/admin/users/{identifier}/`
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"first_name": "Joe"}'
```

> Admin update user response

```json
{
    "status": "success",
    "data": {
        "identifier": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": "",
        "id_number": "",
        "profile": null,
        "currency": {
            "description": "Rand",
            "code": "ZAR",
            "symbol": "R",
            "unit": "rand",
            "divisibility": 2
        },
        "company": "rehive",
        "language": "en",
        "nationality": "ZA",
        "metadata": null,
        "mobile_number": "+27840000000",
        "skype_name": "@skype",
        "timezone": "Asia/Dhaka"
        "date_joined": 1464912953000
    }
}
```

Update a user's details.

#### Endpoint

`https://rehive.com/api/3/admin/users/{identifier}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`first_name` | first name | "" | false
`last_name` | last name | "" | false
`id_number` | ID number | "" | false
`language` | language code (en, af etc.) | "" | false
`nationality` | bationality code (ZA, USA etc.) | "" | false
`metadata` | custom user data  | {} | false
`timezone` | timezone (Asia/Dhaka, Africa/Harare etc.) | string | false

### List User Switches

List all switches related to a user.

> List User Switches request

```shell
curl https://rehive.com/api/3/admin/users/{identifier}/switches/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List User Switches response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "tx_type": "credit",
            "subtype": null,
            "enabled": true,
            "created": 1497362397968,
            "updated": 1497362397968
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/{identifier}/switches/`

### Create User Switches

Create a new switch related to a user.

> Create User Switches request

```shell
curl https://rehive.com/api/3/admin/users/{identifier}/switches/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"tx_type": "credit",
       "enabled": true}'
```

> Create User Switches response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "tx_type": "credit",
        "subtype": null,
        "enabled": true,
        "created": 1497362397968,
        "updated": 1497362397968
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/{identifier}/switches/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`tx_type` | Transaction Type | | true
`subtype_id` | Subtype ID | null | false
`enabled` | Enabled | false | true

### Retrieve User Switches

Retrieve a specific switch related to a user

> Retrieve User Switches request

```shell
curl https://rehive.com/api/3/admin/users/{identifier}/switches/{id}
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve User Switches response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "tx_type": "credit",
        "subtype": null,
        "enabled": true,
        "created": 1497362397968,
        "updated": 1497362397968
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/{identifier}/switches/{id}`

### Update User Switches

Update a specific switch related to a user

> Update User Switches request

```shell
curl https://rehive.com/api/3/admin/users/{identifier}/switches/{id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"enabled": false}'
```

> Update User Switches response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "tx_type": "credit",
        "subtype": null,
        "enabled": false,
        "created": 1497362397968,
        "updated": 1497362931403
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/{identifier}/switches/{id}`


--------------------------------------------------------------------------------

## Emails


### List Emails

> Admin list emails request

```shell
curl https://www.rehive.com/admin/api/3/admin/users/emails/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin list emails response

```json
{
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "user": {
                    "identifier": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": "",
                    "mobile_number": "+27840000000",
                    "profile": null
                },
                "id": 1,
                "email": "joe@rehive.com",
                "primary": true,
                "verified": true
            },
        ]
    }
}
```

Get a list of emails belonging to a company.

#### Pagination

The list is paginated and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

#### Filtering

The account currency listing offers filtering on the `user` attribute. This is done through a URL parameter in the request URL:

`/api/3/admin/users/emails/?user=00000000-0000-0000-0000-000000000000`

#### Endpoint

`https://rehive.com/api/3/admin/users/emails/`

### Create Email

> Admin create email reuest

```shell
curl https://www.rehive.com/api/3/admin/users/emails/`
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"user": 00000000-0000-0000-0000-000000000000,
       "verified": true,
       "primary": true,
       "email": "joe@rehive.com"}'
```

> Admin create email response

```json
{
    "status": "success",
    "data": {
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "id": 1,
        "email": "joe@rehive.com",
        "primary": true,
        "verified": true
    }
}
```

Create an email address for a user.

#### Endpoint

`https://rehive.com/api/3/admin/users/emails/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`user` | user identifier | null | true
`verified` | last name | false | false
`primary` | email address | false | false
`email` | email address | null | true

### Retrieve Email

> Admin retrieve email request

```shell
curl https://www.rehive.com/api/3/admin/users/emails/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin retrieve email response

```json
{
    "status": "success",
    "data": {
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "id": 1,
        "email": "joe@rehive.com",
        "primary": true,
        "verified": true
    }
}
```

Retrieve a company's email.

#### Endpoint

`https://rehive.com/api/3/admin/users/emails/{id}/`

### Update Email

> Admin update email request

```shell
curl https://www.rehive.com/api/3/admin/emails/{id}/`
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"verified": true}'
```

> Admin update email response

```json
{
    "status": "success",
    "data": {
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "id": 1,
        "email": "joe@rehive.com",
        "primary": true,
        "verified": true
    }
}
```

Update a user's email.

#### Endpoint

`https://rehive.com/api/3/admin/users/emails/{id}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`verified` | last name | false | false
`primary` | email address | false | false



--------------------------------------------------------------------------------

## Mobiles

### List Mobiles

> Admin list mobiles request

```shell
curl https://www.rehive.com/admin/api/3/admin/users/mobiles/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin list mobiles response

```json
{
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "user": {
                    "identifier": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": "",
                    "mobile_number": "+27840000000",
                    "profile": null
                },
                "id": 1,
                "number": "+27840000000",
                "primary": true,
                "verified": true
            },
        ]
    }
}
```

Get a list of mobile numbers belonging to a company.

#### Pagination

The list is paginated and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

#### Filtering

The account currency listing offers filtering on the `user` attribute. This is done through a URL parameter in the request URL:

`/api/3/admin/users/mobiles/?user=00000000-0000-0000-0000-000000000000`

#### Endpoint

`https://rehive.com/api/3/admin/users/mobiles/`

### Create Mobile

> Admin create mobile request

```shell
curl https://www.rehive.com/api/3/admin/users/mobiles/`
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"user": 00000000-0000-0000-0000-000000000000,
       "verified": true,
       "primary": true,
       "number": "+27840000000"}'
```

> Admin create mobile response

```json
{
    "status": "success",
    "data": {
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "id": 1,
        "email": "+27840000000",
        "primary": true,
        "verified": true
    }
}
```

Create a mobile number for a user.

#### Endpoint

`https://rehive.com/api/3/admin/users/mobiles/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`user` | user identifier | null | true
`verified` | last name | false | false
`primary` | email address | false | false
`email` | email address | null | true

### Retrieve Mobile

> Admin retrieve mobile request

```shell
curl https://www.rehive.com/api/3/admin/users/mobiles/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin retrieve mobile response

```json
{
    "status": "success",
    "data": {
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "id": 1,
        "number": "+27840000000",
        "primary": true,
        "verified": true
    }
}
```

Retrieve a company's mobile.

#### Endpoint

`https://rehive.com/api/3/admin/users/mobiles/{id}/`

### Update Mobile

> Admin update mobile request

```shell
curl https://www.rehive.com/api/3/admin/mobiles/{id}/`
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"verified": true}'
```

> Admin update mobile response

```json
{
    "status": "success",
    "data": {
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "id": 1,
        "number": "+27840000000",
        "primary": true,
        "verified": true
    }
}
```

Update a user's mobile.

#### Endpoint

`https://rehive.com/api/3/admin/users/mobiles/{id}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`verified` | last name | false | false
`primary` | email address | false | false

--------------------------------------------------------------------------------

## Transactions

### List Transactions

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

Get a company's transaction list.

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

`https://rehive.com/api/3/admin/transactions/`

### Total Transactions

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

#### Filtering

The admin transaction totals endpoint has identical filtering to the admin transaction list endpoint.

#### Endpoint

`https://rehive.com/api/3/admin/transactions/totals/`

### Retrieve Transaction

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

Get transaction details for a spcific transactions.

#### Endpoint

`https://rehive.com/api/3/admin/transactions/{tx_code}/`

### Update Transaction

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

Update a transaction's status and metadata. This endpoint can be used to move transactions from pending to complete/failed/deleted and updated the corresponding user's balance accordingly. In addition, you can add metadata and messages to the transaction.

#### Messsages

Custom messages can be attached to transactions by including a `message` attribute in an update request. The `message`
attribute should be a JSON object with 2 attributes `level` and `message`.

1. `level` : message log level, can be `info`, `warning`, `error`.
2. `message`: A text message.

Each message added to a transaction will be stored in a list. Rehive itself will also add messages to this attribute when erorrs occur during processing. 

#### Endpoint

`https://rehive.com/api/3/admin/transactions/{tx_code}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`status` | update action/status (`Complete`, `Failed`, `Deleted`) | null | true
`metadata` | custom metadata | {} | false
`message` | message object | {} | false

### Create Credit

> Admin credit request

```shell
curl https://www.rehive.com/api/3/admin/transactions/credit/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"user": "joe@rehive.com",
       "amount": 500}'
```

> Admin credit response

```json
{
    "status": "success",
    "data": {
        "tx_code": "00000000000000000000",
        "metadata": {}
    }
}
```

Create a credit transaction on behalf of a user.

#### Endpoint

`https://rehive.com/api/3/admin/transactions/credit/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`user` | email, mobile number, unique identifier | null | true
`amount` | amount | 0 | true
`reference` | optional credit reference | blank | false
`subtype` | a custom defined subtype | null | false
`account` | account reference code | null | false
`note` | user's note or message | blank | false
`currency` | currency code | blank | false
`metadata` | custom metadata | {} | false
`confirm_on_create` | complete immediately after creation | false | false

<aside class="notice">
Admin credits (and debit) have an additional <code>confirm_on_create</code> boolean that can be used when the credit/debit  should be processed and completed at the same time. This will override the normal behaviour of requiring an update or manual "completion" via the dashboard.
</aside>

<aside class="notice">
For all admin "create transaction" endpoints a <code>user</code> should always be specified in the request.
</aside>

### Create Debit

> Admin debit request

```shell
curl https://www.rehive.com/api/3/admin/transactions/debit/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"user": "joe@rehive.com",
       "amount": 500}'
```

> Admin debit response

```json
{
    "status": "success",
    "data": {
        "tx_code": "00000000000000000000",
        "metadata": {}
    }
}
```

Create a debit transaction on behalf of a user.

#### Endpoint

`https://rehive.com/api/3/admin/transactions/debit/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`user` | email, mobile number, unique identifier | null | true
`amount` | amount | 0 | true
`reference` | optional debit reference | blank | false
`subtype` | a custom defined subtype | null | false
`account` | account reference code | null | false
`note` | user's note or message | blank | false
`currency` | currency code | blank | false
`metadata` | custom metadata | {} | false
`confirm_on_create` | complete immediately after creation | false | false

### Create Transfer

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

#### Endpoint

`https://rehive.com/api/3/admin/transactions/transfer/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`user` | email, mobile number, unique identifier | null | true
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

--------------------------------------------------------------------------------

## Accounts

### List Accounts

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
                "currencies": [
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

#### Pagination

The list is paginated and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

#### Filtering

The account listing offers filtering on the `active` and `user` attributes. This is done through URL parameters in the request URL:

`/api/3/admin/accounts/?active=true`

#### Endpoint

`https://rehive.com/api/3/admin/accounts/`

### Retrieve Account

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
        "currencies": [
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

#### Filtering

The account view offers filtering of currencies based on the `active` attribute. This is done through a URL parameter in the request URL:

`/api/3/admin/accounts/{reference}/?active=true`

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/`

### List Account Currencies

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

#### Pagination

The list is paginated and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

#### Filtering

The account currency listing offers filtering on the `active` attribute. This is done through a URL parameter in the request URL:

`/api/3/admin/accounts/{reference}/currencies/?active=true`

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/`

### Retrieve Account Currency

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

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}`

### Update Account Currency

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

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`active` | is active currency | false | false

### List Account Currency Limits

List all Limits related to am account currency.

> List Account Currency request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List Account Currency Limits response

```json
{
    "data": [
        {
            "id": 1,
            "value": 1000,
            "type": "Maximum",
            "tx_type": "credit",
            "subtype": null,
            "created": 1497428787920,
            "updated": 1497428787921
        }
    ],
    "status": "success"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/`

### Create Account Currency Limit

Create a new limit related to an account currency.

> Create Account Currency Limit request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 1000,
       "type": "max",
       "tx_type": "credit"}'
```

> Create Account Currency response

```json
{
    "data": {
        "id": 1,
        "value": 1000,
        "type": "Maximum",
        "tx_type": "credit",
        "subtype": null,
        "created": 1497428787920,
        "updated": 1497428787921
    },
    "status": "success"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`value` | Limit value | 0 | true
`type` | Limit Type |  | true
`tx_type` | Transaction type limits are applied | | true
`subtype_id` | Transaction subtype ID | null | false

#### Limit Types

Value | Description 
--- | --- 
`max` | Maximum 
`day_max` | Maximum per day 
`month_max` | Maximum per month 
`min` | Minimum 

#### Transaction Types

Value | Description 
--- | --- 
`credit` | Credit 
`debit` | Debit

### Retrieve Account Currency Limit

Retrieve a specific requirement related to an account currency.

> Retrieve Account Currency request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve Account Currency Limit response

```json
{
    "data": {
        "id": 1,
        "value": 1000,
        "type": "Maximum",
        "tx_type": "credit",
        "subtype": null,
        "created": 1497428787920,
        "updated": 1497428787921
    },
    "status": "success"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}`

### Update Account Currency Limit

Update a specific limits related to an account currency.

> Update Account Currency request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 5000,
       "type": "min"}'
```

> Update Account Currency response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "value": 5000,
        "type": "Minimum",
        "tx_type": "credit",
        "subtype": null,
        "created": 1497428787920,
        "updated": 1497429648948
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}`

### List Account Currency Fees

List all fees related to am account currency.

> List Account Currency Fees request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List Account Currency Fees response

```json
{
    "data": [
        {
            "id": 1,
            "value": 1000,
            "percentage": null,
            "tx_type": "credit",
            "subtype": null,
            "created": 1497431721587,
            "updated": 1497431721587
        }
    ],
    "status": "success"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/`

### Create Account Currency Fee

Create a new fee related to an account currency.

> Create Account Currency Fee request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 1000,
       "tx_type": "credit"}'
```

> Create Account Currency Fee response

```json
{
    "data": {
        "id": 1,
        "value": 1000,
        "percentage": null,
        "tx_type": "credit",
        "subtype": null,
        "created": 1497431721587,
        "updated": 1497431721587
    },
    "status": "success"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`value` | Fee amount | 0 | false
`percentage` | Percentage amount |  | false
`tx_type` | Transaction type fees are applied | | true
`subtype_id` | Transaction subtype ID | null | false

#### Transaction Types

Value | Description 
--- | --- 
`credit` | Credit 
`debit` | Debit

### Retrieve Account Currency fee

Retrieve a specific requirement related to an account currency.

> Retrieve Account Currency Fee request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve Account Currency fee response

```json
{
    "data": {
        "id": 1,
        "value": 1000,
        "percentage": null,
        "tx_type": "credit",
        "subtype": null,
        "created": 1497431721587,
        "updated": 1497431721587
    },
    "status": "success"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}`

### Update Account Currency Fee

Update a specific fees related to an account currency.

> Update Account Currency request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 5000}'
```

> Update Account Currency response

```json
{
    "data": {
        "id": 1,
        "value": 5000,
        "percentage": null,
        "tx_type": "credit",
        "subtype": null,
        "created": 1497431721587,
        "updated": 1497431938971
    },
    "status": "success"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}`

### List Account Currency Switches

List all switches related to the currency

> List Account Currency Switches request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List Account Currency Switches response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "tx_type": "credit",
            "subtype": null,
            "enabled": true,
            "created": 1497362397968,
            "updated": 1497362397968
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/`

### Create Account Currency Switches

Create a new switch for the currency

> Create Account Currency Switches request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"tx_type": "credit",
       "enabled": true}'
```

> Create Account Currency Switches response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "tx_type": "credit",
        "subtype": null,
        "enabled": true,
        "created": 1497362397968,
        "updated": 1497362397968
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`tx_type` | Transaction Type | | true
`subtype_id` | Subtype ID | null | false
`enabled` | Enabled | false | true

### Retrieve Account Currency Switches

Retrieve a specific switch related to the currency

> Retrieve Account Currency Switches request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/{id}
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve Account Currency Switches response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "tx_type": "credit",
        "subtype": null,
        "enabled": true,
        "created": 1497362397968,
        "updated": 1497362397968
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/{id}`

### Update Account Currency Switches

Update a specific switch related to the currency

> Update Account Currency Switches request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/{id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"enabled": false}'
```

> Update Account Currency Switches response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "tx_type": "credit",
        "subtype": null,
        "enabled": false,
        "created": 1497362397968,
        "updated": 1497362931403
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/{id}`

--------------------------------------------------------------------------------

## Currencies

### List Currencies

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

#### Endpoint

`https://rehive.com/api/3/admin/currencies/`

### Create Currency

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

#### Endpoint

`https://rehive.com/api/3/admin/currencies/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`code` | currency code | null | true
`description` | name of currency | null | true
`symbol` | currency symbol | null | true
`unit` | unit, like `dollar` | null | true
`divisibility` | number of decimal places | 0 | true


### Retrieve Currency

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

#### Endpoint

`https://rehive.com/api/3/admin/currencies/{code}/`

### Update Currency

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

#### Endpoint

`https://rehive.com/api/3/admin/currencies/{code}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`code` | currency code | null | true
`description` | name of currency | null | true
`symbol` | currency symbol | null | true
`unit` | unit, like `dollar` | null | true
`divisibility` | number of decimal places | 0 | true
`enabled` | whether active for a company | false | true

--------------------------------------------------------------------------------

## Company

### Retrieve Company

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

#### Endpoint

`https://rehive.com/api/3/admin/company/`

### Update Company

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

#### Endpoint

`https://rehive.com/api/3/admin/company/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | Company Name | blank | false
`description` | Company Description | blank | false
`website` | Company website URL | blank | false
`logo` | Company logo URL | blank | false
`password_reset_url` | Custom company password reset URL | blank | false
`email_confirmation_url` | Custom company email confirmation URL | blank | false
`default_currency` | Default company currency | null | false

### List Company Switches

List all switches related to a company.

> List Company Switches request

```shell
curl https://rehive.com/api/3/admin/company/switches/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List Company Switches response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "tx_type": "credit",
            "subtype": null,
            "enabled": true,
            "created": 1497362397968,
            "updated": 1497362397968
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/company/switches/`

### Create Company Switches

Create switches related to a company.

> Create Company Switches request

```shell
curl https://rehive.com/api/3/admin/company/switches/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"tx_type": "credit",
       "enabled": true}'
```

> Create Company Switches response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "tx_type": "credit",
        "subtype": null,
        "enabled": true,
        "created": 1497362397968,
        "updated": 1497362397968
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/company/switches/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`tx_type` | Transaction Type | | true
`subtype_id` | Subtype ID | null | false
`enabled` | Enabled | false | true

### Retrieve Company Switches

Retrieve a specific switch related to a company.

> Retrieve Company Switches request

```shell
curl https://rehive.com/api/3/admin/company/switches/{id}
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve Company Switches response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "tx_type": "credit",
        "subtype": null,
        "enabled": true,
        "created": 1497362397968,
        "updated": 1497362397968
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/company/switches/{id}`

### Update Company Switches

Update a specific switch related to a company.

> Update Company Switches request

```shell
curl https://rehive.com/api/3/admin/company/switches/{id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"enabled": false}'
```

> Update Company Switches response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "tx_type": "credit",
        "subtype": null,
        "enabled": false,
        "created": 1497362397968,
        "updated": 1497362931403
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/company/switches/{id}`



--------------------------------------------------------------------------------

## Webhooks

### List Webhooks

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
            "tx_type": "debit",
            "secret": "supersecret"
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/webhooks/`

### Create Webhooks

> Create webhooks request

```shell
curl https://rehive.com/api/3/admin/webhooks/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"url": "http://mysite.com/webhook_endpoint",
       "tx_type": "debit",
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
            "tx_type": "debit",
            "secret": "supersecret"
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/webhooks/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`url` | Webhook URL | blank | true
`tx_type` | Transaction type | blank | true
`secret` | Webhook secret | blank | false

### Retrieve Webhook

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
        "tx_type": "debit",
        "secret": "supersecret"
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/webhooks/{id}`

### Update Webhook

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
            "tx_type": "debit",
            "secret": "supersecret"
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/webhooks/{id}`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`url` | Webhook URL | blank | true
`tx_type` | Transaction type | blank | true
`secret` | Webhook secret | blank | false

--------------------------------------------------------------------------------

## Subtypes

### List Subtypes

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
            "name": "credit_subtype",
            "label": "Our credit",
            "description": "Description for our credit",
            "tx_type": "credit",
            "created": "2017-04-28T11:36:57.396723Z",
            "updated": "2017-04-28T11:36:57.396743Z"
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/subtypes/`

### Create subtypes

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
        "name": "credit_subtype",
        "label": "Our credit",
        "description": "Description for our credit",
        "tx_type": "credit",
        "created": "2017-04-28T11:36:57.396723Z",
        "updated": "2017-04-28T11:36:57.396743Z"
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/subtypes/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | name | blank | true
`label` | label | blank | false
`description` | description | blank | false
`tx_type` | Transaction type | blank | true

### Retrieve Subtypes

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
        "name": "credit_subtype",
        "label": "Our credit",
        "description": "Description for our credit",
        "tx_type": "credit",
        "created": "2017-04-28T11:36:57.396723Z",
        "updated": "2017-04-28T11:36:57.396743Z"
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/subtypes/{id}`

### Update subtypes

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
        "name": "credit_subtype",
        "label": "Our credit",
        "description": "New description",
        "tx_type": "credit",
        "created": "2017-04-28T11:36:57.396723Z",
        "updated": "2017-04-28T11:36:57.396743Z"
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/subtypes/{id}`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | name | blank | true
`label` | label | blank | false
`description` | description | blank | false
`tx_type` | Transaction type | blank | true

--------------------------------------------------------------------------------

## Bank Accounts

### List Bank Accounts

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

#### Endpoint

`https://rehive.com/api/3/admin/bank-accounts/`

### Create Bank Account

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

#### Endpoint

`https://rehive.com/api/3/admin/bank-accounts/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | Account Name | blank | false
`number` | Account Number | blank | false
`type` | Account Type | blank | false
`bank_name` | Bank Name | blank | false
`bank_code` | Bank Code | blank | false
`branch_code` | Branch Code | blank | false

### Retrieve Bank Account

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

#### Endpoint

`https://rehive.com/api/3/admin/bank-accounts/{id}`

### Update Bank Account

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

#### Endpoint

`https://rehive.com/api/3/admin/bank-accounts/{id}`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | Account Name | blank | false
`number` | Account Number | blank | false
`type` | Account Type | blank | false
`bank_name` | Bank Name | blank | false
`bank_code` | Bank Code | blank | false
`branch_code` | Branch Code | blank | false

--------------------------------------------------------------------------------

## Notifications

### List Notifications

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
            "name": "tx_debit",
            "description": "Debit transaction notifications",
            "enabled": true
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/notifications/`

### Retrieve Notifications

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
        "name": "tx_debit",
        "description": "Debit transaction notifications",
        "enabled": true
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/notifications/{id}`

### Update Notifications

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
        "name": "tx_debit",
        "description": "Debit transaction notifications",
        "enabled": false
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/notifications/{id}`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`enabled` | Account Name | false | true

--------------------------------------------------------------------------------

## Tiers

Tiers are a way in which to categorise users based on requirements for the tier.
Tiers are set on a currency to limit users' transactions on that currency.

Tiers are checked in ascending order based on their level, with the user getting
validation corresponding to the highest tier they matched. 

### Create Tier

Create a new tier.

> Create Tier request

```shell
curl https://rehive.com/api/3/admin/tiers/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"switch_type": "transactions",
       "enabled": false}'
```

> Create Tier response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "currency": "ZAR",
        "level": 1,
        "name": "First Tier",
        "description": "My First Tier",
        "requirements": [],
        "limits": [],
        "fees": [],
        "switches": [],
        "created": 1497367640298,
        "updated": 1497367640298
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`currency` | Currency code related to this tier | | true
`name` | Name of the tier | blank | false
`description` | Description of the tier | blank | false

### List Tier

List all tiers.

> List Tier request

```shell
curl https://rehive.com/api/3/admin/tiers/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List Tier response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "currency": "ZAR",
            "level": 1,
            "name": "First Tier",
            "description": "My First Tier",
            "requirements": [],
            "limits": [],
            "fees": [],
            "switches": [],
            "created": 1497367640298,
            "updated": 1497367640298
        }
    ]
}
```

#### Filtering

Tiers can be filtered by `currency` as well as `requirement`.
This is done through URL parameters in the request URL:

`/api/3/admin/tiers/?currency=ZAR` 

`/api/3/admin/tiers/?requirement=nationality`

#### Endpoint

`https://rehive.com/api/3/admin/tiers/`

### Retrieve Tier

Retrieve a specific tier.

> Retrieve Tier request

```shell
curl https://rehive.com/api/3/admin/tiers/{id}
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve Tier response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "currency": "ZAR",
        "level": 1,
        "name": "First Tier",
        "description": "My First Tier",
        "requirements": [],
        "limits": [],
        "fees": [],
        "switches": [],
        "created": 1497367640298,
        "updated": 1497367640298
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{id`

### Update Tier

Update the name of description of a tier.

> Update Tier request

```shell
curl https://rehive.com/api/3/admin/tiers/{id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "Updated Name"}'
```

> Update Tier response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "currency": "ZAR",
        "level": 1,
        "name": "Updated Name",
        "description": "My First Tier",
        "requirements": [],
        "limits": [],
        "fees": [],
        "switches": [],
        "created": 1497367640298,
        "updated": 1497369829536
    }
}
```

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | Name of the tier | blank | false
`description` | Description of the tier | blank | false


#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}`

### List Tier Requirements

List all requirements related to a tier.

> List Tier Requirements request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List Tier Requirements response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
            "requirement": "First Name"
        },
        {
            "id": 2,
            "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
            "requirement": "Last Name"
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/`

### Create Tier Requirements

Create a new switch related to a Tier.

> Create Tier Requirements request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"requirement": "birth_date"}'
```

> Create Tier Requirements response

```json
{
    "status": "success",
    "data": {
        "id": 3,
        "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
        "requirement": "Birth Date"
    }
}
```

#### Requirement Types

Value | Description 
--- | --- 
`first_name` | First Name
`last_name` | Last Name
`nationality` | Nationality
`birth_date` | Birth Date
`id_number` | ID Number
`language` | Language
`address` | Address
`bank_account` | Bank Account
`email_address` | Email Address
`mobile_number` | Mobile Number
`proof_of_identity` | Proof of identity
`proof_of_address` | Proof of address
`advanced_proof_of_identity` | Advanced proof of identity

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`requirement` | Requirement Type | | true

### Retrieve Tier Requirements

Retrieve a specific requirement related to a Tier

> Retrieve Tier Requirements request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/{requirement_id}
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve Tier Requirements response

```json
{
    "status": "success",
    "data": {
        "id": 3,
        "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
        "requirement": "Birth Date"
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/{requirement_id}`

### Update Tier Requirements

Update a specific requirement related to a Tier

> Update Tier Requirements request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/{switch_id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"enabled": "proof_of_identity"}'
```

> Update Tier Requirements response

```json
{
    "status": "success",
    "data": {
        "id": 3,
        "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
        "requirement": "Proof Of Identity"
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/{requirement_id}`

### List Tier Limits

List all Limits related to a tier.

> List Tier Limits request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/limits/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List Tier Limits response

```json
  {
    "status": "success",
    "data": [
        {
            "id": 1,
            "value": 1000,
            "type": "Maximum",
            "tx_type": "credit",
            "subtype": null,
            "created": 1497374071027,
            "updated": 1497374071027
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/limits/`

### Create Tier Limits

Create a new limit related to a Tier.

> Create Tier Limits request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/limits/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"requirement": "birth_date"}'
```

> Create Tier Limits response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "value": 1000,
        "type": "Maximum",
        "tx_type": "credit",
        "subtype": null,
        "created": 1497374071027,
        "updated": 1497374071027
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`value` | Limit value | 0 | true
`type` | Limit Type |  | true
`tx_type` | Transaction type limits are applied | | true
`subtype_id` | Transaction subtype ID | null | false

#### Limit Types

Value | Description 
--- | --- 
`max` | Maximum 
`day_max` | Maximum per day 
`month_max` | Maximum per month 
`min` | Minimum 

#### Transaction Types

Value | Description 
--- | --- 
`credit` | Credit 
`debit` | Debit

### Retrieve Tier Limits

Retrieve a specific requirement related to a Tier

> Retrieve Tier Limits request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/limits/{limit_id}
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve Tier Limits response

```json
{
    "data": {
        "id": 1,
        "value": 1000,
        "type": "Maximum",
        "tx_type": "credit",
        "subtype": null,
        "created": 1497374071027,
        "updated": 1497374071027
    },
    "status": "success"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/limits/{limits_id}`

### Update Tier Limits

Update a specific limits related to a Tier

> Update Tier Limits request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/limits/{switch_id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 5000,
       "type": "min"}'
```

> Update Tier Limits response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "value": 5000,
        "type": "Minimum",
        "tx_type": "credit",
        "subtype": null,
        "created": 1497374071027,
        "updated": 1497374886088
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/limits/{limits_id}`

### List Tier Fees

List all fees related to a Tier.

> List Tier Fees request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/fees/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List Tier Fees response

```json
{
    "data": [
        {
            "id": 1,
            "value": 1000,
            "percentage": null,
            "tx_type": "credit",
            "subtype": null,
            "created": 1497431721587,
            "updated": 1497431721587
        }
    ],
    "status": "success"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/fees/`

### Create Tier Fee

Create a new fee related to a Tier.

> Create Tier Fee request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/fees/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 1000,
       "tx_type": "credit"}'
```

> Create Tier Fee response

```json
{
    "data": {
        "id": 1,
        "value": 1000,
        "percentage": null,
        "tx_type": "credit",
        "subtype": null,
        "created": 1497431721587,
        "updated": 1497431721587
    },
    "status": "success"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/fees/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`value` | Fee amount | 0 | false
`percentage` | Percentage amount |  | false
`tx_type` | Transaction type fees are applied | | true
`subtype_id` | Transaction subtype ID | null | false

#### Transaction Types

Value | Description 
--- | --- 
`credit` | Credit 
`debit` | Debit

### Retrieve Tier fee

Retrieve a specific requirement related to a Tier.

> Retrieve Tier Fee request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/fees/{fee_id}
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve Tier Fee response

```json
{
    "data": {
        "id": 1,
        "value": 1000,
        "percentage": null,
        "tx_type": "credit",
        "subtype": null,
        "created": 1497431721587,
        "updated": 1497431721587
    },
    "status": "success"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/fees/{fee_id}`

### Update Tier Fee

Update a specific fees related to a Tier.

> Update Tier request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/fees/{fee_id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 5000}'
```

> Update Tier response

```json
{
    "data": {
        "id": 1,
        "value": 5000,
        "percentage": null,
        "tx_type": "credit",
        "subtype": null,
        "created": 1497431721587,
        "updated": 1497431938971
    },
    "status": "success"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/fees/{fee_id}`

### List Tier Switches

List all switches related to a tier.

> List Tier Switches request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/switches/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List Tier Switches response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "tx_type": "credit",
            "subtype": null,
            "enabled": true,
            "created": 1497370313086,
            "updated": 1497370313086
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/switches/`

### Create Tier Switches

Create a new switch related to a Tier.

> Create Tier Switches request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/switches/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"tx_type": "credit",
       "enabled": true}'
```

> Create Tier Switches response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "tx_type": "credit",
        "subtype": null,
        "enabled": true,
        "created": 1497370313086,
        "updated": 1497370313086
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/switches/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`tx_type` | Transaction Type | | true
`subtype_id` | Subtype ID | null | false
`enabled` | Enabled | false | true

### Retrieve Tier Switches

Retrieve a specific switch related to a Tier

> Retrieve Tier Switches request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/switches/{switch_id}
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve Tier Switches response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "tx_type": "credit",
        "subtype": null,
        "enabled": true,
        "created": 1497370313086,
        "updated": 1497370313086
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/switches/{switch_id}`

### Update Tier Switches

Update a specific switch related to a Tier

> Update Tier Switches request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/switches/{switch_id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"enabled": false}'
```

> Update Tier Switches response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "tx_type": "credit",
        "subtype": null,
        "enabled": true,
        "created": 1497370313086,
        "updated": 1497370313086
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/switches/{switch_id}`

--------------------------------------------------------------------------------

## Switches

Switches are a way to determine which actions are allowed to the users in terms of transactions.

Global switches are the highest level switches by overriding any switches that are
set on a user, company, currency or tier level.

### Create Global Switches

Create a new global switch.

> Create Global Switches request

```shell
curl https://rehive.com/api/3/admin/switches/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"switch_type": "transactions",
       "enabled": false}'
```

> Create Global Switches response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "company": {
            "identifier": "test_company_1",
            "name": "Test Company 1",
            "description": "Wallets for everyone.",
            "website": "http://wwww.rehive.io",
            "logo": null
        },
        "switch_type": "Allow transactions",
        "enabled": false,
        "created": 1497348308625,
        "updated": 1497348318654
    }
}
```

#### Types
Global switches can be one of the following 2 types.

Value | Description
--- | ---
`transactions` | Allow transactions
`verification` | Allow transactions for unverified users

#### Endpoint

`https://rehive.com/api/3/admin/switches/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`switch_type` | Global Switch Type Label | | true
`enabled` | Account Name | false | true

### List Global Switches

List all the global switches.

> List Global Switches request

```shell
curl https://rehive.com/api/3/admin/switches/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List Global Switches response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "company": {
                "identifier": "test_company_1",
                "name": "Test Company 1",
                "description": "Wallets for everyone.",
                "website": "http://wwww.rehive.io",
                "logo": null
            },
            "switch_type": "Allow transactions",
            "enabled": true,
            "created": 1497347723605,
            "updated": 1497347723605
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/switches/`

### Retrieve Global Switches

Retrieve a specific global switch.

> Retrieve Global Switches request

```shell
curl https://rehive.com/api/3/admin/switches/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve Global Switches response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "company": {
            "identifier": "test_company_1",
            "name": "Test Company 1",
            "description": "Wallets for everyone.",
            "website": "http://wwww.rehive.io",
            "logo": null
        },
        "switch_type": "Allow transactions",
        "enabled": true,
        "created": 1497347723605,
        "updated": 1497347723605
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/switches/{id}`

### Update Global Switches

Update a specific global switch.

> Update Global Switches request

```shell
curl https://rehive.com/api/3/admin/switches/{id}
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"enabled": false}'
```

> Update Global Switches response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "company": {
            "identifier": "test_company_1",
            "name": "Test Company 1",
            "description": "Wallets for everyone.",
            "website": "http://wwww.rehive.io",
            "logo": null
        },
        "switch_type": "Allow transactions",
        "enabled": false,
        "created": 1497348308625,
        "updated": 1497348318654
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/switches/{id}`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`switch_type` | Global Switch Type | | false
`enabled` | Account Name | false | false

--------------------------------------------------------------------------------
