# Authentication

The authentication endpoints provide the core for all Rehive access control.
This includes such tasks as registration, login, verification, password
changes and lost password retrievals.

## Authorization
Rehive uses a token-based HTTP Authentication scheme.

Once a user has logged in and received a token, each subsequent request should
include the token in the HTTP Authorization header.

Tokens expire 10 hours after creation. Once a token has expired, login is required in order to re-authenticate.

Rehive's tokens allow for a single user to have multiple active tokens on separate devices as well
as the ability for admin users to create tokens that do not expire.

<aside class="warning">
    For security reasons Rehive will only expose the token once, on login or on
    register, and never again. Be sure to store it somewhere safe.
</aside>

<aside class="notice">
    See <a href="/#tokens">Tokens</a> for managing authentication tokens.
</aside>

**Authorization Header**

> Token authorization request

```shell
curl https://api.rehive.com/3/
  -H "Authorization: Token {token}"
```

```javascript
"The javascript SDK handles storing and sending the authentication token"
```

```python
"The python SDK handles storing and sending the authentication token"
```

When making requests, the API key should be included as a token in the `Authorization` header:

`Authorization: Token {token}`

<aside class="notice">
You must replace <code>{token}</code> with your API token.
</aside>


## Company Register

> Company registration request

```shell
curl https://api.rehive.com/3/auth/company/register/
  -X POST
  -H "Content-Type: application/json"
  -d '{"first_name": "Joe",
       "last_name": "Soap",
       "email": "joe@rehive.com",
       "mobile": "+00000000000",
       "company": "rehive",
       "password1": "joe1234",
       "password2":"joe1234",
       "terms_and_conditions": true}'
```

```javascript
rehive.auth.registerCompany({
    first_name: "Joe",
    last_name: "Soap",
    email: "joe@rehive.com",
    mobile:"+00000000000",
    company: "rehive",
    password1: "joe1234",
    password2: "joe1234",
    terms_and_conditions: true
}).then(function (user) {
    ...
}, function (err) {
    ...
})
```

```python
rehive.auth.register_company(
    first_name="Joe",
    last_name="Soap",
    email="joe@rehive.com",
    mobile="+00000000000",
    company="rehive",
    password1="joe1234",
    password2="joe1234",
    terms_and_conditions=True
)
```

> Company registration response

```shell
{
    "status": "success"
    "data": {
        "token": "{token}",
        "user": {
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
            "verification": {
                "email": true,
                "mobile": true
            },
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
}
```

```javascript
{
    "token": "{token}",
    "user": {
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
        "verification": {
            "email": true,
            "mobile": true
        },
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

```python
{
    "token": "{token}",
    "user": {
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
        "verification": {
            "email": true,
            "mobile": true
        },
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

Register a company owner with the details specified. A successful registration
will create a company, return the user's details and a token that can be used
for subsequent requests.

#### Endpoint

`https://api.rehive.com/3/auth/company/register/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`first_name` | first name | null
`last_name` | last name | null
`email` | email address | null
`company` | company id | null
`password1` | password | null
`password2` | repeat password | null
`terms_and_conditions` | agreed to terms | false

#### Optional Fields

Field | Description | Default
--- | --- | ---
`mobile` | mobile number | null
`nationality` | country code | null
`session_duration` | session duration | 36000000


## Register

> User registration request

```shell
curl https://api.rehive.com/3/auth/register/
  -X POST
  -H "Content-Type: application/json"
  -d '{"first_name": "Joe",
       "last_name": "Soap",
       "email": "joe@rehive.com",
       "company": "rehive",
       "password1": "joe1234",
       "password2":"joe1234"}'
```

```javascript
rehive.auth.register({
    first_name: "Joe",
    last_name: "Soap",
    email: "joe@rehive.com",
    company: "rehive",
    password1: "joe1234",
    password2:"joe1234",
    terms_and_conditions:true
}).then(function(user){
    ...
},function(err){
    ...
});
```

```python
rehive.auth.register(
  first_name="Joe",
  last_name="Soap",
  email="joe@rehive.com",
  company="rehive",
  password1="joe1234",
  password2="joe1234",
  terms_and_conditions=True
)
```

> User registration response

```shell
{
    "status": "success"
    "data": {
        "token": "{token}",
        "user": {
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
            "verification": {
                "email": true,
                "mobile": true
            },
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
}
```

```javascript
{
    "token": "{token}",
    "user": {
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
        "verification": {
            "email": true,
            "mobile": true
        },
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

```python
{
    "token": "{token}",
    "user": {
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
        "verification": {
            "email": true,
            "mobile": true
        },
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

Register a user with the credentials provided. A successful registration will
return the user's details and a token that can be used for subsequent requests.

#### Endpoint

`https://api.rehive.com/3/auth/register/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`first_name` | first name | null
`last_name` | last name | null
`email` | email address | null
`company` | company id | null
`password1` | password | null
`password2` | repeat password | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`terms_and_conditions` | agreed to terms | false
`mobile` | mobile number | null
`nationality` | country code | null
`session_duration` | session duration | 36000000

<aside class="notice">
<code>terms_and_conditions</code> can be set as a required by enabling the
<code>require_terms_and_conditions</code> setting on the company.
</aside>

<aside class="notice">
<code>session_duration</code> is an optional field that can be set to specify the
duration (in milliseconds) of the authentication token that is created when
loggin in. If the field is not set, the duration defaults to 10 hours.
NOTE: This field only becomes available after the company setting
<code>allow_session_durations</code> has been enabled.
</aside>

## Login

> User login request

```shell
curl https://api.rehive.com/3/auth/login/
  -X POST
  -H "Content-Type: application/json"
  -d '{"user": "joe@rehive.com",
       "company": "rehive"
       "password": "joe1234"}'
```

```javascript
rehive.auth.login({
    user: "joe@rehive.com",
    company: "rehive",
    password: "joe1234"
}).then(function(user){
    ...
},function(err){
    ...
})
```

```python
rehive.auth.login(
    user="joe@rehive.com",
    company="rehive",
    password="joe1234"
)
```

> User login response

```shell
{
    "status": "success"
    "data": {
        "token": "{token}",
        "user": {
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
            "verification": {
                "email": true,
                "mobile": true
            },
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
}
```

```javascript
{
    "token": "{token}",
    "user": {
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
        "verification": {
            "email": true,
            "mobile": true
        },
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

```python
{
  "status": "success"
  "data": {
    "token": "{token}",
    "user": {
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
        "verification": {
            "email": true,
            "mobile": true
        },
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
}
```

Login a user with the credentials provided. A successful login will return the
user's details and a token that can be used for subsequent requests.

<aside class="warning">
    If multi-factor authentication is enabled, see the OTP
    <a href="/#verify-multi-factor-authentication">verify endpoint</a> for how to verify OTPs after login.
</aside>

#### Endpoint

`https://api.rehive.com/3/auth/login/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`user` | email, mobile number, or unique id | null
`company` | company id | null
`password` | password | null

#### Optional Fields

Field | Description | Default
--- | --- | ---
`session_duration` | session duration | 36000000

## Logout

> User logout request

```shell
curl https://api.rehive.com/3/auth/logout/
  -X POST
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
```

```javascript
rehive.auth.logout().then(function(res){
    ...
},function(err){
    ...
})
```

```python
rehive.auth.logout()
```

> User logout response

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

Logs the current user out and invalidates the token that was used to authenticate.

#### Endpoint

`https://api.rehive.com/3/auth/logout/`

## Logout All

> User logout all request

```shell
curl https://api.rehive.com/3/auth/logout/all/
  -X POST
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
```

```javascript
rehive.auth.logoutAll().then(function(res){
    ...
}, function (err){
    ...
})
```

```python
rehive.auth.logout_all()
```

> User logout all response

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

Logs the current user out and invalidates all the tokens related to the user that have expiry dates.

#### Endpoint

`https://api.rehive.com/3/auth/logout/all/`

## Change Password

> User change password request

```shell
curl https://api.rehive.com/3/auth/password/change/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"old_password": "joe1234",
       "new_password1": "joe1234",
       "new_password2": "joe1234"}'
```

```javascript
rehive.auth.password.change({
    old_password: "joe1234",
    new_password1: "joe1234",
    new_password2: "joe1234"
}).then(function(res){
    ...
},function(err){
    ...
})
```

```python
rehive.auth.password.change(
    old_password="joe1234",
    new_password1="joe1234",
    new_password2="joe1234"
)
```

> User change password response

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

Change a user's password.

<aside class="notice">
Take note of the <code>Authorization</code> header required for authentication.
</aside>

#### Endpoint

`https://api.rehive.com/3/auth/password/change/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`old_password` | old password | null
`new_password1` | new password | null
`new_password2` | confirm new password | null

## Reset Password

> User reset password request

```shell
curl https://api.rehive.com/3/auth/password/reset/
  -X POST
  -H "Content-Type: application/json"
  -d '{"user": "joe@rehive.com",
       "company": "rehive"}'
```


```javascript
rehive.auth.password.reset({
    user: "joe@rehive.com",
    company: "rehive"
}).then(function(res){
    ...
}, function (err) {
    ...
})
```

```python
rehive.auth.password.reset(
  user="joe@rehive.com",
  company="rehive"
)
```

> User reset password response

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

Send a password reset email.

#### Endpoint

`https://api.rehive.com/3/auth/password/reset/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`user` | email, mobile number, or unique id | null
`company` | company id | null

## Reset Password Confirm

> User reset password confirm request

```shell
curl https://api.rehive.com/3/auth/password/reset/confirm/
  -X POST
  -H "Content-Type: application/json"
  -d '{"new_password1": "joe1234",
       "new_password2": "joe1234",
       "uid": "{uid}",
       "token": "{token}"}'
```

```javascript
rehive.auth.password.resetConfirm({
    new_password1: "joe1234",
    new_password2: "joe1234",
    uid: "{uid}",
    token: "{token}"
}).then(function(res){
    ...
},function(err){
    ...
})
```

```python
rehive.auth.password.reset_confirm_password(
  new_password1="joe1234",
  new_password2="joe1234",
  uid="{uid}",
  token="{token}"
)
```

> User reset password confirm response

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

Reset a password using a reset `token` and `uid`. These details are sent in an email by Rehive.

<aside class="notice">
The URL included in the reset email can be customized via the dashboard in
`settings -> company info`. Changing this URL is required if you wish to make
use of your own client side UI for resetting emails.
</aside>

#### Endpoint

`https://api.rehive.com/3/auth/password/reset/confirm/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`new_password1` | password | null
`new_password2` | password confirm | null
`uid` | unique identifer for reset | null
`token` | unique token for reset | null

## Resend Email Verification

> User resend email verification request

```shell
curl https://api.rehive.com/3/auth/email/verify/resend/
  -X POST
  -H "Content-Type: application/json"
  -d '{"email": "joe@rehive.com",
       "company": "rehive"}'
```

```javascript
rehive.auth.email.resendEmailVerification({
    email: "joe@rehive.com",
    company: "rehive"
}).then(function(res){
    ...
},function(err){
    ...
})
```

```python
rehive.auth.email.resend_email_verification(
  email="joe@rehive.com",
  company="rehive"
)
```

> User resend email verification response

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

Resend email verifications for an email.

#### Endpoint

`https://api.rehive.com/3/auth/email/verify/resend/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`email` | email address | null
`company` | company id | null

## Resend Mobile Verification

> User resend mobile verification request

```shell
curl https://api.rehive.com/3/auth/mobile/verify/resend/
  -X POST
  -H "Content-Type: application/json"
  -d '{"mobile": "+27840000000",
       "company": "rehive"}'
```

```javascript
rehive.auth.mobile.resendMobileVerification({
    mobile: "+27840000000",
    company: "rehive"
}).then(function(res){
    ...
},function(err){
    ...
})
```

```python
rehive.auth.mobile.resend_mobile_verification(
  mobile="+27840000000",
  company="rehive"
)
```

> User resend mobile verification response

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

Resends mobile verifications for a mobile number.

#### Endpoint

`https://api.rehive.com/3/auth/mobile/verify/resend/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`mobile` | mobile number | null
`company` | company id | null


## Verify Email

> User verify email request

```shell
curl https://api.rehive.com/3/auth/email/verify/
  -X POST
  -H "Content-Type: application/json"
  -d '{"key": "{key}"}'
```
```javascript
rehive.auth.email.verify({
    key: key
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.auth.email.verify(
    key='{key}'
)
```

> User verify email response

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

Verify an email number with a key. The key is sent in an email by Rehive.

#### Endpoint

`https://api.rehive.com/3/auth/email/verify/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`key` | verification key | null


## Verify Mobile

> User verify mobile request

```shell
curl https://api.rehive.com/3/auth/mobile/verify/
  -X POST
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
  -d '{"otp": "{otp}"}'
```

```javascript
rehive.auth.mobile.verify({
    otp: otp
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.auth.verify(
  otp="{otp}"
)
```

> User verify mobile response

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

Verify a mobile number with an OTP. Unlike the "Verify Email", the user needs to
be logged in for this functionality to work.

#### Endpoint

`https://api.rehive.com/3/auth/mobile/verify/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`otp` | one time password | null


## Tokens

The tokens endpoints provide some basic access to managing user and admin tokens.
The ability to create infinite lifespan tokens as well as viewing active tokens and
deleting unused tokens.

<aside class="notice">
    For security purposes Rehive stores hashed authentication tokens and has
    no access to the orginal token value.
</aside>

### List Tokens

> List tokens request

```shell
curl https://api.rehive.com/3/auth/tokens/
  -X GET
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
```

```javascript
rehive.auth.tokens.get().then(function(res){
    ...
},function(err){
    ...
});
```

```python
rehive.auth.tokens.get()
```

> List user tokens response

```shell
{
  "status": "success",
  "data": [
    {
      "token_key": "00000000",
      "expires": null
    }
  ]
}
```

```javascript
    [
        {
          "expires": null,
          "token_key": "00000000"
        },
        {
          "expires": "2001-01-01T01:01:01.000001Z",
          "token_key": "00000000",
        },
        {
          "expires": "2001-01-01T01:01:01.000002Z",
          "token_key": "00000000",
        }
    ]
```

```python
[
  {
    "token_key": "00000000",
    "expires": null
  }
]
```

Retrieve a list of the current active tokens for the authenticated user.
Notice that only the `token_key` is exposed here and not the whole token, in case
user tokens need to be managed on the client side.

### Create Token

> Create token request

```shell
curl https://api.rehive.com/3/auth/tokens/
  -X POST
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
  -D "{"password": "joe1234"}"
```

```javascript
rehive.auth.tokens.create({
    password: "joe12345"
}).then(function(res){
    ...
},function(err){
    ...
})
```

```python
rehive.auth.tokens.create(
  password="joe1234"
)
```

> Create token response

```shell
{
    "status": "success"
    "data": {
        "token": "{token}",
        "user": {
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
            "verification": {
                "email": true,
                "mobile": true
            },
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
}
```

```javascript
{
    "token": "{token}",
    "user": {
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
        "verification": {
            "email": true,
            "mobile": true
        },
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

```python
{
    "token": "{token}",
    "user": {
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
        "verification": {
            "email": true,
            "mobile": true
        },
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

Creating a token here will remove the expiration time on the token, thus giving it an infinite lifespan.

#### Endpoint

`https://api.rehive.com/3/auth/tokens/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`password` | password | null

### Delete Token

> Delete token request

```shell
curl https://api.rehive.com/3/auth/tokens/{token_key}/
  -X DELETE
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
```

```javascript
rehive.auth.tokens.delete("token_key").then(function(res){
    ...
},function(err){
    ...
})
```

```python
rehive.auth.tokens.delete("{token_key}")
```

> Delete token response

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

`https://api.rehive.com/3/auth/tokens/{token_key}/`

### Verify Token

> Verify token request

```shell
curl https://api.rehive.com/3/auth/tokens/verify/
  -X POST
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
  -D "{"token": "{token}"}"
```

```javascript
rehive.auth.tokens.verify("token_key").then(function(res){
    ...
},function(err){
    ...
})
```

```python
rehive.auth.tokens.verify("{token_key}")
```

> Verify token response

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
        "verification": {
            "email": true,
            "mobile": true
        },
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
    "verification": {
        "email": true,
        "mobile": true
    },
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
    "status": "success",
    "user": {
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
        "verification": {
            "email": true,
            "mobile": true
        },
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

#### Endpoint

`https://api.rehive.com/3/auth/tokens/verify/`
