# Program for interacting with jsonplaceholder.typicode API.
# Run program with `python main.py --help` for more information.

# First party
import argparse
from pprint import pprint

# Custom
from api import get_todos, delete_todo, create_todo

parser = argparse.ArgumentParser()
parser.description = (
    "Interact with jsonplaceholder.typicode API. Get, create, and delete todos."
)
parser.add_argument(
    "--request-type",
    type=str,
    required=True,
    help="The type of request to make. Required.",
    choices=["get-todos", "create-todo", "delete-todo"],
)

# --------- Delete todo arguments.  ---------
parser.add_argument(
    "--todo-id",
    type=int,
    required=False,
    help="The ID of the todo item to delete. Must be an integer. Required for delete-todo.",
)

# --------- Get todos arguments. ---------
parser.add_argument(
    "--count",
    type=int,
    default=200,
    required=False,
    help="The number of todo items to get. Min: 1, Max: 200. Optional for get-todos.",
)

# --------- Create todo arguments. ---------
parser.add_argument(
    "--user-id",
    type=int,
    required=False,
    help="The ID of the user to create a todo item for. Required for create-todo.",
)
parser.add_argument(
    "--title",
    type=str,
    required=False,
    help="The title of the todo item to create. Required for create-todo.",
)
parser.add_argument(
    "--completed",
    type=bool,
    required=False,
    default=False,
    help="Whether or not the todo item is completed. Optional for create-todo.",
)


def main():
    args = parser.parse_args()

    if args.request_type == "get-todos":
        pprint(get_todos(args.count))
    elif args.request_type == "create-todo":
        pprint(create_todo(args.user_id, args.title, args.completed))
    elif args.request_type == "delete-todo":
        pprint(delete_todo(args.todo_id))
    else:
        raise ValueError("Invalid request type.")


if __name__ == "__main__":
    main()
