from .cli_handler_base import CliHandlerBase

class ProfileHandler(CliHandlerBase):
    def _get_command_method(self, command):
        command_dict = {
            'list': self.list
        }
        return command_dict.get(command)

    def list(self, args):
        pm = self.arcgis.gis.ProfileManager()
        profiles_list = pm.list()
        if len(profiles_list) == 0:
            print('No profiles found')
        else:
            print('Profiles:')
        for profile in profiles_list:
            print(profile)