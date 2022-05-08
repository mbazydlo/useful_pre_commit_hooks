from __future__ import annotations

import argparse
import re

PATTERN = re.compile('(={2,3}|!=|~=|>=?|<=?).+')


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args()

    return_value = 0

    for filename in args.filenames:
        with open(filename, mode='r') as file:
            for requirement in file.readlines():
                if not PATTERN.search(requirement):
                    print(f'Requirement library does not contain version info: {requirement}', end='')
                    return_value = 1
    return return_value


if __name__ == '__main__':
    raise SystemExit(main())
