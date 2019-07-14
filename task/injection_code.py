import sys
import traceback


def check_usage_possibility(func, importing_module=None):
    def inner(*args, **kwargs):
        usage_counter = 0
        stack = traceback.extract_stack()
        for line in stack:
            if line[0] == '<string>':
                usage_counter += 1
        try:
            if not importing_module:
                banned_function = inner.__name__
                if usage_counter == len(stack):
                    raise PermissionError(f"Function {banned_function} not allowed to use")

            banned_import = args[0]
            if usage_counter == len(stack) and banned_import == importing_module:
                raise PermissionError(f"Module {banned_import} not allowed to use")

        except PermissionError as message:
            print(message)
            sys.exit()

        return func(*args, **kwargs)

    inner.__name__ = func.__name__
    return inner


for banned_import in sys.argv[1].split(','):
    __builtins__.__dict__['__import__'] = check_usage_possibility(__builtins__.__dict__['__import__'], banned_import)
for banned_function in sys.argv[2].split(','):
    __builtins__.__dict__[banned_function] = check_usage_possibility(__builtins__.__dict__['exec'])

del check_usage_possibility
