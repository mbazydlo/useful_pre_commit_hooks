import argparse
import ast
from typing import Union


def parse_code_for_exec_eval(
        object_: Union[ast.FunctionDef, ast.ClassDef, ast.Module],
        filename: str,
        is_exec_eval: int = 0
) -> int:
    code_ast = ast.parse(object_)
    for object_ in code_ast.body:
        if isinstance(object_, (ast.FunctionDef, ast.ClassDef)):
            parse_code_for_exec_eval(object_, filename)

        elif isinstance(object_, ast.Expr) and isinstance(object_.value, ast.Call):
            func_name = object_.value.func.id

            if func_name in ('exec', 'eval'):
                print(f'File {filename} contains exec/eval function !')
                is_exec_eval = 1
    return is_exec_eval


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args()

    return_value = 0

    for filename in args.filenames:
        with open(filename, mode='r') as file:
            code = ast.parse(file.read())
            result = parse_code_for_exec_eval(code, filename)

            if result:
                return_value = 1

    return return_value


if __name__ == '__main__':
    raise SystemExit(main())