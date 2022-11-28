def get_giscli_argument_parser():
    import argparse
    parser = argparse.ArgumentParser(
        prog='gis',
        description="a cli tool to manage your online gis, powered by ArcGIS API for Python")
    subparsers = parser.add_subparsers(dest='command')

    # admin
    admin_parser = subparsers.add_parser('admin', help='Admin tools for ArcGIS Enterprise or Online')
    admin_subparsers = admin_parser.add_subparsers(dest='admin_command')
    admin_credit_parser = admin_subparsers.add_parser('credit', help='Manaage credits for ArcGIS Online')
    admin_idp_parser = admin_subparsers.add_parser('idp', help='Manaage Identity Providers (IDP) for ArcGIS Enterprise or Online')
    admin_license_parser = admin_subparsers.add_parser('license', help='Manage licensing for ArcGIS Enterprise')
    admin_license_subparsers = admin_license_parser.add_subparsers(dest='admin_license_command')
    admin_license_assign_parser = admin_license_subparsers.add_parser('assign', help='Assign license from pool to named user')
    admin_license_update_parser = admin_license_subparsers.add_parser('update', help='Update license for ArcGIS Enterprise instance')
    admin_password_policy_parser = admin_subparsers.add_parser('password-policy', help='Set password policy for ArcGIS Enterprise')
    admin_reindex_parser = admin_subparsers.add_parser('reindex', help='Manage indexes for ArcGIS Enterprise')
    admin_ssl_parser = admin_subparsers.add_parser('ssl', help='Manage SSL Certificates for ArcGIS Enterprise')

    # group
    group_parser = subparsers.add_parser('group', help='Manage group configuration for ArcGIS Enterprise or Online')
    group_subparsers = group_parser.add_subparsers()
    group_clone_parser = group_subparsers.add_parser('clone', help='Clone groups from one site to another')
    group_export_parser = group_subparsers.add_parser('export', help='Export groups to file')
    group_import_parser = group_subparsers.add_parser('import', help='Import groups from file')

    # profile
    profile_parser = subparsers.add_parser('profile', help='Manage connection profiles to ArcGIS Enterprise or Online')
    profile_subparsers = profile_parser.add_subparsers(dest='profile_command')
    profile_create_parser = profile_subparsers.add_parser('create', help='Create connection profile to ArcGIS Enterprise or Online')
    profile_current_parser = profile_subparsers.add_parser('current', help='Get currently selected connection profile name context')
    profile_delete_parser = profile_subparsers.add_parser('delete', help='Delete connection profile')
    profile_destination_parser = profile_subparsers.add_parser('destination', help='Get currently selected destination connection profile name context (for clone operations)')
    profile_get_parser = profile_subparsers.add_parser('get', help='Get connection profile properties')
    profile_list_parser = profile_subparsers.add_parser('list', help='List connection profile names')
    profile_test_parser = profile_subparsers.add_parser('test', help='Test connection to profile')
    profile_update_parser = profile_subparsers.add_parser('update', help='Update connection profile properties')

    # role
    role_parser = subparsers.add_parser('role', help='Manage role configuration for ArcGIS Enterprise or Online')
    role_subparsers = role_parser.add_subparsers(dest='role_command')
    role_clone_parser = role_subparsers.add_parser('clone', help='Clone roles from one site to another')
    role_export_parser = role_subparsers.add_parser('export', help='Export roles to file')
    role_import_parser = role_subparsers.add_parser('import', help='Import roles from file')

    # ux
    ux_parser = subparsers.add_parser('ux', help='Manage UX configuration for your ArcGIS site')
    ux_subparsers = ux_parser.add_subparsers(dest='ux_command')
    ux_clone_parser = ux_subparsers.add_parser('clone', help='Clone UX settings from one site to another')
    ux_export_parser = ux_subparsers.add_parser('export', help='Export UX settings to file')
    ux_import_parser = ux_subparsers.add_parser('import', help='Import UX settings from file')

    # user
    user_parser = subparsers.add_parser('user', help='Manage users for ArcGIS Enterprise or Online')
    user_subparsers = user_parser.add_subparsers(dest='user_command')
    user_clone_parser = user_subparsers.add_parser('clone', help='Clone users from one site to another')
    user_create_parser = user_subparsers.add_parser('create', help='Create user on site')
    user_export_parser = user_subparsers.add_parser('export', help='Export users to file')
    user_import_parser = user_subparsers.add_parser('import', help='Import users from file')
    user_update_parser = user_subparsers.add_parser('update', help='Update user on site')

    # webhook
    webhook_parser = subparsers.add_parser('webhook', help='Manage webhook configurations for ArcGIS Enterprise')
    webhook_subparsers = webhook_parser.add_subparsers(dest='webhook_command')
    webhook_create_parser = webhook_subparsers.add_parser('create', help='Create webhook configuration for ArcGIS Enterprise')
    webhook_delete_parser = webhook_subparsers.add_parser('delete', help='Delete webhook configuration for ArcGIS Enterprise')
    webhook_list_parser = webhook_subparsers.add_parser('list', help='List webhook configurations for ArcGIS Enterprise')
    webhook_update_parser = webhook_subparsers.add_parser('update', help='Update webhook configuration for ArcGIS Enterprise')
    return parser