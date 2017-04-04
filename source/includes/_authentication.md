# Authentication

The authentication endpoints provide the core for all Rehive access control. This includes such tasks as registration, login, verification, password changes and lost password retrievals.

## Authorization

Rehive uses Token as the method of authorization.

Once a user has logged in and received a Token, each subsequent request should include the Token in the HTTP Authorization header.

All Tokens have a 10 hour lifespan after which it will be removed. Login would be required in order to re-authenticate.

Rehive's tokens allows for a single user to have multiple active tokens on separate devices as well
as the ability for admin users to create tokens that do not expire.

<aside class="warning">
    For security reasons Rehive will only expose the token once, on login and register, and never again. Be sure to store it somewhere safe.
</aside>

<aside class="notice">
    See <a href="/#tokens">Tokens</a> for managing authentication tokens.
</aside>

**Authorization**

> Token authorization request

```shell
curl https://www.rehive.com/api/3/
  -H "Authorization: Token {token}"
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
       "company_id": "rehive",
       "password1": "joe1234",
       "password2":"joe1234"}'
```

> User registration response

```json
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

Register a user with the credentials provided. A successful registration will return the user's details and a Token that can be used for subsequent requests.

### Endpoint

`https://rehive.com/api/3/auth/register/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`first_name` | first name | null | true
`last_name` | last name | null | true
`email` | email address | null | true
`mobile_number` | mobile number | null | false
`company_id` | company identifier | null | true
`password1` | password | null | true
`password2` | repeat password | null | true

## Login

> User login request

```shell
curl https://www.rehive.com/api/3/auth/login/
  -X POST
  -H "Content-Type: application/json"
  -d '{"idenifier": "joe@rehive.com",
       "company_id": "rehive"
       "password": "joe1234"}'
```

> User login response

```json
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

Login a user with the credentials provided. A successful login will return the user's details and a Token that can be used for subsequent requests.

### Endpoint

`https://rehive.com/api/3/auth/login/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`identifier` | email, mobile number, unique identifier | null | true
`company_id` | company identifier | null | true
`password` | password | null | true

## Logout

> User logout request

```shell
curl https://www.rehive.com/api/3/auth/logout/
  -X POST
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
```

> User logout response

```json
{
  "message": "Successfully logged out.",
  "status": "success"
}
```

Logs the current user out and destroy the Token that was used to authenticate.

### Endpoint

`https://rehive.com/api/3/auth/logout/`

## Logout All

> User logout all request

```shell
curl https://www.rehive.com/api/3/auth/logout/all/
  -X POST
  -H "Content-Type: application/json"
  -H "Authorization: Token {token}"
```

> User logout all response

```json
{
  "message": "Successfully logged out all sessions.",
  "status": "success"
}
```

Logs the current user out and destroy all the Tokens related to the user that have expiry dates.

### Endpoint

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

> User change password response

```json
{
  "message": "New password has been saved.",
  "status": "success"
}
```

Change a user's password.

<aside class="notice">
Take note of the <code>Authorization</code> header required for authentication.
</aside>

### Endpoint

`https://rehive.com/api/3/auth/password/change/`

### Fields

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
  -d '{"identifier": "joe@rehive.com",
       "company_id": "rehive"}'
```

> User reset password response

```json
{
  "message": "Password reset message has been sent.",
  "status": "success"
}
```

Send a password reset email.

### Endpoint

`https://rehive.com/api/3/auth/password/reset/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`identifier` | email, mobile number, unique identifier | null | true
`company_id` | company identifier | null | true

## Reset Cofirm Password

> User reset confirm password request

```shell
curl https://www.rehive.com/api/3/auth/password/reset/confirm/
  -X POST
  -H "Content-Type: application/json"
  -d '{"new_password1": "joe1234",
       "new_password1": "joe1234",
       "uid": "{uid}",
       "token": "{token}"}'
```

> User reset confirm password response

```json
{
  "message": "Password has been reset with the new password.",
  "status": "success"
}
```

Reset a password using a reset `token` and `uid`. These details are sent in an email by Rehive.

<aside class="notice">
The URL included in the reset email can be customized via the dashboard in `settings -> company info`. Changing this URL is required if you wish to make use of your own client side UI for resetting emails.
</aside>

### Endpoint

`https://rehive.com/api/3/auth/password/reset/confirm/`

### Fields

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
  -d '{"identifier": "joe@rehive.com",
       "company_id": "rehive"}'
```

> User resend email verification response

```json
{
  "status": "success"
}
```

Resends all email verifications for an account.

### Endpoint

`https://rehive.com/api/3/auth/email/verify/resend/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`identifier` | email, mobile number, unique identifier | null | true
`company_id` | company identifier | null | true

## Resend Mobile Verification

> User resend email verification request

```shell
curl https://www.rehive.com/api/3auth/mobile/verify/resend/
  -X POST
  -H "Content-Type: application/json"
  -d '{"identifier": "joe@rehive.com",
       "company_id": "rehive"}'
```

> User resend email verification response

```json
{
  "status": "success"
}
```

Resends all mobile verifications for an account.

### Endpoint

`https://www.rehive.com/api/3/auth/mobile/verify/resend/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`identifier` | email, mobile number, unique identifier | null | true
`company_id` | company identifier | null | true

## Verify Mobile

> User verify mobile request

```shell
curl https://rehive.com/api/3/auth/mobile/verify/
  -X POST
  -H "Content-Type: application/json"
  -d '{"otp": "{otp}"}'
```

> User verify mobile response

```json
{
  "status": "success"
}
```

Verify a mobile number with an OTP.

### Endpoint

`https://rehive.com/api/3/auth/mobile/verify/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`otp` | one time password | null | true