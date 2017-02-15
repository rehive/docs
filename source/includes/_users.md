# Users

## Retrieve Profile

> User profile request

```shell
curl https://www.rehive.com/api/3/users/profile/
  -X GET
  -H "Authorization: JWT {token}"
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
        "balance": 0,
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
        "metadata": null
    }
}
```

Retrieve a user's profile information.

### Endpoint

`https://rehive.com/api/3/users/profile/`

## Update Profile

> User update profile request

```shell
curl https://www.rehive.com/api/3/users/profile/
  -X PATCH
  -H "Authorization: JWT {token}"
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
        "balance": 0,
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
        "metadata": null
    }
}
```

Update a user's profile information.

### Endpoint

`https://rehive.com/api/3/users/profile/`

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

## Retrieve Company

> User retrieve company request

```shell
curl https://www.rehive.com/api/3/users/company/
  -X GET
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
```

> User retrieve company response

```json
{
    "status": "success",
    "data": {
        "identifier": "rehive",
        "name": "Rehive",
        "description": "Wallets for everyone.",
        "website": "http://www.rehive.com",
        "logo": null
    }
}
```

Retrieve a user's company information.

### Endpoint

`https://rehive.com/api/3/users/company/`

## Retrieve Address

> User retrieve address request

```shell
curl https://www.rehive.com/api/3/users/address/
  -X GET
  -H "Authorization: JWT {token}"
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

`https://rehive.com/api/3/users/address/`

## Update Address

> User update address request

```shell
curl https://www.rehive.com/api/3/users/address/
  -X PATCH
  -H "Authorization: JWT {token}"
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

`https://rehive.com/api/3/users/address/`

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
curl https://www.rehive.com/api/3/users/bank_accounts/
  -X GET
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
```

> User list bank accounts response

```json
{
    "status": "success",
    "data": [
        {
            "id": 25,
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

`https://rehive.com/api/3/users/bank_accounts/`

## List Bitcoin Accounts

> User list bitcoin accounts request

```shell
curl https://www.rehive.com/api/3/users/bitcoin_accounts/
  -X GET
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
```

> User list bitcoin accounts response

```json
{
    "status": "success",
    "data": [
        {
            "id": 30,
            "address": "123456789asd",
            "code": "bitcoin_123456789asd"
        }
    ]
}
```

List a user's bitcoin addresses.

### Endpoint

`https://rehive.com/api/3/users/bitcoin_accounts/`

## Create Document

> User documents request

```shell
curl https://www.rehive.com/api/3/users/document/
  -X POST
  -H "Authorization: JWT {token}"
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

`https://rehive.com/api/3/users/document/`

### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`file` | a document file | null | true
`document_category` | The document category | other | false
`document_type` | The type of docuemnt | other | false

## List Email Addresses

> User list email addresses request

```shell
curl https://www.rehive.com/api/3/users/emails/
  -X GET
  -H "Authorization: JWT {token}"
  -H "Content-Type: application/json"
```

> User list email addresses response

```json
{
    "status": "success",
    "data": [
        {
            "id": 8,
            "email": "joe@rehive.com",
            "primary": true,
            "verified": true
        }
    ]
}
```

Get a list of user's email addresses.

### Endpoint

`https://www.rehive.com/api/3/users/emails/`

## List Mobile Numbers

> User mobile numbers request

```shell
curl https://www.rehive.com/api/3/users/mobiles/
  -X GET
  -H "Authorization: JWT {token}"
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

`https://www.rehive.com/api/3/users/mobiles/`

## List Notifications

> User list notifcations request

```shell
curl https://www.rehive.com/api/3/users/notifications/
  -X GET
  -H "Authorization: JWT {token}"
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

`https://rehive.com/api/3/users/notifications/`