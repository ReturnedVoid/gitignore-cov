"""Main module for the script."""
import glob
import os
import sys


def get_uncovered_patterns():
    """Get all uncovered patterns from .gitignore."""
    with open('.gitignore') as file:
        for line in file.readlines():
            line = line.strip()
            if line:
                if not glob.glob(line):
                    yield line


def main():
    """Main entry point."""
    if not os.path.exists('.gitignore'):
        print('.gitignore not found')
        sys.exit(1)

    for pattern in get_uncovered_patterns():
        print('Possibly useless pattern: "{}"'.format(pattern))
