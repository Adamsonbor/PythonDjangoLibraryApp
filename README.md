# PythonDjangoLibraryApp

### Installation

##### Clone
``` bash
git clone https://github.com/Adamsonbor/PythonDjangoLibraryApp.git
```
##### Run
``` bash
cd PythonDjangoLibraryApp
docker compose up
```

### API
##### Books
Book model - 
{
    "isbn": "",
    "title": "",
    "author": "",
    "year": null
}
- Books management http://localhost:8000/api/v1/books/
- Books detail view http://localhost:8000/api/v1/books/[isbn]
##### Users
User model -
{
    "username": "",
    "email": ""
}
- User registration http://localhost:8000/api/v1/users/register/
