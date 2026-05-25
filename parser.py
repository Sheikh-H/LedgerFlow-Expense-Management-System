import argparse

parser = argparse.ArgumentParser(
    prog="expense-tracker.py",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description=f"Welcome to the Python Expense Tracker CLI. This program was made as part of one of the projects in Roadmap.sh to learn the Python programming language.",
    epilog="Use -h for help. GitHub: Sheikh-H",
)

subparsers = parser.add_subparsers(required=True, dest="InitialCommand")
add_parser = subparsers.add_parser(
    name="add",
    help="Add a new expense - 4 positional arguments [--description, --amount, --date, --category]",
)
add_parser.add_argument("--description", required=True, type=str)
add_parser.add_argument("--amount", required=True, type=float)
add_parser.add_argument("--category", required=True, type=str)
add_parser.add_argument("--date", required=True, type=str)
update_parser = subparsers.add_parser(
    name="update",
    help="Update an existing expense - 5 optional arguments [--id, --description, --amount, --date, --category]",
)
update_parser.add_argument("--id", required=True, type=int)
update_parser.add_argument("--description", type=str)
update_parser.add_argument("--amount", type=float)
update_parser.add_argument("--category", type=str)
update_parser.add_argument("--date", type=str)

view_parser = subparsers.add_parser(
    name="view",
    help="View expenses - 5 optional arguments [--id, --description, --category, --amount]",
)
view_parser.add_argument("--description", required=False, type=str)
view_parser.add_argument("--amount", required=False, type=float)
view_parser.add_argument("--category", required=False, type=str)
view_parser.add_argument("--date", required=False, type=str)
view_parser.add_argument("--id", required=False, type=int)


delete_parser = subparsers.add_parser(
    name="delete",
    help="Delete an expense - 1 of 2 optional arguments [--id, --description]",
)
delete_parser_group = delete_parser.add_mutually_exclusive_group(required=True)

delete_parser_group.add_argument("--description", type=str)
delete_parser_group.add_argument("--id", type=int)

args = parser.parse_args()
