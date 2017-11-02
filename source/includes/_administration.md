# Administration

Rehive includes a set of admin-only endpoints that can make working with users and their transactions extremely easy.

## Users

### Users Overview

> Admin users overview request

```shell
curl https://www.rehive.com/admin/api/3/admin/users/overview/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin list users overview response

```shell
{
    "data": {
        "total": 1,
        "active": 1
    },
    "status": "success"
}
```

Get an overview of users belonging to a company.

#### Endpoint

`https://rehive.com/api/3/admin/users/overview/`

### List Users

> Admin list users request

```shell
curl https://www.rehive.com/admin/api/3/admin/users/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.users.get()
```

> Admin list users response

```shell
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
                "birth_date": "2000-01-01",
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
                "timezone": "Asia/Dhaka",
                "verified": true,
                "kyc": {
                    "bank_accounts": {
                        "status": null,
                        "updated": null
                    },
                    "status": "pending",
                    "addresses": {
                        "status": null,
                        "updated": null
                    },
                    "documents": {
                        "status": null,
                        "updated": null
                    },
                    "updated": 1509619797959
                },
                "status": "pending",
                "permission_groups": [],
                "permissions": [],
                "date_joined": 1464912953000,
                "switches": [],
                "last_login": null,
                "password": "*********************************00000000"
            }
        ]
    }
}
```

```python
[
    {
        "identifier": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": "",
        "id_number": "",
        "birth_date": "2000-01-01",
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
        "timezone": "Asia/Dhaka",
        "verified": true,
        "kyc": {
            "bank_accounts": {
                "status": null,
                "updated": null
            },
            "status": "pending",
            "addresses": {
                "status": null,
                "updated": null
            },
            "documents": {
                "status": null,
                "updated": null
            },
            "updated": 1509619797959
        },
        "status": "pending",
        "permission_groups": [],
        "permissions": [],
        "date_joined": 1464912953000,
        "switches": [],
        "last_login": null,
        "password": "*********************************00000000"
    }
]
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

```python
rehive.admin.users.create(
    first_name="Joe",
    last_name="Soap",
    mobile_number="+27840000000",
    email="joe@rehive.com"
)
```

> Admin update user response

```shell
{
    "status": "success",
    "data": {
        "identifier": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": "",
        "id_number": "",
        "birth_date": "2000-01-01",
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
        "timezone": "Asia/Dhaka",
        "verified": true,
        "kyc": {
            "bank_accounts": {
                "status": null,
                "updated": null
            },
            "status": "pending",
            "addresses": {
                "status": null,
                "updated": null
            },
            "documents": {
                "status": null,
                "updated": null
            },
            "updated": 1509619797959
        },
        "status": "pending",
        "permission_groups": [],
        "permissions": [],
        "date_joined": 1464912953000,
        "switches": [],
        "last_login": null,
        "password": "*********************************00000000"
    }
}
```

```python
{
    "identifier": "00000000-0000-0000-0000-000000000000",
    "first_name": "Joe",
    "last_name": "Soap",
    "email": "joe@rehive.com",
    "username": "",
    "id_number": "",
    "birth_date": "2000-01-01",
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
    "timezone": "Asia/Dhaka",
    "verified": true,
    "kyc": {
        "bank_accounts": {
            "status": null,
            "updated": null
        },
        "status": "pending",
        "addresses": {
            "status": null,
            "updated": null
        },
        "documents": {
            "status": null,
            "updated": null
        },
        "updated": 1509619797959
    },
    "status": "pending",
    "permission_groups": [],
    "permissions": [],
    "date_joined": 1464912953000,
    "switches": [],
    "last_login": null,
    "password": "*********************************00000000"
}
```

Update a user's details.

#### Endpoint

`https://rehive.com/api/3/admin/users/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`first_name` | first name | blank | false
`last_name` | last name | blank | false
`email` | email address | null| false
`mobile_number` | mobile number | null | false
`id_number` | ID number | blank | false
`profile` | profile image | blank | false
`language` | language code (`af`, `en` etc.) | blank | false
`nationality` | nationality code (`ZA`, `UK` etc.) | blank | false
`metadata` | custom metadata | {} | false
`mobile_number` | mobile number | blank | false
`timezone` | timezone | blank | false
`birth_date` | birth date | blank | false

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

```python
rehive.admin.users.get(
    "{identifier}"
)
```

> Admin retrieve user response

```shell
{
    "status": "success",
    "data": {
        "identifier": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": "",
        "id_number": "",
        "birth_date": "2000-01-01",
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
        "timezone": "Asia/Dhaka",
        "verified": true,
        "kyc": {
            "bank_accounts": {
                "status": null,
                "updated": null
            },
            "status": "pending",
            "addresses": {
                "status": null,
                "updated": null
            },
            "documents": {
                "status": null,
                "updated": null
            },
            "updated": 1509619797959
        },
        "status": "pending",
        "permission_groups": [],
        "permissions": [],
        "date_joined": 1464912953000,
        "switches": [],
        "last_login": null,
        "password": "*********************************00000000"
    }
}
```

```python
{
    "identifier": "00000000-0000-0000-0000-000000000000",
    "first_name": "Joe",
    "last_name": "Soap",
    "email": "joe@rehive.com",
    "username": "",
    "id_number": "",
    "birth_date": "2000-01-01",
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
    "timezone": "Asia/Dhaka",
    "verified": true,
    "kyc": {
        "bank_accounts": {
            "status": null,
            "updated": null
        },
        "status": "pending",
        "addresses": {
            "status": null,
            "updated": null
        },
        "documents": {
            "status": null,
            "updated": null
        },
        "updated": 1509619797959
    },
    "status": "pending",
    "permission_groups": [],
    "permissions": [],
    "date_joined": 1464912953000,
    "switches": [],
    "last_login": null,
    "password": "*********************************00000000"
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

```python
rehive.admin.users.update(
    "{identifier}",
    first_name="Joe"
)
```

> Admin update user response

```shell
{
    "status": "success",
    "data": {
        "identifier": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": "",
        "id_number": "",
        "birth_date": "2000-01-01",
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
        "timezone": "Asia/Dhaka",
        "verified": true,
        "kyc": {
            "bank_accounts": {
                "status": null,
                "updated": null
            },
            "status": "pending",
            "addresses": {
                "status": null,
                "updated": null
            },
            "documents": {
                "status": null,
                "updated": null
            },
            "updated": 1509619797959
        },
        "status": "pending",
        "permission_groups": [],
        "permissions": [],
        "date_joined": 1464912953000,
        "switches": [],
        "last_login": null,
        "password": "*********************************00000000"
    }
}
```

```python
{
    "identifier": "00000000-0000-0000-0000-000000000000",
    "first_name": "Joe",
    "last_name": "Soap",
    "email": "joe@rehive.com",
    "username": "",
    "id_number": "",
    "birth_date": "2000-01-01",
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
    "timezone": "Asia/Dhaka",
    "verified": true,
    "kyc": {
        "bank_accounts": {
            "status": null,
            "updated": null
        },
        "status": "pending",
        "addresses": {
            "status": null,
            "updated": null
        },
        "documents": {
            "status": null,
            "updated": null
        },
        "updated": 1509619797959
    },
    "status": "pending",
    "permission_groups": [],
    "permissions": [],
    "date_joined": 1464912953000,
    "switches": [],
    "last_login": null,
    "password": "*********************************00000000"
}
```

Update a user's details.

#### Endpoint

`https://rehive.com/api/3/admin/users/{identifier}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`first_name` | first name | blank | false
`last_name` | last name | blank | false
`id_number` | ID number | blank | false
`profile` | profile image | blank | false
`language` | language code (`af`, `en` etc.) | blank | false
`nationality` | nationality code (`ZA`, `UK` etc.) | blank | false
`metadata` | custom metadata | {} | false
`mobile_number` | mobile number | blank | false
`timezone` | timezone | blank | false
`birth_date` | birth date | blank | false
`status` | status | pending | false

#### Statuses

Value | Description 
--- | --- 
`obsolete` | Obsolete
`declined` | Declined
`pending` | Pending
`incomplete` | Incomplete
`verified` | Verified

### List User Switches

List all switches related to a user.

> List User Switches request

```shell
curl https://rehive.com/api/3/admin/users/{identifier}/switches/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
"To be implemented"
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

```python
"To be implemented"
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
`subtype` | Subtype name | null | false
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

```python
"To be implemented"
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

```python
"To be implemented"
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

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`tx_type` | Transaction type | | true
`subtype` | Transaction subtype | None | false
`enabled` | Enabled | false | false

#### Endpoint

`https://rehive.com/api/3/admin/users/{identifier}/switches/{id}`

### Delete User Switches

Delete a specific switch related to a user

> Delete User Switches request

```shell
curl https://rehive.com/api/3/admin/users/{identifier}/switches/{id}
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
"To be implemented"
```

> Delete User Switches response

```json
{
    "status": "success"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/{identifier}/switches/{id}`


### List Addresses

> List Addresses request

```shell
curl https://rehive.com/api/3/admin/users/addresses/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
"To be implemented"
```

> List Addresses response

```shell
{
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 2,
                "user": {
                    "identifier": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": "",
                    "mobile_number": "+27840000000",
                    "profile": null
                },
                "line_1": "1 Main Street",
                "line_2": "East City",
                "city": "Cape Town",
                "state_province": "Western Cape",
                "country": "ZA",
                "postal_code": "8001"
                "status": "pending"
            }
        ]
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/addresses/`

### Create Address

> Create Address request

```shell
curl https://rehive.com/api/3/admin/users/addresses/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"line_1": "1 Main Street",
        "line_2": "East City",
        "city": "Cape Town",
        "state_province": "Western Cape",
        "country": "ZA",
        "postal_code": "8001",
        "user": "joe@rehive.com"}'
```

```python
"To be implemented"
```

> Create Address response

```shell
{
    "status": "success",
    "data": {
        "id": 2,
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "line_1": "1 Main Street",
        "line_2": "East City",
        "city": "Cape Town",
        "state_province": "Western Cape",
        "country": "ZA",
        "postal_code": "8001"
        "status": "pending"
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/addresses/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`line_1` | address line one | blank | false
`line_2` | address line 2 | blank | false
`city` | city | blank | false
`state_province` | state or province | blank | false
`country` | country code | blank | false
`postal_code` | postal or zip code) | blank | false
`status` | account status | "pending" | false
`user` | user identifier | null | true
`status` | status | pending | false

#### Statuses

Value | Description 
--- | --- 
`obsolete` | Obsolete
`declined` | Declined
`pending` | Pending
`incomplete` | Incomplete
`verified` | Verified

### Retrieve Address

> Retrieve Address request

```shell
curl https://rehive.com/api/3/admin/users/addresses/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
"To be implemented"
```

> Retrieve Address response

```shell
{
    "status": "success",
    "data": {
        "id": 2,
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "line_1": "1 Main Street",
        "line_2": "East City",
        "city": "Cape Town",
        "state_province": "Western Cape",
        "country": "ZA",
        "postal_code": "8001"
        "status": "pending"
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/addresses/{id}/`

### Update Address

> Update Address request

```shell
curl https://rehive.com/api/3/admin/users/addresses/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"line_1": "1 Main Street"}'
```

> Update Address response

```shell
{
    "status": "success",
    "data": {
        "id": 2,
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "line_1": "1 Main Street",
        "line_2": "East City",
        "city": "Cape Town",
        "state_province": "Western Cape",
        "country": "ZA",
        "postal_code": "8001"
        "status": "pending"
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/addresses/{id}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`line_1` | address line one | blank | false
`line_2` | address line 2 | blank | false
`city` | city | blank | false
`state_province` | state or province | blank | false
`country` | country code | blank | false
`postal_code` | postal or zip code) | blank | false
`status` | status | pending | false

#### Statuses

Value | Description 
--- | --- 
`obsolete` | Obsolete
`declined` | Declined
`pending` | Pending
`incomplete` | Incomplete
`verified` | Verified

### Delete Address

> Delete address request

```shell
curl https://rehive.com/api/3/admin/users/addresses/{id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Delete address response

```shell
{
    "status": "success",
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/addresses/{id}/`


### List Bank Accounts

> List Bank Accounts request

```shell
curl https://rehive.com/api/3/admin/users/bank-accounts/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.banks_accounts.get()
```

> List Bank Accounts response

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
                "user": {
                    "identifier": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": "",
                    "mobile_number": "+27840000000",
                    "profile": null
                },
                "name": "Bank Account",
                "number": "12341234",
                "type": "Cheque",
                "bank_name": "Bank",
                "bank_code": "1234",
                "branch_code": "1234",
                "swift": null,
                "iban": null,
                "bic": null,
                "code": "bank_account_000000000000",
                "status": "pending"
            }
        ]
    }
}
```

```python
[
    {
        "id": 1,
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "name": "Bank Account",
        "number": "12341234",
        "type": "Cheque",
        "bank_name": "Bank",
        "bank_code": "1234",
        "branch_code": "1234",
        "swift": null,
        "iban": null,
        "bic": null,
        "code": "bank_account_000000000000",
        "status": "pending"
    }
]
```

#### Endpoint

`https://rehive.com/api/3/admin/users/bank-accounts/`

### Create Bank Account

> Create Bank Account request

```shell
curl https://rehive.com/api/3/admin/users/bank-accounts/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "Bank Account",
        "number": "12341234",
        "type": "Cheque",
        "bank_name": "Bank",
        "bank_code": "1234",
        "branch_code": "1234",
        "user": "joe@rehive.com"}'
```

```python
rehive.admin.bank_accounts.create(
    name="Bank Account",
    number="12341234",
    type="Cheque",
    bank_name="Bank",
    bank_code="1234",
    branch_code="1234",
    user=joe@rehive.com
)
```

> Create Bank Account response

```shell
{
    "status": "success",
    "data": {
        "id": 2,
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "name": "Bank Account",
        "number": "12341234",
        "type": "Cheque",
        "bank_name": "Bank",
        "bank_code": "1234",
        "branch_code": "1234",
        "swift": null,
        "iban": null,
        "bic": null,
        "code": "bank_account_000000000000",
        "status": "pending"
    }
}
```

```python
 {
    "id": 2,
    "user": {
        "identifier": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": "",
        "mobile_number": "+27840000000",
        "profile": null
    },
    "name": "Bank Account",
    "number": "12341234",
    "type": "Cheque",
    "bank_name": "Bank",
    "bank_code": "1234",
    "branch_code": "1234",
    "swift": null,
    "iban": null,
    "bic": null,
    "code": "bank_account_000000000000",
    "status": "pending"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/bank-accounts/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | Account Name | blank | false
`number` | Account Number | blank | false
`type` | Account Type | blank | false
`bank_name` | Bank Name | blank | false
`bank_code` | Bank Code | blank | false
`branch_code` | Branch Code | blank | false
`status` | account status | "pending" | false
`swift` | swift | blank | false
`iban` | iban | blank | false
`bic` | bic | blank | false
`user` | user identifier | null | true

#### Statuses

Value | Description 
--- | --- 
`obsolete` | Obsolete
`declined` | Declined
`pending` | Pending
`incomplete` | Incomplete
`verified` | Verified

### Retrieve Bank Account

> Retrieve Bank Account request

```shell
curl https://rehive.com/api/3/admin/users/bank-accounts/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.bank_accounts.get("{id}")
```

> Retrieve Bank Account response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "name": "Bank Account",
        "number": "12341234",
        "type": "Cheque",
        "bank_name": "Bank",
        "bank_code": "1234",
        "branch_code": "1234",
        "swift": null,
        "iban": null,
        "bic": null,
        "code": "bank_account_000000000000",
        "status": "pending"
    }
}
```

```python
{
    "id": 1,
    "user": {
        "identifier": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": "",
        "mobile_number": "+27840000000",
        "profile": null
    },
    "name": "Bank Account",
    "number": "12341234",
    "type": "Cheque",
    "bank_name": "Bank",
    "bank_code": "1234",
    "branch_code": "1234",
    "swift": null,
    "iban": null,
    "bic": null,
    "code": "bank_account_000000000000",
    "status": "pending"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/bank-accounts/{id}/`

### Update Bank Account

> Update Bank Account request

```shell
curl https://rehive.com/api/3/admin/users/bank-accounts/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "New account name"}'
```

```python
rehive.admin.bank_accounts.update(
    "{id}",
    name="New account name"
)
```

> Update Bank Account response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "name": "New account name",
        "number": "12341234",
        "type": "Cheque",
        "bank_name": "Bank",
        "bank_code": "1234",
        "branch_code": "1234",
        "swift": null,
        "iban": null,
        "bic": null,
        "code": "bank_account_000000000000",
        "status": "pending"
    }
}
```

```python
{
    "id": 1,
    "user": {
        "identifier": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": "",
        "mobile_number": "+27840000000",
        "profile": null
    },
    "name": "New account name",
    "number": "12341234",
    "type": "Cheque",
    "bank_name": "Bank",
    "bank_code": "1234",
    "branch_code": "1234",
    "swift": null,
    "iban": null,
    "bic": null,
    "code": "bank_account_000000000000",
    "status": "pending"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/bank-accounts/{id}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | Account Name | blank | false
`number` | Account Number | blank | false
`type` | Account Type | blank | false
`bank_name` | Bank Name | blank | false
`bank_code` | Bank Code | blank | false
`branch_code` | Branch Code | blank | false
`swift` | swift | blank | false
`iban` | iban | blank | false
`bic` | bic | blank | false
`status` | account status | "pending" | false

#### Statuses

Value | Description 
--- | --- 
`obsolete` | Obsolete
`declined` | Declined
`pending` | Pending
`incomplete` | Incomplete
`verified` | Verified

### Delete Bank Account

> Delete Bank Account request

```shell
curl https://rehive.com/api/3/admin/users/bank-accounts/{id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Delete Bank Account response

```shell
{
    "status": "success",
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/bank-accounts/{id}/`


### List Crypto Accounts

> Admin list crypto accounts request

```shell
curl https://www.rehive.com/api/3/admin/users/crypto-accounts/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
"To be implemented"

```

```python
"To be implemented"
```

> Admin list crypto accounts response

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
                "user": {
                    "identifier": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": "",
                    "mobile_number": "+27840000000",
                    "profile": null
                },
                "address": "0000000000000000000000000000000000",
                "code": "crypto_account_000000000000",
                "crypto_type": "bitcoin",
                "metadata": {},
                "status": "pending"
            }
        ]
    }
}
```

List a user's cryptocurrency addresses.

#### Endpoint

`https://rehive.com/api/3/admin/users/crypto-accounts/`

### Create Crypto Account

> Admin create crypto account request

```shell
curl https://www.rehive.com/api/3/admin/users/crypto-accounts/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"address": "0000000000000000000000000000000000",
        "user": "joe@rehive.com"}'
```

```javascript
"To be implemented"
```

```python
"To be implemented"
```

> Admin create crypto account response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "address": "0000000000000000000000000000000000",
        "code": "crypto_account_000000000000",
        "crypto_type": "bitcoin",
        "metadata": {},
        "status": "pending"
    }
}
```

Create a crypto account for a user.

#### Endpoint

`https://rehive.com/api/3/admin/users/crypto-accounts/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`address` | full bitcoin address | null | true
`crypto_type` | string type (bitcoin, ethereum, other) | bitcoin |  false
`metadata` | custom metadata | {} | false
`status` | string status | 'pending' | false
`user` | user identifier | null | true

#### Statuses

Value | Description 
--- | --- 
`obsolete` | Obsolete
`declined` | Declined
`pending` | Pending
`incomplete` | Incomplete
`verified` | Verified

### Retrieve Crypto Account

> Retrieve Crypto Account request

```shell
curl https://rehive.com/api/3/admin/users/crypto-accounts/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
"To be implemented"
```

> Retrieve Crypto Account response

```shell
{
    "status": "success",
    "data": {
        "id": {account_id},
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "address": "0000000000000000000000000000000000",
        "code": "crypto_account_000000000000",
        "crypto_type": "bitcoin",
        "metadata": {},
        "status": "pending"
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/crypto-accounts/{id}/`

### Update Crypto Account

> Admin update crypto account request

```shell
curl https://www.rehive.com/api/3/admin/users/crypto-accounts/{account_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"address": "0000000000000000000000000000000000"}'
```

```javascript
"To be implemented"
```

```python
"To be implemented"
```

> Admin update crypto account response

```shell
{
    "status": "success",
    "data": {
        "id": {account_id},
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "address": "0000000000000000000000000000000000",
        "code": "crypto_account_000000000000",
        "crypto_type": "bitcoin",
        "metadata": {},
        "status": "pending"
    }
}
```

Update a user's crypto account.

#### Endpoint

`https://rehive.com/api/3/admin/users/crypto-accounts/{account_id}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`address` | full bitcoin address | null | true
`crypto_type` | string type (bitcoin, ethereum, other) | bitcoin |  false
`metadata` | custom metadata | {} | false
`status` | string status | 'pending' | false

#### Statuses

Value | Description 
--- | --- 
`obsolete` | Obsolete
`declined` | Declined
`pending` | Pending
`incomplete` | Incomplete
`verified` | Verified

### Delete Crypto Account

> Admin delete crypto account request

```shell
curl https://www.rehive.com/api/3/admin/users/crypto-accounts/{account_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin delete crypto account response

```shell
{
    "status": "success",
}
```

Delete a user's crypto account.

#### Endpoint

`https://rehive.com/api/3/admin/users/crypto-accounts/{account_id}/`


### List Documents

> Admin list documents request

```shell
curl https://www.rehive.com/api/3/admin/users/documents/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
"To be implemented"
```

```python
"To be implemented"
```

> Admin list documents response

```shell
{
    "status": "success",
    "data": {
        "count": 0,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "user": {
                    "identifier": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": "",
                    "mobile_number": "+27840000000",
                    "profile": null
                },
                "file": "https://url.to/file.pdf",
                "document_category": "other",
                "document_type": "other",
                "metadata": {},
                "status": "pending"
            }
        ]
    }
}
```

Get a list of users' documents.

#### Endpoint

`https://www.rehive.com/api/3/admin/users/documents/`


### Create Document

> Admin documents request

```shell
curl https://www.rehive.com/api/3/admin/document/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -F file=@localfilename
```

```javascript
"To be implemented"
```

```python
"To be implemented"
```

> Admin documents response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "file": "https://url.to/file.pdf",
        "document_category": "other",
        "document_type": "other",
        "metadata": {},
        "status": "pending"
    }
}
```

Upload user document.

#### Endpoint

`https://rehive.com/api/3/admin/document/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`file` | a document file | null | true
`document_category` | The document category | other | false
`document_type` | The type of docuemnt | other | false
`metadata` | custom metadata | {} | false
`status` | document status | pending | false
`user` | user identifier | null | true

#### Statuses

Value | Description 
--- | --- 
`obsolete` | Obsolete
`declined` | Declined
`pending` | Pending
`incomplete` | Incomplete
`verified` | Verified

### Retrieve Document

> Retrieve Document request

```shell
curl https://rehive.com/api/3/admin/users/documents/{document_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
"To be implemented"
```

> Retrieve Document response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "file": "https://url.to/file.pdf",
        "document_category": "other",
        "document_type": "other",
        "metadata": {},
        "status": "pending"
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/documents/{document_id}/`

### Update Document

> Update document request

```shell
curl https://www.rehive.com/api/3/admin/users/documents/{document_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"status": "verified"}'
```

```javascript
"To be implemented"
```

```python
"To be implemented"
```

> Admin update crypto account response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "user": {
            "identifier": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": "",
            "mobile_number": "+27840000000",
            "profile": null
        },
        "file": "https://url.to/file.pdf",
        "document_category": "other",
        "document_type": "other",
        "metadata": {},
        "status": "verified"
    }
}
```

Update a user's document.

#### Endpoint

`https://rehive.com/api/3/admin/users/documents/{document_id}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`file` | a document file | null | true
`document_category` | The document category | other | false
`document_type` | The type of docuemnt | other | false
`metadata` | custom metadata | {} | false
`status` | document status | pending | false

#### Statuses

Value | Description 
--- | --- 
`obsolete` | Obsolete
`declined` | Declined
`pending` | Pending
`incomplete` | Incomplete
`verified` | Verified


### List Emails

> Admin list emails request

```shell
curl https://www.rehive.com/admin/api/3/admin/users/emails/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.users.emails.get()
```

> Admin list emails response

```shell
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

```python
[
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

```python
rehive.admin.users.emails.create(
    user="00000000-0000-0000-0000-000000000000",
    verified=True,
    primary=True,
    email="joe@rehive.com"
)
```

> Admin create email response

```shell
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

```python
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
}
```

Create an email address for a user.

#### Endpoint

`https://rehive.com/api/3/admin/users/emails/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`user` | user identifier | null | true
`verified` | verified status | false | false
`primary` | primary status | false | false
`email` | email address | null | true

### Retrieve Email

> Admin retrieve email request

```shell
curl https://www.rehive.com/api/3/admin/users/emails/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.users.emails.get(
    "{id}"
)
```

> Admin retrieve email response

```shell
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

```python
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
}
```

Retrieve a company's email.

#### Endpoint

`https://rehive.com/api/3/admin/users/emails/{id}/`

### Update Email

> Admin update email request

```shell
curl https://www.rehive.com/api/3/admin/users/emails/{id}/`
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"verified": true}'
```

```python
rehive.admin.users.emails.update(
    "{id}",
    verified=True
)
```

> Admin update email response

```shell
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

```python
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
}
```

Update a user's email.

#### Endpoint

`https://rehive.com/api/3/admin/users/emails/{id}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`verified` | verified status | false | false
`primary` | primary status | false | false

### Delete Email

> Admin delete email request

```shell
curl https://www.rehive.com/api/3/admin/users/emails/{id}/`
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin delete email response

```shell
{
    "status": "success",
}
```

Delete a user's email.

#### Endpoint

`https://rehive.com/api/3/admin/users/emails/{id}/`


### List Mobiles

> Admin list mobiles request

```shell
curl https://www.rehive.com/admin/api/3/admin/users/mobiles/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.users.mobiles.get()
```

> Admin list mobiles response

```shell
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

```python
[
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

```python
rehive.admin.users.mobiles.create(
    user="00000000-0000-0000-0000-000000000000",
    verified=True,
    primary=True,
    number="+27840000000"
)
```

> Admin create mobile response

```shell
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

```python
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
    "email": "+27840000000",
    "primary": true,
    "verified": true
}
```

Create a mobile number for a user.

#### Endpoint

`https://rehive.com/api/3/admin/users/mobiles/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`user` | user identifier | null | true
`verified` | verified status | false | false
`primary` | primary status | false | false
`mobile` | mobile number | null | true

### Retrieve Mobile

> Admin retrieve mobile request

```shell
curl https://www.rehive.com/api/3/admin/users/mobiles/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.users.mobiles.get(
    "{id}"
)
```

> Admin retrieve mobile response

```shell
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

```python
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
}
```

Retrieve a company's mobile.

#### Endpoint

`https://rehive.com/api/3/admin/users/mobiles/{id}/`

### Update Mobile

> Admin update mobile request

```shell
curl https://www.rehive.com/api/3/admin/users/mobiles/{id}/`
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"verified": true}'
```

```python
rehive.admin.users.mobiles.update(
    "{id}",
    verified=True
)
```

> Admin update mobile response

```shell
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

```python
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
}
```

Update a user's mobile.

#### Endpoint

`https://rehive.com/api/3/admin/users/mobiles/{id}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`verified` | verified status | false | false
`primary` | primary status | false | false


### Delete Mobile

> Admin delete mobile request

```shell
curl https://www.rehive.com/api/3/admin/users/mobiles/{id}/`
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.users.mobiles.update(
    "{id}",
    verified=True
)
```

> Admin delete mobile response

```shell
{
    "status": "success",
}
```

Delete a user's mobile.

#### Endpoint

`https://rehive.com/api/3/admin/users/mobiles/{id}/`


## Transactions

### List Transactions

> Admin transactions request

```shell
curl https://www.rehive.com/api/3/admin/transactions/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.transactions.get()

# Paginations is handled internally by the SDK
rehive.admin.transactions.get_next()
rehive.admin.transactions.get_previous()
```

> Admin transactions response

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
                "note": "",
                "metadata": {},
                "status": "Complete",
                "reference": "",
                "amount": 500,
                "fee": 0,
                "total_amount": 500,
                "balance": 500,
                "account": "0000000000",
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
                "created": 1509618707485,
                "updated": 1509618708277
            }
        ]
    }
}
```

```python
[
    {
        "id": "000000000000000000000",
        "tx_type": "credit",
        "subtype": null,
        "note": "",
        "metadata": {},
        "status": "Complete",
        "reference": "",
        "amount": 500,
        "fee": 0,
        "total_amount": 500,
        "balance": 500,
        "account": "0000000000",
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
        "created": 1509618707485,
        "updated": 1509618708277
    }
]
```

Get a company's transaction list.

#### Pagination

The list is paginated by default and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

#### Filtering

The transactions listing offers filtering on the `id`, `tx_type`, `subtype`, `status`, `created` and `metadata` fields. This is done through URL parameters in the request URL:

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

```python
rehive.admin.transactions.get_totals()
```

> Admin total transactions response

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

```python
{
    "amount": 1000,
    "fees": 0,
    "count": 2,
    "currency": "ZAR"
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
curl https://www.rehive.com/api/3/admin/transactions/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.transactions.get(
    "{id}"
)
```

> Retrieve transaction response

```shell
{
    "status": "success",
    "data":  {
        "id": "000000000000000000000",
        "tx_type": "credit",
        "subtype": null,
        "note": "",
        "metadata": {},
        "status": "Complete",
        "reference": "",
        "amount": 500,
        "fee": 0,
        "total_amount": 500,
        "balance": 500,
        "account": "0000000000",
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
        "created": 1509618707485,
        "updated": 1509618708277
    }
}
```

```python
{
    "id": "000000000000000000000",
    "tx_type": "credit",
    "subtype": null,
    "note": "",
    "metadata": {},
    "status": "Complete",
    "reference": "",
    "amount": 500,
    "fee": 0,
    "total_amount": 500,
    "balance": 500,
    "account": "0000000000",
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
    "created": 1509618707485,
    "updated": 1509618708277
}
```

Get transaction details for a spcific transactions.

#### Endpoint

`https://rehive.com/api/3/admin/transactions/{id}/`

### Update Transaction

> Admin update transaction request

```shell
curl https://rehive.com/api/3/admin/transactions/{id}/
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"status": "Complete"}'
```

```python
rehive.admin.transactions.update(
    "{id}",
    status="Complete"
)

# Quick methods for updating
rehive.admin.transactions.confirm("{id}")
rehive.admin.transactions.fail("{id}")
rehive.admin.transactions.delete("{id}")
```

> Admin update transaction response

```shell
{
    "status": "success",
    "data":  {
        "id": "000000000000000000000",
        "tx_type": "credit",
        "subtype": null,
        "note": "",
        "metadata": {},
        "status": "Complete",
        "reference": "",
        "amount": 500,
        "fee": 0,
        "total_amount": 500,
        "balance": 500,
        "account": "0000000000",
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
        "created": 1509618707485,
        "updated": 1509618708277
    }
}
```

```python
{
    "id": "000000000000000000000",
    "tx_type": "credit",
    "subtype": null,
    "note": "",
    "metadata": {},
    "status": "Complete",
    "reference": "",
    "amount": 500,
    "fee": 0,
    "total_amount": 500,
    "balance": 500,
    "account": "0000000000",
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
    "created": 1509618707485,
    "updated": 1509618708277
}
```

Update a transaction. This endpoint can be used to transition a transaction to any state. The following states transitions are permitted: `Pending`, `Complete`, `Failed`, `Deleted`. 

In addition, you can update the transaction metadata and add messages to the transaction message logs.

#### Messsages

Custom messages can be attached to transactions by including a `message` attribute in an update request. The `message`
attribute should be a JSON object with 2 attributes `level` and `message`.

1. `level` : The message log level, this can be `info`, `warning`, or `error`.
2. `message`: The message text detail.

Each message added to a transaction will be stored in a list. Rehive will also add messages to this list when erorrs occur during processing. 

#### Endpoint

`https://rehive.com/api/3/admin/transactions/{id}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`status` | update action/status (`Pending`, `Complete`, `Failed`, `Deleted`) | null | true
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

```python
rehive.admin.transactions.create_credit(
    user="joe@rehive.com",
    amount=500
)
```

> Admin credit response

```shell
{
    "status": "success",
    "data": {
        "id": "00000000000000000000",
        "metadata": {}
    }
}
```

```python
{
    "id": "00000000000000000000",
    "metadata": {}
}
```

Create a credit transaction on behalf of a user.

#### Endpoint

`https://rehive.com/api/3/admin/transactions/credit/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`user` | email, mobile number, or unique identifier | null | true
`amount` | amount | null | true
`reference` | optional credit reference | blank | false
`subtype` | a custom defined subtype | null | false
`account` | account reference code | null | false
`note` | user's note or message | blank | false
`currency` | currency code | blank | false
`metadata` | custom metadata | {} | false
`status` | status to transition to | Pending | false

<aside class="notice">
When creating transaction admin users have an additional <code>status</code> field. This field
will force a transaction to transition to the specified status immediately after creation. By default, a transaction will
transition to `Pending` when created but if you wish to complete it immediately after creation you can specify a status
of `Complete`.
</aside>

<aside class="notice">
When creating a transaction as an admin user, a <code>user</code> attribute should always be included in the request.
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

```python
rehive.admin.transactions.create_debit(
    user="joe@rehive.com",
    amount=500
)
```

> Admin debit response

```json
{
    "status": "success",
    "data": {
        "id": "00000000000000000000",
        "metadata": {}
    }
}
```

```python
{
    "id": "00000000000000000000",
    "metadata": {}
}
```

Create a debit transaction on behalf of a user.

#### Endpoint

`https://rehive.com/api/3/admin/transactions/debit/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`user` | email, mobile number, or unique identifier | null | true
`amount` | amount | null | true
`reference` | optional debit reference | blank | false
`subtype` | a custom defined subtype | null | false
`account` | account reference code | null | false
`note` | user's note or message | blank | false
`currency` | currency code | blank | false
`metadata` | custom metadata | {} | false
`status` | status to transition to | Pending | false

### Create Transfer

> Admin transfer request

```shell
curl https://www.rehive.com/api/3/admin/transactions/transfer/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"user": "joe@rehive.com",
       "amount": 500,
       "recipient": "sally@rehive.com"}'
```

```python
rehive.admin.transactions.create_transfer(
    user="joe@rehive.com",
    amount=500,
    recipient="sally@rehive.com"
)
```

> Admin transfer response

```shell
{
    "status": "success",
    "data": {
        "id": "00000000000000000000",
        "metadata": {}
    }
}
```

```python
{
    "id": "00000000000000000000",
    "metadata": {}
}
```

Create a transfer transaction on behalf of a user. This will transfer currency from one user to another. If the recipient reference does not exist as a user in Rehive and the reference is an email address or mobile number then an invitation message will be sent to the recipient informing them they have an unclaimed transaction.

#### Endpoint

`https://rehive.com/api/3/admin/transactions/transfer/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`user` | email, mobile number, or unique identifier | null | true
`amount` | amount | null | true
`recipient` | email, mobile number, or unique identifier | null | true
`currency` | currency code | blank | false
`debit_subtype` | a custom defined subtype | null | false
`debit_account` | account reference code | null | false
`debit_note` | user's note or message | blank | false
`debit_metadata` | custom metadata | {} | false
`debit_reference` | optional debit reference | string | false
`credit_subtype` | a custom defined subtype | null | false
`credit_account` | account reference code | null | false
`credit_note` | user's note or message | blank | false
`credit_metadata` | custom metadata | {} | false
`credit_reference` | optional credit reference | string | false


### List Transaction Webhooks

> List transaction webhooks request

```shell
curl https://rehive.com/api/3/admin/transactions/webhooks/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List transaction webhooks response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "url": "http://mysite.com/webhook_endpoint",
            "event": "transaction.create",
            "tx_type": "debit",
            "secret": "supersecret"
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/transactions/webhooks/`

### Create Transaction Webhooks

> Create transaction webhooks request

```shell
curl https://rehive.com/api/3/admin/transactions/webhooks/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"url": "http://mysite.com/webhook_endpoint",
       "event": "transaction.create",
       "tx_type": "debit",
       "secret": "secret"}'
```

> List transaction webhooks response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "url": "http://mysite.com/webhook_endpoint",
            "event": "transaction.create",
            "tx_type": "debit",
            "secret": "secret"
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/transactions/webhooks/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`url` | Webhook URL | blank | true
`event` | Webhook event | null | true
`tx_type` | Transaction type | null | false
`secret` | Webhook secret | "secret" | false

### Retrieve Transaction Webhook

> Retrieve transaction webhook request

```shell
curl https://rehive.com/api/3/admin/transactions/webhooks/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve transaction webhook response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "url": "http://mysite.com/webhook_endpoint",
        "event": "transaction.create",
        "tx_type": "debit",
        "secret": "secret"
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/transactions/webhooks/{id}/`

### Update Transaction Webhook

> Update transaction webhook request

```shell
curl https://rehive.com/api/3/admin/transactions/webhooks/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"url": "http://mysite.com/webhook_endpoint"}'
```

> Update transaction webhook response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "url": "http://mysite.com/webhook_endpoint",
            "event": "transaction.create",
            "tx_type": "debit",
            "secret": "secret"
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/transactions/webhooks/{id}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`url` | Webhook URL | blank | true
`event` | Webhook event | null | true
`tx_type` | Transaction type | null | false
`secret` | Webhook secret | "secret" | false


### Delete Transaction Webhook

> Delete transaction webhook request

```shell
curl https://rehive.com/api/3/admin/transactions/webhooks/{id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Delete transaction webhook response

```json
{
    "status": "success",
}
```

#### Endpoint

`https://rehive.com/api/3/admin/transactions/webhooks/{id}/`


### List Company Switches

List all switches related to transactions.

> List transaction switches request

```shell
curl https://rehive.com/api/3/admin/transactions/switches/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List transaction switches response

```shell
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

`https://rehive.com/api/3/admin/transactions/switches/`

### Create Transaction Switches

Create switches related to transactions.

> Create transaction switches request

```shell
curl https://rehive.com/api/3/admin/transactions/switches/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"tx_type": "credit",
       "enabled": true}'
```

> Create transaction switches response

```shell
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

`https://rehive.com/api/3/admin/transactions/switches/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`tx_type` | Transaction Type | | true
`subtype` | Subtype name | null | false
`enabled` | Enabled | false | true

### Retrieve Company Switches

Retrieve a specific switch related to transactions.

> Retrieve transaction switches request

```shell
curl https://rehive.com/api/3/admin/transactions/switches/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve transaction switches response

```shell
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

`https://rehive.com/api/3/admin/transactions/switches/{id}/`

### Update Transaction Switches

Update a specific switch related to transactions.

> Update transaction switches request

```shell
curl https://rehive.com/api/3/admin/transactions/switches/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"enabled": false}'
```

> Update transaction switches response

```shell
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

`https://rehive.com/api/3/admin/transactions/switches/{id}/`










## Accounts

### Create Account

> Admin create account request

```shell
curl https://www.rehive.com/api/3/admin/accounts/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"name": "savings",
       "user": "joe@rehive.com",}'
```

```python
rehive.admin.accounts.create(
    name="savings",
    user="joe@rehive.com"
)
```

> Admin create account response

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

Create a account for a user.

#### Endpoint

`https://rehive.com/api/3/admin/accounts/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | account name | null | true
`user` | account user | null | true
`reference` | account reference | 10 random chars | false
`primary` | account primary status | false | false


### List Accounts

> Admin list accounts request

```shell
curl https://www.rehive.com/api/3/admin/accounts/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.accounts.get()
```

> Admin list accounts response

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
                "user": "joe@rehive.com",
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

```python
[
    {
        "name": "default",
        "reference": "0000000000",
        "user": "joe@rehive.com",
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

```python
rehive.admin.accounts.get(
    "{reference}"
)
```

> Admin retrieve account response

```shell
{
    "status": "success",
    "data": {
        "name": "default",
        "reference": "0000000000",
        "user": "joe@rehive.com",
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

```python
{
    "name": "default",
    "reference": "0000000000",
    "user": "joe@rehive.com",
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

Retrieve an account belonging to a company.

#### Filtering

The account view offers filtering of currencies based on the `active` attribute. This is done through a URL parameter in the request URL:

`/api/3/admin/accounts/{reference}/?active=true`

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/`


### Update Account

> Admin update account request

```shell
curl https://www.rehive.com/api/3/admin/accounts/{reference}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"name": "savings"}'
```

```python
rehive.admin.accounts.update(
    "{reference}",
    name="savings"
)
```

> Admin update account response

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

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | account name | null | true
`user` | account user | null | true
`reference` | account reference | 10 random chars | false
`primary` | account primary status | false | false


### List Account Currencies

> Admin list account currencies request

```shell
curl https://www.rehive.com/admin/api/3/accounts/{reference}/currencies/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.accounts.obj("{reference}").currencies.get()
```

> Admin list account currencies response

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

```python
[
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

```python
rehive.admin.accounts.obj("{reference}").currencies.get(
    "{code}"
)
```

> Admin retrieve account currency response

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

```python
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

Retrieve an account's currency belonging to a company.

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}`

### Update Account Currency

> Admin retrieve account currency request

```shell
curl https://www.rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"active": true}'
```

```python
rehive.admin.accounts.obj("{reference}").currencies.update(
    "{code}",
    active=True
)
```

> Admin retrieve account currency response

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

```python
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

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/`

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

```python
rehive.admin.accounts.obj("{reference}").currencies.obj("{code}").limits.get()
```

> List Account Currency Limits response

```shell
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

```python
[
    {
        "id": 1,
        "value": 1000,
        "type": "Maximum",
        "tx_type": "credit",
        "subtype": null,
        "created": 1497428787920,
        "updated": 1497428787921
    }
]
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

```python
rehive.admin.accounts.obj("{reference}").currencies.obj("{code}").limits.create(
    value=1000,
    type="max",
    tx_type="credit"
)
```

> Create Account Currency response

```shell
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

```python
{
    "id": 1,
    "value": 1000,
    "type": "Maximum",
    "tx_type": "credit",
    "subtype": null,
    "created": 1497428787920,
    "updated": 1497428787921
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
`subtype` | Transaction subtype name | null | false

#### Limit Types

Value | Description 
--- | --- 
`max` | Maximum 
`day_max` | Maximum per day 
`month_max` | Maximum per month 
`min` | Minimum 
`overdraft` | Overdraft 

#### Transaction Types

Value | Description 
--- | --- 
`credit` | Credit 
`debit` | Debit

### Retrieve Account Currency Limit

Retrieve a specific requirement related to an account currency.

> Retrieve Account Currency request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.accounts.obj("{reference}").currencies.obj("{code}").limits.get(
    "{limit_id}"
)
```

> Retrieve Account Currency Limit response

```shell
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

```python
 {
    "id": 1,
    "value": 1000,
    "type": "Maximum",
    "tx_type": "credit",
    "subtype": null,
    "created": 1497428787920,
    "updated": 1497428787921
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}/`

### Update Account Currency Limit

Update a specific limits related to an account currency.

> Update Account Currency request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 5000,
       "type": "min"}'
```

```python
rehive.admin.accounts.obj("{reference}").currencies.obj("{code}").limits.update(
    "{limit_id}",
    value=500,
    type="min"
)
```

> Update Account Currency response

```shell
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

```python
{
    "id": 1,
    "value": 5000,
    "type": "Minimum",
    "tx_type": "credit",
    "subtype": null,
    "created": 1497428787920,
    "updated": 1497429648948
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`value` | Limit value | 0 | true
`type` | Limit Type |  | true
`tx_type` | Transaction type limits are applied | | true
`subtype` | Transaction subtype name | null | false

#### Limit Types

Value | Description 
--- | --- 
`max` | Maximum 
`day_max` | Maximum per day 
`month_max` | Maximum per month 
`min` | Minimum 
`overdraft` | Overdraft 

#### Transaction Types

Value | Description 
--- | --- 
`credit` | Credit 
`debit` | Debit

### Delete Account Currency Limit

Delete a specific limits related to an account currency.

> Delete Account Currency request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Delete Account Currency response

```shell
{
    "status": "success",
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}/`


### List Account Currency Fees

List all fees related to am account currency.

> List Account Currency Fees request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.accounts.obj("{reference}").currencies.obj("{code}").fees.get()
```

> List Account Currency Fees response

```shell
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

```python
[
    {
        "id": 1,
        "value": 1000,
        "percentage": null,
        "tx_type": "credit",
        "subtype": null,
        "created": 1497431721587,
        "updated": 1497431721587
    }
]
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

```python
rehive.admin.accounts.obj("{reference}").currencies.obj("{code}").fees.create(
    value=1000,
    tx_type="credit"
)
```

> Create Account Currency Fee response

```shell
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

```python
{
    "id": 1,
    "value": 1000,
    "percentage": null,
    "tx_type": "credit",
    "subtype": null,
    "created": 1497431721587,
    "updated": 1497431721587
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
`subtype` | Transaction subtype name | null | false

#### Transaction Types

Value | Description 
--- | --- 
`credit` | Credit 
`debit` | Debit

### Retrieve Account Currency fee

Retrieve a specific requirement related to an account currency.

> Retrieve Account Currency Fee request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.accounts.obj("{reference}").currencies.obj("{code}").fees.get(
    "{fee_id}"
)
```

> Retrieve Account Currency fee response

```shell
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

```python
{
    "id": 1,
    "value": 1000,
    "percentage": null,
    "tx_type": "credit",
    "subtype": null,
    "created": 1497431721587,
    "updated": 1497431721587
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}/`

### Update Account Currency Fee

Update a specific fees related to an account currency.

> Update Account Currency request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 5000}'
```

```python
rehive.admin.accounts.obj("{reference}").currencies.obj("{code}").fees.update(
    "{fee_id}",
    value=5000
)
```

> Update Account Currency response

```shell
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

```python
{
    "id": 1,
    "value": 5000,
    "percentage": null,
    "tx_type": "credit",
    "subtype": null,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`value` | Fee amount | 0 | false
`percentage` | Percentage amount |  | false
`tx_type` | Transaction type fees are applied | | true
`subtype` | Transaction subtype name | null | false

#### Transaction Types

Value | Description 
--- | --- 
`credit` | Credit 
`debit` | Debit

### Delete Account Currency Fee

Delete a specific fees related to an account currency.

> Delete Account Currency request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Delete Account Currency response

```shell
{
    "status": "success"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}/`

### List Account Currency Switches

List all switches related to the currency

> List Account Currency Switches request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.accounts.obj("{reference}").currencies.obj("{code}").switches.get()
```

> List Account Currency Switches response

```shell
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

```python
[
    {
        "id": 1,
        "tx_type": "credit",
        "subtype": null,
        "enabled": true,
        "created": 1497362397968,
        "updated": 1497362397968
    }
]
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

```python
rehive.admin.accounts.obj("{reference}").currencies.obj("{code}").switches.create(
    tx_type="credit",
    enabled=True
)
```

> Create Account Currency Switches response

```shell
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

```python
{
    "id": 1,
    "tx_type": "credit",
    "subtype": null,
    "enabled": true,
    "created": 1497362397968,
    "updated": 1497362397968
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`tx_type` | Transaction Type | | true
`subtype` | Subtype name | null | false
`enabled` | Enabled | false | true

### Retrieve Account Currency Switches

Retrieve a specific switch related to the currency

> Retrieve Account Currency Switches request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.accounts.obj("{reference}").currencies.obj("{code}").switches.get(
    "{id}"
)
```


> Retrieve Account Currency Switches response

```shell
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

```python
{
    "id": 1,
    "tx_type": "credit",
    "subtype": null,
    "enabled": true,
    "created": 1497362397968,
    "updated": 1497362397968
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/{id}/`

### Update Account Currency Switches

Update a specific switch related to the currency

> Update Account Currency Switches request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"enabled": false}'
```

```python
rehive.admin.accounts.obj("{reference}").currencies.obj("{code}").switches.update(
    "{id}",
    enabled=False
)
```

> Update Account Currency Switches response

```shell
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

```python
{
    "id": 1,
    "tx_type": "credit",
    "subtype": null,
    "enabled": false,
    "created": 1497362397968,
    "updated": 1497362931403
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/{id}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`tx_type` | Transaction Type | | true
`subtype` | Subtype name | null | false
`enabled` | Enabled | false | true

### Delete Account Currency Switches

Delete a specific switch related to the currency.

> Delete Account Currency Switches request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/{id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Delete Account Currency Switches response

```shell
{
    "status": "success",
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/{id}/`


## Currencies

### List Currencies

> Admin list currencies request

```shell
curl https://www.rehive.com/api/3/admin/currencies/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.currencies.get()
```

> Admin list currencies response

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

```python
rehive.admin.currencies.create(
    code="XBT",
    description="bitcoin",
    symbol="฿",
    unit="satoshi",
    divisibility=8
)
```

> Admin create currency response

```shell
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

```python
{
    "code": "XBT",
    "description": "bitcoin",
    "symbol": "฿",
    "unit": "bitcoin",
    "divisibility": 8,
    "enabled": false
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

```python
rehive.admin.currencies.get("{code}")
```

> Admin retrieve currency response

```shell
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

```python
{
    "code": "XBT",
    "description": "bitcoin",
    "symbol": "฿",
    "unit": "bitcoin",
    "divisibility": 8,
    "enabled": true
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

```python
rehive.admin.currencies.update(
    "{code}",
    enabled=True
)
```

> Admin update currency response

```shell
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

```python
{
    "code": "XBT",
    "description": "bitcoin",
    "symbol": "฿",
    "unit": "bitcoin",
    "divisibility": 8,
    "enabled": true
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

## Company

### Retrieve Company

> View the company info

```shell
curl https://rehive.com/api/3/admin/company/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.company.get()
```

> Company info response

```shell
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

```python
{
    "identifier": "test_company",
    "name": "Test Company 1",
    "description": "A Test Company.",
    "website": "http://www.test_company.com",
    "logo": "https://www.test_company.com/logo.jpg",
    "password_reset_url": null,
    "email_confirmation_url": null,
    "default_currency": "XBT"
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

```python
rehive.admin.company.update(
    description="A new description"
)
```

> Update company info response

```shell
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

```python
{
    "identifier": "test_company",
    "name": "Test Company 1",
    "description": "A new description",
    "website": "http://www.test_company.com",
    "logo": "https://www.test_company.com/logo.jpg",
    "password_reset_url": null,
    "email_confirmation_url": null,
    "default_currency": "XBT"
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


### List Bank Accounts

> List Bank Accounts request

```shell
curl https://rehive.com/api/3/admin/bank-accounts/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> List Bank Accounts response

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
                "name": "New account name",
                "number": "12341234",
                "type": "Cheque",
                "bank_name": "Bank",
                "bank_code": "1234",
                "branch_code": "1234",
                "swift": null,
                "iban": null,
                "bic": null,
            }
        ]
    }
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
        "bank_name": "Bank",
        "bank_code": "1234",
        "branch_code": "1234"}'
```

> Create Bank Account response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "name": "New account name",
        "number": "12341234",
        "type": "Cheque",
        "bank_name": "Bank",
        "bank_code": "1234",
        "branch_code": "1234",
        "swift": null,
        "iban": null,
        "bic": null,
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
`swift` | swift | blank | false
`iban` | iban | blank | false
`bic` | bic | blank | false

### Retrieve Bank Account

> Retrieve Bank Account request

```shell
curl https://rehive.com/api/3/admin/bank-accounts/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve Bank Account response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "name": "New account name",
        "number": "12341234",
        "type": "Cheque",
        "bank_name": "Bank",
        "bank_code": "1234",
        "branch_code": "1234",
        "swift": null,
        "iban": null,
        "bic": null,
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/bank-accounts/{id}/`

### Update Bank Account

> Update Bank Account request

```shell
curl https://rehive.com/api/3/admin/bank-accounts/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "New account name"}'
```

> Update Bank Account response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "name": "New account name",
        "number": "12341234",
        "type": "Cheque",
        "bank_name": "Bank",
        "bank_code": "1234",
        "branch_code": "1234",
        "swift": null,
        "iban": null,
        "bic": null,
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/bank-accounts/{id}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | Account Name | blank | false
`number` | Account Number | blank | false
`type` | Account Type | blank | false
`bank_name` | Bank Name | blank | false
`bank_code` | Bank Code | blank | false
`branch_code` | Branch Code | blank | false
`swift` | swift | blank | false
`iban` | iban | blank | false
`bic` | bic | blank | false


### Delete Bank Account

> Delete Bank Account request

```shell
curl https://rehive.com/api/3/admin/bank-accounts/{id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Delete Bank Account response

```shell
{
    "status": "success",
}
```

#### Endpoint

`https://rehive.com/api/3/admin/bank-accounts/{id}/`


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
            "event": "user.create",
            "secret": "secret"
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/webhooks/`

### Create Webhook

> Create webhooks request

```shell
curl https://rehive.com/api/3/admin/webhooks/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"url": "http://mysite.com/webhook_endpoint",
       "event": "user.create",
       "secret": "secret"}'
```

```python
"To be implemented"
```

> List webhooks response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "url": "http://mysite.com/webhook_endpoint",
            "event": "user.create",
            "secret": "secret"
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
`event` | Webhook event | null | true
`secret` | Webhook secret | "secret" | false

### Retrieve Webhook

> Retrieve webhook request

```shell
curl https://rehive.com/api/3/admin/webhooks/{id}/
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
        "event": "user.create",
        "secret": "secret"
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/webhooks/{id}/`

### Update Webhook

> Update webhook request

```shell
curl https://rehive.com/api/3/admin/webhooks/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"url": "http://mysite.com/webhook_endpoint"}'
```

> Update webhook response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "url": "http://mysite.com/webhook_endpoint",
            "event": "user.create",
            "secret": "secret"
        }
    ]
}
```

#### Endpoint

`https://rehive.com/api/3/admin/webhooks/{id}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`url` | Webhook URL | blank | true
`event` | Webhook event | null | true
`secret` | Webhook secret | "secret" | false

### Delete Webhook

> Delete webhook request

```shell
curl https://rehive.com/api/3/admin/webhooks/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Delete webhook response

```json
{
    "status": "success",
}
```

#### Endpoint

`https://rehive.com/api/3/admin/webhooks/{id}/`


## Subtypes

### List Subtypes

> List subtypes request

```shell
curl https://rehive.com/api/3/admin/subtypes/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.subtypes.get()
```

> List subtypes response

```shell
{
    "status": "success",
    "data": [
        {
            "id": 20,
            "name": "credit_subtype",
            "label": "Our credit",
            "description": "Description for our credit",
            "tx_type": "credit",
            "enabled": true,
            "created": 1509529290352,
            "updated": 1509529290352
        }
    ]
}
```

```python
[
    {
        "id": 20,
        "name": "credit_subtype",
        "label": "Our credit",
        "description": "Description for our credit",
        "tx_type": "credit",
        "enabled": true,
        "created": 1509529290352,
        "updated": 1509529290352
    }
]
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

```python
rehive.admin.subtypes.create(
    name="credit_subtype",
    label="Our credit",
    description="Description for our credit",
    tx_type="credit",
    enabled=True
)
```

> Create subtypes response

```shell
{
    "status": "success",
    "data": {
        "id": 20,
        "name": "credit_subtype",
        "label": "Our credit",
        "description": "Description for our credit",
        "tx_type": "credit",
        "created": 1509529290352,
        "updated": 1509529290352
    }
}
```

```python
 {
    "id": 20,
    "name": "credit_subtype",
    "label": "Our credit",
    "description": "Description for our credit",
    "tx_type": "credit",
    "created": 1509529290352,
    "updated": 1509529290352
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
`enabled` | enabled status | true | false

### Retrieve Subtypes

> Retrieve subtypes request

```shell
curl https://rehive.com/api/3/admin/subtypes/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.subtypes.get("{id}")
```

> Retrieve subtypes response

```shell
{
    "status": "success",
    "data": {
        "id": 20,
        "name": "credit_subtype",
        "label": "Our credit",
        "description": "Description for our credit",
        "tx_type": "credit",
        "created": 1509529290352,
        "updated": 1509529290352
    }
}
```

```python
{
    "id": 20,
    "name": "credit_subtype",
    "label": "Our credit",
    "description": "Description for our credit",
    "tx_type": "credit",
    "created": 1509529290352,
    "updated": 1509529290352
}
```

#### Endpoint

`https://rehive.com/api/3/admin/subtypes/{id}/`

### Update subtype

> Update subtype request

```shell
curl https://rehive.com/api/3/admin/subtypes/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"description": "New description"}'
```

```python
rehive.admin.subtypes.update(
    "{id}",
    description="New description"
)
```

> Update subtype response

```shell
{
    "status": "success",
    "data": {
        "id": 20,
        "name": "credit_subtype",
        "label": "Our credit",
        "description": "New description",
        "tx_type": "credit",
        "created": 1509529290352,
        "updated": 1509529290352
    }
}
```

```python
{
    "id": 20,
    "name": "credit_subtype",
    "label": "Our credit",
    "description": "New description",
    "tx_type": "credit",
    "created": 1509529290352,
    "updated": 1509529290352
}
```

#### Endpoint

`https://rehive.com/api/3/admin/subtypes/{id}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | name | blank | true
`label` | label | blank | false
`description` | description | blank | false
`tx_type` | Transaction type | blank | true
`enabled` | enabled status | true | false

### Delete Subtype

> Delete subtype request

```shell
curl https://rehive.com/api/3/admin/subtypes/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Delete subtype response

```shell
{
    "status": "success",
}
```

<aside class="notice">
You cannot delete a subtype that has already been used in a transaction. If you want to make an already used subtype
inaccessible you can "disable" it instead using the `enabled` attribute.
</aside>

#### Endpoint

`https://rehive.com/api/3/admin/subtypes/{id}/`


## Notifications

### List Notifications

> List Notifications request

```shell
curl https://rehive.com/api/3/admin/notifications/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```python
rehive.admin.notifications.get()
```

> List Notifications response

```shell
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "name": "account_verify",
            "description": "Account verification notifications",
            "enabled": true
        }
    ]
}
```

```python
[
    {
        "id": 1,
        "name": "account_verify",
        "description": "Account verification notifications",
        "enabled": true
    }
]
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

```python
rehive.admin.notifications.get("{id}")
```

> Retrieve Notifications response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "name": "account_verify",
        "description": "Account verification notifications",
        "enabled": true
    }
}
```

```python
{
    "id": 1,
    "name": "account_verify",
    "description": "Account verification notifications",
    "enabled": trueed": true
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

```python
rehive.admin.notifications.update(
    "{id}",
    enabled=False
)
```

> Update Notifications response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "name": "account_verify",
        "description": "Account verification notifications",
        "enabled": false
    }
}
```

```python
{
    "id": 1,
    "name": "account_verify",
    "description": "Account verification notifications",
    "enabled": false
}
```

#### Endpoint

`https://rehive.com/api/3/admin/notifications/{id}`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`enabled` | Account Name | false | true

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

```python
rehive.admin.tiers.create(
    switch_type="transactions",
    enabled=False
)
```

> Create Tier response

```shell
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

```python
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

```python
rehive.admin.tiers.get()
```

> List Tier response

```shell
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

```python
[
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

```python
rehive.admin.tiers.get("{id}")
```

> Retrieve Tier response

```shell
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

```python
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

```python
rehive.admin.tiers.update(
    "{id}",
    name="Updated name"
)
```

> Update Tier response

```shell
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

```python
{
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

```python
rehive.admin.tiers.obj("{tier_id}").requirements.get()
```

> List Tier Requirements response

```shell
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

```python
[
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

```python
rehive.admin.tiers.obj("{tier_id}").requirements.create(
    requirement="birth_date"
)
```

> Create Tier Requirements response

```shell
{
    "status": "success",
    "data": {
        "id": 3,
        "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
        "requirement": "Birth Date"
    }
}
```

```python
{
    "id": 3,
    "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
    "requirement": "Birth Date"
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

```python
rehive.admin.tiers.obj("{tier_id}").requirements.get(
    "{requirement_id}"
)
```

> Retrieve Tier Requirements response

```shell
{
    "status": "success",
    "data": {
        "id": 3,
        "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
        "requirement": "Birth Date"
    }
}
```

```python
{
    "id": 3,
    "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
    "requirement": "Birth Date"
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

```python
rehive.admin.tiers.obj("{tier_id}").requirements.update(
    "{requirement_id}",
    requirement="proof_of_identity"
)
```

> Update Tier Requirements response

```shell
{
    "status": "success",
    "data": {
        "id": 3,
        "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
        "requirement": "Proof Of Identity"
    }
}
```

```python
{
    "id": 3,
    "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
    "requirement": "Proof Of Identity"
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

```python
rehive.admin.tiers.obj("{tier_id}").limits.get()
```

> List Tier Limits response

```shell
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

```python
[
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

```python
rehive.admin.tiers.obj("{tier_id}").limits.create(
    type="Maximum",
    value=1000,
    tx_type="credit"
)
```

> Create Tier Limits response

```shell
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

```python
{
    "id": 1,
    "value": 1000,
    "type": "Maximum",
    "tx_type": "credit",
    "subtype": null,
    "created": 1497374071027,
    "updated": 1497374071027
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/limits/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`value` | Limit value | 0 | true
`type` | Limit Type |  | true
`tx_type` | Transaction type limits are applied | | true
`subtype` | Transaction subtype name | null | false

#### Limit Types

Value | Description 
--- | --- 
`max` | Maximum 
`day_max` | Maximum per day 
`month_max` | Maximum per month 
`min` | Minimum 
`overdraft` | Overdraft 

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

```python
rehive.admin.tiers.obj("{tier_id}").limits.get(
    "{limit_id}"
)
```

> Retrieve Tier Limits response

```shell
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

```python
{
    "id": 1,
    "value": 1000,
    "type": "Maximum",
    "tx_type": "credit",
    "subtype": null,
    "created": 1497374071027,
    "updated": 1497374071027
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/limits/{limits_id}`

### Update Tier Limits

Update a specific limits related to a Tier

> Update Tier Limits request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/limits/{limits_id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 5000,
       "type": "min"}'
```

```python
rehive.admin.tiers.obj("{tier_id}").limits.update(
    "{limit_id}",
    value=500,
    type="min"
)
```

> Update Tier Limits response

```shell
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

```python
{
    "id": 1,
    "value": 5000,
    "type": "Minimum",
    "tx_type": "credit",
    "subtype": null,
    "created": 1497374071027,
    "updated": 1497374886088
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

```python
rehive.admin.tiers.obj("{tier_id}").fees.get()
```

> List Tier Fees response

```shell
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

```python
[
    {
        "id": 1,
        "value": 1000,
        "percentage": null,
        "tx_type": "credit",
        "subtype": null,
        "created": 1497431721587,
        "updated": 1497431721587
    }
]
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

```python
rehive.admin.tiers.obj("{tier_id}").fees.create(
    value=1000,
    tx_type="credit"
)
```

> Create Tier Fee response

```shell
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

```python
{
    "id": 1,
    "value": 1000,
    "percentage": null,
    "tx_type": "credit",
    "subtype": null,
    "created": 1497431721587,
    "updated": 1497431721587
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
`subtype` | Transaction subtype name | null | false

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

```python
rehive.admin.tiers.obj("{tier_id}").fees.get(
    "{fee_id}"
)
```

> Retrieve Tier Fee response

```shell
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

```python
{
    "id": 1,
    "value": 1000,
    "percentage": null,
    "tx_type": "credit",
    "subtype": null,
    "created": 1497431721587,
    "updated": 1497431721587
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

```python
rehive.admin.tiers.obj("{tier_id}").fees.update(
    "{fee_id}",
    value=5000
)
```

> Update Tier response

```shell
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

```python
{
    "id": 1,
    "value": 5000,
    "percentage": null,
    "tx_type": "credit",
    "subtype": null,
    "created": 1497431721587,
    "updated": 1497431938971
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

```python
rehive.admin.tiers.obj("{tier_id}").switches.get()
```

> List Tier Switches response

```shell
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

```python
[
    {
        "id": 1,
        "tx_type": "credit",
        "subtype": null,
        "enabled": true,
        "created": 1497370313086,
        "updated": 1497370313086
    }
]
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

```python
rehive.admin.tiers.obj("{tier_id}").switches.create(
    tx_type="credit",
    enabled=True
)
```

> Create Tier Switches response

```shell
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

```python
{
    "id": 1,
    "tx_type": "credit",
    "subtype": null,
    "enabled": true,
    "created": 1497370313086,
    "updated": 1497370313086
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/switches/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`tx_type` | Transaction Type | | true
`subtype` | Subtype name | null | false
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

```python
rehive.admin.tiers.obj("{tier_id}").switches.get("{switch_id}")
```

> Retrieve Tier Switches response

```shell
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

```python
{
    "id": 1,
    "tx_type": "credit",
    "subtype": null,
    "enabled": true,
    "created": 1497370313086,
    "updated": 1497370313086
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

```python
rehive.admin.tiers.obj("{tier_id}").switches.update(
    "{switch_id}",
    enabled=False
)
```

> Update Tier Switches response

```shell
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

```python
{
    "id": 1,
    "tx_type": "credit",
    "subtype": null,
    "enabled": true,
    "created": 1497370313086,
    "updated": 1497370313086
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/switches/{switch_id}`

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

```python
rehive.admin.swtiches.create(
    switch_type="transactions",
    enabled=False
)
```

> Create Global Switches response

```shell
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

```python
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
    "enabled": false,
    "created": 1497348308625,
    "updated": 1497348318654
}
```

#### Types
Global switches can be one of the following 2 types.

Value | Description
--- | ---
`transactions` | Allow transactions
`verification` | Allow transactions for unverified users
`overdraft` | Allow unlimited overdrafts
`auto_confirm | Automatically complete transactions on creation
`manage_accounts` | Allow users to manage their accounts
`session_duration` | Allow users to set their own session duration

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

```python
rehive.admin.switches.get()
```

> List Global Switches response

```shell
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

```python
[
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

```python
rehive.admin.switches.get("{id}")
```

> Retrieve Global Switches response

```shell
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

```python
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

```python
rehive.admin.switches.update(
    "{id}",
    enabled=False
)
```

> Update Global Switches response

```shell
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

```python
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
    "enabled": false,
    "created": 1497348308625,
    "updated": 1497348318654
}
```

#### Endpoint

`https://rehive.com/api/3/admin/switches/{id}`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`switch_type` | Global Switch Type | | false
`enabled` | Account Name | false | false
