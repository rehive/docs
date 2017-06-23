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

When making requests, the API key should be included as a token in the `Authorization` header:

`Authorization: Token {token}`

<aside class="notice">
You must replace <code>{token}</code> with your API token.
</aside>

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

> User registration response

```shell
  {
    "status": "success"
    "data": {
      "token": "{token}",
      "user": {
        "identifier": "00000000-0000-0000-0000-000000000000",
        "email": "joe@rehive.com",
        "mobile_number": "+00000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "company": "rehive",
        "profile": null,
        "language": "en"
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

Register a user with the credentials provided. A successful registration will 
return the user's details and a token that can be used for subsequent requests.

#### Endpoint

`https://rehive.com/api/3/auth/register/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`first_name` | first name | null | true
`last_name` | last name | null | true
`email` | email address | null | true
`mobile_number` | mobile number | null | false
`company` | company identifier | null | true
`password1` | password | null | true
`password2` | repeat password | null | true

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

> User login response

```shell
  {
    "status": "success"
    "data": {
      "token": "{token}",
      "user": {
        "identifier": "00000000-0000-0000-0000-000000000000",
        "email": "joe@rehive.com",
        "mobile_number": "+00000000000",
        "first_name": "Joe",
        "last_name": "Soap",
        "company": "rehive",
        "profile": null,
        "language": "en"
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

Login a user with the credentials provided. A successful login will return the 
user's details and a token that can be used for subsequent requests.

#### Endpoint

`https://rehive.com/api/3/auth/login/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`user` | email, mobile number, unique identifier | null | true
`company` | company identifier | null | true
`password` | password | null | true

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

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`old_password` | old password | null | true
`new_password1` | new password | null | true
`new_password2` | confirm new password | null | true

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

Send a password reset email.

#### Endpoint

`https://rehive.com/api/3/auth/password/reset/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`user` | email, mobile number, unique identifier | null | true
`company` | company identifier | null | true

## Reset Confirm Password

> User reset confirm password request

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

> User reset confirm password response

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

Reset a password using a reset `token` and `uid`. These details are sent in an email by Rehive.

<aside class="notice">
The URL included in the reset email can be customized via the dashboard in 
`settings -> company info`. Changing this URL is required if you wish to make 
use of your own client side UI for resetting emails.
</aside>

#### Endpoint

`https://rehive.com/api/3/auth/password/reset/confirm/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`new_password1` | password | null | true
`new_password2` | password confirm | null | true
`uid` | uniqie identifer for reset | null | true
`token` | uniqie token for reset | null | true

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

> User resend email verification response

```shell
{
  "status": "success"
}
```

```javascript
{ }
```

Resend email verifications for an email.

#### Endpoint

`https://rehive.com/api/3/auth/email/verify/resend/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`email` | email address | null | true
`company` | company identifier | null | true

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

> User resend mobile verification response

```shell
{
  "status": "success"
}
```

```javascript
{ }
```

Resends mobile verifications for a mobile number.

#### Endpoint

`https://www.rehive.com/api/3/auth/mobile/verify/resend/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`mobile` | mobile number | null | true
`company` | company identifier | null | true

## Verify Mobile

> User verify mobile request

```shell
curl https://rehive.com/api/3/auth/mobile/verify/
  -X POST
  -H "Content-Type: application/json"
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

> User verify mobile response

```shell
{
  "status": "success"
}
```

```javascript
{ }
```

Verify a mobile number with an OTP.

#### Endpoint

`https://rehive.com/api/3/auth/mobile/verify/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`otp` | one time password | null | true
