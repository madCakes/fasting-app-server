# fasting app server

---

## Routes

| Request | Path           | Request                                              | Response                                         | Comment                                                    |
| ------- | -------------- | ---------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------- |
| GET     | `'/'`          | `tbc`                                                | `code: 200`                                      | Homepage, doesn't require a login                          |
| GET     | `'/dashboard'` | `tbc`                                                | `code: 200`                                      | Protected at the frontend, no access unless user logged in |
| POST    | `'/login'`     | `{ "username": [username], "password": [password] }` | `{ "bearer token": "Bearer [token]"}, code: 200` | N/A                                                        |
| POST    | `'/register'`  | `{ "username": [username], "password": [password]}`  | `{ "bearer token": "Bearer [token]"}, code: 201` | N/A                                                        |
| POST    | `'/dashboard'` | `{ "bearer token": "Bearer [token]"}, fasting data ` | `{ "bearer token": "Bearer [token]"}, code: 201` | Fasting data from graphs\*                                 |
|
