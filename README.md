# service_metal_products

## Table of contents

- [Product detail page ERD](#product-detail-page-erd)
  - [Reference page](#reference-page)
  - [Corresponding MySQL DDL](#corresponding-mysql-ddl)
- [How to run API Interaction](#how-to-run-api-interaction)
- [How to run permutations.py](#how-to-run-permutationspy)

## Product detail page ERD

An entity relationship diagram draft for product details page. Review SQL @ [sql/ddl.sql](https://github.com/theodoremoreland/service_metal_products/blob/main/sql/ddl.sql) to see updated entity model.

<img src="sql/SMT ERD.png" width="600">

### Reference page

https://www.pvcfittingsonline.com/8008-015ab-1-1-2-schedule-80-pvc-pipe-5-ft-section.html#

### Corresponding MySQL DDL

Find MySQL DDL for rendering product on [reference page](https://www.pvcfittingsonline.com/8008-015ab-1-1-2-schedule-80-pvc-pipe-5-ft-section.html#) @ [`sql/ddl.sql`](https://github.com/theodoremoreland/SM/blob/main/sql/ddl.sql).

## How to run API Interaction

`Python >=3.8.10` (greater than or equal to version 3.8.10) should work. No third party libraries were used, so no installations beyond Python itself is required.

**It is assumed the user is at the root of this project and is using a UNIX style command line environment when referencing the CLI commands below.**

The program requires the user to pass in command line arguments to qualify one of three
API requests, _getting a list of todos_, _creating a todo_, or _deleting a todo_. The program can be ran with the following command to get help with the arguments required:

```
python main.py --help
```

Should result in something similar to the following:

```
Interact with jsonplaceholder.typicode API. Get, create, and delete todos.

options:
  -h, --help            show this help message and exit
  --request-type {get-todos,create-todo,delete-todo}
                        The type of request to make. Required.
  --todo-id TODO_ID     The ID of the todo item to delete. Must be an integer. Required for delete-todo.
  --count COUNT         The number of todo items to get. Min: 1, Max: 200. Optional for get-todos.
  --user-id USER_ID     The ID of the user to create a todo item for. Required for create-todo.
  --title TITLE         The title of the todo item to create. Required for create-todo.
  --completed COMPLETED
                        Whether or not the todo item is completed. Optional for create-todo.
```

Get todos example:

```
python main.py --request-type="get-todos" --count=10
```

Create todo example:

```
python main.py --request-type="create-todo" --user-id=1 --title="Review coding test" --completed=False
```

Delete todo example:

```
python main.py --request-type="delete-todo" --todo-id=201
```

## How to run permutations.py

`Python >=3.8.10` (greater than or equal to version 3.8.10) should work. No third party libraries were used, so no installations beyond Python itself is required.

**It is assumed the user is at the root of this project and is using a UNIX style command line environment when referencing the CLI commands below.**

Run the following command where the value of the `file-path` argument is an absolute path or relative path to the file needed:

```
python scripts/permutations.py --file-path="./example/relative-path.txt"
```
