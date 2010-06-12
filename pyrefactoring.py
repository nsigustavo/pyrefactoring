import os
import sys
from tokenize import generate_tokens
from StringIO import StringIO

def pyreplace():
    old, new = sys.argv[1], sys.argv[2]
    for file_path in list_python_files():
        with file(file_path) as f:
            source = f.read()
        source_refactored = replace(source, old, new)
        source_refactored
        with file(file_path, 'w') as f:
            f.write(source_refactored)


def replace(source, old, new):
    lines = source.split('\n')
    text = StringIO(source)
    for token_type, token, (lineno, col_init), (lineno_exit, col_exit), line_source in generate_tokens(text.readline):
        if token == old:
            line = lines[lineno-1]
            lines[lineno-1] = lin-e[:col_init] + new + line[col_exit:]
    return '\n'.join(lines)


def list_python_files(dir=os.getcwd()):
    tests = []
    for item in os.listdir(dir):
        path = os.path.join(dir, item)
        if item.endswith('.py'):
            tests.append(path)
        elif os.path.isdir(path):
            tests += list_python_files(path)
    return tests

