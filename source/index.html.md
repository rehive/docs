---
title: API Reference

language_tabs:
  - shell

includes:
  - errors

search: true
---

# Introduction

> API Endpoint 

```
https://rehive.com/api/3/
```

Welcome to the Rehive API!

JSON is returned by all API responses. API errors will result in a JSON response as well as a correspoding HTTP response code.

# JWT Authentication

The JWT authentication method should be used for any user based interactions with the Rehive platform. This authentication schema offers a simple standardized way to securely trasmit information between parties using a JSON object.

Once a user is logged in, each subsequent request should include a JWT. This will permit the user to access  their content and associated functionality.

## Authorization

When making requests using a JWT, the JWT should be included as a token in the `Authorization` header:

`Authorization: JWT {jwt}`

<aside class="notice">
You must replace <code>{jwt}</code> with a user's JWT.
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
```

Register a user with the credentials provided. A successful registration will return the user's details and a JWT that can be used for subsequent requests.

### Endpoint

`https://rehive.com/api/3/register/`

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
       "password1": "joe1234"}'
```

> User login response

```json
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
      "language": "en"
    }
  }
```

Login a user with the credentials provided. A successful login will return the user's details and a JWT that can be used for subsequent requests.

### Endpoint

`https://rehive.com/api/3/login/`

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
```

> User logout response

```json
{
  "message": "Successfully logged out.",
  "status": "success"
}
```

Logs the current user out.

### Endpoint

`https://rehive.com/api/3/auth/logout/`

## Verify

> User verify jwt request

```shell
curl https://www.rehive.com/api/3/auth/jwt/verify/
  -X POST 
  -H "Content-Type: application/json" 
  -d '{"token": "{token}"}'
```

> User verify jwt response

```json
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
      "language": "en"
    }
  }
```

Verify JWT. This endpoint will return a user's details if the JWT is successfully verified.

### Endpoint

`https://rehive.com/api/3/auth/jwt/verify/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`token` | jwt to be verified | null | true

## Refresh

> User refresh jwt request

```shell
curl https://www.rehive.com/api/3/auth/jwt/refresh/
  -X POST 
  -H "Content-Type: application/json" 
  -d '{"token": "{token}"}'
```

> User refresh jwt response

```json
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
      "language": "en"
    }
  }
```

Refresh JWT. This endpoint will return a user's details in addition to a new JWT if the JWT provided is successfully verified.

### Endpoint

`https://rehive.com/api/3/auth/jwt/refresh/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`token` | jwt to be verified | null | true

## Change Password

> User change password request

```shell
curl https://www.rehive.com/api/3/auth/password/change/
  -X POST 
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

Send a password reset email.

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

Reset a password using a reset `token` and `uid`. These details are sent in an email by Rehive. The included reset URL can be customized via the dashboard in `settings -> company info`.

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

Resends all email verification for an account.

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

# Users

Description of section.

## Profile

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Company

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Address 

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Bank Accounts

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Bitcoin Accounts

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Documents

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Email Addresses

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Mobile Numbers

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Notifications

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

# Transactions 

Description of section.

## List Transactions

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Total Transactions

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Transfer

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Deposits

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Withdraw

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

# Accounts

Description of section.

## Balances

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Currencies

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Set Currency

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Bank Deposits

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

# Token Authentication

Token authntication is an extra method of authentication that comapny's can use to access admin only functionality. Admin endpoints that require token authentication can be used to interact with admin functionality or alternatively complete tasks on behalf of a user.

## Authorization

> To authorize, use this code:

```shell
curl {api_endpoint}
  -H "Authorization: Token {token}"
```

> Make sure to replace `token` with your API key.

The admin API key can be retrieved via `settings -> security` in the Rehive dashboard.

When making requests on admin resources, the API key should be included as a token in the `Authorization` header:

`Authorization: Token {token}`

<aside class="notice">
You must replace <code>{token}</code> with your company API key.
</aside>

# Administration

Description of section.

## List Transactions

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Total Transactions

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Transfer

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Deposit

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Withdraw

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Update Transaction

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Verify Email Address

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value

## Verify Mobile Number

> Request description

```shell
```

> Response description

```json
```

Endpoint description.

### Endpoint

`https://rehive.com`

### Fields

Field | Description | Default
---------- | ----------------- | --------------
field_name | field_description | value
