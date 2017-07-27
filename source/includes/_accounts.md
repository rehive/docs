# Accounts

## Create Account

> User create account request

```shell
curl https://www.rehive.com/api/3/accounts/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"name": "savings"}'
```

> User create account response

```shell
{
    "status": "success",
    "data": {
        "name": "savings",
        "reference": "0000000000",
        "primary": true,
        "currencies": [],
        "created": 1501145581365,
        "updated": 1501145581370
    },
}
```

Create a account for a user.

<aside class="notice">
Users cannot manage their accounts (create or update) by default. In order to 
enable account management for users please set the corresponding global company 
switch. 
</aside>

#### Endpoint

`https://rehive.com/api/3/accounts/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | account name | null | true
`primary` | account primary status | false | false


## List Accounts

> User list accounts request

```shell
curl https://www.rehive.com/api/3/accounts/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
var filter = {active:true};

rehive.accounts.getAccountsList(filter).then(function(res){
        // ...
    },function(err){
        // ...
    })
```

> User list accounts response

```shell
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

```javascript
{
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
```

Get a list of accounts belonging to a user.

#### Pagination

The list is paginated and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

#### Filtering

The account listing offers filtering on the `active` attribute. This is done through a URL parameter in the request URL:

`/api/3/accounts/?active=true`

#### Endpoint

`https://rehive.com/api/3/accounts/`

## Retrieve Account

> User retrieve account request

```shell
curl https://www.rehive.com/api/3/accounts/{reference}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
var filter = {active:true}

rehive.accounts.getAccount(reference,filter).then(function(res){
        // ...
    },function(err){
        // ...
    })
```

> User retrieve account response

```shell
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

```javascript
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
```

Retrieve an account belonging to a user.

#### Filtering

The account view offers filtering of currencies based on the `active` attribute. This is done through a URL parameter in the request URL:

`/api/3/accounts/{reference}/?active=true`

#### Endpoint

`https://rehive.com/api/3/accounts/{reference}/`


## Update Account

> User update account request

```shell
curl https://www.rehive.com/api/3/accounts/{reference}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"name": "savings"}'
```

> User update account response

```shell
{
    "status": "success",
    "data": {
        "name": "savings",
        "reference": "0000000000",
        "primary": true,
        "currencies": [],
        "created": 1501145581365,
        "updated": 1501145581370
    },
}
```

Update an account for a user.

<aside class="notice">
Users cannot manage their accounts (create or update) by default. In order to 
enable account management for users please set the corresponding global company 
switch. 
</aside>

#### Endpoint

`https://rehive.com/api/3/accounts/{reference}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | account name | null | true
`primary` | account primary status | false | false


## List Account Currencies

> User list account currencies request

```shell
curl https://www.rehive.com/api/3/accounts/{reference}/currencies/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
var filter = {active:true}

rehive.accounts.getAccountCurrenciesList(reference,filter).then(function(res){
        // ...
    },function(err){
        // ...
    })
```

> User list account currencies response

```shell
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

```javascript
{
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
```

Get a list of currencies for an account belonging to a user.

#### Pagination

The list is paginated and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

#### Filtering

The account currency listing offers filtering on the `active` attribute. This is done through a URL parameter in the request URL:

`/api/3/accounts/{reference}/currencies/?active=true`

#### Endpoint

`https://rehive.com/api/3/accounts/{reference}/currencies/`

## Retrieve Account Currency

> User retrieve account currency request

```shell
curl https://www.rehive.com/api/3/accounts/{reference}/currencies/{code}
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.accounts.getAccountCurrency(reference,currencyCode).then(function(res){
        // ...
    },function(err){
        // ...
    })
```

> User retrieve account currency response

```shell
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

```javascript
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
```

Retrieve an account's currency belonging to a user.

#### Endpoint

`https://rehive.com/api/3/accounts/{reference}/currencies/{code}`

## Update Account Currency

> User retrieve account currency request

```shell
curl https://www.rehive.com/api/3/accounts/{reference}/currencies/{code}
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"active": true}'
```

```javascript
rehive.accounts.updateAccountCurrency(reference,currencyCode,{active: true}).then(function(res){
        // ...
    },function(err){
        // ...
    })
```

> User retrieve account currency response

```shell
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

```javascript
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
```

Update the active status of an account currency. Activating an account's currency will result in that currency getting used by default for all transactions if no other account/currency is specified.

#### Endpoint

`https://rehive.com/api/3/accounts/{reference}/currencies/{code}`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`active` | is active currency | false | false
