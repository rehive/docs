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

```python
rehive.accounts.create(
    name="savings"
)
```


> User create account response

```shell
{
    "status": "success",
    "data": {
        "name": "savings",
        "reference": "0000000000",
        "primary": false,
        "currencies": [],
        "created": 1501145581365,
        "updated": 1501145581370
    },
}
```

```python
{
    "name": "savings",
    "reference": "0000000000",
    "primary": false,
    "currencies": [],
    "created": 1501145581365,
    "updated": 1501145581370
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

```python
#Filters are not required
filters = {
    "active":True
}
rehive.accounts.get(
    filters=filters
)
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
                "primary": true,
                "currencies": [
                    {
                        "balance": 10000,
                        "available_balance": 10000,
                        "currency": {
                            "code": "XBT",
                            "description": "bitcoin",
                            "symbol": "฿",
                            "unit": "bitcoin",
                            "divisibility": 8
                        },
                        "limits": [],
                        "fees": [],
                        "switches": [],
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
            "primary": true,
            "currencies": [
                {
                    "balance": 10000,
                    "available_balance": 10000,
                    "currency": {
                        "code": "XBT",
                        "description": "bitcoin",
                        "symbol": "฿",
                        "unit": "bitcoin",
                        "divisibility": 8
                    },
                    "limits": [],
                    "fees": [],
                    "switches": [],
                    "active": true
                }
            ],
            "created": 1464858068745,
            "updated": 1464858068745
        }
    ]
}
```

```python
[
    {
        "name": "default",
        "reference": "0000000000",
        "primary": true,
        "currencies": [
            {
                "balance": 10000,
                "available_balance": 10000,
                "currency": {
                    "code": "XBT",
                    "description": "bitcoin",
                    "symbol": "฿",
                    "unit": "bitcoin",
                    "divisibility": 8
                },
                "limits": [],
                "fees": [],
                "switches": [],
                "active": true
            }
        ],
        "created": 1464858068745,
        "updated": 1464858068745
    }
]
```

Get a list of accounts belonging to a user.

#### Filtering

Field | Type 
--- | --- 
`reference` | string
`name` | string
`active` | boolean 
`primary` | boolean

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

```python
rehive.accounts.get(
    "{reference}"
)
```

> User retrieve account response

```shell
{
    "status": "success",
    "data": {
        "name": "default",
        "reference": "0000000000",
        "primary": true,
        "currencies": [
            {
                "balance": 10000,
                "available_balance": 10000,
                "currency": {
                    "code": "XBT",
                    "description": "bitcoin",
                    "symbol": "฿",
                    "unit": "bitcoin",
                    "divisibility": 8
                },
                "limits": [],
                "fees": [],
                "switches": [],
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
    "primary": true,
    "currencies": [
        {
            "balance": 10000,
            "available_balance": 10000,
            "currency": {
                "code": "XBT",
                "description": "bitcoin",
                "symbol": "฿",
                "unit": "bitcoin",
                "divisibility": 8
            },
            "limits": [],
            "fees": [],
            "switches": [],
            "active": true
        }
    ],
    "created": 1464858068745,
    "updated": 1464858068745
}
```

```python
{
    "name": "default",
    "reference": "0000000000",
    "primary": true,
    "currencies": [
        {
            "balance": 10000,
            "available_balance": 10000,
            "currency": {
                "code": "XBT",
                "description": "bitcoin",
                "symbol": "฿",
                "unit": "bitcoin",
                "divisibility": 8
            },
            "limits": [],
            "fees": [],
            "switches": [],
            "active": true
        }
    ],
    "created": 1464858068745,
    "updated": 1464858068745
}
```

Retrieve an account belonging to a user.

#### Filtering

Field | Type 
--- | --- 
`active` | boolean 

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

```python
rehive.accounts.update(
    "{reference}",
    name="savings"
)
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

```python
{
    "name": "savings",
    "reference": "0000000000",
    "primary": true,
    "currencies": [],
    "created": 1501145581365,
    "updated": 1501145581370
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

```python
rehive.accounts.obj("{reference}").currencies.get()
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
                "available_balance": 10000,
                "currency": {
                    "code": "XBT",
                    "description": "bitcoin",
                    "symbol": "฿",
                    "unit": "bitcoin",
                    "divisibility": 8
                },
                "limits": [],
                "fees": [],
                "switches": [],
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
            "available_balance": 10000,
            "currency": {
                "code": "XBT",
                "description": "bitcoin",
                "symbol": "฿",
                "unit": "bitcoin",
                "divisibility": 8
            },
            "limits": [],
            "fees": [],
            "switches": [],
            "active": true
        }
    ]

}
```

```python
[
    {
        "balance": 10000,
        "available_balance": 10000,
        "currency": {
            "code": "XBT",
            "description": "bitcoin",
            "symbol": "฿",
            "unit": "bitcoin",
            "divisibility": 8
        },
        "limits": [],
        "fees": [],
        "switches": [],
        "active": true
    }
]
```

Get a list of currencies for an account belonging to a user.

#### Filtering

Field | Type 
--- | --- 
`active` | boolean

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

```python
rehive.accounts.obj("{reference}").currencies.get(
    "{code}"
)
```

> User retrieve account currency response

```shell
{
    "status": "success",
    "data": {
        "balance": 10000,
        "available_balance": 10000,
        "currency": {
            "code": "XBT",
            "description": "bitcoin",
            "symbol": "฿",
            "unit": "bitcoin",
            "divisibility": 8
        },
        "limits": [],
        "fees": [],
        "switches": [],
        "active": true
    }
}
```

```javascript
{
    "balance": 10000,
    "available_balance": 10000,
    "currency": {
        "code": "XBT",
        "description": "bitcoin",
        "symbol": "฿",
        "unit": "bitcoin",
        "divisibility": 8
    },
    "limits": [],
    "fees": [],
    "switches": [],
    "active": true
}
```

```python
{
    "balance": 10000,
    "available_balance": 10000,
    "currency": {
        "code": "XBT",
        "description": "bitcoin",
        "symbol": "฿",
        "unit": "bitcoin",
        "divisibility": 8
    },
    "limits": [],
    "fees": [],
    "switches": [],
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

```python
rehive.accounts.obj("{reference}").currencies.update(
    "{code}",
    active=True
)

# Quick method for setting active
rehive.accounts.obj("{reference}").currencies.make_active_currency(
    "{code}"
)
```

> User retrieve account currency response

```shell
{
    "status": "success",
    "data": {
        "balance": 10000,
        "available_balance": 10000,
        "currency": {
            "code": "XBT",
            "description": "bitcoin",
            "symbol": "฿",
            "unit": "bitcoin",
            "divisibility": 8
        },
        "limits": [],
        "fees": [],
        "switches": [],
        "active": true
    }
}
```

```javascript
{
    "balance": 10000,
    "available_balance": 10000,
    "currency": {
        "code": "XBT",
        "description": "bitcoin",
        "symbol": "฿",
        "unit": "bitcoin",
        "divisibility": 8
    },
    "limits": [],
    "fees": [],
    "switches": [],
    "active": true
}
```

```python
{
    "balance": 10000,
    "available_balance": 10000,
    "currency": {
        "code": "XBT",
        "description": "bitcoin",
        "symbol": "฿",
        "unit": "bitcoin",
        "divisibility": 8
    },
    "limits": [],
    "fees": [],
    "switches": [],
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
