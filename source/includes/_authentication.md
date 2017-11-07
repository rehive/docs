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
curl https://www.rehive.com/api/3/
  -H "Authorization: Token {token}"
```

```javascript
"Not applicable for sdk"
```

```python
"Not applicable for sdk"
```

When making requests, the API key should be included as a token in the `Authorization` header:

`Authorization: Token {token}`

<aside class="notice">
You must replace <code>{token}</code> with your API token.
</aside>


## Company Register

> Company registration request

```shell
curl https://www.rehive.com/api/3/auth/company/register/
  -X POST
  -H "Content-Type: application/json"
  -d '{"first_name": "Joe",
       "last_name": "Soap",
       "email": "joe@rehive.com",
       "mobile_number": "+00000000000",
       "company": "rehive",
       "password1": "joe1234",
       "password2":"joe1234",
       "terms_and_conditions": true}'
```

> Company registration response

```shell
{
    "status": "success"
    "data": {
        "token": "{token}",
        "user": {
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
}
```

Register a company owner with the details specified. A successful registration 
will create a company, return the user's details and a token that can be used 
for subsequent requests.

#### Endpoint

`https://rehive.com/api/3/auth/company/register/`

#### Required Fields

Field | Description | Default 
--- | --- | --- 
`first_name` | first name | null
`last_name` | last name | null
`email` | email address | null
`company` | company identifier | null
`password1` | password | null
`password2` | repeat password | null
`terms_and_conditions` | agreed to terms | false

#### Optional Fields

Field | Description | Default 
--- | --- | --- 
`mobile_number` | mobile number | null
`nationality` | country code | null
`session_duration` | session duration | 36000000


## Register

> User registration request

```shell
curl https://www.rehive.com/api/3/auth/register/
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
rehive.auth.register(
        {first_name: "Joe",
         last_name: "Soap",
         email: "joe@rehive.com",
         company: "rehive",
         password1: "joe1234",
         password2:"joe1234"
        }).then(function(user){
            // ...
        },function(err){
            // ...
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
}
```

```javascript
{
  "identifier": "00000000-0000-0000-0000-000000000000",
  "email": "joe@rehive.com",
  "mobile_number": "+00000000000",
  "first_name": "Joe",
  "last_name": "Soap",
  "company": "rehive",
  "profile": null,
  "language": "en"
}
```

```python
{
  "token": "{token}",
  "user": {
    "identifier": "00000000-0000-0000-0000-000000000000",
    "email": "joe@rehive.com",
    "mobile_number": "+00000000000",
    "first_name": "Joe",
    "last_name": "Soap",
    "company": "rehive",
    "profile": null,
    "language": "en",
    'nationality': '',
    "currency": {},
    "metadata": {},
    "mobile_number": "",
    "timezone": None,
    "verified": False,
    "kyc_verified": False,
    "status": "pending",
    "permission_group": "user",
    "groups": [],
    "permissions": [],
    "date_joined": 1505813314238
  }
}
```

Register a user with the credentials provided. A successful registration will 
return the user's details and a token that can be used for subsequent requests.

#### Endpoint

`https://rehive.com/api/3/auth/register/`

#### Required Fields

Field | Description | Default 
--- | --- | --- 
`first_name` | first name | null
`last_name` | last name | null
`email` | email address | null
`company` | company identifier | null
`password1` | password | null
`password2` | repeat password | null

#### Optional Fields

Field | Description | Default 
--- | --- | --- 
`terms_and_conditions` | agreed to terms | false
`mobile_number` | mobile number | null
`nationality` | country code | null
`session_duration` | session duration | 36000000

<aside class="notice">
<code>terms_and_conditions</code> can be set as a required by enabling the 
<code>terms_and_conditions</code> global switch. See <a href="/#switches">switches</a> 
for more information.
</aside>

<aside class="notice">
<code>session_duration</code> is an optional field that can be set to specify the 
duration (in milliseconds) of the authentication token that is created when 
loggin in. If the field is not set, the duration defaults to 10 hours. 
NOTE: This field only becomes available after the global switch <code>session_duration</code> 
has been enabled. See <a href="/#switches">switches</a> for more information.
</aside>

## Login

> User login request

```shell
curl https://www.rehive.com/api/3/auth/login/
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
            console.log(user);
            },function(err){
            // ...
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
  "status": "success"
  "data": {
    "token": "{token}",
    "user": {
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
}
```

Login a user with the credentials provided. A successful login will return the 
user's details and a token that can be used for subsequent requests.

<aside class="warning">
    If multi-factor authentication is enabled, see the OTP 
    <a href="/#verify-multi-factor-authentication">verify endpoint</a> for how to verify OTPs after login.
</aside>

#### Endpoint

`https://rehive.com/api/3/auth/login/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`user` | email, mobile number, or unique identifier | null
`company` | company identifier | null
`password` | password | null

#### Optional Fields

Field | Description | Default 
--- | --- | ---
`session_duration` | session duration | 36000000

## Logout

> User logout request

```shell
curl https://www.rehive.com/api/3/auth/logout/
  -X POST
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
```

```javascript
rehive.auth.logout().then(function(res){
        // ...
    },function(err){
        // ...
    })
```

```python
rehive.auth.logout()
```

> User logout response

```shell
{
  "message": "Successfully logged out.",
  "status": "success"
}
```

```javascript
{
  "message": "Successfully logged out."
}
```

```python
{
  "message": "Successfully logged out.",
  "status": "success"
}
```

Logs the current user out and invalidates the token that was used to authenticate.

#### Endpoint

`https://rehive.com/api/3/auth/logout/`

## Logout All

> User logout all request

```shell
curl https://www.rehive.com/api/3/auth/logout/all/
  -X POST
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
```

```javascript
rehive.auth.logoutAll().then(function(res){
            // ...
        }, function (err){
            // ...
        })
```

```python
rehive.auth.logout_all()
```

> User logout all response

```shell
{
  "message": "Successfully logged out all sessions.",
  "status": "success"
}
```

```javascript
{
  "message": "Successfully logged out all sessions."
}
```

```python
{
  "message": "Successfully logged out all sessions.",
  "status": "success"
}
```

Logs the current user out and invalidates all the tokens related to the user that have expiry dates.

#### Endpoint

`https://rehive.com/api/3/auth/logout/all/`

## Change Password

> User change password request

```shell
curl https://www.rehive.com/api/3/auth/password/change/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"old_password": "joe1234",
       "new_password1": "joe1234",
       "new_password2": "joe1234"}'
```

```javascript
rehive.auth.changePassword(
        {
            old_password: "joe1234",
            new_password1: "joe1234",
            new_password2: "joe1234"
        }).then(function(res){
            // ...
        },function(err){
            // ...
        })
```

```python
"To be implemented"
```

> User change password response

```shell
{
  "message": "New password has been saved.",
  "status": "success"
}
```

```javascript
{
  "message": "New password has been saved."
}
```

Change a user's password.

<aside class="notice">
Take note of the <code>Authorization</code> header required for authentication.
</aside>

#### Endpoint

`https://rehive.com/api/3/auth/password/change/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`old_password` | old password | null
`new_password1` | new password | null
`new_password2` | confirm new password | null

## Reset Password

> User reset password request

```shell
curl https://www.rehive.com/api/3/auth/password/reset/
  -X POST
  -H "Content-Type: application/json"
  -d '{"user": "joe@rehive.com",
       "company": "rehive"}'
```

```javascript
rehive.auth.resetPassword(
        {
            user: "joe@rehive.com",
            company: "rehive"
        }).then(function(res){
            // ...
        }, function (err) {
            // ...
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
  "message": "Password reset message has been sent.",
  "status": "success"
}
```

```javascript
{
  "message": "Password reset message has been sent."
}
```

```python
{
  "message": "Password reset message has been sent.",
  "status": "success"
}
```

Send a password reset email.

#### Endpoint

`https://rehive.com/api/3/auth/password/reset/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`user` | email, mobile number, or unique identifier | null
`company` | company identifier | null

## Reset Password Confirm

> User reset password confirm request

```shell
curl https://www.rehive.com/api/3/auth/password/reset/confirm/
  -X POST
  -H "Content-Type: application/json"
  -d '{"new_password1": "joe1234",
       "new_password2": "joe1234",
       "uid": "{uid}",
       "token": "{token}"}'
```

```javascript
rehive.auth.resetConfirmPassword(
        {
            new_password1: "joe1234",
            new_password2: "joe1234",
            uid: "{uid}",
            token: "{token}"
        }).then(function(res){
            // ...
        },function(err){
            // ...
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
  "message": "Password has been reset with the new password.",
  "status": "success"
}
```

```javascript
{
  "message": "Password has been reset with the new password."
}
```

```python
{
  "message": "Password has been reset with the new password.",
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

`https://rehive.com/api/3/auth/password/reset/confirm/`

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
curl https://www.rehive.com/api/3/auth/email/verify/resend/
  -X POST
  -H "Content-Type: application/json"
  -d '{"email": "joe@rehive.com",
       "company": "rehive"}'
```

```javascript
rehive.auth.resendEmailVerification(
        {
            email: "joe@rehive.com",
            company: "rehive"
        }).then(function(res){
            // ...
        },function(err){
            // ...
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
{ }
```

```python
{
  "status": "success"
}
```

Resend email verifications for an email.

#### Endpoint

`https://rehive.com/api/3/auth/email/verify/resend/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`email` | email address | null
`company` | company identifier | null

## Resend Mobile Verification

> User resend mobile verification request

```shell
curl https://www.rehive.com/api/3auth/mobile/verify/resend/
  -X POST
  -H "Content-Type: application/json"
  -d '{"mobile": "+27840000000",
       "company": "rehive"}'
```

```javascript
rehive.auth.resendMobileVerification(
        {
            mobile: "+27840000000",
            company: "rehive"
        }).then(function(res){
            // ...
        },function(err){
            // ...
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
{ }
```

```python
{
  "status": "success"
}
```

Resends mobile verifications for a mobile number.

#### Endpoint

`https://www.rehive.com/api/3/auth/mobile/verify/resend/`

#### Required Fields

Field | Description | Default
--- | --- | --- 
`mobile` | mobile number | null
`company` | company identifier | null


## Verify Email

> User verify email request

```shell
curl https://rehive.com/api/3/auth/email/verify/
  -X POST
  -H "Content-Type: application/json"
  -d '{"key": "{key}"}'
```

> User verify email response

```shell
{
  "status": "success"
}
```

Verify an email number with a key. The key is sent in an email by Rehive.

#### Endpoint

`https://rehive.com/api/3/auth/email/verify/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`key` | verification key | null


## Verify Mobile

> User verify mobile request

```shell
curl https://rehive.com/api/3/auth/mobile/verify/
  -X POST
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
  -d '{"otp": "{otp}"}'
```

```javascript
rehive.auth.verifyMobile(
        {
            otp: "{otp}"
        }).then(function(res){
            // ...
        },function(err){
            // ...
        })
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
{ }
```

```python
{
  "status": "success"
}
```

Verify a mobile number with an OTP. Unlike the "Verify Email", the user needs to 
be logged in for this functionality to work.

#### Endpoint

`https://rehive.com/api/3/auth/mobile/verify/`

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
curl https://www.rehive.com/api/3/auth/tokens/
  -X GET
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
```

```javascript
rehive.token.getTokensList().then(function(res){
        // ...
    },function(err){
        // ...
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
    "token_key": "00000000",
    "expires": null
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
curl https://www.rehive.com/api/3/auth/tokens/
  -X POST
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
  -D "{"password": "joe1234"}"
```

```javascript
rehive.token.createToken(
        {
            password: "joe1234"
        }).then(function(res){
            // ...
        },function(err){
            // ...
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
}
```

```javascript
{
    "token": "{token}",
    "user": {
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

```python
{
    "token": "{token}",
    "user": {
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

Creating a token here will remove the expiration time on the token, thus giving it an infinite lifespan.

#### Endpoint

`https://rehive.com/api/3/auth/tokens/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`password` | password | null

### Delete Token

> Delete token request

```shell
curl https://www.rehive.com/api/3/auth/tokens/{token_key}/
  -X DELETE
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
```

```javascript
rehive.token.deleteToken("000a0a00").then(function(res){
        // ...
    },function(err){
        // ...
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
{ }
```

```python
{
  "status": "success"
}
```

#### Endpoint

`https://rehive.com/api/3/auth/tokens/{token_key}/`

### Verify Token

> Verify token request

```shell
curl https://www.rehive.com/api/3/auth/tokens/verify/
  -X POST
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
  -D "{"token": "{token}"}"
```

```javascript
rehive.token.deleteToken("000a0a00").then(function(res){
        // ...
    },function(err){
        // ...
    })
```

```python
rehive.auth.tokens.delete("{token_key}")
```

> Delete token response

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
    "status": "success",
    "user": {
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

```python
{
    "status": "success",
    "user": {
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

#### Endpoint

`https://rehive.com/api/3/auth/tokens/{token_key}`

