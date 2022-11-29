import sys
from ._argument_parser import get_giscli_argument_parser
from .command_handler import get_handler

def main():
    parser = get_giscli_argument_parser()
    args = parser.parse_args()
    module_name = _get_fully_qualified_module_name(args)
    handler = get_handler(module_name)
    if not handler:
        subparser = parser.get_subparser(module_name)
        if subparser:
            subparser.print_help()
        elif module_name == None:
            parser.print_help()
        else:
            print(f"Sorry, not implemented for `gis {args.module}`")
        sys.exit(2)

    handler.execute(args)

def _get_fully_qualified_module_name(args):
    module_name = args.module
    args_dict = vars(args)
    if args_dict.get('submodule'):
        module_name = f'{args.module}.{args.submodule}'
    return module_name
    