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
        "active": 1
    },
    "status": "success"
}
```

```javascript
{
    "total": 1,
    "active": 1
}
```

```python
{
    "total": 1,
    "active": 1
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

```javascript
{
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

#### Filtering

Field | Type 
--- | --- 
`identifier` | string
`email` | string 
`mobile_number` | string
`first_name` | string
`last_name` | string
`username` | string
`id_number` | string
`language` | string
`nationality` | string
`status` | string
`currency` | string
`date_joined` | millsecond timestamp 
`last_login` | millsecond timestamp 

#### Endpoint

`https://rehive.com/api/3/admin/users/`

### Create User

> Admin create user request

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
formData.append('mobile_number', mobile_number);
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

```javascript
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
    "active": true,
    "password": "*********************************00000000"
}
```

Update a user's details.

#### Endpoint

`https://rehive.com/api/3/admin/users/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`first_name` | first name | blank
`last_name` | last name | blank
`email` | email address | null
`mobile_number` | mobile number | null
`id_number` | ID number | blank
`profile` | profile image | blank
`language` | language code (`af`, `en` etc.) | blank
`nationality` | nationality code (`ZA`, `UK` etc.) | blank
`metadata` | custom metadata | {}
`mobile_number` | mobile number | blank
`timezone` | timezone | blank
`birth_date` | birth date | blank

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

```javascript
rehive.admin.users.get({identifier: identifier}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "active": true,
        "password": "*********************************00000000"
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
    "active": true,
    "password": "*********************************00000000"
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
    "active": true,
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

rehive.admin.users.update(identifier, formData).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "active": true,
        "password": "*********************************00000000"
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
    "active": true,
    "password": "*********************************00000000"
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
    "active": true,
    "password": "*********************************00000000"
}
```

Update a user's details.

#### Endpoint

`https://rehive.com/api/3/admin/users/{identifier}/`

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
`status` | status | pending
`active` | boolean | true

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

```javascript
rehive.admin.users.switches.get(identifier).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.obj('{identifier}').switches.get()
```

> List User Switches response

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

```javascript
{
    [
        {
            "created":1509362224879
            "enabled":false
            "id":47
            "subtype":null
            "tx_type":"credit"
            "updated":1509362224879
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

```javascript
rehive.admin.users.switches.create(identifier,
{
    subtype:null,
    tx_type:"credit",
    enabled:false
}).then(function (res) {
   ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.obj('{identifier}').switches.create(
    switch_type="credit",
    enabled=True
)
```

> Create User Switches response

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

```javascript
{
    "id": 1,
    "tx_type": "credit",
    "subtype": null,
    "enabled": true,
    "created": 1497362397968,
    "updated": 1497362397968
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

`https://rehive.com/api/3/admin/users/{identifier}/switches/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`tx_type` | Transaction Type | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`subtype` | Subtype name | null
`enabled` | Enabled | false

### Retrieve User Switches

Retrieve a specific switch related to a user

> Retrieve User Switches request

```shell
curl https://rehive.com/api/3/admin/users/{identifier}/switches/{id}
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.switches.get(identifier, {id: id}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.obj('{identifier}').switches.get(
    {id}
)
```

> Retrieve User Switches response

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

```javascript
{
    "id": 1,
    "tx_type": "credit",
    "subtype": null,
    "enabled": true,
    "created": 1497362397968,
    "updated": 1497362397968
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

```javascript
rehive.admin.users.switches.update(identifier, id, {
    enabled: true
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.obj('{identifier}').switches.update(
    {id},
    enabled=False
)
```

> Update User Switches response

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

```javascript
{
    "id": 1,
    "tx_type": "credit",
    "subtype": null,
    "enabled": true,
    "created": 1497362397968,
    "updated": 1497362397968
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

#### Required Fields

Field | Description | Default
--- | --- | --- 
`tx_type` | Transaction Type | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`subtype` | Subtype name | null
`enabled` | Enabled | false

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

```javascript
rehive.admin.users.switches.delete(identifier, id).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.users.obj('{identifier}').switches.delete(
    {id}
)
```

> Delete User Switches response

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

`https://rehive.com/api/3/admin/users/{identifier}/switches/{id}`


### List Addresses

> List Addresses request

```shell
curl https://rehive.com/api/3/admin/users/addresses/
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

```javascript
{
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
```

```python
[
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
```

#### Filtering

Field | Type 
--- | --- 
`user` | string
`status` | string

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

```javascript
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
    "line_1": "1 Main Street",
    "line_2": "East City",
    "city": "Cape Town",
    "state_province": "Western Cape",
    "country": "ZA",
    "postal_code": "8001"
    "status": "pending"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/addresses/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`user` | user identifier | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`line_1` | address line one | blank | false
`line_2` | address line 2 | blank | false
`city` | city | blank | false
`state_province` | state or province | blank | false
`country` | country code | blank | false
`postal_code` | postal or zip code) | blank | false
`status` | account status | "pending" | false

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

```javascript
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
    "line_1": "1 Main Street",
    "line_2": "East City",
    "city": "Cape Town",
    "state_province": "Western Cape",
    "country": "ZA",
    "postal_code": "8001"
    "status": "pending"
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

```javascript
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
    "line_1": "1 Main Street",
    "line_2": "East City",
    "city": "Cape Town",
    "state_province": "Western Cape",
    "country": "ZA",
    "postal_code": "8001"
    "status": "pending"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/users/addresses/{id}/`

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`line_1` | address line one | blank | false
`line_2` | address line 2 | blank | false
`city` | city | blank | false
`state_province` | state or province | blank | false
`country` | country code | blank | false
`postal_code` | postal or zip code) | blank | false
`status` | account status | "pending" | false

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

`https://rehive.com/api/3/admin/users/addresses/{id}/`


### List Bank Accounts

> List Bank Accounts request

```shell
curl https://rehive.com/api/3/admin/users/bank-accounts/
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

```javascript
{
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
            "bank_name": "Barclays",
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

```javascript
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
    "bank_name": "Barclays",
    "bank_code": "1234",
    "branch_code": "1234",
    "swift": null,
    "iban": null,
    "bic": null,
    "code": "bank_account_000000000000",
    "status": "pending"
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

#### Required Fields

Field | Description | Default
--- | --- | --- 
`user` | user identifier | null

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

```javascript
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
    "bank_name": "Barclays",
    "bank_code": "1234",
    "branch_code": "1234",
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

```javascript
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
    "bank_name": "Barclays",
    "bank_code": "1234",
    "branch_code": "1234",
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

```javascript
{
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
        "address": "0000000000000000000000000000000000",
        "code": "crypto_account_000000000000",
        "crypto_type": "bitcoin",
        "metadata": {},
        "status": "pending"
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

```javascript
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
    "address": "0000000000000000000000000000000000",
    "code": "crypto_account_000000000000",
    "crypto_type": "bitcoin",
    "metadata": {},
    "status": "pending"
}
```

Create a crypto account for a user.

#### Endpoint

`https://rehive.com/api/3/admin/users/crypto-accounts/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`user` | user identifier | null
`address` | full bitcoin address | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`crypto_type` | string type (bitcoin, ethereum, other) | bitcoin
`metadata` | custom metadata | {}
`status` | string status | 'pending'

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

```javascript
{
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
```

```python
{
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

```javascript
{
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
```

```python
{
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
```

Update a user's crypto account.

#### Endpoint

`https://rehive.com/api/3/admin/users/crypto-accounts/{account_id}/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`user` | user identifier | null
`address` | full bitcoin address | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`crypto_type` | string type (bitcoin, ethereum, other) | bitcoin
`metadata` | custom metadata | {}
`status` | string status | 'pending'

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
                "status": "pending",
                "note": null
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
            "status": "pending",
            "note": null
        }
    ]
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
        "file": "https://url.to/file.pdf",
        "document_category": "other",
        "document_type": "other",
        "metadata": {},
        "status": "pending",
        "note": null
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

`https://www.rehive.com/api/3/admin/users/documents/`


### Create Document

> Admin documents request

```shell
curl https://www.rehive.com/api/3/admin/documents/
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
        "status": "pending",
        "note": null
    }
}
```

```javascript
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
    "status": "pending",
    "note": null
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
    "file": "https://url.to/file.pdf",
    "document_category": "other",
    "document_type": "other",
    "metadata": {},
    "status": "pending",
    "note": null
}
```

Upload user document.

#### Endpoint

`https://rehive.com/api/3/admin/document/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`user` | user identifier | null
`file` | a document file | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`document_category` | The document category | other
`document_type` | The type of docuemnt | other
`metadata` | custom metadata | {}
`status` | document status | pending

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
        "status": "pending",
        "note": null
    }
}
```

```javascript
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
    "status": "pending",
    "note": null
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
    "file": "https://url.to/file.pdf",
    "document_category": "other",
    "document_type": "other",
    "metadata": {},
    "status": "pending",
    "note": null
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
        "status": "verified",
        "note": null
    }
}
```

```javascript
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
    "status": "verified",
    "note": null
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
    "file": "https://url.to/file.pdf",
    "document_category": "other",
    "document_type": "other",
    "metadata": {},
    "status": "verified",
    "note": null
}
```

Update a user's document.

#### Endpoint

`https://rehive.com/api/3/admin/users/documents/{document_id}/`

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

```javascript
{
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
}```

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

#### Filtering

Field | Type 
--- | --- 
`user` | string

#### Endpoint

`https://rehive.com/api/3/admin/users/emails/`

### Create Email

> Admin create email request

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

```javascript
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

#### Required Fields

Field | Description | Default
--- | --- | --- 
`user` | user identifier | null
`email` | email address | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`verified` | verified status | false
`primary` | primary status | false

### Retrieve Email

> Admin retrieve email request

```shell
curl https://www.rehive.com/api/3/admin/users/emails/{id}/
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

```javascript
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

```javascript
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

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`verified` | verified status | false
`primary` | primary status | false

### Delete Email

> Admin delete email request

```shell
curl https://www.rehive.com/api/3/admin/users/emails/{id}/`
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

`https://rehive.com/api/3/admin/users/emails/{id}/`


### List Mobiles

> Admin list mobiles request

```shell
curl https://www.rehive.com/admin/api/3/admin/users/mobiles/
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

```javascript
{
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

#### Filtering

Field | Type 
--- | --- 
`user` | string

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

```javascript
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

#### Required Fields

Field | Description | Default
--- | --- | --- 
`user` | user identifier | null
`mobile` | mobile number | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`verified` | verified status | false
`primary` | primary status | false

### Retrieve Mobile

> Admin retrieve mobile request

```shell
curl https://www.rehive.com/api/3/admin/users/mobiles/{id}/
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

```javascript
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

```javascript
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

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`verified` | verified status | false
`primary` | primary status | false


### Delete Mobile

> Admin delete mobile request

```shell
curl https://www.rehive.com/api/3/admin/users/mobiles/{id}/`
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
`metadata` | any

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

```javascript
rehive.admin.transactions.getTotals().then(function (res) {
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

`https://rehive.com/api/3/admin/transactions/totals/`

### Retrieve Transaction

> Retrieve transaction request

```shell
curl https://www.rehive.com/api/3/admin/transactions/{id}/
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

```javascript
rehive.admin.transactions.createCredit(
{
    user: "joe@rehive.com",
    amount: 500
}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "id": "00000000000000000000"
    }
}
```

```javascript
{
    "id": "00000000000000000000"
}
```

```python
{
    "id": "00000000000000000000"
}
```

Create a credit transaction on behalf of a user.

#### Endpoint

`https://rehive.com/api/3/admin/transactions/credit/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`user` | email, mobile number, or unique identifier | null
`amount` | amount | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`reference` | optional credit reference | blank
`subtype` | a custom defined subtype | null
`account` | account reference code | null
`note` | user's note or message | blank
`currency` | currency code | blank
`metadata` | custom metadata | {}
`status` | status to transition to | Pending

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

```javascript
rehive.admin.transactions.createDebit(
{
    user: "joe@rehive.com",
    amount: 500
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.transactions.create_debit(
    user="joe@rehive.com",
    amount=500
)
```

> Admin debit response

```shell
{
    "status": "success",
    "data": {
        "id": "00000000000000000000"
    }
}
```

```javascript
{
    "id": "00000000000000000000"
}
```

```python
{
    "id": "00000000000000000000"
}
```

Create a debit transaction on behalf of a user.

#### Endpoint

`https://rehive.com/api/3/admin/transactions/debit/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`user` | email, mobile number, or unique identifier | null
`amount` | amount | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`reference` | optional debit reference | blank
`subtype` | a custom defined subtype | null
`account` | account reference code | null
`note` | user's note or message | blank
`currency` | currency code | blank
`metadata` | custom metadata | {}
`status` | status to transition to | Pending

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

```javascript
rehive.admin.transactions.createTransfer(
{
    user: "joe@rehive.com",
    amount: 500,
    recipient: "sally@rehive.com"
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
    recipient="sally@rehive.com"
)
```

> Admin transfer response

```shell
{
    "status": "success",
    "data": {
        "id": "00000000000000000000"
    }
}
```

```javascript
{
    "id": "00000000000000000000"
}
```

```python
{
    "id": "00000000000000000000"
}
```

Create a transfer transaction on behalf of a user. This will transfer currency from one user to another. If the recipient reference does not exist as a user in Rehive and the reference is an email address or mobile number then an invitation message will be sent to the recipient informing them they have an unclaimed transaction.

#### Endpoint

`https://rehive.com/api/3/admin/transactions/transfer/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`user` | email, mobile number, or unique identifier | null
`amount` | amount | null
`recipient` | email, mobile number, or unique identifier | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`currency` | currency code | blank
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


### Update Transaction

> Admin update transaction request

```shell
curl https://rehive.com/api/3/admin/transactions/{id}/
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

#### Required Fields

Field | Description | Default
--- | --- | --- 
`status` | update action/status (`Pending`, `Complete`, `Failed`, `Deleted`) | null | true

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`metadata` | custom metadata | {}
`message` | message object | {}


#### Endpoint

`https://rehive.com/api/3/admin/transactions/webhooks/{id}/`


### List Transaction Switches

List all switches related to transactions.

> List transaction switches request

```shell
curl https://rehive.com/api/3/admin/transactions/switches/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.transactions.switches.get().then(function (res) {
    ...
}, function (err) {
    ...
});
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

```javascript
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

```javascript
rehive.admin.transactions.switches.create({
    tx_type: "credit",
    enabled: true
}).then(function (res) {
    ...
}, function (err) {
    ...
});
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

```javascript
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

`https://rehive.com/api/3/admin/transactions/switches/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`tx_type` | Transaction Type | 
`enabled` | Enabled | false 

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`subtype` | Subtype name | null

### Retrieve Transaction Switches

Retrieve a specific switch related to transactions.

> Retrieve transaction switches request

```shell
curl https://rehive.com/api/3/admin/transactions/switches/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.transactions.switches.get({id: id}).then(function (res) {
    ...
}, function (err) {
    ...
});
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

```javascript
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

```javascript
rehive.admin.transactions.switches.update(id, {enabled: false}).then(function (res) {
    ...
}, function (err) {
    ...
});
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

```javascript
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

`https://rehive.com/api/3/admin/transactions/switches/{id}/`



## Accounts

### List Accounts

> Admin list accounts request

```shell
curl https://www.rehive.com/api/3/admin/accounts/
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
                            "symbol": "???",
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
            "user": "joe@rehive.com",
            "currencies": [
                {
                    "balance": 10000,
                    "available_balance": 10000,
                    "currency": {
                        "code": "XBT",
                        "description": "bitcoin",
                        "symbol": "???",
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
        "user": "joe@rehive.com",
        "currencies": [
            {
                "balance": 10000,
                "available_balance": 10000,
                "currency": {
                    "code": "XBT",
                    "description": "bitcoin",
                    "symbol": "???",
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

#### Filtering

Field | Type 
--- | --- 
`reference` | string
`name` | string
`active` | boolean 
`primary` | boolean
`user` | string

#### Endpoint

`https://rehive.com/api/3/admin/accounts/`

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
    "created": 1501145581365,
    "updated": 1501145581370
}
```

Create a account for a user.

#### Endpoint

`https://rehive.com/api/3/admin/accounts/`

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

### Retrieve Account

> Admin retrieve account request

```shell
curl https://www.rehive.com/api/3/admin/accounts/{reference}/
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
                    "symbol": "???",
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
    "user": "joe@rehive.com",
    "currencies": [
        {
            "balance": 10000,
            "available_balance": 10000,
            "currency": {
                "code": "XBT",
                "description": "bitcoin",
                "symbol": "???",
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
    "user": "joe@rehive.com",
    "currencies": [
        {
            "balance": 10000,
            "available_balance": 10000,
            "currency": {
                "code": "XBT",
                "description": "bitcoin",
                "symbol": "???",
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

Field | Type 
--- | --- 
`active` | boolean 

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
    "created": 1501145581365,
    "updated": 1501145581370
}
```

Update an account for a user.

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/`

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


### List Account Currencies

> Admin list account currencies request

```shell
curl https://www.rehive.com/admin/api/3/accounts/{reference}/currencies/
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
                "currency": {
                    "code": "XBT",
                    "description": "bitcoin",
                    "symbol": "???",
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
                "symbol": "???",
                "unit": "bitcoin",
                "divisibility": 8
            },
            "active": true
        }
    ]
}
```

```python
[
    {
        "balance": 10000,
        "currency": {
            "code": "XBT",
            "description": "bitcoin",
            "symbol": "???",
            "unit": "bitcoin",
            "divisibility": 8
        },
        "active": true
    }
]
```

Get a list of currencies for an account belonging to a company.

#### Filtering

Field | Type 
--- | --- 
`active` | boolean 

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
        "currency": {
            "code": "XBT",
            "description": "bitcoin",
            "symbol": "???",
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
        "symbol": "???",
        "unit": "bitcoin",
        "divisibility": 8
    },
    "active": true
}
```

```python
{
    "balance": 10000,
    "currency": {
        "code": "XBT",
        "description": "bitcoin",
        "symbol": "???",
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
        "currency": {
            "code": "XBT",
            "description": "bitcoin",
            "symbol": "???",
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
        "symbol": "???",
        "unit": "bitcoin",
        "divisibility": 8
    },
    "active": true
}
```

```python
{
    "balance": 10000,
    "currency": {
        "code": "XBT",
        "description": "bitcoin",
        "symbol": "???",
        "unit": "bitcoin",
        "divisibility": 8
    },
    "active": true
}
```

Update the active status of an account currency. Activating an account's currency will result in that currency getting used by default for all transactions if no other account/currency is specified.

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/`

#### Optional Fields

Field | Description | Default
--- | --- | --- 
`active` | is active currency | false

### List Account Currency Limits

List all Limits related to am account currency.

> List Account Currency request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/
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
    "created": 1497428787920,
    "updated": 1497428787921
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/`

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
    "created": 1497428787920,
    "updated": 1497429648948
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/limits/{limit_id}/`

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
    "created": 1497431721587,
    "updated": 1497431721587
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/`

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
    "created": 1497431721587,
    "updated": 1497431938971
}
```

#### Endpoint

`https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/fees/{fee_id}/`

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

```javascript
rehive.admin.accounts.currencies.switches.get(reference, code).then(function (res) {
    ...
}, function (err) {
    ...
});
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

```javascript
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

```javascript
rehive.admin.accounts.currencies.switches.create(reference, code, {
    tx_type: "credit"
    enabled: true
}).then(function (res) {
    ...
}, function (err) {
    ...
});
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

```javascript
{
    "id": 1,
    "tx_type": "credit",
    "subtype": null,
    "enabled": true,
    "created": 1497362397968,
    "updated": 1497362397968
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

#### Required Fields

Field | Description | Default
--- | --- | --- 
`tx_type` | Transaction Type | 
`enabled` | Enabled | false

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`subtype` | Subtype name | null

### Retrieve Account Currency Switches

Retrieve a specific switch related to the currency

> Retrieve Account Currency Switches request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.accounts.currencies.switches.get(reference, code, {id: id}).then(function (res) {
    ...
}, function (err) {
    ...
});
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

```javascript
{
    "id": 1,
    "tx_type": "credit",
    "subtype": null,
    "enabled": true,
    "created": 1497362397968,
    "updated": 1497362397968
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

```javascript
rehive.admin.accounts.currencies.switches.update(reference, code, id, {enabled: false}).then(function (res) {
    ...
}, function (err) {
    ...
});
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

```javascript
{
    "id": 1,
    "tx_type": "credit",
    "subtype": null,
    "enabled": false,
    "created": 1497362397968,
    "updated": 1497362931403
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

#### Required Fields

Field | Description | Default
--- | --- | --- 
`tx_type` | Transaction Type | 
`enabled` | Enabled | false

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`subtype` | Subtype name | null

### Delete Account Currency Switches

Delete a specific switch related to the currency.

> Delete Account Currency Switches request

```shell
curl https://rehive.com/api/3/admin/accounts/{reference}/currencies/{code}/switches/{id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.accounts.currencies.switches.delete(reference, code, id).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.accounts.obj("{reference}").currencies.obj("{code}").switches.delete(
    "{id}"
)
```

> Delete Account Currency Switches response

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
                "symbol": "???",
                "unit": "bitcoin",
                "divisibility": 8,
                "enabled": true
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
            "symbol": "???",
            "unit": "bitcoin",
            "divisibility": 8,
            "enabled": true
        }
    ]
}
```

```python
[
    {
        "code": "XBT",
        "description": "bitcoin",
        "symbol": "???",
        "unit": "bitcoin",
        "divisibility": 8,
        "enabled": true
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
        "symbol": "???",
        "unit": "bitcoin",
        "divisibility": 8}'
```

```javascript
rehive.admin.currencies.create(
{
    code: "XBT",
    description: "bitcoin",
    symbol: "???",
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
    symbol="???",
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
        "symbol": "???",
        "unit": "bitcoin",
        "divisibility": 8,
        "enabled": false
    }
}
```

```javascript
{
    "code": "XBT",
    "description": "bitcoin",
    "symbol": "???",
    "unit": "bitcoin",
    "divisibility": 8,
    "enabled": false
}
```

```python
{
    "code": "XBT",
    "description": "bitcoin",
    "symbol": "???",
    "unit": "bitcoin",
    "divisibility": 8,
    "enabled": false
}
```

Create a custom currency. This currency will be unique to the company that created it.

#### Endpoint

`https://rehive.com/api/3/admin/currencies/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`code` | currency code | null
`description` | name of currency | null
`symbol` | currency symbol | null
`unit` | unit, like `dollar` | null
`divisibility` | number of decimal places | 0


### Retrieve Currency

> Admin retrieve currency request

```shell
curl https://www.rehive.com/api/3/admin/currencies/{code}/
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
        "symbol": "???",
        "unit": "bitcoin",
        "divisibility": 8,
        "enabled": true
    }
}
```

```javascript
{
    "code": "XBT",
    "description": "bitcoin",
    "symbol": "???",
    "unit": "bitcoin",
    "divisibility": 8,
    "enabled": true
}
```

```python
{
    "code": "XBT",
    "description": "bitcoin",
    "symbol": "???",
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

```javascript
rehive.admin.currencies.update(code, {enabled: true}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "symbol": "???",
        "unit": "bitcoin",
        "divisibility": 8,
        "enabled": true
    }
}
```

```javascript
{
    "code": "XBT",
    "description": "bitcoin",
    "symbol": "???",
    "unit": "bitcoin",
    "divisibility": 8,
    "enabled": true
}
```

```python
{
    "code": "XBT",
    "description": "bitcoin",
    "symbol": "???",
    "unit": "bitcoin",
    "divisibility": 8,
    "enabled": true
}
```

This endpoint can be used to enable an existing currency or if it is a custom currency, edit its details.

<aside class="notice">
Note that default currencies can not be updated, and only custom currencies can be updated.
</aside>

#### Endpoint

`https://rehive.com/api/3/admin/currencies/{code}/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`code` | currency code | null
`description` | name of currency | null
`symbol` | currency symbol | null
`unit` | unit, like `dollar` | null
`divisibility` | number of decimal places | 0
`enabled` | whether active for a company | false

### Delete Currency

> Admin delete currency request

```shell
curl https://www.rehive.com/api/3/admin/currencies/{code}/
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

This endpoint can be used to delete custom currencies that was created.

#### Endpoint

`https://rehive.com/api/3/admin/currencies/{code}/`

### Currency Overview

> Admin currency overview request

```shell
curl https://www.rehive.com/api/3/admin/currencies/{code}/overview/
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

`https://rehive.com/api/3/admin/currencies/{code}/overview/`

## Company

### Retrieve Company

> View the company info

```shell
curl https://rehive.com/api/3/admin/company/
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
        "identifier": "test_company",
        "name": "Test Company 1",
        "description": "A Test Company.",
        "website": "http://www.test_company.com",
        "logo": "https://www.test_company.com/logo.jpg",
        "password_reset_url": null,
        "email_confirmation_url": null,
        "default_currency": "XBT",
        "nationalities": [],
        "address": {
            // ...
        },
        "switches": []
    }
}
```

```javascript
{
    "identifier": "test_company",
    "name": "Test Company 1",
    "description": "A Test Company.",
    "website": "http://www.test_company.com",
    "logo": "https://www.test_company.com/logo.jpg",
    "password_reset_url": null,
    "email_confirmation_url": null,
    "default_currency": "XBT",
    "nationalities": [],
    "address": {
        // ...
    },
    "switches": []
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
    "nationalities": [],
    "address": {
        # ...
    },
    "switches": []
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
        "identifier": "test_company",
        "name": "Test Company 1",
        "description": "A new description",
        "website": "http://www.test_company.com",
        "logo": "https://www.test_company.com/logo.jpg",
        "password_reset_url": null,
        "email_confirmation_url": null,
        "default_currency": "XBT",
        "nationalities": [],
        "address": {
            // ...
        },
        "switches": []
    }
}
```

```javascript
{
    "identifier": "test_company",
    "name": "Test Company 1",
    "description": "A Test Company.",
    "website": "http://www.test_company.com",
    "logo": "https://www.test_company.com/logo.jpg",
    "password_reset_url": null,
    "email_confirmation_url": null,
    "default_currency": "XBT",
    "nationalities": [],
    "address": {
        // ...
    },
    "switches": []
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
    "default_currency": "XBT",
    "nationalities": [],
    "address": {
        // ...
    },
    "switches": []
}
```

Retrieve the company info.

#### Endpoint

`https://rehive.com/api/3/admin/company/`

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`name` | Company Name | blank
`description` | Company Description | blank
`website` | Company website URL | blank
`logo` | Company logo URL | blank
`nationalities` | List of accepted nationalities | blank
`password_reset_url` | Custom company password reset URL | blank
`email_confirmation_url` | Custom company email confirmation URL | blank
`default_currency` | Default company currency | null

<aside class="notice">
When adding a logo image, the Content-type header needs to be set to multipart/form-data.
</aside>

## Bank Accounts

### List Bank Accounts

> List Bank Accounts request

```shell
curl https://rehive.com/api/3/admin/bank-accounts/
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
    "data": [
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
    }
]
```

#### Filtering

Field | Type 
--- | --- 
`user` | string
`status` | string

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
}
```

#### Endpoint

`https://rehive.com/api/3/admin/bank-accounts/`

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

### Retrieve Bank Account

> Retrieve Bank Account request

```shell
curl https://rehive.com/api/3/admin/bank-accounts/{id}/
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
}
```

#### Endpoint

`https://rehive.com/api/3/admin/bank-accounts/{id}/`

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


### Delete Bank Account

> Delete Bank Account request

```shell
curl https://rehive.com/api/3/admin/bank-accounts/{id}/
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
                "secret": "secret"

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
            "secret": "secret"

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
        "secret": "secret"
    }
]
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
        "secret": "secret"
    }
}
```

```javascript
{
    "id": 1,
    "url": "http://mysite.com/webhook_endpoint",
    "event": "user.create",
    "condition": null,
    "secret": "secret"
}
```

```python
{
    "id": 1,
    "url": "http://mysite.com/webhook_endpoint",
    "event": "user.create",
    "condition": null,
    "secret": "secret"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/webhooks/`

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
curl https://rehive.com/api/3/admin/webhooks/{id}/
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
        "secret": "secret"
    }
}
```

```javascript
 {
    "id": 1,
    "url": "http://mysite.com/webhook_endpoint",
    "event": "user.create",
    "secret": "secret"
}
```

```python
{
    "id": 1,
    "url": "http://mysite.com/webhook_endpoint",
    "event": "user.create",
    "condition": null,
    "secret": "secret"
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
            "secret": "secret"
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
    "secret": "secret"
}
```

```python
{
    "id": 1,
    "url": "http://mysite.com/webhook_endpoint",
    "event": "user.create",
    "condition": null,
    "secret": "secret"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/webhooks/{id}/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`url` | Webhook URL | blank
`event` | Webhook event | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`secret` | Webhook secret | "secret"

### Delete Webhook

> Delete webhook request

```shell
curl https://rehive.com/api/3/admin/webhooks/{id}/
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

`https://rehive.com/api/3/admin/webhooks/{id}/`


### List Webhook Tasks

> List webhook tasks request

```shell
curl https://rehive.com/api/3/admin/webhook-tasks/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
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
                "created": 1511546662487,
                "updated": 1511546662774          
            }
        ]
    }
}
```

#### Filtering

Field | Type 
--- | --- 
`webhook` | string
`webhook__event` | string 
`webhook__secret` | string

#### Endpoint

`https://rehive.com/api/3/admin/webhook-tasks/`

### Retrieve Webhook Task

> Retrieve webhook task request

```shell
curl https://rehive.com/api/3/admin/webhook-tasks/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
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
        "created": 1511546662487,
        "updated": 1511546662774          
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/webhook-task/{id}/`


### List Webhook Task Requests

> List webhook task requests request

```shell
curl https://rehive.com/api/3/admin/webhook-tasks/{id}/requests/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
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
                "created": 1511546662778
            }
        ]
    }
}
```

#### Filtering

Field | Type 
--- | --- 
`response_code` | string

#### Endpoint

`https://rehive.com/api/3/admin/webhook-tasks/{id}/requests/`

### Retrieve Webhook Task Request

> Retrieve webhook task request request

```shell
curl https://rehive.com/api/3/admin/webhook-tasks/{id}/requests/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Retrieve webhook task request response

```shell
{
    "status": "success",
    "data": {
        "id": 1,
        "response_code": 200,
        "error": null,
        "created": 1511546662778
    }
}
```

#### Endpoint

`https://rehive.com/api/3/admin/webhook-task/{id}/requests/{id}/`


## Subtypes

### List Subtypes

> List subtypes request

```shell
curl https://rehive.com/api/3/admin/subtypes/
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
            "enabled": true,
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
        "enabled": true,
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

```javascript
rehive.admin.subtypes.create(
{
    name: "credit_subtype",
    label: "Our credit",
    description: "Description for our credit",
    tx_type:"credit",
    enabled: true
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

```javascript
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
`enabled` | enabled status | true

### Retrieve Subtypes

> Retrieve subtypes request

```shell
curl https://rehive.com/api/3/admin/subtypes/{id}/
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
    "created": 1509529290352,
    "updated": 1509529290352
}
```

#### Endpoint

`https://rehive.com/api/3/admin/subtypes/{id}/`

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
`enabled` | enabled status | true

### Delete Subtype

> Delete subtype request

```shell
curl https://rehive.com/api/3/admin/subtypes/{id}/
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

`https://rehive.com/api/3/admin/notifications/`

### Retrieve Notifications

> Retrieve Notifications request

```shell
curl https://rehive.com/api/3/admin/notifications/{id}/
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

`https://rehive.com/api/3/admin/notifications/{id}`

#### Required Fields

Field | Description | Default
--- | --- | ---
`enabled` | Account Name | false

## Tiers

Tiers are a way in which to categorise users based on requirements for the tier.
Tiers are set on a currency to limit users' transactions on that currency.

Tiers are checked in ascending order based on their level, with the user getting
validation corresponding to the highest tier they matched. 

### List Tiers

List all tiers.

> List Tier request

```shell
curl https://rehive.com/api/3/admin/tiers/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.tiers.get().then(function (res) {
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
            "switches": [],
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
        "switches": [],
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
        "switches": [],
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

`https://rehive.com/api/3/admin/tiers/`

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

```javascript
rehive.admin.tiers.create(
{
    currency: "XBT",
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
    "switches": [],
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
    "switches": [],
    "created": 1497367640298,
    "updated": 1497367640298
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/`

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

### Retrieve Tier

Retrieve a specific tier.

> Retrieve Tier request

```shell
curl https://rehive.com/api/3/admin/tiers/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.tiers.get({id: id}).then(function (res) {
    ...
}, function (error) {
    ...
})
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
    "switches": [],
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
    "switches": [],
    "created": 1497367640298,
    "updated": 1497367640298
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{id}/`

### Update Tier

Update the name of description of a tier.

> Update Tier request

```shell
curl https://rehive.com/api/3/admin/tiers/{id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "Updated Name"}'
```

```javascript
rehive.admin.tiers.update(tierId, data).then(function (res) {
    ...
}, function (error) {
    ...
})
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
    "switches": [],
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
    "switches": [],
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


#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/`

### Delete Tier

Delete a specific tier.

> Delete Tier request

```shell
curl https://rehive.com/api/3/admin/tiers/{id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.tiers.delete(tierId).then(function (res) {
    ...
}, function (error) {
    ...
})
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

`https://rehive.com/api/3/admin/tiers/{id}/`

### List Tier Requirements

List all requirements related to a tier.

> List Tier Requirements request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.tiers.requirements.get(tierId).then(function (res) {
    ...
}, function (error) {
    ...
})
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
            "token_tier_id": 1,
            "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
            "requirement": "First Name"
        }
    ]
}
```

```javascript
[
    {
        "id": 1,
        "token_tier_id": 1,
        "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
        "requirement": "First Name"
    }
]
```

```python
[
    {
        "id": 1,
        "token_tier_id": 1,
        "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
        "requirement": "First Name"
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

```javascript
rehive.admin.tiers.requirements.create(tierId, {
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
        "id": 3,
        "token_tier_id": 1,
        "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
        "requirement": "Birth Date"
    }
}
```

```javascript
{
    "id": 3,
    "token_tier_id": 1,
    "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
    "requirement": "Birth Date"
}
```

```python
{
    "id": 3,
    "token_tier_id": 1,
    "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
    "requirement": "Birth Date"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/`

#### Required Fields

Field | Description | Default 
--- | --- | --- 
`requirement` | Requirement Type | 

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

### Retrieve Tier Requirements

Retrieve a specific requirement related to a Tier

> Retrieve Tier Requirements request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/{requirement_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.tiers.requirements.get(tierId,{id: requirementId}).then(function (res) {
    ...
}, function (error) {
    ...
})
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
        "token_tier_id": 1,
        "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
        "requirement": "Birth Date"
    }
}
```

```javascript
{
    "id": 3,
    "token_tier_id": 1,
    "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
    "requirement": "Birth Date"
}
```

```python
{
    "id": 3,
    "token_tier_id": 1,
    "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
    "requirement": "Birth Date"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/{requirement_id}/`

### Update Tier Requirements

Update a specific requirement related to a Tier

> Update Tier Requirements request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/{requirement_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"requirement": "proof_of_identity"}'
```

```javascript
rehive.admin.tiers.requirements.update(tierId, requirementId, {requirement: "proof_of_identity"}).then(function (res) {
    ...
}, function (error) {
    ...
})
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
        "token_tier_id": 1,
        "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
        "requirement": "Proof Of Identity"
    }
}
```

```javascript
{
    "id": 3,
    "token_tier_id": 1,
    "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
    "requirement": "Proof Of Identity"
}
```

```python
{
    "id": 3,
    "token_tier_id": 1,
    "token_tier": "Tier-1 Updated Name (ZAR_test_company_1)",
    "requirement": "Proof Of Identity"
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/{requirement_id}/`

#### Required Fields

Field | Description | Default 
--- | --- | --- 
`requirement` | Requirement Type | 

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

### Delete Tier Requirements

Delete a specific requirement related to a Tier

> Delete Tier Requirements request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/{requirement_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.tiers.requirements.delete(tierId,requirementId).then(function (res) {
    ...
}, function (error) {
    ...
})
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

`https://rehive.com/api/3/admin/tiers/{tier_id}/requirements/{requirement_id}/`

### List Tier Limits

List all Limits related to a tier.

> List Tier Limits request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/limits/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.tiers.limits.get(tierId).then(function (res) {
    ...
}, function (error) {
    ...
})
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

```javascript
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

```javascript
rehive.admin.tiers.limits.create(tierId, {
    value: 1000,
    type: "Maximum",
    tx_type: "credit"
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
        "created": 1497374071027,
        "updated": 1497374071027
    }
}
```

```javascript
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
curl https://rehive.com/api/3/admin/tiers/{tier_id}/limits/{limit_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.tiers.limits.get(tierId, {id: limitId}).then(function (res) {
    ...
}, function (error) {
    ...
})
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

```javascript
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

`https://rehive.com/api/3/admin/tiers/{tier_id}/limits/{limit_id}/`

### Update Tier Limits

Update a specific limits related to a Tier

> Update Tier Limits request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/limits/{limit_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 5000,
       "type": "min"}'
```

```javascript
rehive.admin.tiers.limits.update(tierId, limitId,{
    value: 5000,
    type: "min"
}).then(function (res) {
    ...
}, function (error) {
    ...
})
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

```javascript
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

`https://rehive.com/api/3/admin/tiers/{tier_id}/limits/{limit_id}/`

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
curl https://rehive.com/api/3/admin/tiers/{tier_id}/limits/{limit_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.tiers.limits.delete(tierId, limitId).then(function (res) {
    ...
}, function (error) {
    ...
})
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

`https://rehive.com/api/3/admin/tiers/{tier_id}/limits/{limit_id}/`

### List Tier Fees

List all fees related to a Tier.

> List Tier Fees request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/fees/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.tiers.fees.get(tierId).then(function (res) {
    ...
}, function (error) {
    ...
})
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

```javascript
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

```javascript
rehive.admin.tiers.fees.create(tierId, {
    value: 1000,
    tx_type: "credit"
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
        "subtype": null,
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
    "created": 1497431721587,
    "updated": 1497431721587
}
```

#### Endpoint

`https://rehive.com/api/3/admin/tiers/{tier_id}/fees/`

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

#### Transaction Types

Value | Description 
--- | --- 
`credit` | Credit 
`debit` | Debit

### Retrieve Tier fee

Retrieve a specific requirement related to a Tier.

> Retrieve Tier Fee request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/fees/{fee_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.tiers.fees.get(tierId, {id: feeId}).then(function (res) {
    ...
}, function (error) {
    ...
})
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

```javascript
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

`https://rehive.com/api/3/admin/tiers/{tier_id}/fees/{fee_id}/`

### Update Tier Fee

Update a specific fees related to a Tier.

> Update Tier request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/fees/{fee_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"value": 5000}'
```

```javascript
rehive.admin.tiers.fees.update(tierId, feeId,{value: 5000}).then(function (res) {
    ...
}, function (error) {
    ...
})
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

```javascript
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

`https://rehive.com/api/3/admin/tiers/{tier_id}/fees/{fee_id}/`

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

#### Transaction Types

Value | Description 
--- | --- 
`credit` | Credit 
`debit` | Debit

### Delete Tier fee

Delete a specific requirement related to a Tier.

> Delete Tier Fee request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/fees/{fee_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.tiers.fees.delete(tierId, feeId).then(function (res) {
    ...
}, function (error) {
    ...
})
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

`https://rehive.com/api/3/admin/tiers/{tier_id}/fees/{fee_id}/`

### List Tier Switches

List all switches related to a tier.

> List Tier Switches request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/switches/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.tiers.switches.get(tierId).then(function (res) {
    ...
}, function (error) {
    ...
})
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

```javascript
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

```javascript
rehive.admin.tiers.switches.create(tierId, {
    tx_type: "credit",
    enabled: true
}).then(function (res) {
    ...
}, function (err) {
    ...
})
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

```javascript
{
    "id": 1,
    "tx_type": "credit",
    "subtype": null,
    "enabled": true,
    "created": 1497370313086,
    "updated": 1497370313086
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

#### Required Fields

Field | Description | Default
--- | --- | --- 
`tx_type` | Transaction Type | 
`enabled` | Enabled | false

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`subtype` | Subtype name | null

#### Transaction Types

Value | Description 
--- | --- 
`credit` | Credit 
`debit` | Debit

### Retrieve Tier Switches

Retrieve a specific switch related to a Tier

> Retrieve Tier Switches request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/switches/{switch_id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.tiers.switches.get(tierId, {id: switchId}).then(function (res) {
    ...
}, function (error) {
    ...
})
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

```javascript
{
    "id": 1,
    "tx_type": "credit",
    "subtype": null,
    "enabled": true,
    "created": 1497370313086,
    "updated": 1497370313086
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

`https://rehive.com/api/3/admin/tiers/{tier_id}/switches/{switch_id}/`

### Update Tier Switches

Update a specific switch related to a Tier

> Update Tier Switches request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/switches/{switch_id}/
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"enabled": false}'
```

```javascript
rehive.admin.tiers.switches.update(tierId, switchId,{enabled: false}).then(function (res) {
    ...
}, function (error) {
    ...
})
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

```javascript
{
    "id": 1,
    "tx_type": "credit",
    "subtype": null,
    "enabled": true,
    "created": 1497370313086,
    "updated": 1497370313086
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

`https://rehive.com/api/3/admin/tiers/{tier_id}/switches/{switch_id}/`

### Delete Tier Switches

Delete a specific switch related to a Tier

> Delete Tier Switches request

```shell
curl https://rehive.com/api/3/admin/tiers/{tier_id}/switches/{switch_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.tiers.switches.delete(tierId, switchId).then(function (res) {
    ...
}, function (error) {
    ...
})
```

```python
rehive.admin.tiers.obj({tier_id}).switches.delete(
   {switch_id} 
)
```

> Delete Tier Switches response

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

`https://rehive.com/api/3/admin/tiers/{tier_id}/switches/{switch_id}/`

## Switches

Switches are a way to determine which actions are allowed to the users in terms of transactions.

Global switches are the highest level switches by overriding any switches that are
set on a user, company, currency or tier level.

### List Global Switches

List all the global switches.

> List Global Switches request

```shell
curl https://rehive.com/api/3/admin/switches/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.switches.get().then(function (res) {
    ...
}, function (err) {
    ...
});
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
            "switch_type": "Allow transactions",
            "enabled": true,
            "created": 1497347723605,
            "updated": 1497347723605
        }
    ]
}
```

```javascript
[
    {
        "id": 1,
        "switch_type": "Allow transactions",
        "enabled": true,
        "created": 1497347723605,
        "updated": 1497347723605
    }
]
```

```python
[
    {
        "id": 1,
        "switch_type": "Allow transactions",
        "enabled": true,
        "created": 1497347723605,
        "updated": 1497347723605
    }
]
```

#### Endpoint

`https://rehive.com/api/3/admin/switches/`

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

```javascript
rehive.admin.switches.create(
{
    switch_type: "transactions",
    enabled: false
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.switches.create(
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
        "switch_type": "Allow transactions",
        "enabled": false,
        "created": 1497348308625,
        "updated": 1497348318654
    }
}
```

```javascript
{
    "id": 1,
    "switch_type": "Allow transactions",
    "enabled": false,
    "created": 1497348308625,
    "updated": 1497348318654
}
```

```python
{
    "id": 1,
    "switch_type": "Allow transactions",
    "enabled": false,
    "created": 1497348308625,
    "updated": 1497348318654
}
```

#### Endpoint

`https://rehive.com/api/3/admin/switches/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`enabled` | Account Name | false
`switch_type` | Global Switch Type Label | 

#### Types
Global switches can be one of the following types.

Value | Description
--- | ---
`transactions` | Allow transactions
`verification` | Allow transactions for unverified users
`overdraft` | Allow unlimited overdrafts
`auto_confirm` | Automatically complete transactions on creation
`manage_accounts` | Allow users to manage their accounts
`session_duration` | Allow users to set their own session duration

### Retrieve Global Switches

Retrieve a specific global switch.

> Retrieve Global Switches request

```shell
curl https://rehive.com/api/3/admin/switches/{id}/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.switches.get({id: id}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "switch_type": "Allow transactions",
        "enabled": true,
        "created": 1497347723605,
        "updated": 1497347723605
    }
}
```

```javascript
{
    "id": 1,
    "switch_type": "Allow transactions",
    "enabled": true,
    "created": 1497347723605,
    "updated": 1497347723605
}
```

```python
{
    "id": 1,
    "switch_type": "Allow transactions",
    "enabled": true,
    "created": 1497347723605,
    "updated": 1497347723605
}
```

#### Endpoint

`https://rehive.com/api/3/admin/switches/{id}/`

### Update Global Switches

Update a specific global switch.

> Update Global Switches request

```shell
curl https://rehive.com/api/3/admin/switches/{id}/
  -X PUT
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"enabled": false}'
```

```javascript
rehive.admin.switches.update(id, {enabled: false}).then(function (res) {
    ...
}, function (err) {
    ...
});
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
        "switch_type": "Allow transactions",
        "enabled": false,
        "created": 1497348308625,
        "updated": 1497348318654
    }
}
```

```javascript
{
    "id": 1,
    "switch_type": "Allow transactions",
    "enabled": false,
    "created": 1497348308625,
    "updated": 1497348318654
}
```

```python
{
    "id": 1,
    "switch_type": "Allow transactions",
    "enabled": false,
    "created": 1497348308625,
    "updated": 1497348318654
}
```

#### Endpoint

`https://rehive.com/api/3/admin/switches/{id}/`

#### Optional Fields

Field | Description | Default
--- | --- | ---
`switch_type` | Global Switch Type | 
`enabled` | Account Name | false

#### Types
Global switches can be one of the following types.

Value | Description
--- | ---
`transactions` | Allow transactions
`verification` | Allow transactions for unverified users
`overdraft` | Allow unlimited overdrafts
`auto_confirm` | Automatically complete transactions on creation
`manage_accounts` | Allow users to manage their accounts
`session_duration` | Allow users to set their own session duration

### Delete Global Switches

Delete a specific global switch.

> Delete Global Switches request

```shell
curl https://rehive.com/api/3/admin/switches/{id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.switches.delete(id).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.switches.delete(
    {id}
)
```

> Delete Global Switches response

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

`https://rehive.com/api/3/admin/switches/{id}/`

## Permissions

#### Permission Groups
Rehive includes fine-grained permission management system, that allows admin users to create permission groups as well as individually manage users' permissions to view, add, edit or delete data from the system via admin endpoints.

#### Users and Permissions
Users can either be assigned permission groups, or permissions directly. When assigning permission groups to a user, the user will have the access specified in the permission assigned to the permission group. Individual permissions can be assigned to user if some additional permission only need to be provided to a specific user.

### List permission groups

> Admin list permission groups request

```shell
curl https://www.rehive.com/api/3/admin/permission-groups/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.permissionGroups.get().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.permission_groups.get()
```

> Admin list permission groups response

```shell
{
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "name": "test_group",
                "permissions": []
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
            "name": "test_group",
            "permissions": []
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
            "name": "test_group",
            "permissions": []
        }
    ]
}
```

Get a list of permission groups that have been created with the associated permissions.

#### Pagination

The list is paginated and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

#### Endpoint

`https://rehive.com/api/3/admin/permission-groups/`

### Create permission groups

> Admin create permission groups request

```shell
curl https://www.rehive.com/api/3/admin/permission-groups/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "test_group"}'
```

```javascript
rehive.admin.permissionGroups.create({name: "test_group"}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.permission_groups.create(
    name="test_group"
)
```

> Admin create permission groups response

```shell
{
    "data": {
        "name": "test_group",
        "permissions": []
    },
    "status": "success"
}
```

```javascript
{
    "name": "test_group",
    "permissions": []
}
```

```python
{
    "name": "test_group",
    "permissions": []
}
```

Create a new permission group with no permission associated to it.

#### Endpoint

`https://rehive.com/api/3/admin/permission-groups/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`name` | Permission group name | ""

### Update permission groups

> Admin update permission groups request

```shell
curl https://www.rehive.com/api/3/admin/permission-groups/{group_name}/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "new_name"}'
```

```javascript
rehive.admin.permissionGroups.update(groupName,{name: "new_name"}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.permission_groups.update(
   {group_name},
   name="new_name" 
)
```

> Admin update permission groups response

```shell
{
    "data": {
        "name": "new_name",
        "permissions": []
    },
    "status": "success"
}
```

```javascript
{
    "name": "new_name",
    "permissions": []
}
```

```python
{
    "name": "new_name",
    "permissions": []
}
```

Update the permission group's name.

#### Endpoint

`https://rehive.com/api/3/admin/permission-groups/{group_name}/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`name` | Permission group name | ""

### Delete permission groups

> Admin delete permission groups request

```shell
curl https://www.rehive.com/api/3/admin/permission-groups/{group_name}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```
```javascript
rehive.admin.permissionGroups.delete(groupName).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.permission_groups.delete(
   {group_name}
)
```

> Admin delete permission groups response

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

Delete the permission group and all associated permissions assigned to it.

#### Endpoint

`https://rehive.com/api/3/admin/permission-groups/{group_name}/`

### List permissions

> Admin list permissions request

```shell
curl https://www.rehive.com/api/3/admin/permission-groups/{group_name}/permissions/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.permissionGroups.permissions.get(groupName).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.permission_groups.obj({group_name}).permissions.get()
```

> Admin list permissions response

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

List all the permissions associated to a permission group.

#### Pagination

The list is paginated and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

#### Endpoint

`https://rehive.com/api/3/admin/permission-groups/{group_name}/permissions/`

### Add permissions

> Admin add permissions request

```shell
curl https://www.rehive.com/admin/api/3/admin/permission-groups/{group_name}/permissions/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"type": "account",
       "level": "view"}'
```

```javascript
rehive.admin.permissionGroups.permissions.create(groupName,
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
rehive.admin.permission_groups.obj({group_name}).permissions.create(
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

Add the given permission to the permission group.

#### Pagination

The list is paginated and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

#### Endpoint

`https://rehive.com/api/3/admin/permission-groups/{group_name}/permissions/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`type` | Permission type | ""
`level` | Level of permission | ""

### Remove permissions

> Admin remove permissions request

```shell
curl https://www.rehive.com/admin/api/3/admin/permission-groups/{group_name}/permissions/{permission_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.permissionGroups.permissions.delete(groupName,permissionId).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.admin.permission_groups.obj({group_name}).permissions.delete(
    {permission_id}
)
```

> Admin remove permissions response

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

Remove the permission from the permission group.

#### Endpoint

`https://rehive.com/api/3/admin/permission-groups/{group_name}/permissions/{permission_id}/`


### Assign permission group

> Admin assign permission group request

```shell
curl https://www.rehive.com/api/3/admin/users/{uuid}/permission-groups/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"group": "test_group"}'
```

```javascript
rehive.admin.users.permissionGroups.create(uuid, {
    group: "test_group"
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

> Admin assign permission group response

```shell
{
    "data": {
        "name": "test_group"
    },
    "status": "success"
}
```

```javascript
{
    "name": "test_group"
}
```

Assign a permission group to a user.

#### Endpoint

`https://www.rehive.com/api/3/admin/users/{uuid}/permission-groups/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`group` | Group name | ""

### Unassign permission group

> Admin unassign permission group request

```shell
curl https://www.rehive.com/api/3/admin/users/{uuid}/permission-groups/{group_name}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
rehive.admin.users.permissionGroups.delete(uuid,groupName).then(function (res) {
    ...
}, function (err) {
    ...
});
```

> Admin unassign permission group response

```shell
{
    "status": "success"
}
```

```javascript
{}
```

Unassign a permission group for a user.

#### Endpoint

`https://www.rehive.com/api/3/admin/users/{uuid}/permission-groups/{group_name}/`

### Assign permissions

> Admin assign permissions request

```shell
curl https://www.rehive.com/api/3/admin/users/{uuid}/permissions/
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

Assign a permission to a user.

#### Endpoint

`https://www.rehive.com/api/3/admin/users/{uuid}/permissions/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`type` | Permission type | ""
`level` | Level of permission | ""

### Unassign permissions

> Admin unassign permissions request

```shell
curl https://www.rehive.com/api/3/admin/users/{uuid}/permissions/{permission_id}/
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

`https://www.rehive.com/api/3/admin/users/{uuid}/permissions/{permission_id}/`

