from abc import ABC, abstractmethod
from typing import Callable


class CliHandlerBase(ABC):
    def __init__(self, arcgis):
        self.arcgis = arcgis

    def execute(self, args):
        command_method = self._get_command_method(args.command)
        if not command_method:
            raise NotImplementedError(args.command)
        command_method(args)

    @abstractmethod
    def _get_command_method(self, command) -> Callable:
        pass
