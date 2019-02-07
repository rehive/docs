# Administration

Rehive includes a set of admin-only endpoints that provide adminsitration level functionality to all Rehive resources.

## Users

### Users Overview

> Admin users overview request

```shell
curl https://api.rehive.com/3/admin/users/overview/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.overview.get().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.overview.get()
```

> Admin list users overview response

```shell
{
    "data": {
        "total": 1,
        "archived": 1,
        "active": 1
    },
    "status": "success"
}
```

```javascript
{
    "total": 1,
    "archived": 1,
    "active": 1
}
```

```python
{
    "total": 1,
    "archived": 1,
    "active": 1
}
```

Get an overview of users belonging to a company.

#### Endpoint

`https://api.rehive.com/3/admin/users/overview/`

### List Users

> Admin list users request

```shell
curl https://api.rehive.com/3/admin/users/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.get().then(function (res) {
    ...
}, function (err) {
    ...
});
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
                "id": "00000000-0000-0000-0000-000000000000",
                "first_name": "Joe",
                "last_name": "Soap",
                "email": "joe@rehive.com",
                "username": null,
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
                "mobile": "+27840000000",
                "timezone": "Asia/Dhaka",
                "verified": true,
                "verification": {
                    "email": true,
                    "mobile": true
                },
                "kyc": {
                    "updated": 1509539801040,
                    "status": "pending"
                },
                "status": "pending",
                "groups": [],
                "created": 1464912953000,
                "updated": 1464912953000,
                "last_login": null,
                "archived": false
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
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
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
            "mobile": "+27840000000",
            "timezone": "Asia/Dhaka",
            "verified": true,
            "verification": {
                "email": true,
                "mobile": true
            },
            "kyc": {
                "updated": 1509539801040,
                "status": "pending"
            },
            "status": "pending",
            "groups": [],
            "created": 1464912953000,
            "updated": 1464912953000,
            "last_login": null,
            "archived": false
        }
    ]
}
```

```python
[
    {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
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
        "mobile": "+27840000000",
        "timezone": "Asia/Dhaka",
        "verified": true,
        "verification": {
            "email": true,
            "mobile": true
        },
        "kyc": {
            "updated": 1509539801040,
            "status": "pending"
        },
        "status": "pending",
        "groups": [],
        "created": 1464912953000,
        "updated": 1464912953000,
        "last_login": null,
        "archived": false
    }
]
```

Get a list of users belonging to a company.

#### Filtering

Field | Type
--- | ---
`id` | string
`user` | string
`email` | string
`mobile` | string
`first_name` | string
`last_name` | string
`username` | string
`id_number` | string
`language` | string
`nationality` | string
`status` | string
`currency` | string
`created` | millisecond timestamp
`updated` | millisecond timestamp
`last_login` | millisecond timestamp
`archived` | boolean
`id__contains` | string
`email__contains` | string
`mobile__contains` | string
`username__contains` | string

#### Endpoint

`https://api.rehive.com/3/admin/users/`

### Create User

> Admin create user request

```shell
curl https://api.rehive.com/3/admin/users/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"first_name": "Joe",
       "last_name": "Soap",
       "mobile": "+27840000000",
       "email": "joe@rehive.com"}'
```

```javascript
var fileSelected = document.getElementById("userProfile").files[0],
        formData = new FormData;

formData.append('profile', fileSelected);
formData.append('first_name', first_name);
formData.append('last_name', last_name);
formData.append('email', email);
formData.append('id_number', id_number);
formData.append('language', language);
formData.append('nationality', nationality);
formData.append('metadata', metadata);
formData.append('mobile', mobile);
formData.append('timezone', timezone);

rehive.admin.users.create(formData).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.create(
    first_name="Joe",
    last_name="Soap",
    mobile="+27840000000",
    email="joe@rehive.com"
)
```

> Admin create user response

```shell
{
    "status": "success",
    "data": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
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
        "mobile": "+27840000000",
        "timezone": "Asia/Dhaka",
        "verified": true,
        "verification": {
            "email": true,
            "mobile": true
        },
        "verification": {
            "email": true,
            "mobile": true
        },
        "kyc": {
            "updated": 1509539801040,
            "status": "pending"
        },
        "status": "pending",
        "groups": [],
        "permissions": [],
        "created": 1464912953000,
        "updated": 1464912953000,
        "settings": {
            "allow_transactions": true,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        },
        "last_login": null,
        "archived": false
    }
}
```

```javascript
{
    "id": "00000000-0000-0000-0000-000000000000",
    "first_name": "Joe",
    "last_name": "Soap",
    "email": "joe@rehive.com",
    "username": null,
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
    "mobile": "+27840000000",
    "timezone": "Asia/Dhaka",
    "verified": true,
    "verification": {
        "email": true,
        "mobile": true
    },
    "kyc": {
        "updated": 1509539801040,
        "status": "pending"
    },
    "status": "pending",
    "groups": [],
    "permissions": [],
    "created": 1464912953000,
    "updated": 1464912953000,
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "last_login": null,
    "archived": false
}
```

```python
{
    "id": "00000000-0000-0000-0000-000000000000",
    "first_name": "Joe",
    "last_name": "Soap",
    "email": "joe@rehive.com",
    "username": null,
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
    "mobile": "+27840000000",
    "timezone": "Asia/Dhaka",
    "verified": true,
    "kyc": {
        "updated": 1509539801040,
        "status": "pending"
    },
    "status": "pending",
    "groups": [],
    "permissions": [],
    "created": 1464912953000,
    "updated": 1464912953000,
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "last_login": null,
    "archived": false
}
```

Create a user.

#### Endpoint

`https://api.rehive.com/3/admin/users/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`id` | unique id (cannot be changed once set)| string (uuid)
`username` | unique username (cannot be changed once set) | null
`first_name` | first name | blank
`last_name` | last name | blank
`email` | email address | null
`mobile` | mobile number | null
`id_number` | ID number | blank
`profile` | profile image | blank
`language` | language code (`af`, `en` etc.) | blank
`nationality` | nationality code (`ZA`, `UK` etc.) | blank
`metadata` | custom metadata | {}
`mobile` | mobile number | blank
`timezone` | timezone | blank
`birth_date` | birth date | blank
`archived` | boolean | false

### Retrieve User

> Admin retrieve user request

```shell
curl https://api.rehive.com/3/admin/users/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.get({id: id}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.get(
    "{id}"
)
```

> Admin retrieve user response

```shell
{
    "status": "success",
    "data": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
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
        "mobile": "+27840000000",
        "timezone": "Asia/Dhaka",
        "verified": true,
        "verification": {
            "email": true,
            "mobile": true
        },
        "kyc": {
            "updated": 1509539801040,
            "status": "pending"
        },
        "status": "pending",
        "groups": [],
        "permissions": [],
        "created": 1464912953000,
        "updated": 1464912953000,
        "settings": {
            "allow_transactions": true,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        },
        "last_login": null,
        "archived": false
    }
}
```

```javascript
{
    "id": "00000000-0000-0000-0000-000000000000",
    "first_name": "Joe",
    "last_name": "Soap",
    "email": "joe@rehive.com",
    "username": null,
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
    "mobile": "+27840000000",
    "timezone": "Asia/Dhaka",
    "verified": true,
    "verification": {
        "email": true,
        "mobile": true
    },
    "kyc": {
        "updated": 1509539801040,
        "status": "pending"
    },
    "status": "pending",
    "groups": [],
    "permissions": [],
    "created": 1464912953000,
    "updated": 1464912953000,
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "last_login": null,
    "archived": false
}
```

```python
{
    "id": "00000000-0000-0000-0000-000000000000",
    "first_name": "Joe",
    "last_name": "Soap",
    "email": "joe@rehive.com",
    "username": null,
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
    "mobile": "+27840000000",
    "timezone": "Asia/Dhaka",
    "verified": true,
    "verification": {
        "email": true,
        "mobile": true
    },
    "kyc": {
        "updated": 1509539801040,
        "status": "pending"
    },
    "status": "pending",
    "groups": [],
    "permissions": [],
    "created": 1464912953000,
    "updated": 1464912953000,
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "last_login": null,
    "archived": false
}
```

Retrieve a company's user.

#### Endpoint

`https://api.rehive.com/3/admin/users/{id}/`

### Update User

> Admin update user request

```shell
curl https://api.rehive.com/3/admin/users/{id}/`
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"first_name": "Joe"}'
```

```javascript
var fileSelected = document.getElementById("userUpdateProfile").files[0],
    formData = new FormData,
    data = {first_name: 'Joe'};

if(fileSelected){
    formData.append('profile', fileSelected);
}

for (var key in data) {
    if (data[key]) {
        formData.append(key, data[key]);
    }
}

rehive.admin.users.update(id, formData).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.update(
    "{id}",
    first_name="Joe"
)
```

> Admin update user response

```shell
{
    "status": "success",
    "data": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
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
        "mobile": "+27840000000",
        "timezone": "Asia/Dhaka",
        "verified": true,
        "verification": {
            "email": true,
            "mobile": true
        },
        "kyc": {
            "updated": 1509539801040,
            "status": "pending"
        },
        "status": "pending",
        "groups": [],
        "permissions": [],
        "created": 1464912953000,
        "updated": 1464912953000,
        "settings": {
            "allow_transactions": true,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        },
        "last_login": null,
        "archived": false
    }
}
```

```javascript
{
    "id": "00000000-0000-0000-0000-000000000000",
    "first_name": "Joe",
    "last_name": "Soap",
    "email": "joe@rehive.com",
    "username": null,
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
    "mobile": "+27840000000",
    "timezone": "Asia/Dhaka",
    "verified": true,
    "verification": {
        "email": true,
        "mobile": true
    },
    "kyc": {
        "updated": 1509539801040,
        "status": "pending"
    },
    "status": "pending",
    "groups": [],
    "permissions": [],
    "created": 1464912953000,
    "updated": 1464912953000,
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "last_login": null,
    "archived": false
}
```

```python
{
    "id": "00000000-0000-0000-0000-000000000000",
    "first_name": "Joe",
    "last_name": "Soap",
    "email": "joe@rehive.com",
    "username": null,
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
    "mobile": "+27840000000",
    "timezone": "Asia/Dhaka",
    "verified": true,
    "verification": {
        "email": true,
        "mobile": true
    },
    "kyc": {
        "updated": 1509539801040,
        "status": "pending"
    },
    "status": "pending",
    "groups": [],
    "permissions": [],
    "created": 1464912953000,
    "updated": 1464912953000,
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "last_login": null,
    "archived": false
}
```

Update a user's details.

#### Endpoint

`https://api.rehive.com/3/admin/users/{id}/`

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
`status` | status | pending
`archived` | boolean | false

#### Statuses

Value | Description
--- | ---
`obsolete` | Obsolete
`declined` | Declined
`pending` | Pending
`incomplete` | Incomplete
`verified` | Verified

### Retrieve User Settings

> Admin retrieve user settings request

```shell
curl https://api.rehive.com/3/admin/users/{id}/settings/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.settings.get(id).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.obj('2fba8a20-3d4b-41db-994d-ddc86159316f').settings.get()
```

> Admin retrieve user settings response

```shell
{
    "status": "success",
    "data": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    }
}
```

```javascript
{
    "allow_transactions": true,
    "allow_debit_transactions": true,
    "allow_credit_transactions": true
}
```

```python
{
    "allow_transactions": true,
    "allow_debit_transactions": true,
    "allow_credit_transactions": true
}
```

Retrieve a company's user settings.

#### Endpoint

`https://api.rehive.com/3/admin/users/{id}/settings/`

### Update User Settings

> Admin update user settings request

```shell
curl https://api.rehive.com/3/admin/users/{id}/settings/`
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"allow_transactions": true}'
```

```javascript
rehive.admin.users.settings.update(id, {allow_transactions: true}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.obj('{id}').settings.update(
    allow_transactions=True
)
```

> Admin update user settings response

```shell
{
    "status": "success",
    "data": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    }
}
```

```javascript
{
    "allow_transactions": true,
    "allow_debit_transactions": true,
    "allow_credit_transactions": true
}
```

```python
{
    "allow_transactions": true,
    "allow_debit_transactions": true,
    "allow_credit_transactions": true
}
```

Update a user's settings.

#### Endpoint

`https://api.rehive.com/3/admin/users/{id}/settings/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`allow_transactions` | Allow transactions | true
`allow_debit_transactions` | Allow debit transactions | true
`allow_credit_transactions` | Allow credit transactions | true,


### Retrieve User KYC

> Admin retrieve user kyc request

```shell
curl https://api.rehive.com/3/admin/users/{id}/kyc/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
```

```python
```

> Admin retrieve user kyc response

```shell
{
    "status": "success",
    "data": {
        "status": "pending",
        "updated": 1520929665311
    }
}
```

```javascript
```

```python
```

Retrieve a company's user kyc details.

#### Endpoint

`https://api.rehive.com/3/admin/users/{id}/kyc/`

### Update User KYC

> Admin update user kyc request

```shell
curl https://api.rehive.com/3/admin/users/{id}/kyc/`
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"status": "verified"}'
```

```javascript

```

```python
```

> Admin update user kyc response

```shell
{
    "status": "success",
    "data": {
        "status": "verified",
        "updated": 1520929665311
    }
}
```

```javascript
```

```python
```

Update a user's kyc.

#### Endpoint

`https://api.rehive.com/3/admin/users/{id}/kyc/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`status` | kyc status| true

#### Statuses

Value | Description
--- | ---
`obsolete` | Obsolete
`declined` | Declined
`pending` | Pending
`incomplete` | Incomplete
`verified` | Verified


### List Addresses

> List Addresses request

```shell
curl https://api.rehive.com/3/admin/users/addresses/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.addresses.get().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.addresses.get()
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
                    "id": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": null,
                    "mobile": "+27840000000",
                    "profile": null
                },
                "line_1": "1 Main Street",
                "line_2": "East City",
                "city": "Cape Town",
                "state_province": "Western Cape",
                "country": "ZA",
                "postal_code": "8001"
                "status": "pending",
                "archived": false,
                "created": 1520929665311,
                "updated": 1520929665311
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
            "id": 2,
            "user": {
                "id": "00000000-0000-0000-0000-000000000000",
                "first_name": "Joe",
                "last_name": "Soap",
                "email": "joe@rehive.com",
                "username": null,
                "mobile": "+27840000000",
                "profile": null
            },
            "line_1": "1 Main Street",
            "line_2": "East City",
            "city": "Cape Town",
            "state_province": "Western Cape",
            "country": "ZA",
            "postal_code": "8001"
            "status": "pending",
            "archived": false,
            "created": 1520929665311,
            "updated": 1520929665311
        }
    ]
}
```

```python
[
    {
        "id": 2,
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "line_1": "1 Main Street",
        "line_2": "East City",
        "city": "Cape Town",
        "state_province": "Western Cape",
        "country": "ZA",
        "postal_code": "8001"
        "status": "pending",
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
]
```

#### Filtering

Field | Type
--- | ---
`user` | string
`status` | string

#### Endpoint

`https://api.rehive.com/3/admin/users/addresses/`

### Create Address

> Create Address request

```shell
curl https://api.rehive.com/3/admin/users/addresses/
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

```javascript
rehive.admin.users.addresses.create(
{
    user: "joe@rehive.com",
    line_1: "1 Main Street",
    line_2: "East City",
    city: "Cape Town",
    state_province: "Western Cape",
    country: "ZA",
    postal_code: "8001",
    status: "pending"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.addresses.create(
    line_1="1 Main Street",
    line_2="East City",
    city="Cape Town",
    state_province="Western Cape",
    country="ZA",
    postal_code="8001",
    user="joe@rehive.com"
)
```

> Create Address response

```shell
{
    "status": "success",
    "data": {
        "id": 2,
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "line_1": "1 Main Street",
        "line_2": "East City",
        "city": "Cape Town",
        "state_province": "Western Cape",
        "country": "ZA",
        "postal_code": "8001"
        "status": "pending",
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
}
```

```javascript
{
    "id": 2,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "line_1": "1 Main Street",
    "line_2": "East City",
    "city": "Cape Town",
    "state_province": "Western Cape",
    "country": "ZA",
    "postal_code": "8001"
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

```python
{
    "id": 2,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "line_1": "1 Main Street",
    "line_2": "East City",
    "city": "Cape Town",
    "state_province": "Western Cape",
    "country": "ZA",
    "postal_code": "8001"
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

#### Endpoint

`https://api.rehive.com/3/admin/users/addresses/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`user` | email, mobile number, username, or unique id | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`line_1` | address line one | blank
`line_2` | address line 2 | blank
`city` | city | blank
`state_province` | state or province | blank
`country` | country code | blank
`postal_code` | postal or zip code) | blank
`status` | account status | "pending"
`archived` | archived state | false

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
curl https://api.rehive.com/3/admin/users/addresses/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.addresses.get({id: id}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.addresses.get(
   {id}
)
```

> Retrieve Address response

```shell
{
    "status": "success",
    "data": {
        "id": 2,
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "line_1": "1 Main Street",
        "line_2": "East City",
        "city": "Cape Town",
        "state_province": "Western Cape",
        "country": "ZA",
        "postal_code": "8001"
        "status": "pending",
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
}
```

```javascript
{
    "id": 2,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "line_1": "1 Main Street",
    "line_2": "East City",
    "city": "Cape Town",
    "state_province": "Western Cape",
    "country": "ZA",
    "postal_code": "8001"
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

```python
{
    "id": 2,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "line_1": "1 Main Street",
    "line_2": "East City",
    "city": "Cape Town",
    "state_province": "Western Cape",
    "country": "ZA",
    "postal_code": "8001"
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

#### Endpoint

`https://api.rehive.com/3/admin/users/addresses/{id}/`

### Update Address

> Update Address request

```shell
curl https://api.rehive.com/3/admin/users/addresses/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"line_1": "1 Main Street"}'
```

```javascript
rehive.admin.users.addresses.update(id,{
    line_1: '1 Main Street',
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.addresses.update(
    {id},
    line_1="1 Main Street"
)
```

> Update Address response

```shell
{
    "status": "success",
    "data": {
        "id": 2,
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "line_1": "1 Main Street",
        "line_2": "East City",
        "city": "Cape Town",
        "state_province": "Western Cape",
        "country": "ZA",
        "postal_code": "8001"
        "status": "pending",
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
}
```

```javascript
{
    "id": 2,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "line_1": "1 Main Street",
    "line_2": "East City",
    "city": "Cape Town",
    "state_province": "Western Cape",
    "country": "ZA",
    "postal_code": "8001"
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

```python
{
    "id": 2,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "line_1": "1 Main Street",
    "line_2": "East City",
    "city": "Cape Town",
    "state_province": "Western Cape",
    "country": "ZA",
    "postal_code": "8001"
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

#### Endpoint

`https://api.rehive.com/3/admin/users/addresses/{id}/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`line_1` | address line one | blank
`line_2` | address line 2 | blank
`city` | city | blank
`state_province` | state or province | blank
`country` | country code | blank | false
`postal_code` | postal or zip code) | blank
`status` | account status | "pending"
`archived` | archived state | false

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
curl https://api.rehive.com/3/admin/users/addresses/{id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.addresses.delete(id).then(function (res) {
   ...
}, function (err) {
   ...
});
```

```python
rehive.admin.users.addresses.delete(
    {id}
)
```

> Delete address response

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

#### Endpoint

`https://api.rehive.com/3/admin/users/addresses/{id}/`


### List Bank Accounts

> List Bank Accounts request

```shell
curl https://api.rehive.com/3/admin/users/bank-accounts/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.bankAccounts.get().then(function (res) {
    ...
}, function (err) {
    ...
});
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
                    "id": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": null,
                    "mobile": "+27840000000",
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
                "status": "pending",
                "archived": false,
                "created": 1520929665311,
                "updated": 1520929665311
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
            "id": 1,
            "user": {
                "id": "00000000-0000-0000-0000-000000000000",
                "first_name": "Joe",
                "last_name": "Soap",
                "email": "joe@rehive.com",
                "username": null,
                "mobile": "+27840000000",
                "profile": null
            },
            "name": "Bank Account",
            "number": "12341234",
            "type": "Cheque",
            "bank_name": "Barclays",
            "bank_code": "1234",
            "branch_code": "1234",
            "swift": null,
            "iban": null,
            "bic": null,
            "code": "bank_account_000000000000",
            "status": "pending",
            "archived": false,
            "created": 1520929665311,
            "updated": 1520929665311
        }
    ]
}
```

```python
[
    {
        "id": 1,
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
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
        "status": "pending",
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
]
```

#### Endpoint

`https://api.rehive.com/3/admin/users/bank-accounts/`

### Create Bank Account

> Create Bank Account request

```shell
curl https://api.rehive.com/3/admin/users/bank-accounts/
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

```javascript
rehive.admin.users.bankAccounts.create({
    user: "joe@rehive.com",
    name: "Bank",
    number: "23434",
    type: "cash",
    bank_name: "bank name",
    bank_code: 234342,
    branch_code: 2343,
    swift: "",
    iban: "",
    bic: "",
    status: "verified"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
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
        "status": "pending",
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
}
```

```javascript
{
    "id": 1,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "name": "Bank Account",
    "number": "12341234",
    "type": "Cheque",
    "bank_name": "Barclays",
    "bank_code": "1234",
    "branch_code": "1234",
    "swift": null,
    "iban": null,
    "bic": null,
    "code": "bank_account_000000000000",
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

```python
 {
    "id": 2,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
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
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

#### Endpoint

`https://api.rehive.com/3/admin/users/bank-accounts/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`user` | email, mobile number, username, or unique id | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`name` | Account Name | blank
`number` | Account Number | blank
`type` | Account Type | blank
`bank_name` | Bank Name | blank
`bank_code` | Bank Code | blank
`branch_code` | Branch Code | blank
`status` | account status | "pending"
`swift` | swift | blank
`iban` | iban | blank
`bic` | bic | blank
`archived` | archived state | false

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
curl https://api.rehive.com/3/admin/users/bank-accounts/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.bankAccounts.get({id: id}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
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
        "status": "pending",
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
}
```

```javascript
{
    "id": 1,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "name": "Bank Account",
    "number": "12341234",
    "type": "Cheque",
    "bank_name": "Barclays",
    "bank_code": "1234",
    "branch_code": "1234",
    "swift": null,
    "iban": null,
    "bic": null,
    "code": "bank_account_000000000000",
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

```python
{
    "id": 1,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
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
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

#### Endpoint

`https://api.rehive.com/3/admin/users/bank-accounts/{id}/`

### Update Bank Account

> Update Bank Account request

```shell
curl https://api.rehive.com/3/admin/users/bank-accounts/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "New account name"}'
```

```javascript
rehive.admin.users.bankAccounts.update(id,{
    name: 'New account name'
}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
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
        "status": "pending",
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
}
```

```javascript
{
    "id": 1,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "name": "Bank Account",
    "number": "12341234",
    "type": "Cheque",
    "bank_name": "Barclays",
    "bank_code": "1234",
    "branch_code": "1234",
    "swift": null,
    "iban": null,
    "bic": null,
    "code": "bank_account_000000000000",
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

```python
{
    "id": 1,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
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
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

#### Endpoint

`https://api.rehive.com/3/admin/users/bank-accounts/{id}/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`name` | Account Name | blank
`number` | Account Number | blank
`type` | Account Type | blank
`bank_name` | Bank Name | blank
`bank_code` | Bank Code | blank
`branch_code` | Branch Code | blank
`status` | account status | "pending"
`swift` | swift | blank
`iban` | iban | blank
`bic` | bic | blank
`archived` | archived state | false

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
curl https://api.rehive.com/3/admin/users/bank-accounts/{id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.bankAccounts.delete(id).then(function (res) {
   ...
}, function (err) {
   ...
});
```

```python
rehive.admin.users.bank_accounts.delete(
    {id}
)
```

> Delete Bank Account response

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

#### Endpoint

`https://api.rehive.com/3/admin/users/bank-accounts/{id}/`


### List Crypto Accounts

> Admin list crypto accounts request

```shell
curl https://api.rehive.com/3/admin/users/crypto-accounts/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.cryptoAccounts.get().then(function (res) {
    ...
}, function (err) {
    ...
});

```

```python
rehive.admin.users.crypto_accounts.get()
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
                    "id": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": null,
                    "mobile": "+27840000000",
                    "profile": null
                },
                "address": "0000000000000000000000000000000000",
                "code": "crypto_account_000000000000",
                "crypto_type": "bitcoin",
                "metadata": {},
                "status": "pending",
                "archived": false,
                "created": 1520929665311,
                "updated": 1520929665311
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
            "id": 1,
            "user": {
                "id": "00000000-0000-0000-0000-000000000000",
                "first_name": "Joe",
                "last_name": "Soap",
                "email": "joe@rehive.com",
                "username": null,
                "mobile": "+27840000000",
                "profile": null
            },
            "address": "0000000000000000000000000000000000",
            "code": "crypto_account_000000000000",
            "crypto_type": "bitcoin",
            "metadata": {},
            "status": "pending",
            "archived": false,
            "created": 1520929665311,
            "updated": 1520929665311
        }
    ]
}
```

```python
[
    {
        "id": 1,
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "address": "0000000000000000000000000000000000",
        "code": "crypto_account_000000000000",
        "crypto_type": "bitcoin",
        "metadata": {},
        "status": "pending",
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
]
```

List a user's cryptocurrency addresses.

#### Filtering

Field | Type
--- | ---
`user` | string
`status` | string

#### Endpoint

`https://api.rehive.com/3/admin/users/crypto-accounts/`

### Create Crypto Account

> Admin create crypto account request

```shell
curl https://api.rehive.com/3/admin/users/crypto-accounts/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"address": "0000000000000000000000000000000000",
        "user": "joe@rehive.com"}'
```

```javascript
rehive.admin.users.cryptoAccounts.create(
{
    user: 'joe@rehive.com',
    crypto_type: 'ethereum',
    address: '3242342343223dewwrewrw',
    metadata: {},
    status: 'incomplete'
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.crypto_accounts.create(
    address="0000000000000000000000000000000000",
    type="bitcoin",
    user="joe@rehive.com"
)
```

> Admin create crypto account response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "address": "0000000000000000000000000000000000",
        "code": "crypto_account_000000000000",
        "crypto_type": "bitcoin",
        "metadata": {},
        "status": "pending",
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
}
```

```javascript
{
    "id": 1,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "address": "0000000000000000000000000000000000",
    "code": "crypto_account_000000000000",
    "crypto_type": "bitcoin",
    "metadata": {},
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

```python
{
    "id": 1,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "address": "0000000000000000000000000000000000",
    "code": "crypto_account_000000000000",
    "crypto_type": "bitcoin",
    "metadata": {},
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

Create a crypto account for a user.

#### Endpoint

`https://api.rehive.com/3/admin/users/crypto-accounts/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`user` | email, mobile number, username, or unique id| null
`address` | full bitcoin address | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`crypto_type` | string type (bitcoin, ethereum, other) | bitcoin
`metadata` | custom metadata | {}
`status` | string status | 'pending'
`archived` | archived state | false

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
curl https://api.rehive.com/3/admin/users/crypto-accounts/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.cryptoAccounts.get({id: id}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.crypto_accounts.get(
    {id}
)
```

> Retrieve Crypto Account response

```shell
{
    "status": "success",
    "data": {
        "id": {account_id},
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "address": "0000000000000000000000000000000000",
        "code": "crypto_account_000000000000",
        "crypto_type": "bitcoin",
        "metadata": {},
        "status": "pending",
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
}
```

```javascript
{
    "id": {account_id},
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "address": "0000000000000000000000000000000000",
    "code": "crypto_account_000000000000",
    "crypto_type": "bitcoin",
    "metadata": {},
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

```python
{
    "id": {account_id},
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "address": "0000000000000000000000000000000000",
    "code": "crypto_account_000000000000",
    "crypto_type": "bitcoin",
    "metadata": {},
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

#### Endpoint

`https://api.rehive.com/3/admin/users/crypto-accounts/{id}/`

### Update Crypto Account

> Admin update crypto account request

```shell
curl https://api.rehive.com/3/admin/users/crypto-accounts/{account_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"address": "0000000000000000000000000000000000"}'
```

```javascript
rehive.admin.users.cryptoAccounts.update(id,
{
    address: "0000000000000000000000000000000000"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.crypto_accounts.update(
    {account_id},
    address="0000000000000000000000000000000000"
)
```

> Admin update crypto account response

```shell
{
    "status": "success",
    "data": {
        "id": {account_id},
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "address": "0000000000000000000000000000000000",
        "code": "crypto_account_000000000000",
        "crypto_type": "bitcoin",
        "metadata": {},
        "status": "pending",
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
}
```

```javascript
{
    "id": {account_id},
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "address": "0000000000000000000000000000000000",
    "code": "crypto_account_000000000000",
    "crypto_type": "bitcoin",
    "metadata": {},
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

```python
{
    "id": {account_id},
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "address": "0000000000000000000000000000000000",
    "code": "crypto_account_000000000000",
    "crypto_type": "bitcoin",
    "metadata": {},
    "status": "pending",
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

Update a user's crypto account.

#### Endpoint

`https://api.rehive.com/3/admin/users/crypto-accounts/{account_id}/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`user` | email, mobile number, username, or unique id | null
`address` | full bitcoin address | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`crypto_type` | string type (bitcoin, ethereum, other) | bitcoin
`metadata` | custom metadata | {}
`status` | string status | 'pending'
`archived` | archived state | false

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
curl https://api.rehive.com/3/admin/users/crypto-accounts/{account_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.cryptoAccounts.delete(id).then(function (res) {
   ...
}, function (err) {
   ...
});
```

```python
rehive.admin.users.crypto_accounts.delete(
    {id}
)
```

> Admin delete crypto account response

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

`https://api.rehive.com/3/admin/users/crypto-accounts/{account_id}/`


### List Documents

> Admin list documents request

```shell
curl https://api.rehive.com/3/admin/users/documents/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.documents.get().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.documents.get()
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
                    "id": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": null,
                    "mobile": "+27840000000",
                    "profile": null
                },
                "file": "https://url.to/file.pdf",
                "document_category": "other",
                "document_type": "other",
                "metadata": {},
                "status": "pending",
                "note": null,
                "archived": false,
                "created": 1520929665311,
                "updated": 1520929665311
            }
        ]
    }
}
```

```javascript
{
    "count": 0,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "user": {
                "id": "00000000-0000-0000-0000-000000000000",
                "first_name": "Joe",
                "last_name": "Soap",
                "email": "joe@rehive.com",
                "username": null,
                "mobile": "+27840000000",
                "profile": null
            },
            "file": "https://url.to/file.pdf",
            "document_category": "other",
            "document_type": "other",
            "metadata": {},
            "status": "pending",
            "note": null,
            "archived": false,
            "created": 1520929665311,
            "updated": 1520929665311
        }
    ]
}
```

```python
[
    {
        "id": 1,
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "file": "https://url.to/file.pdf",
        "document_category": "other",
        "document_type": "other",
        "metadata": {},
        "status": "pending",
        "note": null,
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
]
```

Get a list of users' documents.

#### Filtering

Field | Type
--- | ---
`user` | string
`status` | string

#### Endpoint

`https://api.rehive.com/3/admin/users/documents/`


### Create Document

> Admin documents request

```shell
curl https://api.rehive.com/3/admin/users/documents/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: multipart/form-data"
  -F file=@localfilename
```

```javascript
var fileSelected = document.getElementById("adminUserDocument").files[0],
        formData = new FormData();

formData.append('file', fileSelected);
formData.append('user', user);
formData.append('document_type', document_type);
formData.append('metadata', JSON.stringify(metadata));
formData.append('note', note);
formData.append('status', status);

rehive.admin.users.documents.create(formData).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
# File argument should be the fullpath to the file
rehive.admin.documents.upload(
    document_type="other",
    file={localfilename}
)
```

> Admin documents response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "file": "https://url.to/file.pdf",
        "document_category": "other",
        "document_type": "other",
        "metadata": {},
        "status": "pending",
        "note": null,
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
}
```

```javascript
{
    "id": 1,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "file": "https://url.to/file.pdf",
    "document_category": "other",
    "document_type": "other",
    "metadata": {},
    "status": "pending",
    "note": null,
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

```python
{
    "id": 1,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "file": "https://url.to/file.pdf",
    "document_category": "other",
    "document_type": "other",
    "metadata": {},
    "status": "pending",
    "note": null,
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

Create a user document.

#### Endpoint

`https://api.rehive.com/3/admin/users/document/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`user` | email, mobile number, username, or unique id | null
`file` | a document file | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`document_type` | The type of docuemnt | other
`metadata` | custom metadata | {}
`status` | document status | pending
`archived` | archived state | false

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
curl https://api.rehive.com/3/admin/users/documents/{document_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.documents.get({id: document_id}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.documents.get(
    {document_id}
)
```

> Retrieve Document response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "file": "https://url.to/file.pdf",
        "document_category": "other",
        "document_type": "other",
        "metadata": {},
        "status": "pending",
        "note": null,
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
}
```

```javascript
{
    "id": 1,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "file": "https://url.to/file.pdf",
    "document_category": "other",
    "document_type": "other",
    "metadata": {},
    "status": "pending",
    "note": null,
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

```python
{
    "id": 1,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "file": "https://url.to/file.pdf",
    "document_category": "other",
    "document_type": "other",
    "metadata": {},
    "status": "pending",
    "note": null,
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

#### Endpoint

`https://api.rehive.com/3/admin/users/documents/{document_id}/`

### Update Document

> Update document request

```shell
curl https://api.rehive.com/3/admin/users/documents/{document_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: multipart/form-data"
  -F file=@localfilename
```

```javascript
var fileSelected = document.getElementById("updateAdminUserDocument").files[0],
        formData = new FormData(),
        data = {first_name: 'Joe'};

if(fileSelected) {
    formData.append('file', fileSelected);
}

for (var key in data) {
    if (data[key]) {
        formData.append(key, data[key]);
    }
}

rehive.admin.users.documents.update(id, formData).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.documents.update(
    document_type="other"
)
```

> Admin update crypto account response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "file": "https://url.to/file.pdf",
        "document_category": "other",
        "document_type": "other",
        "metadata": {},
        "status": "verified",
        "note": null,
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
}
```

```javascript
{
    "id": 1,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "file": "https://url.to/file.pdf",
    "document_category": "other",
    "document_type": "other",
    "metadata": {},
    "status": "verified",
    "note": null,
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

```python
{
    "id": 1,
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "file": "https://url.to/file.pdf",
    "document_category": "other",
    "document_type": "other",
    "metadata": {},
    "status": "verified",
    "note": null,
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

Update a user's document.

#### Endpoint

`https://api.rehive.com/3/admin/users/documents/{document_id}/`

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
`status` | document status | pending
`archived` | archived state | false

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
curl https://api.rehive.com/3/admin/users/emails/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.emails.get().then(function (res) {
    ...
}, function (err) {
    ...
});
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
                    "id": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": null,
                    "mobile": "+27840000000",
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

```javascript
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "user": {
                "id": "00000000-0000-0000-0000-000000000000",
                "first_name": "Joe",
                "last_name": "Soap",
                "email": "joe@rehive.com",
                "username": null,
                "mobile": "+27840000000",
                "profile": null
            },
            "id": 1,
            "email": "joe@rehive.com",
            "primary": true,
            "verified": true
        },
    ]
}```

```python
[
    {
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
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

#### Filtering

Field | Type
--- | ---
`user` | string

#### Endpoint

`https://api.rehive.com/3/admin/users/emails/`

### Create Email

> Admin create email request

```shell
curl https://api.rehive.com/3/admin/users/emails/`
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"user": 00000000-0000-0000-0000-000000000000,
       "verified": true,
       "primary": true,
       "email": "joe@rehive.com"}'
```

```javascript
rehive.admin.users.emails.create({
    user: '00000000-0000-0000-0000-000000000000',
    email: 'joe@rehive.com',
    primary: true,
    verified: true
}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "id": 1,
        "email": "joe@rehive.com",
        "primary": true,
        "verified": true
    }
}
```

```javascript
{
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "id": 1,
    "email": "joe@rehive.com",
    "primary": true,
    "verified": true
}
```

```python
{
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
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

`https://api.rehive.com/3/admin/users/emails/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`user` | email, mobile number, username, or unique id | null
`email` | email address | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`verified` | verified status | false
`primary` | primary status | false

### Retrieve Email

> Admin retrieve email request

```shell
curl https://api.rehive.com/3/admin/users/emails/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.emails.get({id: id).then(function (res) {
    ...
}, function (err) {
    ...
});
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
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "id": 1,
        "email": "joe@rehive.com",
        "primary": true,
        "verified": true
    }
}
```

```javascript
{
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "id": 1,
    "email": "joe@rehive.com",
    "primary": true,
    "verified": true
}
```

```python
{
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
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

`https://api.rehive.com/3/admin/users/emails/{id}/`

### Update Email

> Admin update email request

```shell
curl https://api.rehive.com/3/admin/users/emails/{id}/`
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"verified": true}'
```

```javascript
rehive.admin.users.emails.update(id,{verified: true}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "id": 1,
        "email": "joe@rehive.com",
        "primary": true,
        "verified": true
    }
}
```

```javascript
{
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "id": 1,
    "email": "joe@rehive.com",
    "primary": true,
    "verified": true
}
```

```python
{
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
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

`https://api.rehive.com/3/admin/users/emails/{id}/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`verified` | verified status | false
`primary` | primary status | false

### Delete Email

> Admin delete email request

```shell
curl https://api.rehive.com/3/admin/users/emails/{id}/`
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.emails.delete(id).then(function (res) {
   ...
}, function (err) {
   ...
});
```

```python
rehive.admin.users.emails.delete(
    {id}
)
```

> Admin delete email response

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

Delete a user's email.

#### Endpoint

`https://api.rehive.com/3/admin/users/emails/{id}/`


### List Mobiles

> Admin list mobiles request

```shell
curl https://api.rehive.com/3/admin/users/mobiles/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.mobiles.get().then(function (res) {
    ...
}, function (err) {
    ...
});
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
                    "id": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": null,
                    "mobile": "+27840000000",
                    "profile": null
                },
                "id": 1,
                "number": "+27840000000",
                "primary": true,
                "verified": true,
                "archived": false,
                "created": 1520929665311,
                "updated": 1520929665311
            },
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
            "user": {
                "id": "00000000-0000-0000-0000-000000000000",
                "first_name": "Joe",
                "last_name": "Soap",
                "email": "joe@rehive.com",
                "username": null,
                "mobile": "+27840000000",
                "profile": null
            },
            "id": 1,
            "number": "+27840000000",
            "primary": true,
            "verified": true,
            "archived": false,
            "created": 1520929665311,
            "updated": 1520929665311
        },
    ]
}
```

```python
[
    {
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "id": 1,
        "number": "+27840000000",
        "primary": true,
        "verified": true,
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    },
]
```

Get a list of mobile numbers belonging to a company.

#### Filtering

Field | Type
--- | ---
`user` | string

#### Endpoint

`https://api.rehive.com/3/admin/users/mobiles/`

### Create Mobile

> Admin create mobile request

```shell
curl https://api.rehive.com/3/admin/users/mobiles/`
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"user": 00000000-0000-0000-0000-000000000000,
       "verified": true,
       "primary": true,
       "number": "+27840000000"}'
```

```javascript
rehive.admin.users.mobiles.create({
   user: 00000000-0000-0000-0000-000000000000,
   verified: true,
   primary: true,
   number: "+27840000000"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "id": 1,
        "email": "+27840000000",
        "primary": true,
        "verified": true,
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
}
```

```javascript
{
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "id": 1,
    "email": "+27840000000",
    "primary": true,
    "verified": true,
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

```python
{
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "id": 1,
    "email": "+27840000000",
    "primary": true,
    "verified": true,
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

Create a mobile number for a user.

#### Endpoint

`https://api.rehive.com/3/admin/users/mobiles/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`user` | email, mobile number, username, or unique id | null
`mobile` | mobile number | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`verified` | verified status | false
`primary` | primary status | false
`archived` | archived state | false

### Retrieve Mobile

> Admin retrieve mobile request

```shell
curl https://api.rehive.com/3/admin/users/mobiles/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.mobiles.get({id: id}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "id": 1,
        "number": "+27840000000",
        "primary": true,
        "verified": true,
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
}
```

```javascript
{
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "id": 1,
    "number": "+27840000000",
    "primary": true,
    "verified": true,
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

```python
{
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "id": 1,
    "number": "+27840000000",
    "primary": true,
    "verified": true,
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

Retrieve a company's mobile.

#### Endpoint

`https://api.rehive.com/3/admin/users/mobiles/{id}/`

### Update Mobile

> Admin update mobile request

```shell
curl https://api.rehive.com/3/admin/users/mobiles/{id}/`
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"verified": true}'
```

```javascript
rehive.admin.users.mobiles.update(id,{
    verified: true
}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "id": 1,
        "number": "+27840000000",
        "primary": true,
        "verified": true,
        "archived": false,
        "created": 1520929665311,
        "updated": 1520929665311
    }
}
```

```javascript
{
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "id": 1,
    "number": "+27840000000",
    "primary": true,
    "verified": true,
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

```python
{
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "id": 1,
    "number": "+27840000000",
    "primary": true,
    "verified": true,
    "archived": false,
    "created": 1520929665311,
    "updated": 1520929665311
}
```

Update a user's mobile.

#### Endpoint

`https://api.rehive.com/3/admin/users/mobiles/{id}/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`verified` | verified status | false
`primary` | primary status | false
`archived` | archived state | false

### Delete Mobile

> Admin delete mobile request

```shell
curl https://api.rehive.com/3/admin/users/mobiles/{id}/`
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.mobiles.delete(id).then(function (res) {
   ...
}, function (err) {
   ...
});
```

```python
rehive.admin.users.mobiles.delete(
    "{id}"
)
```

> Admin delete mobile response

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

Delete a user's mobile.

#### Endpoint

`https://api.rehive.com/3/admin/users/mobiles/{id}/`


## Transactions

### List Transactions

> Admin transactions request

```shell
curl https://api.rehive.com/3/admin/transactions/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.transactions.get().then(function (res) {
    ...
}, function (err) {
    ...
});

// Paginations is handled internally by the SDK
rehive.admin.transactions.getNext()
rehive.admin.transactions.getPrevious()
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
                "status": "Pending",
                "reference": "",
                "amount": 500,
                "fee": 0,
                "total_amount": 500,
                "balance": 0,
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
                    "id": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": null,
                    "mobile": "+27840000000",
                    "profile": null
                },
                "source_transaction": null,
                "destination_transaction": null,
                "archived": false,
                "created": 1509618707485,
                "updated": 1509618708277
            }
        ]
    }
}
```

```javascript
{
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
            "status": "Pending",
            "reference": "",
            "amount": 500,
            "fee": 0,
            "total_amount": 500,
            "balance": 0,
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
                "id": "00000000-0000-0000-0000-000000000000",
                "first_name": "Joe",
                "last_name": "Soap",
                "email": "joe@rehive.com",
                "username": null,
                "mobile": "+27840000000",
                "profile": null
            },
            "source_transaction": null,
            "destination_transaction": null,
            "archived": false,
            "created": 1509618707485,
            "updated": 1509618708277
        }
    ]
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
        "status": "Pending",
        "reference": "",
        "amount": 500,
        "fee": 0,
        "total_amount": 500,
        "balance": 0,
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
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "source_transaction": null,
        "destination_transaction": null,
        "archived": false,
        "created": 1509618707485,
        "updated": 1509618708277
    }
]
```

Get a company's transaction list.

#### Filtering

Field | Type
--- | ---
`id` | string
`tx_type` | boolean
`subtype` | string
`status` | string
`account` | string
`user` | string
`source_transaction` | boolean
`destination_transaction` | boolean
`created` | millsecond timestamp
`updated` | millsecond timestamp
`metadata` | any
`archived` | boolean

#### Endpoint

`https://api.rehive.com/3/admin/transactions/`

### Total Transactions

> Admin total transactions request

```shell
curl https://api.rehive.com/3/admin/transactions/totals/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.transactions.totals.get().then(function (res) {
    ...
}, function (err) {
    ...
});
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

```javascript
{
    "amount": 1000,
    "fees": 0,
    "count": 2,
    "currency": "ZAR"
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

See Transaction List filtering above.

#### Endpoint

`https://api.rehive.com/3/admin/transactions/totals/`


### Create Credit

> Admin credit request

```shell
curl https://api.rehive.com/3/admin/transactions/credit/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"user": "joe@rehive.com",
       "amount": 500,
       "currency": "ZAR"}'
```

```javascript
rehive.admin.transactions.createCredit(
{
    user: "joe@rehive.com",
    amount: 500,
    currency: "ZAR"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.transactions.create_credit(
    user="joe@rehive.com",
    amount=500,
    currency="ZAR"
)
```

> Admin credit response

```shell
{
    "status": "success",
    "data": {
        "id": "00000000-0000-0000-0000-000000000000",
        "tx_type": "credit",
        "subtype": null,
        "note": "",
        "metadata": {},
        "status": "Pending",
        "reference": null,
        "amount": 500,
        "fee": 0,
        "total_amount": 500,
        "balance": 0,
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
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "source_transaction": null,
        "destination_transaction": null,
        "messages": [],
        "fees": [],
        "archived": false,
        "created": 1476691969394,
        "updated": 1496135465287
    }
}
```

```javascript
{
    "id": "00000000-0000-0000-0000-000000000000",
    "tx_type": "credit",
    "subtype": null,
    "note": "",
    "metadata": {},
    "status": "Pending",
    "reference": null,
    "amount": 500,
    "fee": 0,
    "total_amount": 500,
    "balance": 0,
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
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "source_transaction": null,
    "destination_transaction": null,
    "messages": [],
    "fees": [],
    "archived": false,
    "created": 1476691969394,
    "updated": 1496135465287
}
```

```python
{
    "id": "00000000-0000-0000-0000-000000000000",
    "tx_type": "credit",
    "subtype": null,
    "note": "",
    "metadata": {},
    "status": "Pending",
    "reference": null,
    "amount": 500,
    "fee": 0,
    "total_amount": 500,
    "balance": 0,
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
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "source_transaction": null,
    "destination_transaction": null,
    "messages": [],
    "fees": [],
    "archived": false,
    "created": 1476691969394,
    "updated": 1496135465287
}
```

Create a credit transaction on behalf of a user.

#### Endpoint

`https://api.rehive.com/3/admin/transactions/credit/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`user` | email, mobile number, username, or unique id| null
`amount` | amount | null
`currency` | currency code | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`id` | unique id (cannot be changed once set)| string (uuid)
`reference` | optional credit reference | blank
`subtype` | a custom defined subtype | null
`account` | account reference code | null
`note` | user's note or message | blank
`metadata` | custom metadata | {}
`status` | status to transition to | Pending
`archived` | archived state | false

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
curl https://api.rehive.com/3/admin/transactions/debit/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"user": "joe@rehive.com",
       "amount": 500,
       "currency": "ZAR"}'
```

```javascript
rehive.admin.transactions.createDebit(
{
    user: "joe@rehive.com",
    amount: 500,
    currency: "ZAR"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.transactions.create_debit(
    user="joe@rehive.com",
    amount=500,
    currency="ZAR"
)
```

> Admin debit response

```shell
{
    "status": "success",
    "data": {
        "id": "00000000-0000-0000-0000-000000000000",
        "tx_type": "debit",
        "subtype": null,
        "note": "",
        "metadata": {},
        "status": "Pending",
        "reference": null,
        "amount": -500,
        "fee": 0,
        "total_amount": -500,
        "balance": 0,
        "account": "0000000000",
        "label": "Debit",
        "company": "rehive",
        "currency": {
            "description": "Rand",
            "code": "ZAR",
            "symbol": "R",
            "unit": "rand",
            "divisibility": 2
        },
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "source_transaction": null,
        "destination_transaction": null,
        "messages": [],
        "fees": [],
        "archived": false,
        "created": 1476691969394,
        "updated": 1496135465287
    }
}
```

```javascript
{
    "id": "00000000-0000-0000-0000-000000000000",
    "tx_type": "debit",
    "subtype": null,
    "note": "",
    "metadata": {},
    "status": "Pending",
    "reference": null,
    "amount": -500,
    "fee": 0,
    "total_amount": -500,
    "balance": 0,
    "account": "0000000000",
    "label": "Debit",
    "company": "rehive",
    "currency": {
        "description": "Rand",
        "code": "ZAR",
        "symbol": "R",
        "unit": "rand",
        "divisibility": 2
    },
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "source_transaction": null,
    "destination_transaction": null,
    "messages": [],
    "fees": [],
    "archived": false,
    "created": 1476691969394,
    "updated": 1496135465287
}
```

```python
{
    "id": "00000000-0000-0000-0000-000000000000",
    "tx_type": "debit",
    "subtype": null,
    "note": "",
    "metadata": {},
    "status": "Pending",
    "reference": null,
    "amount": -500,
    "fee": 0,
    "total_amount": -500,
    "balance": 0,
    "account": "0000000000",
    "label": "Debit",
    "company": "rehive",
    "currency": {
        "description": "Rand",
        "code": "ZAR",
        "symbol": "R",
        "unit": "rand",
        "divisibility": 2
    },
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "source_transaction": null,
    "destination_transaction": null,
    "messages": [],
    "fees": [],
    "archived": false,
    "created": 1476691969394,
    "updated": 1496135465287
}
```

Create a debit transaction on behalf of a user.

#### Endpoint

`https://api.rehive.com/3/admin/transactions/debit/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`user` | mail, mobile number, username, or unique id | null
`amount` | amount | null
`currency` | currency code | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`id` | unique id (cannot be changed once set)| string (uuid)
`reference` | optional debit reference | blank
`subtype` | a custom defined subtype | null
`account` | account reference code | null
`note` | user's note or message | blank
`metadata` | custom metadata | {}
`status` | status to transition to | Pending
`archived` | archived state | false

### Create Transfer

> Admin transfer request

```shell
curl https://api.rehive.com/3/admin/transactions/transfer/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"user": "joe@rehive.com",
       "amount": 500,
       "currency": "ZAR",
       "recipient": "susan@rehive.com"}'
```

```javascript
rehive.admin.transactions.createTransfer(
{
    user: "joe@rehive.com",
    amount: 500,
    currency: "ZAR",
    recipient: "susan@rehive.com"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.transactions.create_transfer(
    user="joe@rehive.com",
    amount=500,
    currency="ZAR",
    recipient="susan@rehive.com"
)
```

> Admin transfer response

```shell
{
    "status": "success",
    "data": {
        "id": "00000000-0000-0000-0000-000000000000",
        "tx_type": "debit",
        "subtype": null,
        "note": "",
        "metadata": {},
        "status": "Pending",
        "reference": null,
        "amount": -500,
        "fee": 0,
        "total_amount": -500,
        "balance": 0,
        "account": "0000000000",
        "label": "Debit",
        "company": "rehive",
        "currency": {
            "description": "Rand",
            "code": "ZAR",
            "symbol": "R",
            "unit": "rand",
            "divisibility": 2
        },
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "source_transaction": null,
        "destination_transaction": {
            "id": "00000000-0000-0000-0000-000000000000",
            "user": {
                "id": "00000000-0000-0000-0000-000000000000",
                "first_name": "Susan",
                "last_name": "Brown",
                "email": "susan@rehive.com",
                "username": null,
                "mobile": "+27850000000",
                "profile": null
            }
        },
        "messages": [],
        "fees": [],
        "archived": false,
        "created": 1476691969394,
        "updated": 1496135465287
    }
}
```

```javascript
{
    "id": "00000000-0000-0000-0000-000000000000",
    "tx_type": "debit",
    "subtype": null,
    "note": "",
    "metadata": {},
    "status": "Pending",
    "reference": null,
    "amount": -500,
    "fee": 0,
    "total_amount": -500,
    "balance": 0,
    "account": "0000000000",
    "label": "Debit",
    "company": "rehive",
    "currency": {
        "description": "Rand",
        "code": "ZAR",
        "symbol": "R",
        "unit": "rand",
        "divisibility": 2
    },
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "source_transaction": null,
    "destination_transaction": {
        "id": "00000000-0000-0000-0000-000000000000",
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Susan",
            "last_name": "Brown",
            "email": "susan@rehive.com",
            "username": null,
            "mobile": "+27850000000",
            "profile": null
        }
    },
    "messages": [],
    "fees": [],
    "archived": false,
    "created": 1476691969394,
    "updated": 1496135465287
}
```

```python
{
    "id": "00000000-0000-0000-0000-000000000000",
    "tx_type": "debit",
    "subtype": null,
    "note": "",
    "metadata": {},
    "status": "Pending",
    "reference": null,
    "amount": -500,
    "fee": 0,
    "total_amount": -500,
    "balance": 0,
    "account": "0000000000",
    "label": "Debit",
    "company": "rehive",
    "currency": {
        "description": "Rand",
        "code": "ZAR",
        "symbol": "R",
        "unit": "rand",
        "divisibility": 2
    },
    "user": {
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "source_transaction": null,
    "destination_transaction": {
        "id": "00000000-0000-0000-0000-000000000000",
        "user": {
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Susan",
            "last_name": "Brown",
            "email": "susan@rehive.com",
            "username": null,
            "mobile": "+27850000000",
            "profile": null
        }
    },
    "messages": [],
    "fees": [],
    "archived": false,
    "created": 1476691969394,
    "updated": 1496135465287
}
```

Create a transfer transaction on behalf of a user. This will transfer currency from one user to another. If the recipient reference does not exist as a user in Rehive and the reference is an email address or mobile number then an invitation message will be sent to the recipient informing them they have an unclaimed transaction.

#### Endpoint

`https://api.rehive.com/3/admin/transactions/transfer/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`user` | mail, mobile number, username, or unique id | null
`amount` | amount | null
<ul><li>`recipient`</li>and/or<li>`credit_account`</li></ul> | <ul><li>email, mobile number, username, or unique id</li><li>account reference code</li></ul> | null
`currency` | currency code | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`debit_subtype` | a custom defined subtype | null
`debit_account` | account reference code | null
`debit_note` | user's note or message | blank
`debit_metadata` | custom metadata | {}
`debit_reference` | optional debit reference | string
`credit_subtype` | a custom defined subtype | null
`credit_account` | account reference code | null
`credit_note` | user's note or message | blank
`credit_metadata` | custom metadata | {}
`credit_reference` | optional credit reference | string
`archived` | archived state | false

### Create Transactions

> Admin create transactions request

```shell
curl https://api.rehive.com/3/admin/transactions/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"transactions": [{"tx_type": "debit",
       "user": "joe@rehive.com",
       "amount": 500,
       "currency": "ZAR"},
       {"tx_type": "debit",
       "user": "joe@rehive.com",
       "amount": 500,
       "currency": "ZAR"}]}'
```

```javascript
```

```python
```

> Admin create transactions response

```shell
{
    "status": "success",
    "data": {
        "transactions": [
            {
                "id": "00000000-0000-0000-0000-000000000000",
                "tx_type": "credit",
                "subtype": null,
                "note": "",
                "metadata": {},
                "status": "Pending",
                "reference": null,
                "amount": 500,
                "fee": 0,
                "total_amount": 500,
                "balance": 0,
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
                    "id": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": null,
                    "mobile": "+27840000000",
                    "profile": null
                },
                "source_transaction": null,
                "destination_transaction": null,
                "messages": [],
                "fees": [],
                "archived": false,
                "created": 1476691969394,
                "updated": 1496135465287
            },
            {
                "id": "00000000-0000-0000-0000-000000000000",
                "tx_type": "credit",
                "subtype": null,
                "note": "",
                "metadata": {},
                "status": "Pending",
                "reference": null,
                "amount": 500,
                "fee": 0,
                "total_amount": 500,
                "balance": 0,
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
                    "id": "00000000-0000-0000-0000-000000000000",
                    "first_name": "Joe",
                    "last_name": "Soap",
                    "email": "joe@rehive.com",
                    "username": null,
                    "mobile": "+27840000000",
                    "profile": null
                },
                "source_transaction": null,
                "destination_transaction": null,
                "messages": [],
                "fees": [],
                "archived": false,
                "created": 1476691969394,
                "updated": 1496135465287
            }
        ]
    }
}
```

```javascript
```

```python
```

Create a batch of transactions on behalf of a user. This action is atomic and the whole batch will either fail or succeed at the same time. This endpoint can create up to 24 transactions at the same time.

#### Endpoint

`https://api.rehive.com/3/admin/transactions/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`user` | email, mobile number, username, or unique id| null
`amount` | amount | null
`currency` | currency code | null
`tx_type` | transaction type | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`id` | unique id (cannot be changed once set)| string (uuid)
`reference` | optional credit reference | blank
`subtype` | a custom defined subtype | null
`account` | account reference code | null
`note` | user's note or message | blank
`metadata` | custom metadata | {}
`status` | status to transition to | Pending
`archived` | archived state | false


### Retrieve Transaction

> Retrieve transaction request

```shell
curl https://api.rehive.com/3/admin/transactions/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.transactions.get({id: id}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "status": "Pending",
        "reference": "",
        "amount": 500,
        "fee": 0,
        "total_amount": 500,
        "balance": 0,
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
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "source_transaction": null,
        "destination_transaction": null,
        "messages": [],
        "fees": [],
        "archived": false,
        "created": 1509618707485,
        "updated": 1509618708277
    }
}
```

```javascript
{
    "id": "000000000000000000000",
    "tx_type": "credit",
    "subtype": null,
    "note": "",
    "metadata": {},
    "status": "Pending",
    "reference": "",
    "amount": 500,
    "fee": 0,
    "total_amount": 500,
    "balance": 0,
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
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "source_transaction": null,
    "destination_transaction": null,
    "messages": [],
    "fees": [],
    "archived": false,
    "created": 1509618707485,
    "updated": 1509618708277
}
```

```python
{
    "id": "000000000000000000000",
    "tx_type": "credit",
    "subtype": null,
    "note": "",
    "metadata": {},
    "status": "Pending",
    "reference": "",
    "amount": 500,
    "fee": 0,
    "total_amount": 500,
    "balance": 0,
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
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "source_transaction": null,
    "destination_transaction": null,
    "messages": [],
    "fees": [],
    "archived": false,
    "created": 1509618707485,
    "updated": 1509618708277
}
```

Get transaction details for a spcific transactions.

#### Endpoint

`https://api.rehive.com/3/admin/transactions/{id}/`

### Update Transaction

> Admin update transaction request

```shell
curl https://api.rehive.com/3/admin/transactions/{id}/
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"status": "Complete"}'
```

```javascript
rehive.admin.transactions.update(id, {status: "Complete"}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
            "id": "00000000-0000-0000-0000-000000000000",
            "first_name": "Joe",
            "last_name": "Soap",
            "email": "joe@rehive.com",
            "username": null,
            "mobile": "+27840000000",
            "profile": null
        },
        "source_transaction": null,
        "destination_transaction": null,
        "messages": [],
        "fees": [],
        "archived": false,
        "created": 1509618707485,
        "updated": 1509618708277
    }
}
```

```javascript
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
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "source_transaction": null,
    "destination_transaction": null,
    "messages": [],
    "fees": [],
    "archived": false,
    "created": 1509618707485,
    "updated": 1509618708277
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
        "id": "00000000-0000-0000-0000-000000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": null,
        "mobile": "+27840000000",
        "profile": null
    },
    "source_transaction": null,
    "destination_transaction": null,
    "messages": [],
    "fees": [],
    "archived": false,
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

`https://api.rehive.com/3/admin/transactions/{id}/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`status` | update action/status (`Pending`, `Complete`, `Failed`) | null | true
`metadata` | custom metadata | {}
`message` | message object | {}
`archived` | archived state | false

#### Endpoint

`https://api.rehive.com/3/admin/transactions/webhooks/{id}/`


### List Transaction Sets

> Admin list transaction sets request

```shell
curl https://api.rehive.com/3/admin/transactions/sets/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
```

```python
```

> Admin list transaction sets response

```shell
{
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": "00000000-0000-0000-0000-000000000000",
                "type": "transaction",
                "query": {},
                "status": "complete",
                "progress": 100,
                "count": 5000,
                "page_size": 5000,
                "archived": false,
                "created": 1530102672434,
                "updated": 1530102672474
            },
        ]
    }
}
```

```javascript
```

```python
```

Get a list of transaction sets.

<aside class="notice">
Transaction sets are currently in beta.
</aside>

#### Filtering

Field | Type
--- | ---
`status` | string (`pending`, `complete`, `failed`)

#### Endpoint

`https://api.rehive.com/3/admin/transactions/sets/`

### Create Transaction Set

> Admin create transaction sets request

```shell
curl https://api.rehive.com/3/admin/transactions/sets/`
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"page_size": 5000}'
```

```javascript
```

```python
```

> Admin create transaction set response

```shell
{
    "status": "success",
    "data": {
        "id": "00000000-0000-0000-0000-000000000000",
        "type": "transaction",
        "query": {},
        "status": "complete",
        "progress": 100,
        "count": 5000,
        "page_size": 5000,
        "pages": [
            {
                "count": 5000,
                "page": 1,
                "status": "complete",
                "file": "https://path.to.file.com/file.json"
            }
        ],
        "archived": false,
        "created": 1530102672434,
        "updated": 1530102672474
    }
}
```

```javascript
```

```python
```

Create a transaction set.

#### Endpoint

`https://api.rehive.com/3/admin/transactions/sets/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`page_size` | number of results per page | 5000
`query` | key value object containing query filters | {}


#### Query Filtering

All filters available on the admin transaction list endpoint aare also
available on the create transaction set endpoint. Simply include them in the
`query` object like: `{"status": "complete"}`.

### Retrieve Transaction Set

> Admin retrieve transaction set request

```shell
curl https://api.rehive.com/3/admin/transactions/sets/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
```

```python
```

> Admin retrieve transaction set response

```shell
    "status": "success",
    "data": {
        "id": "00000000-0000-0000-0000-000000000000",
        "type": "transaction",
        "query": {},
        "status": "complete",
        "progress": 100,
        "count": 5000,
        "page_size": 5000,
        "pages": [
            {
                "count": 5000,
                "page": 1,
                "status": "complete",
                "file": "https://path.to.file.com/file.json"
            }
        ],
        "archived": false,
        "created": 1530102672434,
        "updated": 1530102672474
    }
```

```javascript
```

```python
```

Retrieve a transaction set.

#### Endpoint

`https://api.rehive.com/3/admin/transactions/sets/{id}/`

### Delete Transaction Set

> Admin delete transaction set request

```shell
curl https://api.rehive.com/3/admin/transactions/sets/{id}/`
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
```

```python
```

> Admin delete transaction set response

```shell
{
    "status": "success",
}
```

```javascript
```

```python
```

Delete a transaction set.

#### Endpoint

`https://api.rehive.com/3/admin/transactions/sets/{id}/`

## Accounts

### List Accounts

> Admin list accounts request

```shell
curl https://api.rehive.com/3/admin/accounts/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.accounts.get().then(function (res) {
    ...
}, function (err) {
    ...
});
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
                        "settings": {
                            "allow_transactions": true,
                            "allow_debit_transactions": true,
                            "allow_credit_transactions": true
                        },
                        "active": true
                    }
                ],
                "archived": false,
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
                    "settings": {
                        "allow_transactions": true,
                        "allow_debit_transactions": true,
                        "allow_credit_transactions": true
                    },
                    "active": true
                }
            ],
            "archived": false,
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
                "settings": {
                    "allow_transactions": true,
                    "allow_debit_transactions": true,
                    "allow_credit_transactions": true
                },
                "active": true
            }
        ],
        "archived": false,
        "created": 1464858068745,
        "updated": 1464858068745
    }
]
```

Get a list of accounts belonging to users in a company.

#### Filtering

Field | Type
--- | ---
`reference` | string
`name` | string
`active` | boolean
`primary` | boolean
`user` | string

#### Endpoint

`https://api.rehive.com/3/admin/accounts/`

### Create Account

> Admin create account request

```shell
curl https://api.rehive.com/3/admin/accounts/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"name": "savings",
       "user": "joe@rehive.com",}'
```

```javascript
rehive.admin.accounts.create(
{
    name: "savings",
    user: "joe@rehive.com"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "archived": false,
        "created": 1501145581365,
        "updated": 1501145581370
    },
}
```

```javascript
{
    "name": "savings",
    "reference": "0000000000",
    "primary": true,
    "currencies": [],
    "archived": false,
    "created": 1501145581365,
    "updated": 1501145581370
}
```

```python
{
    "name": "savings",
    "reference": "0000000000",
    "primary": true,
    "currencies": [],
    "archived": false,
    "created": 1501145581365,
    "updated": 1501145581370
}
```

Create a account for a user.

#### Endpoint

`https://api.rehive.com/3/admin/accounts/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`name` | account name | null
`user` | account user | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`reference` | account reference | 10 random chars
`primary` | account primary status | false
`archived` | archived state | false

### Retrieve Account

> Admin retrieve account request

```shell
curl https://api.rehive.com/3/admin/accounts/{reference}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.accounts.get({reference: reference}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
                "settings": {
                    "allow_transactions": true,
                    "allow_debit_transactions": true,
                    "allow_credit_transactions": true
                },
                "active": true
            }
        ],
        "archived": false,
        "created": 1464858068745,
        "updated": 1464858068745
    }
}
```

```javascript
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
            "settings": {
                "allow_transactions": true,
                "allow_debit_transactions": true,
                "allow_credit_transactions": true
            },
            "active": true
        }
    ],
    "archived": false,
    "created": 1464858068745,
    "updated": 1464858068745
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
            "settings": {
                "allow_transactions": true,
                "allow_debit_transactions": true,
                "allow_credit_transactions": true
            },
            "active": true
        }
    ],
    "archived": false,
    "created": 1464858068745,
    "updated": 1464858068745
}
```

Retrieve an account belonging to a company.

#### Filtering

Field | Type
--- | ---
`active` | boolean

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/`


### Update Account

> Admin update account request

```shell
curl https://api.rehive.com/3/admin/accounts/{reference}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"name": "savings"}'
```

```javascript
rehive.admin.accounts.update(reference, {name: "savings"}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "archived": false,
        "created": 1501145581365,
        "updated": 1501145581370
    },
}
```

```javascript
{
    "name": "savings",
    "reference": "0000000000",
    "primary": true,
    "currencies": [],
    "archived": false,
    "created": 1501145581365,
    "updated": 1501145581370
}
```

```python
{
    "name": "savings",
    "reference": "0000000000",
    "primary": true,
    "currencies": [],
    "archived": false,
    "created": 1501145581365,
    "updated": 1501145581370
}
```

Update an account for a user.

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`name` | account name | null
`user` | account user | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`reference` | account reference | 10 random chars
`primary` | account primary status | false
`archived` | archived state | false


### List Account Currencies

> Admin list account currencies request

```shell
curl https://api.rehive.com/3/accounts/{reference}/currencies/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.accounts.currencies.get(reference).then(function (res) {
    ...
}, function (err) {
    ...
});
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
                "active": false,
                "settings": {
                    "allow_transactions": true,
                    "allow_debit_transactions": true,
                    "allow_credit_transactions": true
                },
                "archived": false,
                "created": 1464858068732,
                "updated": 1464858068732
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
            "active": false,
            "settings": {
                "allow_transactions": true,
                "allow_debit_transactions": true,
                "allow_credit_transactions": true
            },
            "archived": false,
            "created": 1464858068732,
            "updated": 1464858068732e": true
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
        "active": false,
        "settings": {
            "allow_transactions": true,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        },
        "archived": false,
        "created": 1464858068732,
        "updated": 1464858068732
    }
]
```

Get a list of currencies for an account belonging to a company.

#### Filtering

Field | Type
--- | ---
`active` | boolean

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/currencies/`


### Create Account Currency

> Admin create account currency request

```shell
curl https://api.rehive.com/3/admin/accounts/{reference}/currencies/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"currency": "XBT"}'
```

```javascript
rehive.admin.accounts.currencies.create(
    reference,
    {currency: "XBT"}
).then(function(res){
    ...
},function(err){
    ...
})
```

```python
rehive.admin.accounts.obj("{reference}").currencies.create(
    currency="XBT"
)
```

> Admin create account currency response

```shell
{
    "status": "success",
    "data": {
        "balance": 0,
        "available_balance": 0,
        "currency": {
            "code": "XBT",
            "description": "bitcoin",
            "symbol": "฿",
            "unit": "bitcoin",
            "divisibility": 8
        },
        "limits": [],
        "fees": [],
        "active": false,
        "settings": {
            "allow_transactions": true,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        },
        "archived": false,
        "created": 1464858068732,
        "updated": 1464858068732
    }
}
```

```javascript
{
    "balance": 0,
    "available_balance": 0,
    "currency": {
        "code": "XBT",
        "description": "bitcoin",
        "symbol": "฿",
        "unit": "bitcoin",
        "divisibility": 8
    },
    "limits": [],
    "fees": [],
    "active": false,
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "archived": false,
    "created": 1464858068732,
    "updated": 1464858068732
}
```

```python
{
    "balance": 0,
    "available_balance": 0,
    "currency": {
        "code": "XBT",
        "description": "bitcoin",
        "symbol": "฿",
        "unit": "bitcoin",
        "divisibility": 8
    },
    "limits": [],
    "fees": [],
    "active": false,
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "archived": false,
    "created": 1464858068732,
    "updated": 1464858068732
}
```

Create an account currency for a user.

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/currencies/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`currency` | currency code | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`active` | is active currency | false
`archived` | archived state | false


### Retrieve Account Currency

> Admin retrieve account currency request

```shell
curl https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.accounts.currencies.get(reference, {code: code}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "active": false,
        "settings": {
            "allow_transactions": true,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        },
        "archived": false,
        "created": 1464858068732,
        "updated": 1464858068732
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
    "active": false,
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "archived": false,
    "created": 1464858068732,
    "updated": 1464858068732
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
    "active": false,
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "archived": false,
    "created": 1464858068732,
    "updated": 1464858068732
}
```

Retrieve an account's currency belonging to a company.

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}`

### Update Account Currency

> Admin retrieve account currency request

```shell
curl https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"active": true}'
```

```javascript
rehive.admin.accounts.currencies.update(reference, code, {active: true}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "active": false,
        "settings": {
            "allow_transactions": true,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        },
        "archived": false,
        "created": 1464858068732,
        "updated": 1464858068732
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
    "active": false,
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "archived": false,
    "created": 1464858068732,
    "updated": 1464858068732
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
    "active": false,
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "archived": false,
    "created": 1464858068732,
    "updated": 1464858068732
}
```

Update the active status of an account currency. Activating an account's currency will result in that currency getting used by default for all transactions if no other account/currency is specified.

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`active` | is active currency | false


### Retrieve Account Currency Settings

> Admin retrieve account currency settings request

```shell
curl https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/settings/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.accounts.currencies.settings.get(reference,code).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.accounts.obj("{reference}").currencies.obj({code}).settings.get()
```

> Admin retrieve account currency settings response

```shell
{
    "status": "success",
    "data": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    }
}
```

```javascript
{
    "allow_transactions": true,
    "allow_debit_transactions": true,
    "allow_credit_transactions": true
}
```

```python
{
    "allow_transactions": true,
    "allow_debit_transactions": true,
    "allow_credit_transactions": true
}
```

Retrieve an account's currency's settings.

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/settings/`

### Update Account Currency Settings

> Admin update account currency settings request

```shell
curl https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/settings/
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"allow_transactions": true}'
```

```javascript
rehive.admin.accounts.currencies.settings.update(reference, code, {allow_transactions: true}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.accounts.obj("{reference}").currencies.obj({code}).settings.update(
    allow_credit_transactions=True
)
```

> Admin retrieve account currency settings response

```shell
{
    "status": "success",
    "data": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    }
}
```

```javascript
{
    "allow_transactions": true,
    "allow_debit_transactions": true,
    "allow_credit_transactions": true
}
```

```python
{
    "allow_transactions": true,
    "allow_debit_transactions": true,
    "allow_credit_transactions": true
}
```

Update the settings of an acocunt currency.

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/settings/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`allow_transactions` | Allow transactions | true
`allow_debit_transactions` | Allow debit transactions | true
`allow_credit_transactions` | Allow credit transactions | true


### List Account Currency Limits

List all Limits related to am account currency.

> List Account Currency request

```shell
curl https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/limits/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.accounts.currencies.limits.get(reference, code).then(function (res) {
    ...
}, function (err) {
    ...
});
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
            "archived": false,
            "created": 1497428787920,
            "updated": 1497428787921
        }
    ],
    "status": "success"
}
```

```javascript
[
    {
        "id": 1,
        "value": 1000,
        "type": "Maximum",
        "tx_type": "credit",
        "subtype": null,
        "archived": false,
        "created": 1497428787920,
        "updated": 1497428787921
    }
]
```

```python
[
    {
        "id": 1,
        "value": 1000,
        "type": "Maximum",
        "tx_type": "credit",
        "subtype": null,
        "archived": false,
        "created": 1497428787920,
        "updated": 1497428787921
    }
]
```

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/limits/`

### Create Account Currency Limit

Create a new limit related to an account currency.

> Create Account Currency Limit request

```shell
curl https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/limits/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 1000,
       "type": "max",
       "tx_type": "credit"}'
```

```javascript
rehive.admin.accounts.currencies.limits.create(reference, code, {
    tx_type: tx_type,
    value: value,
    type: type,
    subtype: subtype
}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "archived": false,
        "created": 1497428787920,
        "updated": 1497428787921
    },
    "status": "success"
}
```

```javascript
{
    "id": 1,
    "value": 1000,
    "type": "Maximum",
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497428787920,
    "updated": 1497428787921
}
```

```python
{
    "id": 1,
    "value": 1000,
    "type": "Maximum",
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497428787920,
    "updated": 1497428787921
}
```

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/limits/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`value` | Limit value | 0
`type` | Limit Type |
`tx_type` | Transaction type limits are applied |

#### Optional Fields

Field | Description | Default
--- | --- | ---
`subtype` | Transaction subtype name | null
`archived` | archived state | false

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
curl https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.accounts.currencies.limits.get(reference, code, {id: limitId}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "archived": false,
        "created": 1497428787920,
        "updated": 1497428787921
    },
    "status": "success"
}
```

```javascript
{
    "id": 1,
    "value": 1000,
    "type": "Maximum",
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497428787920,
    "updated": 1497428787921
}
```

```python
 {
    "id": 1,
    "value": 1000,
    "type": "Maximum",
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497428787920,
    "updated": 1497428787921
}
```

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}/`

### Update Account Currency Limit

Update a specific limits related to an account currency.

> Update Account Currency request

```shell
curl https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 5000,
       "type": "min"}'
```

```javascript
rehive.admin.accounts.currencies.limits.update(reference, code, limitId,
{
    value: 5000,
    type: "min"
}).then(function (res) {
   ...
}, function (err) {
    ...
});
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
        "archived": false,
        "created": 1497428787920,
        "updated": 1497429648948
    }
}
```

```javascript
{
    "id": 1,
    "value": 5000,
    "type": "Minimum",
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497428787920,
    "updated": 1497429648948
}
```

```python
{
    "id": 1,
    "value": 5000,
    "type": "Minimum",
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497428787920,
    "updated": 1497429648948
}
```

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`value` | Limit value | 0
`type` | Limit Type |
`tx_type` | Transaction type limits are applied |

#### Optional Fields

Field | Description | Default
--- | --- | ---
`subtype` | Transaction subtype name | null
`archived` | archived state | false

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
curl https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.accounts.currencies.limits.delete(reference, code, limitId).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.accounts.obj("{reference}").currencies.obj("{code}").limits.delete(
    "{limit_id}"
)
```

> Delete Account Currency response

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

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}/`


### List Account Currency Fees

List all fees related to am account currency.

> List Account Currency Fees request

```shell
curl https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/fees/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.accounts.currencies.fees.get(reference, code).then(function (res) {
    ...
}, function (err) {
    ...
});
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
            "archived": false,
            "created": 1497431721587,
            "updated": 1497431721587
        }
    ],
    "status": "success"
}
```

```javascript
[
    {
        "id": 1,
        "value": 1000,
        "percentage": null,
        "tx_type": "credit",
        "subtype": null,
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431721587
    }
]
```

```python
[
    {
        "id": 1,
        "value": 1000,
        "percentage": null,
        "tx_type": "credit",
        "subtype": null,
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431721587
    }
]
```

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/fees/`

### Create Account Currency Fee

Create a new fee related to an account currency.

> Create Account Currency Fee request

```shell
curl https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/fees/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 1000,
       "tx_type": "credit"}'
```

```javascript
rehive.admin.accounts.currencies.fees.create(reference, code, {
    tx_type: "credit",
    value: 1000
}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431721587
    },
    "status": "success"
}
```

```javascript
{
    "id": 1,
    "value": 1000,
    "percentage": null,
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431721587
}
```

```python
{
    "id": 1,
    "value": 1000,
    "percentage": null,
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431721587
}
```

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/fees/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`tx_type` | Transaction type fees are applied |

#### Optional Fields

Field | Description | Default
--- | --- | ---
`value` | Fee amount | 0
`percentage` | Percentage amount |
`subtype` | Transaction subtype name | null
`archived` | archived state | false

#### Transaction Types

Value | Description
--- | ---
`credit` | Credit
`debit` | Debit

### Retrieve Account Currency fee

Retrieve a specific requirement related to an account currency.

> Retrieve Account Currency Fee request

```shell
curl https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.accounts.currencies.fees.get(reference, code, {id: feeId}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431721587
    },
    "status": "success"
}
```

```javascript
{
    "id": 1,
    "value": 1000,
    "percentage": null,
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431721587
}
```

```python
{
    "id": 1,
    "value": 1000,
    "percentage": null,
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431721587
}
```

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}/`

### Update Account Currency Fee

Update a specific fees related to an account currency.

> Update Account Currency request

```shell
curl https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 5000}'
```

```javascript
rehive.admin.accounts.currencies.fees.update(reference, code, feeId, data).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431938971
    },
    "status": "success"
}
```

```javascript
{
    "id": 1,
    "value": 5000,
    "percentage": null,
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

```python
{
    "id": 1,
    "value": 5000,
    "percentage": null,
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

#### Endpoint

`https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`tx_type` | Transaction type fees are applied |

#### Optional Fields

Field | Description | Default
--- | --- | ---
`value` | Fee amount | 0
`percentage` | Percentage amount |
`subtype` | Transaction subtype name | null
`archived` | archived state | false

#### Transaction Types

Value | Description
--- | ---
`credit` | Credit
`debit` | Debit

### Delete Account Currency Fee

Delete a specific fees related to an account currency.

> Delete Account Currency request

```shell
curl https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.accounts.currencies.fees.delete(reference, code, feeId).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.accounts.obj("{reference}").currencies.obj("{code}").fees.delete(
    "{fee_id}"
)
```

> Delete Account Currency response

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

`https://api.rehive.com/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}/`

## Currencies

### List Currencies

> Admin list currencies request

```shell
curl https://api.rehive.com/3/admin/currencies/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.currencies.get().then(function (res) {
    ...
}, function (err) {
    ...
});
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
                "divisibility": 8,
                "archived": false,
                "created": 1497431721587,
                "updated": 1497431938971
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
            "archived": false,
            "created": 1497431721587,
            "updated": 1497431938971
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
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431938971
    }
]
```

Get a list of all existing currencies. This includes default Rehive currencies as well as any currencies added by the company.

#### Endpoint

`https://api.rehive.com/3/admin/currencies/`

### Create Currency

> Admin create currency request

```shell
curl https://api.rehive.com/3/admin/currencies/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"code": "XBT",
        "description": "bitcoin",
        "symbol": "฿",
        "unit": "bitcoin",
        "divisibility": 8}'
```

```javascript
rehive.admin.currencies.create(
{
    code: "XBT",
    description: "bitcoin",
    symbol: "฿",
    unit: "bitcoin",
    divisibility: 8
}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431938971
    }
}
```

```javascript
{
    "code": "XBT",
    "description": "bitcoin",
    "symbol": "฿",
    "unit": "bitcoin",
    "divisibility": 8,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

```python
{
    "code": "XBT",
    "description": "bitcoin",
    "symbol": "฿",
    "unit": "bitcoin",
    "divisibility": 8,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

Create a custom currency.

#### Endpoint

`https://api.rehive.com/3/admin/currencies/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`code` | currency code | null
`description` | name of currency | null
`symbol` | currency symbol | null
`unit` | unit, like `dollar` | null
`divisibility` | number of decimal places | 0
`archived` | archived state | false


### Retrieve Currency

> Admin retrieve currency request

```shell
curl https://api.rehive.com/3/admin/currencies/{code}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.currencies.get({code: code}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431938971
    }
}
```

```javascript
{
    "code": "XBT",
    "description": "bitcoin",
    "symbol": "฿",
    "unit": "bitcoin",
    "divisibility": 8,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

```python
{
    "code": "XBT",
    "description": "bitcoin",
    "symbol": "฿",
    "unit": "bitcoin",
    "divisibility": 8,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

Retrieve a currencies details.

#### Endpoint

`https://api.rehive.com/3/admin/currencies/{code}/`

### Update Currency

> Admin update currency request

```shell
curl https://api.rehive.com/3/admin/currencies/{code}/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"unit": "bitcoin"}'
```

```javascript
rehive.admin.currencies.update(code, {unit: "bitcoin"}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.currencies.update(
    "{code}",
    unit="bitcoin"
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
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431938971
    }
}
```

```javascript
{
    "code": "XBT",
    "description": "bitcoin",
    "symbol": "฿",
    "unit": "bitcoin",
    "divisibility": 8,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

```python
{
    "code": "XBT",
    "description": "bitcoin",
    "symbol": "฿",
    "unit": "bitcoin",
    "divisibility": 8,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

This endpoint can be used to enable an existing currency or if it is a custom currency, edit its details.

<aside class="notice">
Note that default currencies can not be updated, and only custom currencies can be updated.
</aside>

#### Endpoint

`https://api.rehive.com/3/admin/currencies/{code}/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`code` | currency code | null
`description` | name of currency | null
`symbol` | currency symbol | null
`unit` | unit, like `dollar` | null
`divisibility` | number of decimal places | 0
`archived` | archived state | false

### Delete Currency

> Admin delete currency request

```shell
curl https://api.rehive.com/3/admin/currencies/{code}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.currencies.delete(code).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.currencies.delete(
    "{code}"
)
```

> Admin delete currency response

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

This endpoint can be used to delete custom currencies.

#### Endpoint

`https://api.rehive.com/3/admin/currencies/{code}/`

### Currency Overview

> Admin currency overview request

```shell
curl https://api.rehive.com/3/admin/currencies/{code}/overview/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.currencies.overview.get(code).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.currencies.obj({code}).overview.get()
```

> Admin currency overview response

```shell
{
    "data": {
        "balance_total": 0,
        "available_balance_total": 0,
        "balance_24h": 0,
        "count_total": 0,
        "count_24h": 0,
        "count_debits_pending": 0,
        "count_debits_complete": 0,
        "count_credits_pending": 0,
        "count_credits_complete": 0,
        "sum_debits_pending": 0,
        "sum_debits_complete": 0,
        "sum_credits_pending": 0,
        "sum_credits_complete": 0,
        "sum_24h_debits_pending": 0,
        "sum_24h_debits_complete": 0,
        "sum_24h_credits_pending": 0,
        "sum_24h_credits_complete": 0
    },
    "status": "success"
}
```

```javascript
{
    "balance_total": 0,
    "available_balance_total": 0,
    "balance_24h": 0,
    "count_total": 0,
    "count_24h": 0,
    "count_debits_pending": 0,
    "count_debits_complete": 0,
    "count_credits_pending": 0,
    "count_credits_complete": 0,
    "sum_debits_pending": 0,
    "sum_debits_complete": 0,
    "sum_credits_pending": 0,
    "sum_credits_complete": 0,
    "sum_24h_debits_pending": 0,
    "sum_24h_debits_complete": 0,
    "sum_24h_credits_pending": 0,
    "sum_24h_credits_complete": 0
}
```

```python
{
    "balance_total": 0,
    "available_balance_total": 0,
    "balance_24h": 0,
    "count_total": 0,
    "count_24h": 0,
    "count_debits_pending": 0,
    "count_debits_complete": 0,
    "count_credits_pending": 0,
    "count_credits_complete": 0,
    "sum_debits_pending": 0,
    "sum_debits_complete": 0,
    "sum_credits_pending": 0,
    "sum_credits_complete": 0,
    "sum_24h_debits_pending": 0,
    "sum_24h_debits_complete": 0,
    "sum_24h_credits_pending": 0,
    "sum_24h_credits_complete": 0
}
```

Get an overview of the selected currency's transactions.

#### Endpoint

`https://api.rehive.com/3/admin/currencies/{code}/overview/`

## Company

### Retrieve Company

> View the company info

```shell
curl https://api.rehive.com/3/admin/company/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.company.get().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.company.get()
```

> Company info response

```shell
{
    "status": "success",
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
    }
}
```

```javascript
{
    "id": "test_company",
    "name": "Test Company 1",
    "description": "A Test Company.",
    "website": "http://www.test_company.com",
    "logo": "https://www.test_company.com/logo.jpg",
    "address": {
        // ...
    },
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true,
        "require_verification": true,
        "allow_registrations": true,
        "allow_overdrafts": false,
        "auto_complete_transactions": false,
        "allow_session_durations": false,
        "require_terms_and_conditions": false,
        "password_reset_url": null,
        "email_confirmation_url": null,
        "nationalities": []
    },
    "created": 1497431721587,
    "updated": 1497431938971
}
```

```python
{
    "id": "test_company",
    "name": "Test Company 1",
    "description": "A Test Company.",
    "website": "http://www.test_company.com",
    "logo": "https://www.test_company.com/logo.jpg",
    "address": {
        # ...
    },
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true,
        "require_verification": true,
        "allow_registrations": true,
        "allow_overdrafts": false,
        "auto_complete_transactions": false,
        "allow_session_durations": false,
        "require_terms_and_conditions": false,
        "password_reset_url": null,
        "email_confirmation_url": null,
        "nationalities": []
    },
    "created": 1497431721587,
    "updated": 1497431938971
}
```

Retrieve the company info.

#### Endpoint

`https://api.rehive.com/3/admin/company/`

### Update Company

> Update company info

```shell
curl https://api.rehive.com/3/admin/company/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"description": "A new description"}'
```

```javascript
rehive.admin.company.update({description: "A new description"}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
}
```

```javascript
{
    "id": "test_company",
    "name": "Test Company 1",
    "description": "A Test Company.",
    "website": "http://www.test_company.com",
    "logo": "https://www.test_company.com/logo.jpg",
    "address": {
        // ...
    },
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true,
        "require_verification": true,
        "allow_registrations": true,
        "allow_overdrafts": false,
        "auto_complete_transactions": false,
        "allow_session_durations": false,
        "require_terms_and_conditions": false,
        "password_reset_url": null,
        "email_confirmation_url": null,
        "nationalities": []
    },
    "created": 1497431721587,
    "updated": 1497431938971
}
```

```python
{
    "id": "test_company",
    "name": "Test Company 1",
    "description": "A new description",
    "website": "http://www.test_company.com",
    "logo": "https://www.test_company.com/logo.jpg",
    "address": {
        // ...
    },
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true,
        "require_verification": true,
        "allow_registrations": true,
        "allow_overdrafts": false,
        "auto_complete_transactions": false,
        "allow_session_durations": false,
        "require_terms_and_conditions": false,
        "password_reset_url": null,
        "email_confirmation_url": null,
        "nationalities": []
    },
    "created": 1497431721587,
    "updated": 1497431938971
}
```

Retrieve the company info.

#### Endpoint

`https://api.rehive.com/3/admin/company/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`name` | Company Name | blank
`description` | Company Description | blank
`website` | Company website URL | blank
`logo` | Company logo URL | blank

<aside class="notice">
When adding a logo image, the Content-type header needs to be set to multipart/form-data.
</aside>

## Company Settings

### Retrieve Company Settings

> View the company settings

```shell
curl https://api.rehive.com/3/admin/company/settings/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.company.settings.get().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.company.settings.get()
```

> Company settings response

```shell
{
    "status": "success",
    "data": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true,
        "require_verification": true,
        "allow_registrations": true,
        "allow_overdrafts": false,
        "auto_complete_transactions": false,
        "allow_session_durations": false,
        "require_terms_and_conditions": false,
        "password_reset_url": null,
        "email_confirmation_url": null,
        "nationalities": []
    }
}
```

```javascript
{
    "allow_transactions": true,
    "allow_debit_transactions": true,
    "allow_credit_transactions": true,
    "require_verification": true,
    "allow_registrations": true,
    "allow_overdrafts": false,
    "auto_complete_transactions": false,
    "allow_session_durations": false,
    "require_terms_and_conditions": false,
    "password_reset_url": null,
    "email_confirmation_url": null,
    "nationalities": []
}
```

```python
{
    "allow_transactions": true,
    "allow_debit_transactions": true,
    "allow_credit_transactions": true,
    "require_verification": true,
    "allow_registrations": true,
    "allow_overdrafts": false,
    "auto_complete_transactions": false,
    "allow_session_durations": false,
    "require_terms_and_conditions": false,
    "password_reset_url": null,
    "email_confirmation_url": null,
    "nationalities": []
}
```

Retrieve the company settings.

#### Endpoint

`https://api.rehive.com/3/admin/company/settings/`

### Update Company Settings

> Update company settings

```shell
curl https://api.rehive.com/3/admin/company/settings/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"allow_transactions": true}'
```

```javascript
rehive.admin.company.settings.update({allow_transactions: true}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.company.settings.update(
    allow_transactions=True
)
```

> Update company settings response

```shell
{
    "allow_transactions": true,
    "allow_debit_transactions": true,
    "allow_credit_transactions": true,
    "require_verification": true,
    "allow_registrations": true,
    "allow_overdrafts": false,
    "auto_complete_transactions": false,
    "allow_session_durations": false,
    "require_terms_and_conditions": false,
    "password_reset_url": null,
    "email_confirmation_url": null,
    "nationalities": []
}
```

```javascript
{
    "allow_transactions": true,
    "allow_debit_transactions": true,
    "allow_credit_transactions": true,
    "require_verification": true,
    "allow_registrations": true,
    "allow_overdrafts": false,
    "auto_complete_transactions": false,
    "allow_session_durations": false,
    "require_terms_and_conditions": false,
    "password_reset_url": null,
    "email_confirmation_url": null,
    "nationalities": []
}
```

```python
{
    "allow_transactions": true,
    "allow_debit_transactions": true,
    "allow_credit_transactions": true,
    "require_verification": true,
    "allow_registrations": true,
    "allow_overdrafts": false,
    "auto_complete_transactions": false,
    "allow_session_durations": false,
    "require_terms_and_conditions": false,
    "password_reset_url": null,
    "email_confirmation_url": null,
    "nationalities": []
}
```

Retrieve the company settings.

#### Endpoint

`https://api.rehive.com/3/admin/company/settings/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`allow_transactions` | Allow transactions | true
`allow_debit_transactions` | Allow debit transactions | true
`allow_credit_transactions` | Allow credit transactions | true,
`require_verification` | Require verifications | true
`allow_registrations` | Allow registrations | true
`allow_overdrafts` | Allow overdrafts |false
`auto_complete_transactions` | Auto complete transactions | false
`allow_session_durations` | Allow sesison durations |false
`require_terms_and_conditions` | Require terms and conditions | false
`nationalities` | List of accepted nationalities | blank
`password_reset_url` | Custom company password reset URL | blank
`email_confirmation_url` | Custom company email confirmation URL | blank

## Bank Accounts

### List Bank Accounts

> List Bank Accounts request

```shell
curl https://api.rehive.com/3/admin/bank-accounts/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.bankAccounts.get().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.bank_accounts.get()
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
                "archived": false,
                "created": 1497431721587,
                "updated": 1497431938971
            }
        ]
    }
}
```

```javascript
[
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
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431938971
    }
]
```

```python
[
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
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431938971
    }
]
```

#### Filtering

Field | Type
--- | ---
`user` | string
`status` | string

#### Endpoint

`https://api.rehive.com/3/admin/bank-accounts/`

### Create Bank Account

> Create Bank Account request

```shell
curl https://api.rehive.com/3/admin/bank-accounts/
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

```javascript
rehive.admin.bankAccounts.create(
{
    name: name,
    number: number,
    type: type,
    bank_name: bank_name,
    bank_code: bank_code,
    branch_code: branch_code,
    swift: swift,
    iban: iban,
    bic: bic
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.bank_account.create(
    name="Bank Account",
    number="12341234",
    type="Cheque",
    bank_nam="Bank",
    bank_code="1234",
    branch_code="1234"
)
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
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431938971
    }
}
```

```javascript
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
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

```python
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
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

#### Endpoint

`https://api.rehive.com/3/admin/bank-accounts/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`name` | Account Name | blank
`number` | Account Number | blank
`type` | Account Type | blank
`bank_name` | Bank Name | blank
`bank_code` | Bank Code | blank
`branch_code` | Branch Code | blank
`swift` | swift | blank
`iban` | iban | blank
`bic` | bic | blank
`archived` | archived state | false

### Retrieve Bank Account

> Retrieve Bank Account request

```shell
curl https://api.rehive.com/3/admin/bank-accounts/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.bankAccounts.get({id: id}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.bank_accounts.get(
    {id}
)
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
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431938971
    }
}
```

```javascript
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
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

```python
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
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

### Retrieve Bank Account Currencies

> Retrieve Bank Account Currencies request

```shell
curl https://api.rehive.com/3/admin/bank-accounts/{id}/currencies/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.bankAccounts.currencies.get(id).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.bank_accounts.currencies.get(
    {id}
)
```

> Retrieve Bank Account Currencies response

```shell
{
    "status": "success",
    "data": {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "code": "CAD",
                "description": "Canadian Dollar",
                "symbol": "CA$",
                "unit": "dollar",
                "divisibility": 2,
            },
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
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
       "code": 'CAD',
       "description": 'Canadian Dollar',
       "symbol": 'CA$',
       "unit": 'dollar',
       "divisibility": 2
    },
    {
       "code": 'XBT',
       "description": 'bitcoin',
       "symbol": '฿',
       "unit": 'bitcoin',
       "divisibility": 8
    }
  ]
}
```

```python
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
       "code": 'CAD',
       "description": 'Canadian Dollar',
       "symbol": 'CA$',
       "unit": 'dollar',
       "divisibility": 2
    },
    {
       "code": 'XBT',
       "description": 'bitcoin',
       "symbol": '฿',
       "unit": 'bitcoin',
       "divisibility": 8
    }
  ]
}
```

#### Endpoint

`https://api.rehive.com/3/admin/bank-accounts/{id}/currencies/`

### Retrieve Bank Account Currency

> Retrieve Bank Account Currency request

```shell
curl https://api.rehive.com/3/admin/bank-accounts/{id}/currencies/{currency_code}
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.bankAccounts.currencies.get(id, currencyCode).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.bank_accounts.currencies.get(
    {id}, {currency_code}
)
```

> Retrieve Bank Account Currencies response

```shell
{
    "status": "success",
    "data": {
       "code": 'XBT',
       "description": 'bitcoin',
       "symbol": '฿',
       "unit": 'bitcoin',
       "divisibility": 8
    }
}
```

```javascript
{
    "code": 'XBT',
    "description": 'bitcoin',
    "symbol": '฿',
    "unit": 'bitcoin',
    "divisibility": 8
}
```

```python
{
    "code": 'XBT',
    "description": 'bitcoin',
    "symbol": '฿',
    "unit": 'bitcoin',
    "divisibility": 8
}
```

#### Endpoint

`https://api.rehive.com/3/admin/bank-accounts/{id}/currencies/{currency_code}`

### Delete Bank Account Currency

> Delete Bank Account Currency request

```shell
curl https://api.rehive.com/3/admin/bank-accounts/{id}/currencies/{currency_code}
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.bankAccounts.currencies.delete(id, currencyCode).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.bank_accounts.currencies.delete(
    {id}, {currency_code}
)
```

> Delete Bank Account Currencies response

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

`https://api.rehive.com/3/admin/bank-accounts/{id}/currencies/{currency_code}`

### Add Bank Account Currency

> Add Bank Account Currency request

```shell
curl https://api.rehive.com/3/admin/bank-accounts/{id}/currencies/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"currency": "XBT"}'
```

```javascript
rehive.admin.bankAccounts.currencies.create(id, {currency: "XBT"}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.bank_accounts.currencies.create(
    {id},
    currency="XBT"
)
```

> Add Bank Account Currency response

```shell
{
    "status": "success",
    "data": {
        "code": 'XBT',
        "description": 'bitcoin',
        "symbol": '฿',
        "unit": 'bitcoin',
        "divisibility": 8
    }
}
```

```javascript
{
  "code": 'XBT',
  "description": 'bitcoin',
  "symbol": '฿',
  "unit": 'bitcoin',
  "divisibility": 8
}
```

```python
{
  "code": 'XBT',
  "description": 'bitcoin',
  "symbol": '฿',
  "unit": 'bitcoin',
  "divisibility": 8
}
```

#### Endpoint

`https://api.rehive.com/3/admin/bank-accounts/{id}/currencies/`

#### Fields

Field | Description | Required
--- | --- | ---
`currency` | Currency code of existing currency | true


### Update Bank Account

> Update Bank Account request

```shell
curl https://api.rehive.com/3/admin/bank-accounts/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "New account name"}'
```

```javascript
rehive.admin.bankAccounts.update(id, {name: "New account name"}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.bank_accounts.update(
    {id},
    name="New account name"
)
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
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431938971
    }
}
```

```javascript
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
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

```python
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
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

#### Endpoint

`https://api.rehive.com/3/admin/bank-accounts/{id}/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`name` | Account Name | blank
`number` | Account Number | blank
`type` | Account Type | blank
`bank_name` | Bank Name | blank
`bank_code` | Bank Code | blank
`branch_code` | Branch Code | blank
`swift` | swift | blank
`iban` | iban | blank
`bic` | bic | blank
`archived` | archived state | false

### Delete Bank Account

> Delete Bank Account request

```shell
curl https://api.rehive.com/3/admin/bank-accounts/{id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.bankAccounts.delete(id).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.bank_accounts.delete(
    {id}
)
```

> Delete Bank Account response

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

#### Endpoint

`https://api.rehive.com/3/admin/bank-accounts/{id}/`


## Webhooks

### List Webhooks

> List webhooks request

```shell
curl https://api.rehive.com/3/admin/webhooks/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.webhooks.get().then(function (res) {
    ...
}, function (err) {
    ...
})
```

```python
rehive.admin.webhooks.get()
```

> List webhooks response

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
                "url": "http://mysite.com/webhook_endpoint",
                "event": "user.create",
                "condition": null,
                "secret": "secret",
                "archived": false,
                "created": 1497431721587,
                "updated": 1497431938971
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
            "id": 1,
            "url": "http://mysite.com/webhook_endpoint",
            "event": "user.create",
            "condition": null,
            "secret": "secret",
            "archived": false,
            "created": 1497431721587,
            "updated": 1497431938971
        }
    ]
}
```

```python
[
    {
        "id": 1,
        "url": "http://mysite.com/webhook_endpoint",
        "event": "user.create",
        "condition": null,
        "secret": "secret",
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431938971
    }
]
```

#### Endpoint

`https://api.rehive.com/3/admin/webhooks/`

### Create Webhook

> Create webhooks request

```shell
curl https://api.rehive.com/3/admin/webhooks/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"url": "http://mysite.com/webhook_endpoint",
       "event": "user.create",
       "secret": "secret"}'
```

```javascript
rehive.admin.webhooks.create({
    url: "http://mysite.com/webhook_endpoint",
    event: "user.create",
    secret: "secret"
}).then(function (res) {
    ...
}, function (err) {
    ...
})
```

```python
rehive.admin.webhooks.post(
    url="http://mysite.com/webhook_endpoint",
    event="user.create",
    secret="secret
)
```

> Create webhooks response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "url": "http://mysite.com/webhook_endpoint",
        "event": "user.create",
        "condition": null,
        "secret": "secret",
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431938971
    }
}
```

```javascript
{
    "id": 1,
    "url": "http://mysite.com/webhook_endpoint",
    "event": "user.create",
    "condition": null,
    "secret": "secret",
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

```python
{
    "id": 1,
    "url": "http://mysite.com/webhook_endpoint",
    "event": "user.create",
    "condition": null,
    "secret": "secret",
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

#### Endpoint

`https://api.rehive.com/3/admin/webhooks/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`url` | Webhook URL | blank
`event` | Webhook event | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`condition` | webhook condition* | null
`secret` | Webhook secret | "secret"
`archived` | archived state | false

<aside class="notice">
the <code>condition</code> field is a template strings that is populated with webhook data.
When webhook events are triggered, the string is evluated as python and should result in a boolean upon evluation.
The condition is limited to a max size of 150 characters, has limited recursion
and is only supplied with the webhook data. A valid <code>condition</code> on the
<code>transaction.execute</code> webhook would be <code>'{{ tx_type }}' == 'debit'</code>, which would
result in a webhook only getting triggered if the transaction has a `debit`
transaction type.
</aside>

### Retrieve Webhook

> Retrieve webhook request

```shell
curl https://api.rehive.com/3/admin/webhooks/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.webhooks.get({id: id}).then(function (res) {
    ...
}, function (err) {
    ...
})
```

```python
rehive.admin.webhooks.get(
    {id}
)
```

> Retrieve webhook response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "url": "http://mysite.com/webhook_endpoint",
        "event": "user.create",
        "condition": null,
        "secret": "secret",
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431938971
    }
}
```

```javascript
 {
    "id": 1,
    "url": "http://mysite.com/webhook_endpoint",
    "event": "user.create",
    "secret": "secret",
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

```python
{
    "id": 1,
    "url": "http://mysite.com/webhook_endpoint",
    "event": "user.create",
    "condition": null,
    "secret": "secret",
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

#### Endpoint

`https://api.rehive.com/3/admin/webhooks/{id}/`

### Update Webhook

> Update webhook request

```shell
curl https://api.rehive.com/3/admin/webhooks/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"url": "http://mysite.com/webhook_endpoint"}'
```

```javascript
rehive.admin.webhooks.update(id, {url: "http://mysite.com/webhook_endpoint"}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.webhooks.update(
    url="http://mysite.com/webhook_endpoint"
)
```

> Update webhook response

```shell
{
    "status": "success",
    "data": {
        {
            "id": 1,
            "url": "http://mysite.com/webhook_endpoint",
            "event": "user.create",
            "condition": null,
            "secret": "secret",
            "archived": false,
            "created": 1497431721587,
            "updated": 1497431938971
        }
    }
}
```

```javascript
{
    "id": 1,
    "url": "http://mysite.com/webhook_endpoint",
    "event": "user.create",
    "condition": null,
    "secret": "secret",
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

```python
{
    "id": 1,
    "url": "http://mysite.com/webhook_endpoint",
    "event": "user.create",
    "condition": null,
    "secret": "secret",
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431938971
}
```

#### Endpoint

`https://api.rehive.com/3/admin/webhooks/{id}/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`url` | Webhook URL | blank
`event` | Webhook event | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`secret` | Webhook secret | "secret"
`archived` | archived state | false

### Delete Webhook

> Delete webhook request

```shell
curl https://api.rehive.com/3/admin/webhooks/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.webhooks.delete(id).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.webhooks.delete(
    {id}
)
```

> Delete webhook response

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

#### Endpoint

`https://api.rehive.com/3/admin/webhooks/{id}/`


### List Webhook Tasks

> List webhook tasks request

```shell
curl https://api.rehive.com/3/admin/webhook-tasks/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.webhookTasks.get().then(function (res) {
    ...
}, function (err) {
    ...
})
```

```python
rehive.admin.webhook_tasks.get()
```

> List webhook tasks response

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
                "webhook": {
                    "id": 1,
                    "url": "http://mysite.com/webhook_endpoint",
                    "event": "user.create",
                    "condition": null,
                    "secret": "secret"
                },
                "tries": 1,
                "completed": 1511546662774,
                "failed": null,
                "archived": false,
                "created": 1511546662487,
                "updated": 1511546662774
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
            "id": 1,
            "webhook": {
                "id": 1,
                "url": "http://mysite.com/webhook_endpoint",
                "event": "user.create",
                "condition": null,
                "secret": "secret"
            },
            "tries": 1,
            "completed": 1511546662774,
            "failed": null,
            "archived": false,
            "created": 1511546662487,
            "updated": 1511546662774
        }
    ]
}
```

```python
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "webhook": {
                "id": 1,
                "url": "http://mysite.com/webhook_endpoint",
                "event": "user.create",
                "condition": null,
                "secret": "secret"
            },
            "tries": 1,
            "completed": 1511546662774,
            "failed": null,
            "archived": false,
            "created": 1511546662487,
            "updated": 1511546662774
        }
    ]
}
```

#### Filtering

Field | Type
--- | ---
`webhook` | string
`webhook__event` | string
`webhook__secret` | string

#### Endpoint

`https://api.rehive.com/3/admin/webhook-tasks/`

### Retrieve Webhook Task

> Retrieve webhook task request

```shell
curl https://api.rehive.com/3/admin/webhook-tasks/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.webhookTasks.get({id: id}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.webhook_tasks.get(
    {id}
)
```

> Retrieve webhook task response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "webhook": {
            "id": 1,
            "url": "http://mysite.com/webhook_endpoint",
            "event": "user.create",
            "condition": null,
            "secret": "secret"
        },
        "tries": 1,
        "data": {
            ...
        }
        "completed": 1511546662774,
        "failed": null,
        "archived": false,
        "created": 1511546662487,
        "updated": 1511546662774
    }
}
```

```javascript
{
    "id": 1,
    "webhook": {
        "id": 1,
        "url": "http://mysite.com/webhook_endpoint",
        "event": "user.create",
        "condition": null,
        "secret": "secret"
    },
    "tries": 1,
    "data": {
        ...
    }
    "completed": 1511546662774,
    "failed": null,
    "archived": false,
    "created": 1511546662487,
    "updated": 1511546662774
}
```

```python
{
    "id": 1,
    "webhook": {
        "id": 1,
        "url": "http://mysite.com/webhook_endpoint",
        "event": "user.create",
        "condition": null,
        "secret": "secret"
    },
    "tries": 1,
    "data": {
        ...
    }
    "completed": 1511546662774,
    "failed": null,
    "archived": false,
    "created": 1511546662487,
    "updated": 1511546662774
}
```

#### Endpoint

`https://api.rehive.com/3/admin/webhook-task/{id}/`


### List Webhook Task Requests

> List webhook task requests request

```shell
curl https://api.rehive.com/3/admin/webhook-tasks/{id}/requests/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.webhookTasks.requests.get(webhookTaskID).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.webhook_tasks.obj({id}).requests.get()
```

> List webhook task requests response

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
                "response_code": 200,
                "error": null,
                "created": 1511546662778,
                "updated": 1511546662778
            }
        ]
    }
}
```

```javascript
[
    {
        "id": 1,
        "response_code": 200,
        "error": null,
        "created": 1511546662778,
        "updated": 1511546662778
    }
]
```

```python
[
    {
        "id": 1,
        "response_code": 200,
        "error": null,
        "created": 1511546662778,
        "updated": 1511546662778
    }
]
```

#### Filtering

Field | Type
--- | ---
`response_code` | string

#### Endpoint

`https://api.rehive.com/3/admin/webhook-tasks/{id}/requests/`

### Retrieve Webhook Task Request

> Retrieve webhook task request request

```shell
curl https://api.rehive.com/3/admin/webhook-tasks/{id}/requests/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.webhookTasks.requests.get(webhookTaskID,{id: id}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.webhook_tasks.obj({id}).requests.get(
    {id}
)
```

> Retrieve webhook task request response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "response_code": 200,
        "error": null,
        "created": 1511546662778,
        "updated": 1511546662778
    }
}
```

```javascript
{
    "id": 1,
    "response_code": 200,
    "error": null,
    "created": 1511546662778,
    "updated": 1511546662778
}
```


```python
{
    "id": 1,
    "response_code": 200,
    "error": null,
    "created": 1511546662778,
    "updated": 1511546662778
}
```

#### Endpoint

`https://api.rehive.com/3/admin/webhook-task/{id}/requests/{id}/`


## Subtypes

### List Subtypes

> List subtypes request

```shell
curl https://api.rehive.com/3/admin/subtypes/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.subtypes.get().then(function (res) {
    ...
}, function (err) {
    ...
});
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
            "archived": false,
            "created": 1509529290352,
            "updated": 1509529290352
        }
    ]
}
```

```javascript
[
    {
        "id": 20,
        "name": "credit_subtype",
        "label": "Our credit",
        "description": "Description for our credit",
        "tx_type": "credit",
        "archived": false,
        "created": 1509529290352,
        "updated": 1509529290352
    }
]
```

```python
[
    {
        "id": 20,
        "name": "credit_subtype",
        "label": "Our credit",
        "description": "Description for our credit",
        "tx_type": "credit",
        "archived": false,
        "created": 1509529290352,
        "updated": 1509529290352
    }
]
```

#### Endpoint

`https://api.rehive.com/3/admin/subtypes/`

### Create subtypes

> Create subtypes request

```shell
curl https://api.rehive.com/3/admin/subtypes/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.subtypes.create(
{
    name: "credit_subtype",
    label: "Our credit",
    description: "Description for our credit",
    tx_type:"credit"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.subtypes.create(
    name="credit_subtype",
    label="Our credit",
    description="Description for our credit",
    tx_type="credit"
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
        "archived": false,
        "created": 1509529290352,
        "updated": 1509529290352
    }
}
```

```javascript
 {
    "id": 20,
    "name": "credit_subtype",
    "label": "Our credit",
    "description": "Description for our credit",
    "tx_type": "credit",
    "archived": false,
    "created": 1509529290352,
    "updated": 1509529290352
}
```

```python
 {
    "id": 20,
    "name": "credit_subtype",
    "label": "Our credit",
    "description": "Description for our credit",
    "tx_type": "credit",
    "archived": false,
    "created": 1509529290352,
    "updated": 1509529290352
}
```

#### Endpoint

`https://api.rehive.com/3/admin/subtypes/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`tx_type` | Transaction type | blank
`name` | name | blank

#### Optional Fields

Field | Description | Default
--- | --- | ---
`label` | label | blank
`description` | description | blank
`archived` | archived state | false

### Retrieve Subtypes

> Retrieve subtypes request

```shell
curl https://api.rehive.com/3/admin/subtypes/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.subtypes.get({id: id}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "archived": false,
        "created": 1509529290352,
        "updated": 1509529290352
    }
}
```

```javascript
{
    "id": 20,
    "name": "credit_subtype",
    "label": "Our credit",
    "description": "Description for our credit",
    "tx_type": "credit",
    "archived": false,
    "created": 1509529290352,
    "updated": 1509529290352
}
```

```python
{
    "id": 20,
    "name": "credit_subtype",
    "label": "Our credit",
    "description": "Description for our credit",
    "tx_type": "credit",
    "archived": false,
    "created": 1509529290352,
    "updated": 1509529290352
}
```

#### Endpoint

`https://api.rehive.com/3/admin/subtypes/{id}/`

### Update subtype

> Update subtype request

```shell
curl https://api.rehive.com/3/admin/subtypes/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"description": "New description"}'
```

```javascript
rehive.admin.subtypes.update(id, {description: "New description"}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "archived": false,
        "created": 1509529290352,
        "updated": 1509529290352
    }
}
```

```javascript
{
    "id": 20,
    "name": "credit_subtype",
    "label": "Our credit",
    "description": "New description",
    "tx_type": "credit",
    "archived": false,
    "created": 1509529290352,
    "updated": 1509529290352
}
```

```python
{
    "id": 20,
    "name": "credit_subtype",
    "label": "Our credit",
    "description": "New description",
    "tx_type": "credit",
    "archived": false,
    "created": 1509529290352,
    "updated": 1509529290352
}
```

#### Endpoint

`https://api.rehive.com/3/admin/subtypes/{id}/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`tx_type` | Transaction type | blank
`name` | name | blank

#### Optional Fields

Field | Description | Default
--- | --- | ---
`label` | label | blank
`description` | description | blank
`archived` | archived state | false

### Delete Subtype

> Delete subtype request

```shell
curl https://api.rehive.com/3/admin/subtypes/{id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.subtypes.delete(id).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.subtypes.delete(
    {id}
)
```

> Delete subtype response

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

#### Endpoint

`https://api.rehive.com/3/admin/subtypes/{id}/`


## Notifications

### List Notifications

> List Notifications request

```shell
curl https://api.rehive.com/3/admin/notifications/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.notifications.get().then(function (res) {
    ...
}, function (err) {
    ...
})
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

```javascript
[
    {
        "id": 1,
        "name": "account_verify",
        "description": "Account verification notifications",
        "enabled": true
    }
]
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

`https://api.rehive.com/3/admin/notifications/`

### Retrieve Notifications

> Retrieve Notifications request

```shell
curl https://api.rehive.com/3/admin/notifications/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.notifications.get({id: id}).then(function (res) {
    ...
}, function (err) {
    ...
})
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

```javascript
{
    "id": 1,
    "name": "account_verify",
    "description": "Account verification notifications",
    "enabled": true
}
```

```python
{
    "id": 1,
    "name": "account_verify",
    "description": "Account verification notifications",
    "enabled": true
}
```

#### Endpoint

`https://api.rehive.com/3/admin/notifications/{id}`

### Update Notifications

> Update Notifications request

```shell
curl https://api.rehive.com/3/admin/notifications/{id}
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"enabled": false}'
```

```javascript
rehive.admin.notifications.update(id, {enabled: false).then(function (res) {
    ...
}, function (err) {
    ...
});
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

```javascript
{
    "id": 1,
    "name": "account_verify",
    "description": "Account verification notifications",
    "enabled": false
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

`https://api.rehive.com/3/admin/notifications/{id}`

#### Required Fields

Field | Description | Default
--- | --- | ---
`enabled` | Account Name | false

## Group Tiers

Tiers are a way in which to categorise users based on requirements for the tier.
Tiers are set on a group to limit users' transactions on that group for certain currencies.

Tiers are checked in ascending order based on their level, with the user getting
validation corresponding to the highest tier they matched.

### List Tiers

List all tiers.

> List Tier request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.tiers.get(groupName).then(function (res) {
    ...
}, function (error) {
    ...
})
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
            "settings": {
                "allow_transactions": true,
                "allow_debit_transactions": true,
                "allow_credit_transactions": true
            },
            "archived": false,
            "created": 1497367640298,
            "updated": 1497367640298
        }
    ]
}
```

```javascript
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
        "settings": {
            "allow_transactions": true,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        },
        "archived": false,
        "created": 1497367640298,
        "updated": 1497367640298
    }
]
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
        "settings": {
            "allow_transactions": true,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        },
        "archived": false,
        "created": 1497367640298,
        "updated": 1497367640298
    }
]
```

#### Filtering

Field | Type
--- | ---
`currency` | string
`requirement` | string

#### Endpoint

`https://api.rehive.com/3/admin/{group_name}/tiers/`

### Create Tier

Create a new tier.

> Create Tier request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"currency": "XBT",
       "level": 1
       "name": "First tier"
       "description": "This is a tier"}'
```

```javascript
rehive.admin.groups.tiers.create(groupName,
{
    level: 1,
    name: "First tier",
    description: "This is a tier"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.tiers.create(
    currency="XBT",
    level=1,
    name="First tier",
    description="This is a tier"
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
        "settings": {
            "allow_transactions": true,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        },
        "archived": false,
        "created": 1497367640298,
        "updated": 1497367640298
    }
}
```

```javascript
{
    "id": 1,
    "currency": "ZAR",
    "level": 1,
    "name": "First Tier",
    "description": "My First Tier",
    "requirements": [],
    "limits": [],
    "fees": [],
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "archived": false,
    "created": 1497367640298,
    "updated": 1497367640298
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
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "archived": false,
    "created": 1497367640298,
    "updated": 1497367640298
}
```

#### Endpoint

`https://api.rehive.com/3/admin/{group_name}/tiers/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`currency` | Currency code related to this tier |

#### Optional Fields

Field | Description | Default
--- | --- | ---
`level` | Tier Level | null
`name` | Name of the tier | blank
`description` | Description of the tier | blank
`archived` | archived state | false

### Retrieve Tier

Retrieve a specific tier.

> Retrieve Tier request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.tiers.get(groupName,{id: id}).then(function (res) {
    ...
}, function (error) {
    ...
});
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
        "settings": {
            "allow_transactions": true,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        },
        "archived": false,
        "created": 1497367640298,
        "updated": 1497367640298
    }
}
```

```javascript
{
    "id": 1,
    "currency": "ZAR",
    "level": 1,
    "name": "First Tier",
    "description": "My First Tier",
    "requirements": [],
    "limits": [],
    "fees": [],
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "archived": false,
    "created": 1497367640298,
    "updated": 1497367640298
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
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "archived": false,
    "created": 1497367640298,
    "updated": 1497367640298
}
```

#### Endpoint

`https://api.rehive.com/3/admin/{group_name}/tiers/{id}/`

### Update Tier

Update the name of description of a tier.

> Update Tier request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "Updated Name"}'
```

```javascript
rehive.admin.groups.tiers.update(groupName,tierId, {name: "Updated Name"}).then(function (res) {
    ...
}, function (error) {
    ...
});
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
        "settings": {
            "allow_transactions": true,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        },
        "archived": false,
        "created": 1497367640298,
        "updated": 1497369829536
    }
}
```

```javascript
{
    "id": 1,
    "currency": "ZAR",
    "level": 1,
    "name": "Updated Name",
    "description": "My First Tier",
    "requirements": [],
    "limits": [],
    "fees": [],
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "archived": false,
    "created": 1497367640298,
    "updated": 1497369829536
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
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "archived": false,
    "created": 1497367640298,
    "updated": 1497369829536
}
```

#### Required Fields

Field | Description | Default
--- | --- | ---
`currency` | Currency code related to this tier |

#### Optional Fields

Field | Description | Default
--- | --- | ---
`level` | Tier Level | null
`name` | Name of the tier | blank
`description` | Description of the tier | blank
`archived` | archived state | false

#### Endpoint

`https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/`

### Delete Tier

Delete a specific tier.

> Delete Tier request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.tiers.delete(groupName,tierId).then(function (res) {
    ...
}, function (error) {
    ...
});
```

```python
rehive.admin.tiers.delete(
    {id}
)
```

> Delete Tier response

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

`https://api.rehive.com/3/admin/{group_name}/tiers/{id}/`

### List Tier Requirements

List all requirements related to a tier.

> List Tier Requirements request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/requirements/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.tiers.requirements.get(groupName,tierId).then(function (res) {
    ...
}, function (error) {
    ...
});
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
            "requirement": "First Name",
            "archived": false
        }
    ]
}
```

```javascript
[
    {
        "id": 1,
        "requirement": "First Name",
        "archived": false
    }
]
```

```python
[
    {
        "id": 1,
        "requirement": "First Name",
        "archived": false
    }
]
```

#### Endpoint

`https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/requirements/`

### Create Tier Requirements

Create a new requirement related to a Tier.

> Create Tier Requirements request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/requirements/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"requirement": "birth_date"}'
```

```javascript
rehive.admin.groups.tiers.requirements.create(groupName,tierId, {
    requirement: "birth_date"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "id": 1,
        "requirement": "First Name",
        "archived": false
    }
}
```

```javascript
{
    "id": 1,
    "requirement": "First Name",
    "archived": false
}
```

```python
{
    "id": 1,
    "requirement": "First Name",
    "archived": false
}
```

#### Endpoint

`https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/requirements/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`requirement` | Requirement Type | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`archived` | archived state | false

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
`mobile` | Mobile Number
`proof_of_identity` | Proof of identity
`proof_of_address` | Proof of address
`advanced_proof_of_identity` | Advanced proof of identity

### Retrieve Tier Requirements

Retrieve a specific requirement related to a Tier

> Retrieve Tier Requirements request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/requirements/{requirement_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.tiers.requirements.get(groupName,tierId, {id: id}).then(function (res) {
    ...
}, function (error) {
    ...
});
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
        "id": 1,
        "requirement": "First Name",
        "archived": false
    }
}
```

```javascript
{
    "id": 1,
    "requirement": "First Name",
    "archived": false
}
```

```python
{
    "id": 1,
    "requirement": "First Name",
    "archived": false
}
```

#### Endpoint

`https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/requirements/{requirement_id}/`

### Update Tier Requirements

Update a specific requirement related to a Tier

> Update Tier Requirements request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/requirements/{requirement_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"requirement": "proof_of_identity"}'
```

```javascript
rehive.admin.groups.tiers.requirements.update(groupName,tierId, requirementId,{requirement: "proof_of_identity"}).then(function (res) {
    ...
}, function (error) {
    ...
});
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
        "id": 1,
        "requirement": "Proof of Identity",
        "archived": false
    }
}
```

```javascript
{
    "id": 1,
    "requirement": "Proof of Identity",
    "archived": false
}
```

```python
{
    "id": 1,
    "requirement": "Proof of Identity",
    "archived": false
}
```

#### Endpoint

`https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/requirements/{requirement_id}/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`requirement` | Requirement Type |

#### Optional Fields

Field | Description | Default
--- | --- | ---
`archived` | archived state | false

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
`mobile` | Mobile Number
`proof_of_identity` | Proof of identity
`proof_of_address` | Proof of address
`advanced_proof_of_identity` | Advanced proof of identity

### Delete Tier Requirements

Delete a specific requirement related to a Tier

> Delete Tier Requirements request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/requirements/{requirement_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.tiers.requirements.delete(name,tierId,requirementId).then(function (res) {
    ...
}, function (error) {
    ...
});
```

```python
rehive.admin.tiers.obj({tier_id}).requirements.delete(
    {requirement_id}
)
```

> Delete Tier Requirements response

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

`https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/requirements/{requirement_id}/`

### List Tier Limits

List all Limits related to a tier.

> List Tier Limits request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/limits/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.tiers.limits.get(groupName,tierId).then(function (res) {
    ...
}, function (error) {
    ...
});
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
            "archived": false,
            "created": 1497374071027,
            "updated": 1497374071027
        }
    ]
}
```

```javascript
[
    {
        "id": 1,
        "value": 1000,
        "currency": "USD",
        "type": "Maximum",
        "tx_type": "credit",
        "subtype": null,
        "archived": false,
        "created": 1497374071027,
        "updated": 1497374071027
    }
]
```

```python
[
    {
        "id": 1,
        "value": 1000,
        "type": "Maximum",
        "tx_type": "credit",
        "subtype": null,
        "archived": false,
        "created": 1497374071027,
        "updated": 1497374071027
    }
]
```

#### Endpoint

`https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/limits/`

### Create Tier Limits

Create a new limit related to a Tier.

> Create Tier Limits request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/limits/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"requirement": "birth_date"}'
```

```javascript
rehive.admin.groups.tiers.limits.create(name,tierId, {
    currency: 'USD',
    value: 1000,
    type: "Maximum",
    tx_type: 'credit'
}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "archived": false,
        "created": 1497374071027,
        "updated": 1497374071027
    }
}
```

```javascript
{
    "id": 1,
    "value": 1000,
    "currency": "USD",
    "type": "Maximum",
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497374071027,
    "updated": 1497374071027
}
```

```python
{
    "id": 1,
    "value": 1000,
    "type": "Maximum",
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497374071027,
    "updated": 1497374071027
}
```

#### Endpoint

`https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/limits/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`value` | Limit value | 0
`type` | Limit Type |
`tx_type` | Transaction type limits are applied |

#### Optional Fields

Field | Description | Default
--- | --- | ---
`subtype` | Transaction subtype name | null
`archived` | archived state | false

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
curl https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/limits/{limit_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.tiers.limits.get(groupName,tierId, {id: id}).then(function (res) {
    ...
}, function (error) {
    ...
});
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
        "archived": false,
        "created": 1497374071027,
        "updated": 1497374071027
    },
    "status": "success"
}
```

```javascript
{
    "id": 1,
    "value": 1000,
    "currency": "USD",
    "type": "Maximum",
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497374071027,
    "updated": 1497374071027
}
```

```python
{
    "id": 1,
    "value": 1000,
    "type": "Maximum",
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497374071027,
    "updated": 1497374071027
}
```

#### Endpoint

`https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/limits/{limit_id}/`

### Update Tier Limits

Update a specific limits related to a Tier

> Update Tier Limits request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/limits/{limit_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 5000,
       "type": "min"}'
```

```javascript
rehive.admin.groups.tiers.limits.update(groupName,tierId, limitId,{value: 5000,type: "min"}).then(function (res) {
    ...
}, function (error) {
    ...
});
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
        "archived": false,
        "created": 1497374071027,
        "updated": 1497374886088
    }
}
```

```javascript
{
    "id": 1,
    "value": 5000,
    "currency": "USD",
    "type": "Minimum",
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497374071027,
    "updated": 1497374886088
}
```

```python
{
    "id": 1,
    "value": 5000,
    "type": "Minimum",
    "tx_type": "credit",
    "subtype": null,
    "archived": false,
    "created": 1497374071027,
    "updated": 1497374886088
}
```

#### Endpoint

`https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/limits/{limit_id}/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`value` | Limit value | 0
`type` | Limit Type |
`tx_type` | Transaction type limits are applied |

#### Optional Fields

Field | Description | Default
--- | --- | ---
`subtype` | Transaction subtype name | null
`archived` | archived state | false

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

### Delete Tier Limits

Delete a specific requirement related to a Tier

> Delete Tier Limits request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/limits/{limit_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.tiers.limits.delete(groupName,tierId, limitId).then(function (res) {
    ...
}, function (error) {
    ...
});
```

```python
rehive.admin.tiers.obj({tier_id}).limits.delete(
    {limit_id}
)
```

> Delete Tier Limits response

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

`https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/limits/{limit_id}/`

### List Tier Fees

List all fees related to a Tier.

> List Tier Fees request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/fees/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.tiers.fees.get(groupName,tierId).then(function (res) {
    ...
}, function (error) {
    ...
});
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
            "currency": "ZAR",
            "descrition": "Test Fee"
            "subtype": null,
            "archived": false,
            "created": 1497431721587,
            "updated": 1497431721587
        }
    ],
    "status": "success"
}
```

```javascript
[
    {
        "id": 1,
        "value": 1000,
        "percentage": null,
        "tx_type": "credit",
        "currency": "ZAR",
        "descrition": "Test Fee"
        "subtype": null,
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431721587
    }
]
```

```python
[
    {
        "id": 1,
        "value": 1000,
        "percentage": null,
        "tx_type": "credit",
        "currency": "ZAR",
        "descrition": "Test Fee"
        "subtype": null,
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431721587
    }
]
```

#### Endpoint

`https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/fees/`

### Create Tier Fee

Create a new fee related to a Tier.

> Create Tier Fee request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/fees/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 1000,
       "tx_type": "credit"}'
```

```javascript
rehive.admin.groups.tiers.fees.create(groupName,tierId, {
    currency: 'XBT',
    value: 1000,
    tx_type: 'credit'
}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "currency": "ZAR",
        "descrition": "Test Fee"
        "subtype": null,
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431721587
    },
    "status": "success"
}
```

```javascript
{
    "id": 1,
    "value": 1000,
    "percentage": null,
    "tx_type": "credit",
    "currency": "ZAR",
    "descrition": "Test Fee"
    "subtype": null,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431721587
}
```

```python
{
    "id": 1,
    "value": 1000,
    "percentage": null,
    "tx_type": "credit",
    "currency": "ZAR",
    "descrition": "Test Fee"
    "subtype": null,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431721587
}
```

#### Endpoint

`https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/fees/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`tx_type` | Transaction type fees are applied | null
`currency` | fee currency | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`value` | Fee amount | 0
`percentage` | Percentage amount |
`subtype` | Transaction subtype name | null
`archived` |archived state | false

#### Transaction Types

Value | Description
--- | ---
`credit` | Credit
`debit` | Debit

### Retrieve Tier fee

Retrieve a specific requirement related to a Tier.

> Retrieve Tier Fee request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/fees/{fee_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.tiers.fees.get(groupName,tierId, {id: id}).then(function (res) {
    ...
}, function (error) {
    ...
});
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
        "currency": "ZAR",
        "descrition": "Test Fee"
        "subtype": null,
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431721587
    },
    "status": "success"
}
```

```javascript
{
    "id": 1,
    "value": 1000,
    "percentage": null,
    "tx_type": "credit",
    "currency": "ZAR",
    "descrition": "Test Fee"
    "subtype": null,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431721587
}
```

```python
{
    "id": 1,
    "value": 1000,
    "percentage": null,
    "tx_type": "credit",
    "currency": "ZAR",
    "descrition": "Test Fee"
    "subtype": null,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431721587
}
```

#### Endpoint

`https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/fees/{fee_id}/`

### Update Tier Fee

Update a specific fees related to a Tier.

> Update Tier request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/fees/{fee_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 5000}'
```

```javascript
rehive.admin.groups.tiers.fees.update(groupName,tierId, feeId,{value: 5000}).then(function (res) {
    ...
}, function (error) {
    ...
});
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
        "value": 1000,
        "percentage": null,
        "tx_type": "credit",
        "currency": "ZAR",
        "descrition": "Test Fee"
        "subtype": null,
        "archived": false,
        "created": 1497431721587,
        "updated": 1497431721587
    },
    "status": "success"
}
```

```javascript
{
    "id": 1,
    "value": 1000,
    "percentage": null,
    "tx_type": "credit",
    "currency": "ZAR",
    "descrition": "Test Fee"
    "subtype": null,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431721587
}
```

```python
{
    "id": 1,
    "value": 1000,
    "percentage": null,
    "tx_type": "credit",
    "currency": "ZAR",
    "descrition": "Test Fee"
    "subtype": null,
    "archived": false,
    "created": 1497431721587,
    "updated": 1497431721587
}
```

#### Endpoint

`https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/fees/{fee_id}/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`tx_type` | Transaction type fees are applied |

#### Optional Fields

Field | Description | Default
--- | --- | ---
`value` | Fee amount | 0
`percentage` | Percentage amount |
`subtype` | Transaction subtype name | null
`archived` | archived state | false

#### Transaction Types

Value | Description
--- | ---
`credit` | Credit
`debit` | Debit

### Delete Tier fee

Delete a specific requirement related to a Tier.

> Delete Tier Fee request

```shell
curl https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/fees/{fee_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.tiers.fees.delete(groupName,tierId, feeId).then(function (res) {
    ...
}, function (error) {
    ...
});
```

```python
rehive.admin.tiers.obj({tier_id}).fees.delete(
    {fee_id}
)
```

> Delete Tier Fee response

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

`https://api.rehive.com/3/admin/{group_name}/tiers/{tier_id}/fees/{fee_id}/`

## Groups

Rehive inclused a group management system, that allows admin users to create groups as well as individually manage users'
permissions to view, add, edit or delete data from the system via admin endpoints.

### List groups

> Admin list groups request

```shell
curl https://api.rehive.com/3/admin/groups/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.get().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.groups.get()
```

> Admin list groups response

```shell
{
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "name": "test",
                "label": "Test",
                "description": null,
                "default": false,
                "public": true,
                "permissions": 0,
                "tiers": [],
                "settings": {
                    "allow_transactions": true,
                    "allow_debit_transactions": true,
                    "allow_credit_transactions": true
                },
                "archived": false,
                "created": 1516008597579,
                "updated": 1516008579877
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
            "name": "test",
            "label": "Test",
            "description": null,
            "default": false,
            "public": true,
            "permissions": 0,
            "tiers": [],
            "settings": {
                "allow_transactions": true,
                "allow_debit_transactions": true,
                "allow_credit_transactions": true
            },
            "archived": false,
            "created": 1516008597579,
            "updated": 1516008579877
        }
    ]
}
```

```python
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "test",
            "label": "Test",
            "description": null,
            "default": false,
            "public": true,
            "permissions": 0,
            "tiers": [],
            "settings": {
                "allow_transactions": true,
                "allow_debit_transactions": true,
                "allow_credit_transactions": true
            },
            "archived": false,
            "created": 1516008597579,
            "updated": 1516008579877
        }
    ]
}
```

Get a list of groups that have been created.


#### Filtering

Field | Type
--- | ---
`name` | string


#### Endpoint

`https://api.rehive.com/3/admin/groups/`

### Create groups

> Admin create groups request

```shell
curl https://api.rehive.com/3/admin/groups/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "test"}'
```

```javascript
rehive.admin.groups.create({name: "test"}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.groups.create(
    name="test"
)
```

> Admin create groups response

```shell
{
    "data": {
        "name": "test",
        "label": "Test",
        "description": null,
        "default": false,
        "public": true,
        "permissions": 0,
        "tiers": [],
        "settings": {
            "allow_transactions": false,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        },
        "archived": false,
        "created": 1516008597579,
        "updated": 1516008579877
    },
    "status": "success"
}
```

```javascript
{
    "name": "test",
    "label": "Test",
    "description": null,
    "default": false,
    "public": true,
    "permissions": 0,
    "tiers": [],
    "settings": {
        "allow_transactions": false,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "archived": false,
    "created": 1516008597579,
    "updated": 1516008579877
}
```

```python
{
    "name": "test",
    "label": "Test",
    "description": null,
    "default": false,
    "public": true,
    "permissions": 0,
    "tiers": [],
    "settings": {
        "allow_transactions": false,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "archived": false,
    "created": 1516008597579,
    "updated": 1516008579877
}
```

Create a new group.

#### Endpoint

`https://api.rehive.com/3/admin/groups/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`name` | group name | ""

#### Optional Fields

Field | Description | Default
--- | --- | ---
`archived` | archived state | false

### Update groups

> Admin update groups request

```shell
curl https://api.rehive.com/3/admin/groups/{group_name}/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "new_name"}'
```

```javascript
rehive.admin.groups.update(groupName,{name: "new_name"}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.groups.update(
   {group_name},
   name="new_name"
)
```

> Admin update groups response

```shell
{
    "data": {
        "name": "new_name",
        "label": "Test",
        "description": null,
        "default": false,
        "public": true,
        "permissions": 0,
        "tiers": [],
        "settings": {
            "allow_transactions": false,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        },
        "archived": false,
        "created": 1516008597579,
        "updated": 1516008579877
    },
    "status": "success"
}
```

```javascript
{
    "name": "new_name",
    "label": "Test",
    "description": null,
    "default": false,
    "public": true,
    "permissions": 0,
    "tiers": [],
    "settings": {
        "allow_transactions": false,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "archived": false,
    "created": 1516008597579,
    "updated": 1516008579877
}
```

```python
{
    "name": "new_name",
    "label": "Test",
    "description": null,
    "default": false,
    "public": true,
    "permissions": 0,
    "tiers": [],
    "settings": {
        "allow_transactions": false,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    },
    "archived": false,
    "created": 1516008597579,
    "updated": 1516008579877
}
```

Update the group's details.

#### Endpoint

`https://api.rehive.com/3/admin/groups/{group_name}/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`name` | group name | ""

#### Optional Fields

Field | Description | Default
--- | --- | ---
`archived` | archived state | false

### Delete groups

> Admin delete groups request

```shell
curl https://api.rehive.com/3/admin/groups/{group_name}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```
```javascript
rehive.admin.groups.delete(groupName).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.groups.delete(
   {group_name}
)
```

> Admin delete groups response

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

Delete the group.

#### Endpoint

`https://api.rehive.com/3/admin/groups/{group_name}/`


### Assign group

> Admin assign group request

```shell
curl https://api.rehive.com/3/admin/users/{id}/groups/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"group": "test"}'
```

```javascript
rehive.admin.users.groups.create(uuid, {
    group: "test"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.obj({id}).groups.assign(
    group='test'
)
```

> Admin assign group response

```shell
{
    "data": {
        "name": "test",
        "label": "Test",
        "settings": {
            "allow_transactions": true,
            "allow_debit_transactions": true,
            "allow_credit_transactions": true
        }
    },
    "status": "success"
}
```

```javascript
{
    "name": "test",
    "label": "Test",
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    }
}
```

```python
{
    "name": "test",
    "label": "Test",
    "settings": {
        "allow_transactions": true,
        "allow_debit_transactions": true,
        "allow_credit_transactions": true
    }
}
```

Assign a user to a group.

#### Endpoint

`https://api.rehive.com/3/admin/users/{id}/groups/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`group` | Group name | ""

### Unassign group

> Admin unassign group request

```shell
curl https://api.rehive.com/3/admin/users/{id}/groups/{group_name}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.groups.delete(uuid,groupName).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.obj({id}).groups.unassign(
    group='test'
)
```

> Admin unassign group response

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

Unassign a group from a user.

#### Endpoint

`https://api.rehive.com/3/admin/users/{id}/groups/{group_name}/`

## Permissions

Users can either be assigned groups, or permissions directly. When assigning groups to a user, the user will have the access specified in the permission assigned to the group. Individual permissions can be assigned to user if some additional permission only need to be provided to a specific user.

### List group permissions

> Admin list group permissions request

```shell
curl https://api.rehive.com/3/admin/groups/{group_name}/permissions/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.permissions.get(groupName).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.groups.obj({group_name}).permissions.get()
```

> Admin list group permissions response

```shell
{
    "status": "success",
    "data": {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 55,
                "type": "account",
                "level": "add"
            }
        ]
    }
}
```

```javascript
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 55,
            "type": "account",
            "level": "add"
        }
    ]
}
```

```python
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 55,
            "type": "account",
            "level": "add"
        }
    ]
}
```

List all the permissions associated to a group.

#### Endpoint

`https://api.rehive.com/3/admin/groups/{group_name}/permissions/`

### Add group permissions

> Admin add group permissions request

```shell
curl https://api.rehive.com/3/admin/groups/{group_name}/permissions/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"type": "account",
       "level": "view"}'
```

```javascript
rehive.admin.groups.permissions.create(groupName,
{
    type: "account",
    level: "view"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.groups.obj({group_name}).permissions.create(
    type="account",
    level="view"
)
```

> Admin add permissions response

```shell
{
    "data": {
        "id": 367,
        "type": "account",
        "level": "view"
    },
    "status": "success"
}
```

```javascript
{
    "id": 367,
    "type": "account",
    "level": "view"
}
```

```python
{
    "id": 367,
    "type": "account",
    "level": "view"
}
```

Add the given permission to the group.

#### Endpoint

`https://api.rehive.com/3/admin/groups/{group_name}/permissions/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`type` | Permission type | ""
`level` | Level of permission | ""

### Remove group permissions

> Admin remove group permissions request

```shell
curl https://api.rehive.com/3/admin/groups/{group_name}/permissions/{permission_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.permissions.delete(groupName,permissionId).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.groups.obj({group_name}).permissions.delete(
    {permission_id}
)
```

> Admin remove group permissions response

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

Remove the permission from the group.

#### Endpoint

`https://api.rehive.com/3/admin/groups/{group_name}/permissions/{permission_id}/`

### Assign permissions

> Admin assign permissions request

```shell
curl https://api.rehive.com/3/admin/users/{id}/permissions/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"type": "account",
       "level": "view"}'
```

```javascript
rehive.admin.users.permissions.create(uuid, {
    type: "account",
    level: "view"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.obj({id}).permissions.create(
    type="account",
    level="view"
)
```

> Admin assign permissions response

```shell
{
    "status": "success",
    "data": {
        "id": 269,
        "type": "account",
        "level": "view"
    }
}
```

```javascript
{
    "id": 269,
    "type": "account",
    "level": "view"
}
```

```python
{
    "id": 269,
    "type": "account",
    "level": "view"
}
```

Assign a permission to a user.

#### Endpoint

`https://api.rehive.com/3/admin/users/{id}/permissions/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`type` | Permission type | ""
`level` | Level of permission | ""

### Unassign permissions

> Admin unassign permissions request

```shell
curl https://api.rehive.com/3/admin/users/{id}/permissions/{permission_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.permissions.delete(uuid,permissionId).then(function (res) {
   ...
}, function (err) {
   ...
});
```

```python
rehive.admin.users.obj({id}).permissions.delete(
    {permissions_id}
)
```

> Admin unassign permissions response

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

Unassign a permissions for a user.

#### Endpoint

`https://api.rehive.com/3/admin/users/{id}/permissions/{permission_id}/`

## Group Account Configurations

Account configurations are used to define account presets. The configurations
are attached to specifc groups and can be used to configure account settings
and currencies.

### List Group Account Configuration

> List group account configurations request

```shell
curl https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.accountConfigurations.get(groupName).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.groups.obj({group_name}).account_configurations.get()
```

> List group account configurations response

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
                "label": "Default",
                "currencies": [],
                "default": true,
                "primary": true,
                "archived": false,
                "created": 1464858068732,
                "updated": 1464858068732
            }
        ]
    }
}
```

```javascript
[
    {
        "name": "default",
        "label": "Default",
        "currencies": [],
        "default": true,
        "primary": true,
        "archived": false,
        "created": 1464858068732,
        "updated": 1464858068732
    }
]
```

```python
[
    {
        "name": "default",
        "label": "Default",
        "currencies": [],
        "default": true,
        "primary": true,
        "archived": false,
        "created": 1464858068732,
        "updated": 1464858068732
    }
]
```

List group account configurations.

#### Endpoint

`https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/`

### Create Group Account Configuration

> Create group account configuration request

```shell
curl https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"name": "default",
       "label": "Default"}'
```

```javascript
rehive.admin.groups.accountConfigurations.create(groupName,
{
    name: 'default',
    label: 'Default'

}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.groups.obj({group_name}).account_configurations.create(
    name="default",
    label="Default"
)
```

> Create group account configuration response

```shell
{
    "status": "success",
    "data": {
        "name": "default",
        "label": "Default",
        "currencies": [],
        "default": true,
        "primary": true,
        "archived": false,
        "created": 1464858068732,
        "updated": 1464858068732
    }
}
```

```javascript
{
    "name": "default",
    "label": "Default",
    "currencies": [],
    "default": true,
    "primary": true,
    "archived": false,
    "created": 1464858068732,
    "updated": 1464858068732
}
```

```python
{
    "name": "default",
    "label": "Default",
    "currencies": [],
    "default": true,
    "primary": true,
    "archived": false,
    "created": 1464858068732,
    "updated": 1464858068732
}
```

Create a group account configuration.

#### Endpoint

`https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`name` | Name of account | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`label` | Label of account | blank
`default` | Default to users on register | false
`primary` | The main account for a group | false
`archived` | archived state | false

### Retrieve Group Account Configuration

> Group account configuration request

```shell
curl https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/{config_name}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.accountConfigurations.get(groupName,{name: configName}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.groups.obj({group_name}).account_configurations.get(
    {config_name}
)
```

> Group account configuration response

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
                "label": "Default",
                "currencies": [],
                "default": true,
                "primary": true,
                "archived": false,
                "created": 1464858068732,
                "updated": 1464858068732
            }
        ]
    }
}
```

```javascript
[
    {
        "name": "default",
        "label": "Default",
        "currencies": [],
        "default": true,
        "primary": true,
        "archived": false,
        "created": 1464858068732,
        "updated": 1464858068732
    }
]
```

```python
[
    {
        "name": "default",
        "label": "Default",
        "currencies": [],
        "default": true,
        "primary": true,
        "archived": false,
        "created": 1464858068732,
        "updated": 1464858068732
    }
]
```

Retrieve a group account configuration.

#### Endpoint

`https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/{config_name}/`

### Update Group Account Configuration

> Update group account configuration request

```shell
curl https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/{config_name}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "default", "label": "Default"}'
```

```javascript
rehive.admin.groups.accountConfigurations.update(groupName,configName,{name: "default", label: "Default"}).then(function (res) {
    ...
}, function (error) {
    ...
});
```

```python
rehive.admin.groups.obj({group_name}).account_configurations.update(
    {config_name},
    name="default",
    label="Default"
)
```

> Update group account configuration response

```shell
{
    "status": "success",
    "data": {
        "name": "default",
        "label": "Default",
        "currencies": [],
        "default": true,
        "primary": true,
        "archived": false,
        "created": 1464858068732,
        "updated": 1464858068732
    }
}
```

```javascript
{
    "name": "default",
    "label": "Default",
    "currencies": [],
    "default": true,
    "primary": true,
    "archived": false,
    "created": 1464858068732,
    "updated": 1464858068732
}
```

```python
{
    "name": "default",
    "label": "Default",
    "currencies": [],
    "default": true,
    "primary": true,
    "archived": false,
    "created": 1464858068732,
    "updated": 1464858068732
}
```

Retrieve a group account configuration.

#### Endpoint

`https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/{config_name}/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`name` | Name of account | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`label` | Label of account | blank
`default` | Default to users on register | false
`primary` | The main account for a group | false
`archived` | archived state | false

### Delete Group Account Configuration

> Delete group account configuration request

```shell
curl https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/{config_name}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.accountConfigurations.delete(groupName,configName).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.groups.obj({group_name}).account_configurations.delete(
    {config_name}
)
```

> Delete group account configuration response

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

Delete a group account configuration.

#### Endpoint

`https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/{config_name}/`


### List Group Account Configuration Currencies

> Admin list group account configuration currencies request

```shell
curl https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/{config_name}/currencies/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.accountConfigurations.currencies.get(groupName,configName).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.groups.obj({group_name}).account_configurations.obj({config_name})/.
    currencies.get()
```

> Admin list group account configuration currencies response

```shell
{
    "status": "success",
    "next": null,
    "previous": null,
    "results": [
        {
            "code": "ZAR",
            "description": "Rand",
            "symbol": "R",
            "unit": "rand",
            "divisibility": 2
        }
    ]
}
```

```javascript
[
    {
        "code": "ZAR",
        "description": "Rand",
        "symbol": "R",
        "unit": "rand",
        "divisibility": 2
    }
]
```

```python
[
    {
        "code": "ZAR",
        "description": "Rand",
        "symbol": "R",
        "unit": "rand",
        "divisibility": 2
    }
]
```

Get a list of currencies for a group account configuration.

#### Endpoint

`https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/{config_name}/currencies/`


### Create Group Account Configuration Currency

> Admin create group account configuration currency request

```shell
curl https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/{config_name}/currencies/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"currency": "ZAR"}'
```

```javascript
rehive.admin.groups.accountConfigurations.currencies.create(groupName,configName,
{
    currency: "ZAR"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.groups.obj({group_name}).account_configurations.obj({config_name})/.
    currencies.post(
        currency="ZAR"
    )
```

> Admin create group account configuration currency response

```shell
{
    "status": "success",
    "data": {
        "code": "ZAR",
        "description": "Rand",
        "symbol": "R",
        "unit": "rand",
        "divisibility": 2
    }
}
```

```javascript
{
    "code": "ZAR",
    "description": "Rand",
    "symbol": "R",
    "unit": "rand",
    "divisibility": 2
}
```

```python
{
    "code": "ZAR",
    "description": "Rand",
    "symbol": "R",
    "unit": "rand",
    "divisibility": 2
}
```

Create a currency for a group account configuration.

#### Endpoint

`https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/{config_name}/currencies/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`currency` | Currency code | null

### Retrieve Group Account Configuration Currency

> Admin retrieve group account configuration currency request

```shell
curl https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/{config_name}/currencies/{code}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.accountConfigurations.currencies.get(groupName,configName,{code: 'ZAR'}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.groups.obj({group_name}).account_configurations.obj({config_name})/.
    currencies.get(
        {code}
    )
```

> Admin retrieve group account configuration currency response

```shell
{
    "status": "success",
    "data": {
        "code": "ZAR",
        "description": "Rand",
        "symbol": "R",
        "unit": "rand",
        "divisibility": 2
    }
}
```

```javascript
{
    "code": "ZAR",
    "description": "Rand",
    "symbol": "R",
    "unit": "rand",
    "divisibility": 2
}
```

```python
{
    "code": "ZAR",
    "description": "Rand",
    "symbol": "R",
    "unit": "rand",
    "divisibility": 2
}
```

Retrieve an account's currency belonging to a group account configuration.

#### Endpoint

`https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/{config_name}/currencies/{code}/`

### Delete Account Currency

> Admin retrieve account currency request

```shell
curl https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/{config_name}/currencies/{code}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.groups.accountConfigurations.currencies.delete(groupName,configName,code).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.groups.obj({group_name}).account_configurations.obj({config_name})/.
    currencies.delete(
        {code}
    )
```

> Admin retrieve account currency response

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

Remove a currency from a group account configuration group.

#### Endpoint

`https://api.rehive.com/3/admin/groups/{group_name}/account-configurations/{config_name}/currencies/{code}/`


## Requests

View requests made by users

### Retrieve Requests

> Admin retrieve requests request

```shell
curl https://api.rehive.com/3/admin/requests/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.requests.get().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.requests.get()
```

> Admin retrieve requests response

```shell
{
    "status": "success",
    "data": [
        {
            "id": 11232032,
            "user": [Object],
            "key": null,
            "scheme": 'https',
            "path": '/3/admin/bank-accounts/145/currencies/XBT/',
            "method": 'GET',
            "content_type": 'application/json',
            "params": {},
            "headers": [Object],
            "status_code": 200,
            "archived": false,
            "created": 1527669648572,
            "updated": 1527669648585
        },

        {
            "id": 11231984,
            "user": [Object],
            "key": null,
            "scheme": 'https',
            "path": '/3/admin/bank-accounts/145/currencies/XBT/',
            "method": 'GET',
            "content_type": 'application/json',
            "params": {},
            "headers": [Object],
            "status_code": 200,
            "archived": false,
            "created": 1527669596536,
            "updated": 1527669596546
        }
    ]
}
```

```javascript
 [
    {
        "id": 11232032,
        "user": [Object],
        "key": null,
        "scheme": 'https',
        "path": '/3/admin/bank-accounts/145/currencies/XBT/',
        "method": 'GET',
        "content_type": 'application/json',
        "params": {},
        "headers": [Object],
        "status_code": 200,
        "archived": false,
        "created": 1527669648572,
        "updated": 1527669648585
    },

    {
        "id": 11231984,
        "user": [Object],
        "key": null,
        "scheme": 'https',
        "path": '/3/admin/bank-accounts/145/currencies/XBT/',
        "method": 'GET',
        "content_type": 'application/json',
        "params": {},
        "headers": [Object],
        "status_code": 200,
        "archived": false,
        "created": 1527669596536,
        "updated": 1527669596546
    }
]
```

```python
 [
    {
        "id": 11232032,
        "user": [Object],
        "key": null,
        "scheme": 'https',
        "path": '/3/admin/bank-accounts/145/currencies/XBT/',
        "method": 'GET',
        "content_type": 'application/json',
        "params": {},
        "headers": [Object],
        "status_code": 200,
        "archived": false,
        "created": 1527669648572,
        "updated": 1527669648585
    },

    {
        "id": 11231984,
        "user": [Object],
        "key": null,
        "scheme": 'https',
        "path": '/3/admin/bank-accounts/145/currencies/XBT/',
        "method": 'GET',
        "content_type": 'application/json',
        "params": {},
        "headers": [Object],
        "status_code": 200,
        "archived": false,
        "created": 1527669596536,
        "updated": 1527669596546
    }
]
```

Retrieve admin requests

#### Endpoint

`https://api.rehive.com/3/admin/requests/`

### Retrieve Request

> Admin retrieve request by id request

```shell
curl https://api.rehive.com/3/admin/requests/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.requests.get({id: requestID}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.requests.get(id)
```

> Admin retrieve request by id response

```shell
{
    "status": "success",
    "data":  {
        "id": 11232032,
        "user": [Object],
        "key": null,
        "scheme": 'https',
        "path": '/3/admin/bank-accounts/145/currencies/XBT/',
        "method": 'GET',
        "content_type": 'application/json',
        "params": {},
        "headers": [Object],
        "status_code": 200,
        "archived": false,
        "created": 1527669648572,
        "updated": 1527669648585
    }
}
```

```javascript
 {
    "id": 11232032,
    "user": [Object],
    "key": null,
    "scheme": 'https',
    "path": '/3/admin/bank-accounts/145/currencies/XBT/',
    "method": 'GET',
    "content_type": 'application/json',
    "params": {},
    "headers": [Object],
    "status_code": 200,
    "archived": false,
    "created": 1527669648572,
    "updated": 1527669648585
}
```

```python
  {
    "id": 11232032,
    "user": [Object],
    "key": null,
    "scheme": 'https',
    "path": '/3/admin/bank-accounts/145/currencies/XBT/',
    "method": 'GET',
    "content_type": 'application/json',
    "params": {},
    "headers": [Object],
    "status_code": 200,
    "archived": false,
    "created": 1527669648572,
    "updated": 1527669648585
}
```

Retrieve admin requests

#### Endpoint

`https://api.rehive.com/3/admin/requests/{id}/`