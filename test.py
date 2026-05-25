import argparse

parser = argparse.ArgumentParser(
    prog="expense-tracker.py",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description=f"Welcome to the Python Expense Tracker CLI.This program was made as part of one of the projects in Roadmap.sh to learn the Python programming language.",
    epilog="To view this screen at any time, just run the program with no arguments or type '-h' at the end of the command. GitHub: Sheikh-H",
)

parser.add_argument(
    dest="command",
    type=str,
    help="These are the initial commands use to add, remove, update or view expenses that you store in to the CSV file. The 'export' command is used to create a csv file and store only the type of expenses you would like to see i.e. for a specific month or type",
    choices=["add", "delete", "update", "view", "export"],
)

parser.add_argument_group(
    "Adding an expense",
    "To add an expense use the following:",
)

parser.print_help()
