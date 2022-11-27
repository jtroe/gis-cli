from .cli_handler_base import CliHandlerBase

class ProfileHandler(CliHandlerBase):
    def execute(self, args):
        print(self)