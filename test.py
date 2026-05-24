import argparse

parser = argparse.ArgumentParser(
    prog="expense-tracker.py",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description="Help Screen",
)

parser.add_argument(
    dest="command",
    type=str,
    help="Using this will help to add an expense to your data",
    choices=["add", "delete", "update", "view"],
)

parser.add_subparsers(['--description', '--amount'], title="Subcommands", description="These are subcommands")

parser.add_argument_group(
    "Adding an expense",
    "To add an expense use the following:",
)

parser.print_help()
