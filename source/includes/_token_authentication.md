# Token Authentication

Token authentication is an extra method of authentication that companies can use to access admin only functionality. Admin endpoints that require token authentication can be used to interact with admin-only processes or alternatively complete tasks on behalf of a user.

## Authorization

> Token authorization request

```shell
curl https://www.rehive.com/api/3/
  -H "Authorization: Token {token}"
```

The admin API key can be retrieved via `settings -> security` in the Rehive dashboard.

When making requests on admin resources, the API key should be included as a token in the `Authorization` header:

`Authorization: Token {token}`

<aside class="notice">
You must replace <code>{token}</code> with your company API key.
</aside>

