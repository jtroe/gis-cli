from .cli_handler_base import CliHandlerBase

class WebhookHandler(CliHandlerBase):
    def execute(self, args):
        print(self)