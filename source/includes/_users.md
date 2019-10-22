# Users

All non authentication access on the Rehive API is made by registered users. This is true of the orginal company owner as well as all subsequent users (whether granted admin permissions or not). The user endpoints provide a means to add, alter and view additional user information.

## Retrieve Profile

> User profile request

```shell
curl https://api.rehive.com/3/user/
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
        "id": "00000000-0000-0000-0000-000000000000",
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
        "mobile": "+00000000000",
        "timezone": null,
        "verified": false,
        "kyc": {
            "updated": 1509539801040,
            "status": "pending"
        },
        "status": "pending",
        "groups": [
            {
                "name": "test",
                "label": "Test",
                "settings": {
                    "allow_transactions": true,
                    "allow_debit_transactions": true,
                    "allow_credit_transactions": true
                }
            }
        ],
        "permissions": [],
        "created": 1464912953000,
        "updated": 1464912953000,
        "settings": {
            "allow_transactions": true,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        }
    }
}
```

```javascript
{
    "id": "00000000-0000-0000-0000-000000000000",
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
    "mobile": "+00000000000",
    "timezone": null,
    "verified": false,
    "kyc": {
        "updated": 1509539801040,
        "status": "pending"
    },
    "status": "pending",
    "groups": [
        {
            "name": "test",
            "label": "Test",
            "settings": {
                "allow_transactions": true,
                "allow_debit_transactions": true,
                "allow_credit_transactions": true
            }
        }
    ],
    "permissions": [],
    "created": 1464912953000,
    "updated": 1464912953000,
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    }
}
```

```python
{
    "id": "00000000-0000-0000-0000-000000000000",
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
    "mobile": "+00000000000",
    "timezone": null,
    "verified": false,
    "kyc": {
        "updated": 1509539801040,
        "status": "pending"
    },
    "status": "pending",
    "groups": [
        {
            "name": "test",
            "label": "Test",
            "settings": {
                "allow_transactions": true,
                "allow_debit_transactions": true,
                "allow_credit_transactions": true
            }
        }
    ],
    "permissions": [],
    "created": 1464912953000,
    "updated": 1464912953000,
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    }
}
```

Retrieve a user's profile information.

#### Endpoint

`https://api.rehive.com/3/user/`

## Update Profile

> User update profile request

```shell
curl https://api.rehive.com/3/user/
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
        "id": "00000000-0000-0000-0000-000000000000",
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
        "mobile": "+00000000000",
        "timezone": null,
        "verified": false,
        "kyc": {
            "updated": 1509539801040,
            "status": "pending"
        },
        "status": "pending",
        "groups": [
            {
                "name": "test",
                "label": "Test",
                "settings": {
                    "allow_transactions": true,
                    "allow_debit_transactions": true,
                    "allow_credit_transactions": true
                }
            }
        ],
        "permissions": [],
        "created": 1464912953000,
        "updated": 1464912953000,
        "settings": {
            "allow_transactions": true,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        }
    }
}
```

```javascript
{
    "id": "00000000-0000-0000-0000-000000000000",
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
    "mobile": "+00000000000",
    "timezone": null,
    "verified": false,
    "kyc": {
        "updated": 1509539801040,
        "status": "pending"
    },
    "status": "pending",
    "groups": [
        {
            "name": "test",
            "label": "Test",
            "settings": {
                "allow_transactions": true,
                "allow_debit_transactions": true,
                "allow_credit_transactions": true
            }
        }
    ],
    "permissions": [],
    "created": 1464912953000,
    "updated": 1464912953000,
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    }
}
```

```python
{
    "id": "00000000-0000-0000-0000-000000000000",
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
    "mobile": "+00000000000",
    "timezone": null,
    "verified": false,
    "kyc": {
        "updated": 1509539801040,
        "status": "pending"
    },
    "status": "pending",
    "groups": [
        {
            "name": "test",
            "label": "Test",
            "settings": {
                "allow_transactions": true,
                "allow_debit_transactions": true,
                "allow_credit_transactions": true
            }
        }
    ],
    "permissions": [],
    "created": 1464912953000,
    "updated": 1464912953000,
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    }
}
```

Update a user's profile information.

#### Endpoint

`https://api.rehive.com/3/user/`

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
`mobile` | mobile number | blank
`timezone` | timezone | blank
`birth_date` | birth date | blank

<aside class="notice">
    <code>birth_date</code> should be added in the formal yyyy-mm-dd
</aside>







## List Addresses

> User list addresses request

```shell
curl https://api.rehive.com/3/user/addresses/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
```

```python
```

> User list addresses response

```shell
{
    "status": "success",
    "data": [
        {
            "line_1": "1 Main Street",
            "line_2": "East City",
            "city": "Cape Town",
            "state_province": "Western Cape",
            "country": "ZA",
            "postal_code": "8001",
            "status": "pending",
            "created": 1516281408895,
            "updated": 1528454842365
        }
    ]
}
```

```javascript
```

```python
```

List a user's addresses.

#### Endpoint

`https://api.rehive.com/3/user/addresses/`

## Create Address

> User create address request

```shell
curl https://api.rehive.com/3/user/addresses/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"line_1": "1 Main Street",
        "line_2": "East City",
        "city": "Cape Town",
        "state_province": "Western Cape",
        "country": "ZA",
        "postal_code": "8001"}'
```

```javascript
```

```python
```

> User create address response

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
        "status": "pending",
        "created": 1516281408895,
        "updated": 1528454842365
    }
}
```

```javascript
```

```python
```

Create an address for a user.

#### Endpoint

`https://api.rehive.com/3/user/addresses/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`line_1` | Address line one | null
`line_2` | Address line two | null
`city` | City | null
`state_province` | State or province | null
`country` | country code | null
`postal_code` | Zip or postal code | null


## Retrieve Address

> User retrieve address request

```shell
curl https://api.rehive.com/3/user/addresses/{address_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
```

```python
```

> User retrieve address response

```shell
```

```javascript
{
    "line_1": "1 Main Street",
    "line_2": "East City",
    "city": "Cape Town",
    "state_province": "Western Cape",
    "country": "ZA",
    "postal_code": "8001",
    "status": "pending",
    "created": 1516281408895,
    "updated": 1528454842365
}
```

```python
```

Retrieve a user's address.

#### Endpoint

`https://api.rehive.com/3/user/addresses/{address_id}/`

## Update Address

> User update address request

```shell
curl https://api.rehive.com/3/user/addresses/{address_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"city": "Cape Town"}'
```

```javascript
```

```python
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
        "status": "pending",
        "created": 1516281408895,
        "updated": 1528454842365
    }
}
```

```javascript
```

```python
```

Update a user's address.

#### Endpoint

`https://api.rehive.com/3/user/addresses/{address_id}/`

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
curl https://api.rehive.com/3/user/bank-accounts/
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
            "status": "pending",
            "created": 1516281408895,
            "updated": 1528454842365
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
        "status": "pending",
        "created": 1516281408895,
        "updated": 1528454842365
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
        "status": "pending",
        "created": 1516281408895,
        "updated": 1528454842365
    }
]
```

List a user's bank accounts.

#### Endpoint

`https://api.rehive.com/3/user/bank-accounts/`

## Create Bank Account

> User create bank account request

```shell
curl https://api.rehive.com/3/user/bank-accounts/
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
        "status": "pending",
        "created": 1516281408895,
        "updated": 1528454842365
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
    "status": "pending",
    "created": 1516281408895,
    "updated": 1528454842365
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
    "status": "pending",
    "created": 1516281408895,
    "updated": 1528454842365
}
```

Create a bank account for a user.

#### Endpoint

`https://api.rehive.com/3/user/bank-accounts/`

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
curl https://api.rehive.com/3/user/bank-accounts/{account_id}/
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
        "status": "pending",
        "created": 1516281408895,
        "updated": 1528454842365
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
    "status": "pending",
    "created": 1516281408895,
    "updated": 1528454842365
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

`https://api.rehive.com/3/user/bank-accounts/{account_id}/`


## Update Bank Account

> User update bank account request

```shell
curl https://api.rehive.com/3/user/bank-accounts/{account_id}/
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
        "status": "pending",
        "created": 1516281408895,
        "updated": 1528454842365
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
    "status": "pending",
    "created": 1516281408895,
    "updated": 1528454842365
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
    "status": "pending",
    "created": 1516281408895,
    "updated": 1528454842365
}
```

Update a user's bank account.

#### Endpoint

`https://api.rehive.com/3/user/bank-accounts/{account_id}/`

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
curl https://api.rehive.com/3/user/bank-accounts/{account_id}/
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

`https://api.rehive.com/3/user/bank-accounts/{account_id}/`


## List Crypto Accounts

> User list crypto accounts request

```shell
curl https://api.rehive.com/3/user/crypto-accounts/
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
            "status": "pending",
            "created": 1516281408895,
            "updated": 1528454842365
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
        "status": "pending",
        "created": 1516281408895,
        "updated": 1528454842365
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
        "status": "pending",
        "created": 1516281408895,
        "updated": 1528454842365
    }
]
```

List a user's cryptocurrency addresses.

#### Endpoint

`https://api.rehive.com/3/user/crypto-accounts/`

## Create Crypto Account

> User create crypto account request

```shell
curl https://api.rehive.com/3/user/crypto-accounts/
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
        "status": "pending",
        "created": 1516281408895,
        "updated": 1528454842365
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
    "status": "pending",
    "created": 1516281408895,
    "updated": 1528454842365
}
```

```python
{
    "id": 1,
    "address": "0000000000000000000000000000000000",
    "code": "crypto_account_000000000000",
    "crypto_type": "bitcoin",
    "metadata": {},
    "status": "pending",
    "created": 1516281408895,
    "updated": 1528454842365
}
```

Create a crypto account for a user.

#### Endpoint

`https://api.rehive.com/3/user/crypto-accounts/`

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
curl https://api.rehive.com/3/user/crypto-accounts/{account_id}/
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
        "status": "pending",
        "created": 1516281408895,
        "updated": 1528454842365
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
    "status": "pending",
    "created": 1516281408895,
    "updated": 1528454842365
}
```

```python
{
    "id": {account_id},
    "address": "0000000000000000000000000000000000",
    "code": "crypto_account_000000000000",
    "crypto_type": "bitcoin",
    "metadata": {},
    "status": "pending",
    "created": 1516281408895,
    "updated": 1528454842365
}
```

Get a user's crypto account.

#### Endpoint

`https://api.rehive.com/3/user/crypto-accounts/{account_id}/`


## Update Crypto Account

> User update crypto account request

```shell
curl https://api.rehive.com/3/user/crypto-accounts/{account_id}/
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
        "status": "pending",
        "created": 1516281408895,
        "updated": 1528454842365
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
    "status": "pending",
    "created": 1516281408895,
    "updated": 1528454842365
}
```

```python
{
    "id": {account_id},
    "address": "0000000000000000000000000000000000",
    "code": "crypto_account_000000000000",
    "crypto_type": "bitcoin",
    "metadata": {},
    "status": "pending",
    "created": 1516281408895,
    "updated": 1528454842365
}
```

Update a user's crypto account.

#### Endpoint

`https://api.rehive.com/3/user/crypto-accounts/{account_id}/`

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
curl https://api.rehive.com/3/user/crypto-accounts/{account_id}/
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

`https://api.rehive.com/3/user/crypto-accounts/{account_id}/`


## List Documents

> User list documents request

```shell
curl https://api.rehive.com/3/user/documents/
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
                "note": null,
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
            "id": 0,
            "file": "https://url.to/file.pdf",
            "document_category": "other",
            "document_type": "other",
            "metadata": {},
            "status": "pending",
            "note": null,
            "created": 1516281408895,
            "updated": 1528454842365
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
        "note": null,
        "created": 1516281408895,
        "updated": 1528454842365
    }
]
```

Get a list of user's documents.

#### Endpoint

`https://api.rehive.com/3/user/documents/`


## Retrieve Document

> User retrieve document request

```shell
curl https://api.rehive.com/3/user/documents/{document_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.user.documents.get({id: documentId).then(function (res) {
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
        "id": 0,
        "file": "https://url.to/file.pdf",
        "document_category": "other",
        "document_type": "other",
        "metadata": {},
        "status": "pending",
        "note": null,
        "created": 1516281408895,
        "updated": 1528454842365
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
    "note": null,
    "created": 1516281408895,
    "updated": 1528454842365
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
    "note": null,
    "created": 1516281408895,
    "updated": 1528454842365
}
```

Get a user's document.

#### Endpoint

`https://api.rehive.com/3/user/documents/{document_id}/`


## Create Document

> User create document request

```shell
curl https://api.rehive.com/3/user/documents/
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

> User create document response

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
        "note": null,
        "created": 1516281408895,
        "updated": 1528454842365
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
    "note": null,
    "created": 1516281408895,
    "updated": 1528454842365
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
    "note": null,
    "created": 1516281408895,
    "updated": 1528454842365
}
```

Create a user document.

#### Endpoint

`https://api.rehive.com/3/user/documents/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`file` | a document file | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`document_type` | The type of docuemnt | other
`metadata` | custom metadata | {}

#### Document Types

value | Description
--- | ---
`utility_bill` | Utility Bill
`bank_statement` | Bank Statement
`lease_or_rental_agreement` | Lease or Rental Agreement
`municipal_rate_and_taxes` | Municipal Rate and Taxes
`mortgage_statement` | Mortgage Statement
`telephone` | Telephone
`insurance_policy` | Insurance Policy
`retail_store` | Retail Store
`government_id` | Government ID
`passport` | Passport
`drivers_license` | Drivers License
`id_confirmation` | ID Confirmation
`other` | Other

## List Email Addresses

> User list email addresses request

```shell
curl https://api.rehive.com/3/user/emails/
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

`https://api.rehive.com/3/user/emails/`

## Create Email Address

> User create email address request

```shell
curl https://api.rehive.com/3/user/emails/
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

`https://api.rehive.com/3/user/emails/`

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
curl https://api.rehive.com/3/user/emails/{id}/
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

`https://api.rehive.com/3/user/emails/{id}/`

## Update Email Address

> User update email address request

```shell
curl https://api.rehive.com/3/user/emails/{email_id}
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

`https://api.rehive.com/3/user/emails/{email_id}`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`primary` | is a primary user email | false

## Delete Email Address

> User delete email address request

```shell
curl https://api.rehive.com/3/user/emails/{id}/
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

`https://api.rehive.com/3/user/emails/{id}/`

## List Mobile Numbers

> User mobile numbers request

```shell
curl https://api.rehive.com/3/user/mobiles/
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
            "verified": true,
            "created": 1516281408895,
            "updated": 1528454842365
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
        "verified": true,
        "created": 1516281408895,
        "updated": 1528454842365
    }
]
```

```python
[
    {
        "id": 1,
        "number": "+00000000000",
        "primary": true,
        "verified": true,
        "created": 1516281408895,
        "updated": 1528454842365
    }
]
```

Get a list of user's mobile numbers.

#### Endpoint

`https://api.rehive.com/3/user/mobiles/`

## Create Mobile Number

> User create mobile number request

```shell
curl https://api.rehive.com/3/user/mobiles/
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
        "verified": true,
        "created": 1516281408895,
        "updated": 1528454842365
    }
}
```

```javascript
{
    "id": 1,
    "number": "+00000000000",
    "primary": true,
    "verified": true,
    "created": 1516281408895,
    "updated": 1528454842365
}
```

```python
{
    "id": 1,
    "number": "+00000000000",
    "primary": true,
    "verified": true,
    "created": 1516281408895,
    "updated": 1528454842365
}
```

Create a mobile number for a user.

#### Endpoint

`https://api.rehive.com/3/user/mobiles/`

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
curl https://api.rehive.com/3/user/mobiles/{id}/
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
        "verified": true,
        "created": 1516281408895,
        "updated": 1528454842365
    }
}
```

```javascript
{
    "id": 1,
    "number": "+00000000000",
    "primary": true,
    "verified": true,
    "created": 1516281408895,
    "updated": 1528454842365
}
```

```python
{
    "id": 1,
    "number": "+00000000000",
    "primary": true,
    "verified": true,
    "created": 1516281408895,
    "updated": 1528454842365
}
```

Retrieve a user's mobile number.

#### Endpoint

`https://api.rehive.com/3/user/mobiles/`

## Update Mobile Number

> User update mobile number request

```shell
curl https://api.rehive.com/3/user/mobiles/{number_id}
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
        "verified": true,
        "created": 1516281408895,
        "updated": 1528454842365
    }
}
```

```javascript
{
    "id": 1,
    "number": "+00000000000",
    "primary": true,
    "verified": true,
    "created": 1516281408895,
    "updated": 1528454842365
}
```

```python
{
    "id": 1,
    "number": "+00000000000",
    "primary": true,
    "verified": true,
    "created": 1516281408895,
    "updated": 1528454842365
}
```

Update a user's mobile number. The number can be changed to be the user's primary mobile number. The actual number cannot be updated and a new one should be created instead.

#### Endpoint

`https://api.rehive.com/3/user/mobiles/{number_id}`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`primary` | is a primary user email | false

## Delete Mobile Number

> User delete mobile number request

```shell
curl https://api.rehive.com/3/user/mobiles/{id}/
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

`https://api.rehive.com/3/user/mobiles/{id}/`
