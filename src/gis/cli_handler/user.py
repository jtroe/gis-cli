from .cli_handler_base import CliHandlerBase

class UserHandler(CliHandlerBase):
    def execute(self, args):
        print(self)