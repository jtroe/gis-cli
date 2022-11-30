from .cli_handler_base import CliHandlerBase


class ProfileHandler(CliHandlerBase):
    def _get_command_method(self, command):
        command_dict = {
            "list": self.list,
            "test": self.test,
        }
        return command_dict.get(command)

    def list(self, args):
        profiles_list = self._get_profiles()
        if len(profiles_list) == 0:
            print("No profiles found")
        else:
            print("Profiles:")
        for profile_name in profiles_list:
            profile = profiles_list[profile_name]
            print(f"{profile_name} ({profile.get('url', 'Default')})")
    
    def _get_profiles(self):
        pm = self.arcgis.gis.ProfileManager()
        profile_names = pm.list()
        return {profile: pm.get(profile) for profile in profile_names}

    def test(self, args):
        print(f"Testing profile {args.profile}...")
        profiles = self._get_profiles()
        if args.profile not in profiles:
            print("Profile not configured...")
            return False
        try:
            gis = self.arcgis.GIS(profile=args.profile)
        except:
            print("Profile connection failed")
            return False
        print(f"Connection succeeded to {gis.url}")
