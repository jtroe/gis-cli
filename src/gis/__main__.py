import sys
from _argument_parser import get_giscli_argument_parser

parser = get_giscli_argument_parser()
args = parser.parse_args()

if not args.command:
    parser.print_help()
    sys.exit(2)