# Multi-factor Authentication

Rehive allows for the use of token-based or sms-otp based multi-factor
authentication, both of which can be fully managed and utilised by the API.

## Multi-factor Status

> Status request

```shell
curl https://www.rehive.com/api/3/auth/mfa/
  -X GET
  -H "Content-Type: application/json"
```

```javascript
rehive.auth.mfa.status.get().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.auth.mfa.get()
```

> Status response

```shell
  {
    "status": "success"
    "data": {
        "sms": false,
        "token": false
    }
  }
```

```javascript
{
  "sms":false,
  "token":false
}
```

```python
{
    "sms": false,
    "token": false
}
```

Provides the statuses for SMS and Token bases authentication. When successfully 
enabled, the respective type will be `true`.

#### Endpoint

`https://rehive.com/api/3/auth/mfa/`

## View SMS Authentication

> SMS request

```shell
curl https://www.rehive.com/api/3/auth/mfa/sms/
  -X GET
  -H "Content-Type: application/json"
```

```javascript
rehive.auth.mfa.sms.get().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.auth.mfa.sms.get()
```

> SMS response

```shell
  {
    "status": "success"
    "data": {
        "mobile_number": "+27000000000",
        "confirmed": true
      }
    }
  }
```

```javascript
{
    "mobile_number": "+27000000000",
    "confirmed": false
}
```

```python
{
  "mobile_number": "+27000000000",
  "confirmed": true
}
```

#### Endpoint

`https://rehive.com/api/3/auth/mfa/sms/`

## Enable SMS Authentication

> SMS request

```shell
curl https://www.rehive.com/api/3/auth/mfa/sms/
  -X POST
  -H "Content-Type: application/json"
  -D '{"mobile_number": "+27000000000"}'
```

```javascript
rehive.auth.mfa.sms.enable({
    mobile_number: mobile_no
}).then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.auth.mfa.authorize_number(
  mobile="+27000000000"
)
```

> SMS response

```shell
  {
    "status": "success"
    "data": {
        "mobile_number": "+27000000000",
        "confirmed": false
      },
    }
  }
```

```javascript
{
  "mobile_number": "+27000000000",
  "confirmed": false
}
```

```python
{
  "mobile_number": "+27000000000",
  "confirmed": false
}
```

By posting to this endpoint you are starting the verification process for enabling SMS authentication. At this point an OTP will be sent to the mobile number that was
posted. Use this OTP to verify the mobile number at the [Verify endpoint](#verify-multi-factor-authentication).

#### Endpoint

`https://rehive.com/api/3/auth/mfa/sms/send/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`mobile_number` | Mobile Number | null

## Send SMS

> Send SMS request

```shell
curl https://www.rehive.com/api/3/auth/mfa/sms/send/
  -X POST
  -H "Content-Type: application/json"
```

```javascript
rehive.auth.mfa.sms.send().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.auth.mfa.send_sms(
  mobile="+27000000000"
)
```

> Send SMS response

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

Sends an OTP to the mobile number that was used to enabled SMS based multi-factor authentication.

<aside class="notice">
    This is only required if, for some reason, the automatic SMS was not sent or a new OTP needs to be generated and sent.
</aside>  

#### Endpoint

`https://rehive.com/api/3/auth/mfa/sms/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`mobile_number` | Mobile Number | null

## View Token Authentication

> Token request

```shell
curl https://www.rehive.com/api/3/auth/mfa/token/
  -X GET
  -H "Content-Type: application/json"
```

```javascript
rehive.auth.mfa.token.get().then(function (res) {
     ...
}, function (err) {
     ...
});
```

```python
rehive.auth.mfa.token.get()
```

> Token response

```shell
  {
    "status": "success"
    "data": {
        "otpauth_url": "otpauth://totp/Rehive1%3A%20joe%40rehive.com?secret=00000000000000000000000000000000&digits=6&issuer=Rehive",
        "issuer": "Rehive",
        "account": "joe@rehive.com",
        "key": "00000000000000000000000000000000",
        "confirmed": false
    }
  }
```

```javascript
{
    "otpauth_url": "otpauth://totp/Rehive1%3A%20joe%40rehive.com?secret=00000000000000000000000000000000&digits=6&issuer=Rehive",
    "issuer": "Rehive",
    "account": "joe@rehive.com",
    "key": "00000000000000000000000000000000",
    "confirmed": false
}
```

```python
{
    "otpauth_url": "otpauth://totp/Rehive1%3A%20joe%40rehive.com?secret=00000000000000000000000000000000&digits=6&issuer=Rehive",
    "issuer": "Rehive",
    "account": "joe@rehive.com",
    "key": "00000000000000000000000000000000",
    "confirmed": false
}
```

#### Endpoint

`https://rehive.com/api/3/auth/mfa/token/`

## Enable Token Authentication

> Token request

```shell
curl https://www.rehive.com/api/3/auth/mfa/token/
  -X POST
  -H "Content-Type: application/json"
```

```javascript
rehive.auth.mfa.token.enable().then(function (res) {
    ...
}, function (err) {
    ...
});
```

```python
rehive.auth.mfa.authorize_token()
```

> Token response

```shell
  {
    "status": "success"
    "data": {
        "otpauth_url": "otpauth://totp/Rehive1%3A%20joe%40rehive.com?secret=00000000000000000000000000000000&digits=6&issuer=Rehive",
        "issuer": "Rehive",
        "account": "joe@rehive.com",
        "key": "00000000000000000000000000000000"
    }
  }
```

```javascript
{
    "otpauth_url": "otpauth://totp/Rehive1%3A%20joe%40rehive.com?secret=00000000000000000000000000000000&digits=6&issuer=Rehive",
    "issuer": "Rehive",
    "account": "joe@rehive.com",
    "key": "00000000000000000000000000000000"
}
```

```python
{
    "otpauth_url": "otpauth://totp/Rehive1%3A%20joe%40rehive.com?secret=00000000000000000000000000000000&digits=6&issuer=Rehive",
    "issuer": "Rehive",
    "account": "joe@rehive.com",
    "key": "00000000000000000000000000000000"
}
```

By posting to this endpoint you are starting the verification process for enabling token based authentication. The response contains data that can be used with 
apps such as Google Authenticator. Use the `otpauth_url` to generate a QR code. For more information on how to generate a QR code, check out the [Google Charts API](https://developers.google.com/chart/infographics/docs/qr_codes).
The rest of the data can be used for manual entry into the app. Use the token OTP
generated by the app to finalise the verification process at the [Verify endpoint](#verify-multi-factor-authentication).

#### Endpoint

`https://rehive.com/api/3/auth/mfa/token/`

#### Response Fields

Field | Description 
--- | --- 
`otpauth_url` | url used for QR generation
`issuer` | The company name in Rehive
`account` | The user email address enabling multi-factor authentication
`key` | Secret key

## Verify Multi-factor Authentication

> Verify request

```shell
curl https://www.rehive.com/api/3/auth/mfa/verify/
  -X POST
  -H "Content-Type: application/json"
  -D '{"token": "123456"}'
```

```javascript
rehive.auth.mfa.verify({
    token: token
}).then(function (res) {
    ...
}, function (err) {
    ...
})
```

```python
rehive.auth.mfa.verify(
  token="123456"
)
```

> Verify response

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

This endpoint finalises the verification process for multi-factor authentication.
Once you successfully verify the SMS OTP or the token OTP, your multi-factor authentication will now be enabled. 

<aside class="notice">
    This endpoint is used to finalise the verification process, as well as verifying a token after login.
</aside>  

#### Endpoint

`https://rehive.com/api/3/auth/mfa/verify/`

#### Required Fields

Field | Description | Default
--- | --- | ---
`token` | Token or SMS OTP | null