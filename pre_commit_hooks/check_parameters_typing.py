from __future__ import annotations

import argparse
import json
from typing import Any
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    retval = 1

    for filename in args.filenames:
        print(filename)
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
