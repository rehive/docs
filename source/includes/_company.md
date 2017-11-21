# Company

## Retrieve Company Details

> User retrieve company details request

```shell
curl https://www.rehive.com/api/3/company/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.company.getCompanyDetails().then(function(res){
        // ...
    },function(err){
        // ...
    })
```

```python
rehive.company.get()
```

> User retrieve company details response

```shell
{
    "data": {
        "identifier": "rehive",
        "name": "Rehive",
        "description": "Wallets for everyone.",
        "website": "http://www.rehive.com",
        "nationalities": ["US", "ZA"]
        "logo": null
    },
    "status": "success"
}
```

```javascript
{
    "identifier": "rehive",
    "name": "Rehive",
    "description": "Wallets for everyone.",
    "website": "http://www.rehive.com",
    "logo": null,
    "nationalities":[]
}
```

```python
{
    "identifier": "rehive",
    "name": "Rehive",
    "description": "Wallets for everyone.",
    "website": "http://www.rehive.com",
    "nationalities": ["US", "ZA"]
    "logo": null
}
```

Retrieve current user's company details.

#### Endpoint

`https://rehive.com/api/3/company/`

## List Company Currencies

> User list company currencies request

```shell
curl https://www.rehive.com/api/3/company/currencies/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.company.getCompanyCurrencies().then(function(res){
        // ...
    },function(err){
        // ...
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
                "divisibility": 8
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
            "divisibility": 8
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
        "divisibility": 8
    }
]
```

Get a list of available currencies for the current user's company.

#### Endpoint

`https://rehive.com/api/3/company/currencies/`

## List Company Banks

> User list company banks request

```shell
curl https://www.rehive.com/api/3/company/bank-account/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.company.getCompanyBanks().then(function(res){
        // ...
    },function(err){
        // ...
    })
```

```python
rehive.company.bank_account.get()
```

> User list company banks response

```shell
{
    "status": "success",
    "data": [
        {
            "id": 53,
            "token": 1,
            "bank_account": {
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
            },
            "reference": "xxxxxxxxxx"
        }
    ]
}
```

```javascript
[
    {
        "id": 53,
        "token": 1,
        "bank_account": {
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
        },
        "reference": "xxxxxxxxxx"
    }
]
```

```python
[
    {
        "id": 53,
        "token": 1,
        "bank_account": {
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
        },
        "reference": "xxxxxxxxxx"
    }
]
```

List company banks for the current user's company.

#### Endpoint

`https://rehive.com/api/3/company/bank-account/`
