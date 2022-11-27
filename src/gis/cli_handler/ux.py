from .cli_handler_base import CliHandlerBase

class UxHandler(CliHandlerBase):
    def execute(self, args):
        print(self)