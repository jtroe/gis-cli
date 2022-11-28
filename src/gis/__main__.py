import sys
from ._argument_parser import get_giscli_argument_parser

parser = get_giscli_argument_parser()
args = parser.parse_args()

if not args.command:
    parser.print_help()
    sys.exit(2)

from .command_handler import get_handler_by_command
handler = get_handler_by_command(args.command)
if not handler:
    print(f"Sorry, not implemented for `gis {args.command}`")
    sys.exit(2)

handler.execute(args)