from cli_handler.admin import AdminHandler
from cli_handler.group import GroupHandler
from cli_handler.profile import ProfileHandler
from cli_handler.role import RoleHandler
from cli_handler.user import UserHandler
from cli_handler.ux import UxHandler
from cli_handler.webhook import WebhookHandler

handler_types_by_name = {
    'admin': AdminHandler,
    'group': GroupHandler,
    'profile': ProfileHandler,
    'role': RoleHandler,
    'user': UserHandler,
    'ux': UxHandler,
    'webhook': WebhookHandler,
}

def get_handler_by_command(command_name):
    HandlerClass = handler_types_by_name.get(command_name)
    if not HandlerClass:
        return None
    return HandlerClass()