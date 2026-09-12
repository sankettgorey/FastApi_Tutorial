| Code  | Meaning               | Typical use                   |
| ----- | --------------------- | ----------------------------- |
| `200` | OK                    | Successful GET/update         |
| `201` | Created               | Successful POST/create        |
| `204` | No Content            | Successful delete             |
| `400` | Bad Request           | Invalid request               |
| `401` | Unauthorized          | Not authenticated             |
| `403` | Forbidden             | Authenticated but not allowed |
| `404` | Not Found             | User/resource doesn't exist   |
| `409` | Conflict              | Duplicate resource            |
| `422` | Validation Error      | Invalid Pydantic input        |
| `500` | Internal Server Error | Server-side problem           |
