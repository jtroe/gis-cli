from .cli_handler_base import CliHandlerBase

class AdminHandler(CliHandlerBase):
    def execute(self, args):
        print(self)