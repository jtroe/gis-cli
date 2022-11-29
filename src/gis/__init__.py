import sys
from ._argument_parser import get_giscli_argument_parser
from .command_handler import get_handler


def main():
    parser = get_giscli_argument_parser()
    args = parser.parse_args()
    module_name = _get_fully_qualified_module_name(args)
    try:
        handler = get_handler(module_name)
        handler.execute(args)
    except NotImplementedError as ex:
        command_not_implemented = f'gis {module_name.replace(".", " ")}'
        print(f"Sorry, not implemented: `{command_not_implemented}`")
        subparser = parser.get_subparser(module_name)
        if subparser:
            subparser.print_help()
        elif module_name == None:
            parser.print_help()
        sys.exit(127)


def _get_fully_qualified_module_name(args):
    module_name = args.module
    args_dict = vars(args)
    if args_dict.get("submodule"):
        module_name = f"{args.module}.{args.submodule}"
    return module_name
