# Company

## Retrieve Company Details

> User retrieve company details request

```shell
curl https://api.rehive.com/3/company/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.company.get().then(function(res){
    ...
},function(err){
    ...
})
```

```python
rehive.company.get()
```

> User retrieve company details response

```shell
{
    "data": {
        "id": "rehive",
        "name": "Rehive",
        "description": "Wallets for everyone.",
        "website": "http://www.rehive.com",
        "email": null,
        "logo": "https://path.to.file.com/image.png",
        "address": {
            "line_1": "1 First Avenue",
            "line_2": "",
            "city": "Cape Town",
            "state_province": "Western Cape",
            "country": "ZA",
            "postal_code": "8001"
        },
        "settings": {
            "allow_transactions": true,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true,
            "require_verification": false,
            "allow_registrations": true,
            "allow_overdrafts": false,
            "allow_session_durations": false,
            "require_terms_and_conditions": false,
            "default_transaction_status": "Pending",
            "password_reset_url": "",
            "password_set_url": "",
            "email_confirmation_url": "",
            "nationalities": []
        },
        "created": 1516281408895,
        "updated": 1528454842365
    },
    "status": "success"
}
```

```javascript
{
    "id": "rehive",
    "name": "Rehive",
    "description": "Wallets for everyone.",
    "website": "http://www.rehive.com",
    "email": null,
    "logo": "https://path.to.file.com/image.png",
    "address": {
        "line_1": "1 First Avenue",
        "line_2": "",
        "city": "Cape Town",
        "state_province": "Western Cape",
        "country": "ZA",
        "postal_code": "8001"
    },
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true,
        "require_verification": false,
        "allow_registrations": true,
        "allow_overdrafts": false,
        "allow_session_durations": false,
        "require_terms_and_conditions": false,
        "default_transaction_status": "Pending",
        "password_reset_url": "",
        "password_set_url": "",
        "email_confirmation_url": "",
        "nationalities": []
    },
    "created": 1516281408895,
    "updated": 1528454842365
}
```

```python
{
    "id": "rehive",
    "name": "Rehive",
    "description": "Wallets for everyone.",
    "website": "http://www.rehive.com",
    "email": null,
    "logo": "https://path.to.file.com/image.png",
    "address": {
        "line_1": "1 First Avenue",
        "line_2": "",
        "city": "Cape Town",
        "state_province": "Western Cape",
        "country": "ZA",
        "postal_code": "8001"
    },
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true,
        "require_verification": false,
        "allow_registrations": true,
        "allow_overdrafts": false,
        "allow_session_durations": false,
        "require_terms_and_conditions": false,
        "default_transaction_status": "Pending",
        "password_reset_url": "",
        "password_set_url": "",
        "email_confirmation_url": "",
        "nationalities": []
    },
    "created": 1516281408895,
    "updated": 1528454842365
}
```

Retrieve current user's company details.

#### Endpoint

`https://api.rehive.com/3/company/`

## List Company Currencies

> User list company currencies request

```shell
curl https://api.rehive.com/3/company/currencies/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.company.currencies.get().then(function(res){
    ...
},function(err){
    ...
})
```

```python
rehive.company.currencies.get()
```

> User list company currencies response

```shell
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
                "divisibility": 8,
                "created": 1516281408895,
                "updated": 1528454842365
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
            "code": "XBT",
            "description": "bitcoin",
            "symbol": "฿",
            "unit": "bitcoin",
            "divisibility": 8,
            "created": 1516281408895,
            "updated": 1528454842365
        }
    ]
}
```

```python
[
    {
        "code": "XBT",
        "description": "bitcoin",
        "symbol": "฿",
        "unit": "bitcoin",
        "divisibility": 8,
        "created": 1516281408895,
        "updated": 1528454842365
    }
]
```

Get a list of available currencies for the current user's company.

#### Endpoint

`https://api.rehive.com/3/company/currencies/`

## List Company Banks

> User list company banks request

```shell
curl https://api.rehive.com/3/company/bank-accounts/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
```

```python
rehive.company.bank_accounts.get()
```

> User list company banks response

```shell
{
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
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
                "currencies": [
                    {
                        "code": "ZAR",
                        "description": "Rand",
                        "symbol": "R",
                        "unit": "rand",
                        "divisibility": 2
                    }
                ],
                "created": 1516281408895,
                "updated": 1528454842365
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
        "currencies": [
            {
                "code": "ZAR",
                "description": "Rand",
                "symbol": "R",
                "unit": "rand",
                "divisibility": 2
            }
        ]
    }
]
```

List company banks for the current user's company.

#### Filtering

Field | Type
--- | ---
`currency` | string

#### Endpoint

`https://api.rehive.com/3/company/bank-accounts/`
