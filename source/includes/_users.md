# Users

All non authentication access on the Rehive API is made by registered users. This is true of the orginal company owner
as well as all subsequent users (whether granted admin permissions or not). The user endpoints provide a means to 
add, alter and view additional user information.

<aside class="notice">
All user's are loosely intgrated with the concept of KYC. This includes several features for making it easier to see
how far a user is in the KYC process: KYC statuses on user data (`obsolete`, `declined`, `pending`, `incomplet`, `verified`) 
verification for email addresses and mobile numbers, KYC summaries (under the `kyc` attribute) on top level user objects. 
The KYC summary is a useful tool to see what parts of a user's profile have been added, when the data was lasst updated 
and whether they have an apporiate status.
</aside>

## Retrieve Profile

> User profile request

```shell
curl https://www.rehive.com/api/3/user/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.user.get().then(function(user){
    ...
},function(err){
    ...
})
```

```python
rehive.user.get()
```

> User profile response

```shell
{
    "status": "success",
    "data": {
        "identifier": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": "",
        "id_number": null,
        "birth_date": null,
        "profile": null,
        "currency": null,
        "company": "rehive",
        "language": "en",
        "nationality": "ZA",
        "metadata": {},
        "mobile_number": "+00000000000",
        "timezone": null,
        "verified": false,
        "kyc": {
            "documents": {
                "updated": null,
                "status": null
            },
            "updated": 1509539801040,
            "status": "pending",
            "bank_accounts": {
                "updated": null,
                "status": null
            },
            "addresses": {
                "updated": null,
                "status": null
            }
        },
        "status": "pending",
        "permission_groups": [
            {
                "name": "admin"
            }
        ],
        "permissions": [],
        "date_joined": 1509539800952,
        "switches": []
    }
}
```

```javascript
{
    "identifier": "00000000-0000-0000-0000-000000000000",
    "first_name": "Joe",
    "last_name": "Soap",
    "email": "joe@rehive.com",
    "username": "",
    "id_number": null,
    "birth_date": null,
    "profile": null,
    "currency": null,
    "company": "rehive",
    "language": "en",
    "nationality": "ZA",
    "metadata": {},
    "mobile_number": "+00000000000",
    "timezone": null,
    "verified": false,
    "kyc": {
        "documents": {
            "updated": null,
            "status": null
        },
        "updated": 1509539801040,
        "status": "pending",
        "bank_accounts": {
            "updated": null,
            "status": null
        },
        "addresses": {
            "updated": null,
            "status": null
        }
    },
    "status": "pending",
    "permission_groups": [
        {
            "name": "admin"
        }
    ],
    "permissions": [],
    "date_joined": 1509539800952,
    "switches": []
}
```

```python
{
    "identifier": "00000000-0000-0000-0000-000000000000",
    "first_name": "Joe",
    "last_name": "Soap",
    "email": "joe@rehive.com",
    "username": "",
    "id_number": null,
    "birth_date": null,
    "profile": null,
    "currency": null,
    "company": "rehive",
    "language": "en",
    "nationality": "ZA",
    "metadata": {},
    "mobile_number": "+00000000000",
    "timezone": null,
    "verified": false,
    "kyc": {
        "documents": {
            "updated": null,
            "status": null
        },
        "updated": 1509539801040,
        "status": "pending",
        "bank_accounts": {
            "updated": null,
            "status": null
        },
        "addresses": {
            "updated": null,
            "status": null
        }
    },
    "status": "pending",
    "permission_groups": [
        {
            "name": "admin"
        }
    ],
    "permissions": [],
    "date_joined": 1509539800952,
    "switches": []
}
```

Retrieve a user's profile information.

#### Endpoint

`https://rehive.com/api/3/user/`

## Update Profile

> User update profile request

```shell
curl https://www.rehive.com/api/3/user/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"first_name": "Joe"}'
```

```javascript
rehive.user.update({first_name: "Joe"}).then(function (user) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.update(
    first_name="Joe"
)
```

> User update profile response

```shell
{
    "status": "success",
    "data": {
        "identifier": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": "",
        "id_number": null,
        "birth_date": null,
        "profile": null,
        "currency": null,
        "company": "rehive",
        "language": "en",
        "nationality": "ZA",
        "metadata": {},
        "mobile_number": "+00000000000",
        "timezone": null,
        "verified": false,
        "kyc": {
            "documents": {
                "updated": null,
                "status": null
            },
            "updated": 1509539801040,
            "status": "pending",
            "bank_accounts": {
                "updated": null,
                "status": null
            },
            "addresses": {
                "updated": null,
                "status": null
            }
        },
        "status": "pending",
        "permission_groups": [
            {
                "name": "admin"
            }
        ],
        "permissions": [],
        "date_joined": 1509539800952,
        "switches": []
    }
}
```

```javascript
{
    "identifier": "00000000-0000-0000-0000-000000000000",
    "first_name": "Joe",
    "last_name": "Soap",
    "email": "joe@rehive.com",
    "username": "",
    "id_number": null,
    "birth_date": null,
    "profile": null,
    "currency": null,
    "company": "rehive",
    "language": "en",
    "nationality": "ZA",
    "metadata": {},
    "mobile_number": "+00000000000",
    "timezone": null,
    "verified": false,
    "kyc": {
        "documents": {
            "updated": null,
            "status": null
        },
        "updated": 1509539801040,
        "status": "pending",
        "bank_accounts": {
            "updated": null,
            "status": null
        },
        "addresses": {
            "updated": null,
            "status": null
        }
    },
    "status": "pending",
    "permission_groups": [
        {
            "name": "admin"
        }
    ],
    "permissions": [],
    "date_joined": 1509539800952,
    "switches": []
}
```

```python
{
    "identifier": "00000000-0000-0000-0000-000000000000",
    "first_name": "Joe",
    "last_name": "Soap",
    "email": "joe@rehive.com",
    "username": "",
    "id_number": null,
    "birth_date": null,
    "profile": null,
    "currency": null,
    "company": "rehive",
    "language": "en",
    "nationality": "ZA",
    "metadata": {},
    "mobile_number": "+00000000000",
    "timezone": null,
    "verified": false,
    "kyc": {
        "documents": {
            "updated": null,
            "status": null
        },
        "updated": 1509539801040,
        "status": "pending",
        "bank_accounts": {
            "updated": null,
            "status": null
        },
        "addresses": {
            "updated": null,
            "status": null
        }
    },
    "status": "pending",
    "permission_groups": [
        {
            "name": "admin"
        }
    ],
    "permissions": [],
    "date_joined": 1509539800952,
    "switches": []
}
```

Update a user's profile information.

#### Endpoint

`https://rehive.com/api/3/user/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`first_name` | first name | blank
`last_name` | last name | blank
`id_number` | ID number | blank
`profile` | profile image | blank
`language` | language code (`af`, `en` etc.) | blank
`nationality` | nationality code (`ZA`, `UK` etc.) | blank
`metadata` | custom metadata | {}
`mobile_number` | mobile number | blank
`timezone` | timezone | blank
`birth_date` | birth date | blank

<aside class="notice">
    <code>birth_date</code> should be added in the formal yyyy-mm-dd
</aside>

## Retrieve Address

> User retrieve address request

```shell
curl https://www.rehive.com/api/3/user/address/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.user.address.get().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.address.get()
```

> User retrieve address response

```shell
{
    "status": "success",
    "data": {
        "line_1": "1 Main Street",
        "line_2": "East City",
        "city": "Cape Town",
        "state_province": "Western Cape",
        "country": "ZA",
        "postal_code": "8001",
        "status": "pending"
    }
}
```

```javascript
{
    "line_1": "1 Main Street",
    "line_2": "East City",
    "city": "Cape Town",
    "state_province": "Western Cape",
    "country": "ZA",
    "postal_code": "8001",
    "status": "pending"
}
```

```python
{
    "line_1": "1 Main Street",
    "line_2": "East City",
    "city": "Cape Town",
    "state_province": "Western Cape",
    "country": "ZA",
    "postal_code": "8001",
    "status": "pending"
}
```

Retrieve a user's address.

#### Endpoint

`https://rehive.com/api/3/user/address/`

## Update Address

> User update address request

```shell
curl https://www.rehive.com/api/3/user/address/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"city": "Cape Town"}'
```

```javascript
rehive.user.address.update({city: "Cape Town"}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.address.update(
    city="Cape Town"
)
```

> User update address response

```shell
{
    "status": "success",
    "data": {
        "line_1": "1 Main Street",
        "line_2": "East City",
        "city": "Cape Town",
        "state_province": "Western Cape",
        "country": "ZA",
        "postal_code": "8001",
        "status": "pending"
    }
}
```

```javascript
{
    "line_1": "1 Main Street",
    "line_2": "East City",
    "city": "Cape Town",
    "state_province": "Western Cape",
    "country": "ZA",
    "postal_code": "8001",
    "status": "pending"
}
```

```python
{
    "line_1": "1 Main Street",
    "line_2": "East City",
    "city": "Cape Town",
    "state_province": "Western Cape",
    "country": "ZA",
    "postal_code": "8001",
    "status": "pending"
}
```

Update a user's address.

#### Endpoint

`https://rehive.com/api/3/user/address/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`line_1` | address line one | blank
`line_2` | address line 2 | blank
`city` | city | blank
`state_province` | state or province | blank
`country` | country code | blank
`postal_code` | postal or zip code) | blank


## List Bank Accounts

> User list bank accounts request

```shell
curl https://www.rehive.com/api/3/user/bank-accounts/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.user.bankAccounts.get().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.bank_accounts.get()
```

> User list bank accounts response

```shell
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "name": "Default",
            "number": "9999999999",
            "type": "Cheque",
            "bank_name": "Central Bank",
            "bank_code": "0000",
            "branch_code": "0000",
            "swift": "",
            "iban": "",
            "bic": "",
            "code": "bank_account_VEM7k1y5hnuF",
            "status": "pending"
        }
    ]
}
```

```javascript
[
    {
        "id": 1,
        "name": "Default",
        "number": "9999999999",
        "type": "Cheque",
        "bank_name": "Central Bank",
        "bank_code": "0000",
        "branch_code": "0000",
        "swift": "",
        "iban": "",
        "bic": "",
        "code": "bank_account_VEM7k1y5hnuF",
        "status": "pending"
    }
]

```

```python
[
    {
        "id": 1,
        "name": "Default",
        "number": "9999999999",
        "type": "Cheque",
        "bank_name": "Central Bank",
        "bank_code": "0000",
        "branch_code": "0000",
        "swift": "",
        "iban": "",
        "bic": "",
        "code": "bank_account_VEM7k1y5hnuF",
        "status": "pending"
    }
]
```

List a user's bank accounts.

#### Endpoint

`https://rehive.com/api/3/user/bank-accounts/`

## Create Bank Account

> User create bank account request

```shell
curl https://www.rehive.com/api/3/user/bank-accounts/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"name": "Bank",
       "number": "000000000000000",
       "type": "Cheque",
       "bank_name": "Bank Ltd.",
       "branch_code": "0000"}'
```

```javascript
rehive.user.bankAccounts.create(
{
    name: "Bank",
    number: "000000000000000",
    type: "Cheque",
    bank_name: "Bank Ltd.",
    branch_code: "0000"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.bank_account.create(
    name="Bank",
    number="000000000000000",
    type="Cheque",
    bank_name="Bank Ltd.",
    branch_code="0000"
)
```

> User create bank account response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "name": "Bank",
        "number": "000000000000000",
        "type": "Cheque",
        "bank_name": "Bank Ltd.",
        "bank_code": null,
        "branch_code": "0000",
        "swift": null,
        "iban": null,
        "bic": null,
        "code": "bank_account_000000000000",
        "status": "pending"
    }
}
```

```javascript
{
    "id": 1,
    "name": "Bank",
    "number": "000000000000000",
    "type": "Cheque",
    "bank_name": "Bank Ltd.",
    "bank_code": null,
    "branch_code": "0000",
    "swift": null,
    "iban": null,
    "bic": null,
    "code": "bank_account_000000000000",
    "status": "pending"
}
```

```python
{
    "id": 1,
    "name": "Bank",
    "number": "000000000000000",
    "type": "Cheque",
    "bank_name": "Bank Ltd.",
    "bank_code": null,
    "branch_code": "0000",
    "swift": null,
    "iban": null,
    "bic": null,
    "code": "bank_account_000000000000",
    "status": "pending"
}
```

Create a bank account for a user.

#### Endpoint

`https://rehive.com/api/3/user/bank-accounts/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`name` | account name | null
`number` | account number | null
`type` | account type | null
`bank_name` | bank name | null
`bank_code` | bank code | null
`branch_code` | branch code | null
`swift` | swift number | null
`iban` | IBAN number | null
`bic` | BIC number | null


## Retrieve Bank Account

> User retrieve bank account request

```shell
curl https://www.rehive.com/api/3/user/bank-accounts/{account_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```
```javascript
rehive.user.bankAccounts.get(accountId).then(function (res) {
    ...
}, function (err) {
    ...
});
```
```python
rehive.user.bank_accounts.get(
    {account_id}
)
```

> User retrieve bank account response

```shell
{
    "status": "success",
    "data": {
        "id": {account_id},
        "name": "Bank",
        "number": "000000000000000",
        "type": "Cheque",
        "bank_name": "Bank Ltd.",
        "bank_code": null,
        "branch_code": "0000",
        "swift": null,
        "iban": null,
        "bic": null,
        "code": "bank_account_000000000000",
        "status": "pending"
    }
}
```

```javascript
{
    "id": {account_id},
    "name": "Bank",
    "number": "000000000000000",
    "type": "Cheque",
    "bank_name": "Bank Ltd.",
    "bank_code": null,
    "branch_code": "0000",
    "swift": null,
    "iban": null,
    "bic": null,
    "code": "bank_account_000000000000",
    "status": "pending"
}
```

```python
{
    "id": {account_id},
    "name": "Bank",
    "number": "000000000000000",
    "type": "Cheque",
    "bank_name": "Bank Ltd.",
    "bank_code": null,
    "branch_code": "0000",
    "swift": null,
    "iban": null,
    "bic": null,
    "code": "bank_account_000000000000",
    "status": "pending"
}
```

Retrieve a user's bank account.

#### Endpoint

`https://rehive.com/api/3/user/bank-accounts/{account_id}/`


## Update Bank Account

> User update bank account request

```shell
curl https://www.rehive.com/api/3/user/bank-accounts/{account_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"name": "Bank"}'
```

```javascript
rehive.user.bankAccounts.update(accountId,{name: "Bank"}).then(function(res){
    ...
},function(err){
    ...
})
```

```python
rehive.user.bank_accounts.update(
    {account_id},
    name="Bank"
)
```

> User update bank account response

```shell
{
    "status": "success",
    "data": {
        "id": {account_id},
        "name": "Bank",
        "number": "000000000000000",
        "type": "Cheque",
        "bank_name": "Bank Ltd.",
        "bank_code": null,
        "branch_code": "0000",
        "swift": null,
        "iban": null,
        "bic": null,
        "code": "bank_account_000000000000",
        "status": "pending"
    }
}
```

```javascript
{
    "id": {account_id},
    "name": "Bank",
    "number": "000000000000000",
    "type": "Cheque",
    "bank_name": "Bank Ltd.",
    "bank_code": null,
    "branch_code": "0000",
    "swift": null,
    "iban": null,
    "bic": null,
    "code": "bank_account_000000000000",
    "status": "pending"
}
```

```python
{
    "id": {account_id},
    "name": "Bank",
    "number": "000000000000000",
    "type": "Cheque",
    "bank_name": "Bank Ltd.",
    "bank_code": null,
    "branch_code": "0000",
    "swift": null,
    "iban": null,
    "bic": null,
    "code": "bank_account_000000000000",
    "status": "pending"
}
```

Update a user's bank account.

#### Endpoint

`https://rehive.com/api/3/user/bank-accounts/{account_id}/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`name` | account name | null
`number` | account number | null
`type` | account type | null
`bank_name` | bank name | null
`bank_code` | bank code | null
`branch_code` | branch code | null
`swift` | swift number | null
`iban` | IBAN number | null
`bic` | BIC number | null


## Delete Bank Account

> User delete bank account request

```shell
curl https://www.rehive.com/api/3/user/bank-accounts/{account_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.user.bankAccounts.delete(accountId).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.bank_accounts.delete(
   {account_id} 
)
```

> User delete bank account response

```shell
{
    "status": "success"
}
```
```javascript
{}
```

```python
{
    "status": "success"
}
```

Delete a user's bank account.

#### Endpoint

`https://rehive.com/api/3/user/bank-accounts/{account_id}/`


## List Crypto Accounts

> User list crypto accounts request

```shell
curl https://www.rehive.com/api/3/user/crypto-accounts/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.user.cryptoAccounts.get().then(function (res) {
    ...
}, function (err) {
    ...
})
```

```python
rehive.user.crypto_accounts.get()
```

> User list crypto accounts response

```shell
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "address": "0000000000000000000000000000000000",
            "code": "crypto_account_000000000000",
            "crypto_type": "bitcoin",
            "metadata": {},
            "status": "pending"
        }
    ]
}
```

```javascript
[
    {
        "id": 1,
        "address": "0000000000000000000000000000000000",
        "code": "crypto_account_000000000000",
        "crypto_type": "bitcoin",
        "metadata": {},
        "status": "pending"
    }
]
```

```python
[
    {
        "id": 1,
        "address": "0000000000000000000000000000000000",
        "code": "crypto_account_000000000000",
        "crypto_type": "bitcoin",
        "metadata": {},
        "status": "pending"
    }
]
```

List a user's cryptocurrency addresses.

#### Endpoint

`https://rehive.com/api/3/user/crypto-accounts/`

## Create Crypto Account

> User create crypto account request

```shell
curl https://www.rehive.com/api/3/user/crypto-accounts/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"address": "0000000000000000000000000000000000"}'
```

```javascript
rehive.user.cryptoAccounts.create({
    address: "0000000000000000000000000000000000",
    crypto_type: "bitcoin"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.crypto_accounts.create(
    address="0000000000000000000000000000000000",
    crypto_type="bitcoin"
)
```

> User create crypto account response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "address": "0000000000000000000000000000000000",
        "code": "crypto_account_000000000000",
        "crypto_type": "bitcoin",
        "metadata": {},
        "status": "pending"
    }
}
```

```javascript
{
    "id": 1,
    "address": "0000000000000000000000000000000000",
    "code": "crypto_account_000000000000",
    "crypto_type": "bitcoin",
    "metadata": {},
    "status": "pending"
}
```

```python
{
    "id": 1,
    "address": "0000000000000000000000000000000000",
    "code": "crypto_account_000000000000",
    "crypto_type": "bitcoin",
    "metadata": {},
    "status": "pending"
}
```

Create a crypto account for a user.

#### Endpoint

`https://rehive.com/api/3/user/crypto-accounts/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`address` | full bitcoin address | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`crypto_type` | string type (bitcoin, ethereum, other) | bitcoin
`metadata` | custom metadata | {}


## Retrieve Crypto Account

> User retrieve crypto account request

```shell
curl https://www.rehive.com/api/3/user/crypto-accounts/{account_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.user.cryptoAccounts.get(accountId).then(function (res) {
    ...
}, function (err) {
    ...
})
```

```python
rehive.user.crypto_accounts.get(
    {account_id}
)
```

> User retrieve crypto account response

```shell
{
    "status": "success",
    "data": {
        "id": {account_id},
        "address": "0000000000000000000000000000000000",
        "code": "crypto_account_000000000000",
        "crypto_type": "bitcoin",
        "metadata": {},
        "status": "pending"
    }
}
```

```javascript
{
    "id": 1,
    "address": "0000000000000000000000000000000000",
    "code": "crypto_account_000000000000",
    "crypto_type": "bitcoin",
    "metadata": {},
    "status": "pending"
}
```

```python
{
    "id": {account_id},
    "address": "0000000000000000000000000000000000",
    "code": "crypto_account_000000000000",
    "crypto_type": "bitcoin",
    "metadata": {},
    "status": "pending"
}
```

Get a user's crypto account.

#### Endpoint

`https://rehive.com/api/3/user/crypto-accounts/{account_id}/`


## Update Crypto Account

> User update crypto account request

```shell
curl https://www.rehive.com/api/3/user/crypto-accounts/{account_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"address": "0000000000000000000000000000000000"}'
```

```javascript
rehive.user.cryptoAccounts.update(accountId, {address: "0000000000000000000000000000000000"}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.crypto_accounts.update(
    address="0000000000000000000000000000000000"
)
```

> User update crypto account response

```shell
{
    "status": "success",
    "data": {
        "id": {account_id},
        "address": "0000000000000000000000000000000000",
        "code": "crypto_account_000000000000",
        "crypto_type": "bitcoin",
        "metadata": {},
        "status": "pending"
    }
}
```

```javascript
{
    "id": {account_id},
    "address": "0000000000000000000000000000000000",
    "code": "crypto_account_000000000000",
    "crypto_type": "bitcoin",
    "metadata": {},
    "status": "pending"
}
```

```python
{
    "id": {account_id},
    "address": "0000000000000000000000000000000000",
    "code": "crypto_account_000000000000",
    "crypto_type": "bitcoin",
    "metadata": {},
    "status": "pending"
}
```

Update a user's crypto account.

#### Endpoint

`https://rehive.com/api/3/user/crypto-accounts/{account_id}/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`address` | full bitcoin address | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`crypto_type` | string type (bitcoin, ethereum, other) | bitcoin
`metadata` | custom metadata | {}
`status` | string status | 'pending'


## Delete Crypto Account

> User delete crypto account request

```shell
curl https://www.rehive.com/api/3/user/crypto-accounts/{account_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.user.cryptoAccounts.delete(accountId).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.crypto_accounts.delete(
   {account_id} 
)
```

> User delete crypto account response

```shell
{
    "status": "success",
}
```

```javascript
{}
```

```python
{
    "status": "success",
}
```

Delete a user's crypto account.

#### Endpoint

`https://rehive.com/api/3/user/crypto-accounts/{account_id}/`


## List Documents

> User list documents request

```shell
curl https://www.rehive.com/api/3/user/documents/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.user.documents.get().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.documents.get()
```

> User list documents response

```shell
{
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 0,
                "file": "https://url.to/file.pdf",
                "document_category": "other",
                "document_type": "other",
                "metadata": {},
                "status": "pending",
                "note": null
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
            "id": 0,
            "file": "https://url.to/file.pdf",
            "document_category": "other",
            "document_type": "other",
            "metadata": {},
            "status": "pending",
            "note": null
        }
    ]
}
```

```python
[
    {
        "id": 0,
        "file": "https://url.to/file.pdf",
        "document_category": "other",
        "document_type": "other",
        "metadata": {},
        "status": "pending",
        "note": null
    }
]
```

Get a list of user's documents.

#### Endpoint

`https://www.rehive.com/api/3/user/documents/`


## Retrieve Document

> User retrieve document request

```shell
curl https://www.rehive.com/api/3/user/documents/{document_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.user.documents.get(documentId).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.documents.get(
    {document_id}
)
```

> User retrieve document response

```shell
{
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 0,
                "file": "https://url.to/file.pdf",
                "document_category": "other",
                "document_type": "other",
                "metadata": {},
                "status": "pending",
                "note": null
            }
        ]
    }
}
```

```javascript
{
    "id": 0,
    "file": "https://url.to/file.pdf",
    "document_category": "other",
    "document_type": "other",
    "metadata": {},
    "status": "pending",
    "note": null
}
```

```python
{
    "id": 0,
    "file": "https://url.to/file.pdf",
    "document_category": "other",
    "document_type": "other",
    "metadata": {},
    "status": "pending",
    "note": null
}
```

Get a user's document.

#### Endpoint

`https://www.rehive.com/api/3/user/documents/{document_id}/`


## Create Document

> User documents request

```shell
curl https://www.rehive.com/api/3/user/document/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: multipart/form-data"
  -F file=@localfilename
```

```javascript
var fileSelected = document.getElementById("fileInput").files[0],
    formData = new FormData;

formData.append('file', fileSelected);
formData.append('document_type', document_type);
formData.append('metadata', JSON.stringify(metadata));

rehive.user.documents.create(formData).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
# Note: The file argument should be the full path of the file
rehive.user.documents.upload(
    document_type='other',
    file=file
)
```

> User documents response

```shell
{
    "status": "success",
    "data": {
        "id": 0,
        "file": "https://url.to/file.pdf",
        "document_category": "other",
        "document_type": "other",
        "metadata": {},
        "status": "pending",
        "note": null
    }
}
```

```javascript
{
    "id": 0,
    "file": "https://url.to/file.pdf",
    "document_category": "other",
    "document_type": "other",
    "metadata": {},
    "status": "pending",
    "note": null
}
```

```python
{
    "id": 0,
    "file": "https://url.to/file.pdf",
    "document_category": "other",
    "document_type": "other",
    "metadata": {},
    "status": "pending",
    "note": null
}
```

Upload a user document.

#### Endpoint

`https://rehive.com/api/3/user/document/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`file` | a document file | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`document_category` | The document category | other 
`document_type` | The type of docuemnt | other 
`metadata` | custom metadata | {} 


## List Email Addresses

> User list email addresses request

```shell
curl https://www.rehive.com/api/3/user/emails/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.user.emails.get().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.emails.get()
```

> User list email addresses response

```shell
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "email": "joe@rehive.com",
            "primary": true,
            "verified": true
        }
    ]
}
```

```javascript
[
    {
        "id": 1,
        "email": "joe@rehive.com",
        "primary": true,
        "verified": true
    }
]
```

```python
[
    {
        "id": 1,
        "email": "joe@rehive.com",
        "primary": true,
        "verified": true
    }
]
```

Get a list of user's email addresses.

#### Endpoint

`https://www.rehive.com/api/3/user/emails/`

## Create Email Address

> User create email address request

```shell
curl https://www.rehive.com/api/3/user/emails/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"email": "joe@rehive.com",
       "primary": true}'
```

```javascript
rehive.user.emails.create(
{
    email: "joe@rehive.com",
    primary: true
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.email.create(
    email="joe@rehive.com"
)
```

> User create email address response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "email": "joe@rehive.com",
        "primary": true,
        "verified": true
    }
}
```

```javascript
{
    "id": 1,
    "email": "joe@rehive.com",
    "primary": true,
    "verified": true
}
```

```python
{
    "id": 1,
    "email": "joe@rehive.com",
    "primary": true,
    "verified": true
}
```

Create an email address for a user.

#### Endpoint

`https://rehive.com/api/3/user/emails/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`email` | email address | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`primary` | is a primary user email | false


## Retrieve Email Address

> User retrieve email address request

```shell
curl https://www.rehive.com/api/3/user/emails/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```
```javascript
rehive.user.emails.get(emailId).then(function (res) {
    ...
}, function (err) {
    ...
});
```
```python
rehive.user.emails.get("{email_id}")
```

> User retrieve email address response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "email": "joe@rehive.com",
        "primary": true,
        "verified": true
    }
}
```

```javascript
{
    "id": 1,
    "email": "joe@rehive.com",
    "primary": true,
    "verified": true
}
```

```python
{
    "id": 1,
    "email": "joe@rehive.com",
    "primary": true,
    "verified": true
}
```

#### Endpoint

`https://www.rehive.com/api/3/user/emails/{id}/`

## Update Email Address

> User update email address request

```shell
curl https://www.rehive.com/api/3/user/emails/{email_id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"primary": true}'
```

```javascript
rehive.user.emails.update(emailId, {primary: true}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.emails.update(
    '{email_id}',
    primary=True
)

# Quick method for setting primary
rehive.user.emails.make_primary(
   "{email_id}" 
)
```

> User update email address response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "email": "joe@rehive.com",
        "primary": true,
        "verified": true
    }
}
```

```javascript
{
    "id": 1,
    "email": "joe@rehive.com",
    "primary": true,
    "verified": true
}
```

```python
{
    "id": 1,
    "email": "joe@rehive.com",
    "primary": true,
    "verified": true
}
```

Update a user's email address. The email address can be changed to be the user's primary email address. The actual address cannot be updated and a new one should instead be created.

#### Endpoint

`https://rehive.com/api/3/user/emails/{email_id}`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`primary` | is a primary user email | false

## Delete Email Address

> User delete email address request

```shell
curl https://www.rehive.com/api/3/user/emails/{id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.user.emails.delete(emailId).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.emails.delete(
    {id}
)
```

> User delete email address response

```shell
{
    "status": "success"
}
```

```javascript
{}
```

```python
{
    "status": "success"
}
```

#### Endpoint

`https://www.rehive.com/api/3/user/emails/{id}/`

## List Mobile Numbers

> User mobile numbers request

```shell
curl https://www.rehive.com/api/3/user/mobiles/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.user.mobiles.get().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.mobiles.get()
```

> User mobile numbers response

```shell
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "number": "+00000000000",
            "primary": true,
            "verified": true
        }
    ]
}
```

```javascript
[
    {
        "id": 1,
        "number": "+00000000000",
        "primary": true,
        "verified": true
    }
]
```

```python
[
    {
        "id": 1,
        "number": "+00000000000",
        "primary": true,
        "verified": true
    }
]
```

Get a list of user's mobile numbers.

#### Endpoint

`https://www.rehive.com/api/3/user/mobiles/`

## Create Mobile Number

> User create mobile number request

```shell
curl https://www.rehive.com/api/3/user/mobiles/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"number": "+00000000000",
       "primary": true}'
```

```javascript
rehive.user.mobiles.create({
    number: "+00000000000",
    primary: true
}).then(function (res) {
    ...
}, function (err) {
    ...
})
```

```python
rehive.user.mobiles.create(
    number="+00000000000"
)
```

> User create mobile number response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "number": "+00000000000",
        "primary": true,
        "verified": true
    }
}
```

```javascript
{
    "id": 1,
    "number": "+00000000000",
    "primary": true,
    "verified": true
}
```

```python
{
    "id": 1,
    "number": "+00000000000",
    "primary": true,
    "verified": true
}
```

Create a mobile number for a user.

#### Endpoint

`https://rehive.com/api/3/user/mobiles/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`number` | mobile number address (including area code)| null

#### Optional Fields

Field | Description | Default
--- | --- | --- 
`primary` | is a primary user number | false 

## Retrieve Mobile Numbers

> User retrieve mobile number request

```shell
curl https://www.rehive.com/api/3/user/mobiles/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.user.mobiles.get(numberId).then(function(res){
    ...
},function(err){
    ...
})
```

```python
rehive.user.mobiles.get("{number_id}")
```

> User mobile numbers response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "number": "+00000000000",
        "primary": true,
        "verified": true
    }
}
```

```javascript
{
    "id": 1,
    "number": "+00000000000",
    "primary": true,
    "verified": true
}
```

```python
{
    "id": 1,
    "number": "+00000000000",
    "primary": true,
    "verified": true
}
```

Retrieve a user's mobile number.

#### Endpoint

`https://www.rehive.com/api/3/user/mobiles/`

## Update Mobile Number

> User update mobile number request

```shell
curl https://www.rehive.com/api/3/user/mobiles/{number_id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"primary": true}'
```

```javascript
rehive.user.mobiles.update(numberId, data).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.mobiles.update(
    "{number_id}",
    primary=True
)

# Quick method for setting primary
rehive.user.mobiles.make_primary(
   "{number_id}" 
)
```

> User update mobile number response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "number": "+00000000000",
        "primary": true,
        "verified": true
    }
}
```

```javascript
{
    "id": 1,
    "number": "+00000000000",
    "primary": true,
    "verified": true
}
```

```python
{
    "id": 1,
    "number": "+00000000000",
    "primary": true,
    "verified": true
}
```

Update a user's mobile number. The number can be changed to be the user's primary mobile number. The actual number cannot be updated and a new one should be created instead.

#### Endpoint

`https://rehive.com/api/3/user/mobiles/{number_id}`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`primary` | is a primary user email | false

## Delete Mobile Number

> User delete mobile number request

```shell
curl https://www.rehive.com/api/3/user/mobiles/{id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.user.mobiles.delete(numberId).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.user.mobiles.delete(
    {id}
)
```

> User delete mobile number response

```shell
{
    "status": "success"
}
```

```javascript
{}
```

```python
{
    "status": "success"
}
```

#### Endpoint

`https://www.rehive.com/api/3/user/mobiles/{id}/`
