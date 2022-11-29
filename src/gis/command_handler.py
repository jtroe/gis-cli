from . import cli_handler as handlers

handler_types_by_name = {
    'admin.credit': handlers.AdminCreditHandler,
    'admin.idp': handlers.AdminIdpHandler,
    'admin.license': handlers.AdminLicenseHandler,
    'admin.password-policy': handlers.AdminPasswordPolicyHandler,
    'admin.reindex': handlers.AdminReindexHandler,
    'admin.ssl': handlers.AdminSslHandler,
    'group': handlers.GroupHandler,
    'profile': handlers.ProfileHandler,
    'role': handlers.RoleHandler,
    'user': handlers.UserHandler,
    'ux': handlers.UxHandler,
    'webhook': handlers.WebhookHandler,
}

def get_handler(name):
    HandlerClass = handler_types_by_name.get(name)
    if not HandlerClass or not issubclass(HandlerClass, handlers._CliHandlerBase):
        raise NotImplementedError()
    try:
        import arcgis
    except ImportError as ex:
        print('Failed to import `arcgis`, a required dependency')
        raise ex
    try:
        return HandlerClass(arcgis)
    except TypeError as ex:
        raise NotImplementedError()