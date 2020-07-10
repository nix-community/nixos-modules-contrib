import os.path
import nixops

from nixops.plugins import Plugin


class NixopsContribPlugin(Plugin):

    @staticmethod
    def nixexprs():
        cwd = os.path.dirname(os.path.abspath(__file__))
        return [os.path.join(cwd, "nix")]


@nixops.plugins.hookimpl
def plugin():
    return NixopsContribPlugin()
