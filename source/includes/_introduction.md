# Introduction

```javascript
SDK Initialization

// Both apiVersion and apiToken are optional and the apiVersion defaults to 3
window.rehive = new Rehive({apiVersion: 3, apiToken: 'APITOKEN'});
```

```python
from rehive import Rehive

# The API_TOKEN can be left blank
rehive = Rehive(API_TOKEN)
```

> API Endpoint

```
https://rehive.com/api/3/
```

```python
"""
To override the default add the ENV variable REHIVE_API_URL to your environment
and set this to another Rehive api url: 'https://staging.rehive.com/api/3/'
"""
```


The Rehive API is the core interface for communicating with Rehive. The API is 
organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) 
with predictable resource oriented URLs. Standard HTTP verbs, codes and authentication 
methods are used alongside JSON to ensure ease of implementation.

JSON is returned by all API responses. API errors will result in a JSON response 
as well as a corresponding HTTP response code. For more on errors take a look at [errors](/#errors).

## Browsable API

To ensure the API is easily explorable Rehive has implemented a browsable API. 
In addition to ease of navigation, you can experiment with different request 
formats and methods straight from within your browser:

[Browsable API](https://rehive.com/api/3/)

<aside class="notice">
It is important to remember that the browsable API uses cookie based sessions 
for authentication and therefore differs from the documented method of 
authentication. See <a href="/#authorization">Authentication</a> for 3rd party authentication.
</aside>


## Pagination

> Pagination Response

```shell
 {
    "status": "success",
    "data": {
        "count": 1,
        "next": null,
        "previous": null,
        "results": []
    }
}

```

```javascript
// The SDK handles paginations automatically for every resource.

rehive.resource.get() // Stores pagination if returned
rehive.resource.getNext() // Calls with current next value
rehive.resource.getPrevious() // Call with current previous value
```

```python
# The SDK handles paginations automatically for every resource.

rehive.resource.get() # Stores pagination if returned
rehive.resource.get_next() # Calls with current next value
rehive.resource.get_previous() # Call with current previous value
```

Almost all listing endpoints include a way to perform pagination. The default pagination method
offered by Rehive is offset pagination, which allows navigation to an arbitrary point in 
a list of results as well as via `next` and `prev` attributes. The default page size is 15 but
can be changed by adding a `page_size` query parameter to the request URL.

### Options

Value | Descrition
--- | --- 
`page_size` | number of results per page


## Filters

> Filtered Request

```shell
curl https://www.rehive.com/an/api/endpoint/?field_1=abc&field_2=123&orderby=field_1
  -X GET
  -H "Content-Type: application/json"
```

```javascript
// Filters can be sent to any list resource as an object, ex:
filters = {
   field_1: "abc",
   field_2: 123,
   orderby: "field_1"
}
rehive.resource.get({filters: filters})
```

```python
# Filters can be parsed to any resource as a dictionary, ex:
filters = {
   "field_1": "abc",
   "field_2": 123,
   "orderby": "field_1" 
}
rehive.resource.get(
    filters=filters
)
```

Most listing pages also include a way to filter and/or sort the returned list of objects. All filtering
and sorting is done via query parameters in the GET request. 

Each endpoint's documentation contains a list of fields that are available for filtering and sorting. To filter
by a field, include it in the URL as a standard query parameter with a `?` delimiting the URL and
the start of the query parameters and a `&` between each filtered field.

To sort a result set, an endpoint will often inlcude an `orderby` attribute. Check the specific endpoints
documentation on what fields can be used for sorting.

### Complex Filter Fields

There are several filter field types in the API that offer more complex interactions:

#### Date Fields

Date fields can be further narrowed down by filtering on ranges using the greater 
than (`__gt`) and less than (`__lt`) suffixes (eg. `created__gt`).

#### Metadata Fields 

Custom metadata fields can be filtered on their first level children by adding the child
attribute as a suffix (`__child_attribute`). So if metadata contains a JSON object with an attribute `name` it can 
be filtered using `metadata__name`.

## Currency and Amounts

In order to prevent precision errors due to float data types, the API only deals in integers for currency amounts. 
This means that when posting an amount it should always be converted to it's lowest currency unit size (ie. an integer). For most 
currencies/assets this will be the cents value (eg. $ 1.00 represented as 100 in the API). When returning an integer value for
a currency amount Rehive will always include a currency object and its associated `divisibility` so that it is easy to run
any conversions back to a decimal number.

## Errors

> Error Handling

```python
from rehive import APIException

try:
    rehive.admin.currencies.get()
except APIException as e:
    print(e.status_code)
    print(e.data)
```

> Basic error response:

```shell
{
    "status": "error",
    "message": "Error message."
}
```

```javascript
{
    "message": "Error message."
}
```

```python
{
    "status": "error",
    "message": "Error message."
}
```

> Multiple errors response:

```shell
 {
    "status": "error",
    "message": "First error message, Second error message",
    "data": {
        "field_name1": [
            "First error message."
        ],
        "field_name2": [
            "Second error message."
        ]
    }
}
```

```javascript
 {
    "field_name1": [
        "First error message."
    ],
    "field_name2": [
        "Second error message."
    ]
}
```

```python
{
    "status": "error",
    "message": "First error message, Second error message",
    "data": {
        "field_name1": [
            "First error message."
        ],
        "field_name2": [
            "Second error message."
        ]
    }
}
```

Rehive errors return an API response message (formatted in JSON) as well as a standard HTTP response code.

The JSON error respone generally includes a `message` string. If an error occurred on a specific attribute or
key they will be outputted in the `data` object.