import cli_handler

handler_types_by_name = {
    'admin': cli_handler.AdminHandler,
    'group': cli_handler.GroupHandler,
    'profile': cli_handler.ProfileHandler,
    'role': cli_handler.RoleHandler,
    'user': cli_handler.UserHandler,
    'ux': cli_handler.UxHandler,
    'webhook': cli_handler.WebhookHandler,
}

def get_handler_by_command(command_name):
    HandlerClass = handler_types_by_name.get(command_name)
    if not HandlerClass:
        return None
    return HandlerClass()