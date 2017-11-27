# Beta Features

This section contains experimental features that are not fully developed yet. Experimental features are not always stable and may undergo spot changes on a regular basis.

## Webhook Events

> Webhook format

```json
{
    "event": "event.name",
    "company": "company_identifier",
    "data": {
        ...
    }
}
```

Rehive has a collection of internal events that can be configured to fire off custom webhooks.

Webhooks should always be created with a secure and private `secret` key (See the webhook API endpoint docs for more about creating webhooks). The secret key can be used to identify valid Rehive requests to your server. The secret should be checked in the Authorization header when receiving a webhook.

Rehive expects a `200 OK` HTTP response when webhooks are called. If a 200 response is not returned, Rehive will retry the webhook up to a max of 12 times with a gradually increasing delay between each retry.

### Webhook Events

Rehive currently support the following webhook events:

Event | Description 
--- | --- 
`user.create`  | user created event
`user.update` | user updated event
`user.password.reset` | user password reset request event
`user.email.verify` | user email verification event (Email key)
`user.mobile.verify` | user mobile verification event (OTP key)
`address.create` | address created event
`address.update` | address updated event
`document.create` | document created event
`document.update` | document updated event
`bank_account.create` | bank account created event
`bank_account.update` | bank account updated event
`crypto_account.create` | crypto account created event
`crypto_account.update` | crypto account updated event
`transaction.create` | transaction created event
`transaction.update` | transaction updated event
`transaction.delete` | transaction deleted event
`transaction.initiate` | transaction initiated (pending) event
`transaction.execute` | transaction executed (complete/failed) event

## Idempotent Requests

> Idempotent Request

```shell
curl {url}
  -X GET
  -H "Idempotency-Key: {key}"
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

```javascript
"Not applicable for sdk"
```

The Rehive API supports idempotent requests for ensuring the same operations never occur twice.

To perform an idempotent request, attach a unique key to any `POST`, `PUT` or `PATCH` request made to the API: via the `Idempotency-Key: {key}` header.

API requests made with a new key will get saved along with their HTTP response. Follow up requests made with the same key will always return the same response (As long as the request has the same HTTP method and URL path). The keys (and their associated saved responses) expire after 24 hours.

<aside class="notice">
Idempotent requests will not work for anonymous users and/or any endpoints found under <a href="/#authorization">Authentication</a> (eg. URL paths beginning with `/api/3/auth/`)
</aside>