from .cli_handler_base import CliHandlerBase

class RoleHandler(CliHandlerBase):
    def execute(self, args):
        print(self)