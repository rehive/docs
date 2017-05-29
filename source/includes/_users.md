# Users

## Retrieve Profile

> User profile request

```shell
curl https://www.rehive.com/api/3/user/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> User profile response

```json
{
    "status": "success",
    "data": {
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": "",
        "id_number": "",
        "profile": null,
        "currency": {
            "description": "Rand",
            "code": "ZAR",
            "symbol": "R",
            "unit": "rand",
            "divisibility": 2
        },
        "company": {
            "identifier": "rehive",
            "name": "Rehive",
            "description": "Wallets for everyone.",
            "website": "http://www.rehive.com",
            "logo": null
        },
        "language": "en",
        "nationality": "ZA",
        "metadata": null,
        "mobile_number": "+27840000000",
        "skype_name": "@skype",
        "timezone": "Asia/Dhaka"
    }
}
```

Retrieve a user's profile information.

### Endpoint

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

> User update profile response

```json
{
    "status": "success",
    "data": {
        "first_name": "Joe",
        "last_name": "Soap",
        "email": "joe@rehive.com",
        "username": "",
        "id_number": "",
        "profile": null,
        "currency": {
            "description": "Rand",
            "code": "ZAR",
            "symbol": "R",
            "unit": "rand",
            "divisibility": 2
        },
        "company": {
            "identifier": "rehive",
            "name": "Rehive",
            "description": "Wallets for everyone.",
            "website": "http://www.rehive.com",
            "logo": null
        },
        "language": "en",
        "nationality": "ZA",
        "metadata": null,
        "mobile_number": "+27840000000",
        "skype_name": "@skype",
        "timezone": "Asia/Dhaka"
    }
}
```

Update a user's profile information.

### Endpoint

`https://rehive.com/api/3/user/`

### Fields

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
`skype_name` | skype name | blank | false
`timezone` | timezone | blank | false

## Retrieve Address

> User retrieve address request

```shell
curl https://www.rehive.com/api/3/user/address/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> User retrieve address response

```json
{
    "status": "success",
    "data": {
        "line_1": "1 Main Street",
        "line_2": "East City",
        "city": "Cape Town",
        "state_province": "Western Cape",
        "country": "ZA",
        "postal_code": "8001"
    }
}
```

Retrieve a user's address.

### Endpoint

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

> User update address response

```json
{
    "status": "success",
    "data": {
        "line_1": "1 Main Street",
        "line_2": "East City",
        "city": "Cape Town",
        "state_province": "Western Cape",
        "country": "ZA",
        "postal_code": "8001"
    }
}
```

Update a user's address.

### Endpoint

`https://rehive.com/api/3/user/address/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`line_1` | address line one | blank | false
`line_2` | address line 2 | blank | false
`city` | city | blank | false
`state_province` | state or province | blank | false
`country` | country code | blank | false
`postal_code` | postal or zip code) | blank | false

## List Bank Accounts

> User list bank accounts request

```shell
curl https://www.rehive.com/api/3/user/bank_accounts/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> User list bank accounts response

```json
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
            "code": "bank_account_VEM7k1y5hnuF"
        }
    ]
}
```

List a user's bank accounts.

### Endpoint

`https://rehive.com/api/3/user/bank_accounts/`

## Create Bank Account

> User create bank account request

```shell
curl https://www.rehive.com/api/3/user/bank_accounts/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"name": "Bank",
       "number": "000000000000000",
       "type": "Cheque",
       "bank_name": "Bank Ltd.",
       "branch_code": "0000"}'
```

> User create bank account response

```json
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
        "code": "bank_account_000000000000"
    }
}
```

Create a bank account for a user.

### Endpoint

`https://rehive.com/api/3/user/bank_accounts/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | account name | null | false
`number` | account number | null | false
`type` | account type | null | false
`bank_name` | bank name | null | false
`bank_code` | bank code | null | false
`branch_code` | branch code | null | false
`swift` | swift number | null | false
`iban` | IBAN number | null | false
`bic` | BIC number | null | false

## Update Bank Account

> User update bank account request

```shell
curl https://www.rehive.com/api/3/user/bank_accounts/{account_id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"name": "Bank"}'
```

> User update bank account response

```json
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
        "code": "bank_account_000000000000"
    }
}
```

Update a user's bank account.

### Endpoint

`https://rehive.com/api/3/user/bank_accounts/{account_id}`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | account name | null | false
`number` | account number | null | false
`type` | account type | null | false
`bank_name` | bank name | null | false
`bank_code` | bank code | null | false
`branch_code` | branch code | null | false
`swift` | swift number | null | false
`iban` | IBAN number | null | false
`bic` | BIC number | null | false


## List Bitcoin Accounts

> User list bitcoin accounts request

```shell
curl https://www.rehive.com/api/3/user/bitcoin_accounts/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> User list bitcoin accounts response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "address": "123456789asd",
            "code": "bitcoin_123456789asd"
        }
    ]
}
```

List a user's bitcoin addresses.

### Endpoint

`https://rehive.com/api/3/user/bitcoin_accounts/`

## Create Bitcoin Account

> User create bitcoin account request

```shell
curl https://www.rehive.com/api/3/user/bitcoin_accounts/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"address": "0000000000000000000000000000000000"}'
```

> User create bitcoin account response

```json
{
    "status": "success",
    "data": {
        "id": 1,
        "address": "0000000000000000000000000000000000",
        "code": "bitcoin_0000000000000000000000000000000000"
    }
}
```

Create a bitcoin account for a user.

### Endpoint

`https://rehive.com/api/3/user/bitcoin_accounts/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`address` | full bitcoin address | null | true

## Update Bitcoin Account

> User update bitcoin account request

```shell
curl https://www.rehive.com/api/3/user/bitcoin_accounts/{account_id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"address": "0000000000000000000000000000000000"}'
```

> User update bitcoin account response

```json
{
    "status": "success",
    "data": {
        "id": {account_id},
        "address": "0000000000000000000000000000000000",
        "code": "bitcoin_0000000000000000000000000000000000"
    }
}
```

Update a user's bitcoin account.

### Endpoint

`https://rehive.com/api/3/user/bitcoin_accounts/{account_id}`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`address` | full bitcoin address | null | true

## Create Document

> User documents request

```shell
curl https://www.rehive.com/api/3/user/document/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -F file=@localfilename
```

> User documents response

```json
{
    "status": "success",
    "data": {
        "file": "{file_url}",
        "document_category": "other",
        "document_type": "other"
    }
}
```

Upload user document.

### Endpoint

`https://rehive.com/api/3/user/document/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`file` | a document file | null | true
`document_category` | The document category | other | false
`document_type` | The type of docuemnt | other | false

## List Email Addresses

> User list email addresses request

```shell
curl https://www.rehive.com/api/3/user/emails/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> User list email addresses response

```json
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

Get a list of user's email addresses.

### Endpoint

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

> User create email address response

```json
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

Create an email address for a user.

### Endpoint

`https://rehive.com/api/3/user/emails/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`email` | email address | null | true
`primary` | is a primary user email | false | false

## Update Email Address

> User update email address request

```shell
curl https://www.rehive.com/api/3/user/emails/{email_id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"primary": true}'
```

> User update email address response

```json
{
    "status": "success",
    "data": {
        "id": {email_id},
        "email": "joe@rehive.com",
        "primary": true,
        "verified": true
    }
}
```

Update a user's email adress. The email adress can be changed to be the user's primary email address. The actual address cannot be updated and a new one should instead be created.

### Endpoint

`https://rehive.com/api/3/user/emails/{email_id}`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`primary` | is a primary user email | false | false

## List Mobile Numbers

> User mobile numbers request

```shell
curl https://www.rehive.com/api/3/user/mobiles/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> User mobile numbers response

```json
{
    "status": "success",
    "data": [
        {
            "id": 8,
            "number": "+00000000000",
            "primary": true,
            "verified": true
        }
    ]
}
```

Get a list of user's mobile numbers.

### Endpoint

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

> User create mobile number response

```json
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

Create a mobile number for a user.

### Endpoint

`https://rehive.com/api/3/user/mobiles/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`number` | mobile number address (including area code)| null | true
`primary` | is a primary user number | false | false

## Update Mobile Number

> User update mobile number request

```shell
curl https://www.rehive.com/api/3/user/mobiles/{number_id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"primary": true}'
```

> User update mobile number response

```json
{
    "status": "success",
    "data": {
        "id": {number_id},
        "number": "+00000000000",
        "primary": true,
        "verified": true
    }
}
```

Update a user's mobile number. The number can be changed to be the user's primary mobile number. The actual number cannot be updated and a new one should be created instead.

### Endpoint

`https://rehive.com/api/3/user/mobiles/{number_id}`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`primary` | is a primary user email | false | false

## List Notifications

> User list notifcations request

```shell
curl https://www.rehive.com/api/3/user/notifications/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> User list notifcations response

```json
{
    "status": "success",
    "data": [
        {
            "id": 1,
            "name": "tx_send",
            "description": "Send transaction notifications",
            "email_enabled": true,
            "sms_enabled": true
        },
        {
            "id": 2,
            "name": "tx_receive",
            "description": "Receive transaction notifications",
            "email_enabled": true,
            "sms_enabled": true
        },
        {
            "id": 3,
            "name": "tx_unclaimed",
            "description": "Unclaimed transaction notifications",
            "email_enabled": true,
            "sms_enabled": true
        },
        {
            "id": 4,
            "name": "tx_deposit",
            "description": "Deposit transaction notifications",
            "email_enabled": true,
            "sms_enabled": true
        },
        {
            "id": 9,
            "name": "document_upload",
            "description": "Document upload notifications",
            "email_enabled": true,
            "sms_enabled": true
        },
        {
            "id": 10,
            "name": "document_change",
            "description": "Document status change notifications",
            "email_enabled": true,
            "sms_enabled": true
        }
    ]
}
```

Get a list of available notification settings.

### Endpoint

`https://rehive.com/api/3/user/notifications/`

## Update Notification

> User update notification request

```shell
curl https://www.rehive.com/api/3/user/notifcations/{notification_id}
  -X PATCH
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -d '{"email_enabled": true}'
```

> User update notification response

```json
{
    "status": "success",
    "data": {
        "id": {notification_id},
        "email_enabled": true,
        "sms_enabled": true,
        "name": "tx_deposit",
        "description": "Deposit transaction notifications"
    }
}
```

Update a user's settings for a notification.

### Endpoint

`https://rehive.com/api/3/user/notifcations/{notification_id}`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`email_enabled` | is email notifcation enabled | false | false
`sms_enabled` | is sms notifcation enabled | false | false