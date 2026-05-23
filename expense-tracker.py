import os
import sys
import datetime
import csv


with open("expenses.csv", 'w') as f:
    csv.DictWriter(f,['field1','field2'])
    with open("expenses.csv", 'r') as f:
        data = csv.DictReader(f)

def main():
    pass

if __name__ == "__main__":
    main()