# Permissions

Rehive inclused fine-grained permission management system, that allows admin users to create permission groups as well as individually manage users' permissions to view, add, edit or delete data from the system via admin endpoints.

## Permission Groups

### List permission groups

> Admin list permission groups request

```shell
curl https://www.rehive.com/api/3/admin/permission-groups/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin list permission groups response

```json
{
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "name": "test_group",
                "permissions": []
            }
        ]
    }
}
```

Get a list of permission groups that have been created with the associated permissions.

#### Pagination

The list is paginated and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

#### Endpoint

`https://rehive.com/api/3/admin/permission-groups/`

### Create permission groups

> Admin create permission groups request

```shell
curl https://www.rehive.com/api/3/admin/permission-groups/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "test_group"}'
```

> Admin create permission groups response

```json
{
    "data": {
        "name": "test_group",
        "permissions": []
    },
    "status": "success"
}
```

Create a new permission group with no permission associated to it.

#### Endpoint

`https://rehive.com/api/3/admin/permission-groups/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | Permission group name | "" | true

### Update permission groups

> Admin update permission groups request

```shell
curl https://www.rehive.com/api/3/admin/permission-groups/{group_name}/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"name": "new_name"}'
```

> Admin update permission groups response

```json
{
    "data": {
        "name": "new_name",
        "permissions": []
    },
    "status": "success"
}
```

Update the permission group's name.

#### Endpoint

`https://rehive.com/api/3/admin/permission-groups/{group_name}/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`name` | Permission group name | "" | true

### Delete permission groups

> Admin delete permission groups request

```shell
curl https://www.rehive.com/api/3/admin/permission-groups/{group_name}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin delete permission groups response

```json
{
    "status": "success"
}
```

Delete the permission group and all associated permissions assigned to it.

#### Endpoint

`https://rehive.com/api/3/admin/permission-groups/{group_name}/`

### List permissions

> Admin list permissions request

```shell
curl https://www.rehive.com/api/3/admin/permission-groups/{group_name}/permissions/
  -X GET
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin list permissions response

```json
{
    "status": "success",
    "data": {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 55,
                "type": "account",
                "level": "add"
            },
            {
                "id": 367,
                "type": "account",
                "level": "view"
            }
        ]
    }
}
```

List all the permissions associated to a permission group.

#### Pagination

The list is paginated and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

#### Endpoint

`https://rehive.com/api/3/admin/permission-groups/{group_name}/permissions/`

### Add permissions

> Admin add permissions request

```shell
curl https://www.rehive.com/admin/api/3/admin/permission-groups/{group_name}/permissions/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"type": "account",
       "level": "view"}'
```

> Admin add permissions response

```json
{
    "data": {
        "id": 367,
        "type": "account",
        "level": "view"
    },
    "status": "success"
}
```

Add the given permission to the permission group.

#### Pagination

The list is paginated and can be navigated via the `next` and `previous` fields or by setting a `page` parameter in the request URL.

#### Endpoint

`https://rehive.com/api/3/admin/permission-groups/{group_name}/permissions/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`type` | Permission type | "" | true
`level` | Level of permission | "" | true

### Remove permissions

> Admin remove permissions request

```shell
curl https://www.rehive.com/admin/api/3/admin/permission-groups/{group_name}/permissions/{permission_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin remove permissions response

```json
{
    "status": "success"
}
```

Remove the permission from the permission group.

#### Endpoint

`https://rehive.com/api/3/admin/permission-groups/{group_name}/permissions/{permission_id}/`


## Users and Permissions

Users can either be assigned permission groups, or permissions directly. When assigning permission groups to a user, the user will have the access specified in the permission assigned to the permission group. Individual permissions can be assigned to user if some additional permission only need to be provided to a specific user.

### Assign permission group

> Admin assign permission group request

```shell
curl https://www.rehive.com/api/3/admin/users/{uuid}/permission-groups/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"group": "test_group"}'
```

> Admin assign permission group response

```json
{
    "data": {
        "name": "test_group"
    },
    "status": "success"
}
```

Assign a permission group to a user.

#### Endpoint

`https://www.rehive.com/api/3/admin/users/{uuid}/permission-groups/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`group` | Group name | "" | true

### Unassign permission group

> Admin unassign permission group request

```shell
curl https://www.rehive.com/api/3/admin/users/{uuid}/permission-groups/{group_name}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin unassign permission group response

```json
{
    "status": "success"
}
```

Unassign a permission group for a user.

#### Endpoint

`https://www.rehive.com/api/3/admin/users/{uuid}/permission-groups/{group_name}/`

### Assign permissions

> Admin assign permissions request

```shell
curl https://www.rehive.com/api/3/admin/users/{uuid}/permissions/
  -X POST
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
  -D '{"type": "account",
       "level": "view"}'
```

> Admin assign permissions response

```json
{
    "status": "success",
    "data": {
        "id": 269,
        "type": "account",
        "level": "view"
    }
}
```

Assign a permission to a user.

#### Endpoint

`https://www.rehive.com/api/3/admin/users/{uuid}/permissions/`

#### Fields

Field | Description | Default | Required
--- | --- | --- | ---
`type` | Permission type | "" | true
`level` | Level of permission | "" | true

### Unassign permissions

> Admin unassign permissions request

```shell
curl https://www.rehive.com/api/3/admin/users/{uuid}/permissions/{permission_id}/
  -X DELETE
  -H "Authorization: Token {token}"
  -H "Content-Type: application/json"
```

> Admin unassign permissions response

```json
{
    "status": "success"
}
```

Unassign a permissions for a user.

#### Endpoint

`https://www.rehive.com/api/3/admin/users/{uuid}/permissions/{permission_id}/`
