# API Practice (based on Home Automation Tutorial)
> https://www.youtube.com/watch?v=4T5Gnrmzjak

## Student Registration System

All responses will be of the following format:

```json
{
    "data":"Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```
Subsequent response definitions will only be detail the expected value of the `data field`

### List all devices

**Definition**

`GET /students`

**Response**

 - `200 OK` on success
```json
[
    {
        "id": "1342",
        "first_name": "Doug",
        "last_name": "Funny",
        "age": "14",
    },
    {
        "id": "2731",
        "first_name": "Skeeter",
        "last_name": "Valentine",
        "age": "14",
    }
]
```

### Registering a new device

**Definition**

`POST /students`

**Arguments**
- `"first_name":string` first name of student
- `"last_name":string` last name of student
- `"age":integer` age of student

NOTE: If a student with a given id number alreadt exists, the existing student will be overwrittne

**Response**

 - `201 Created` on success
```json
{
    "id": "1342",
    "first_name": "Doug",
    "last_name": "Funny",
    "age": "14",
}
```

### Lookup student details

`GET /students/<id>`

**Response**

 - `404 Not Found` if student does not exist
 - `200 OK` on success
```json
{
    "id": "1342",
    "first_name": "Doug",
    "last_name": "Funny",
    "age": "14",
}
```

### Delete/remove a student

`DELETE /students/<id>`

**Response**

 - `404 Not Found` if student does not exist
 - `204 No Content` on success
