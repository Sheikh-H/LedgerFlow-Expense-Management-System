import argparse

parser = argparse.ArgumentParser(
    prog="expense-tracker.py",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description=f"Welcome to the Python Expense Tracker CLI.This program was made as part of one of the projects in Roadmap.sh to learn the Python programming language.",
    epilog="To view this screen at any time, just run the program with no arguments or type '-h' at the end of the command. GitHub: Sheikh-H",
)

subparsers = parser.add_subparsers(dest="InitialCommand")
add_parser = subparsers.add_parser("add", help="This takes 4 arguments [--description, --amount, --date, --]")

parser.print_help()