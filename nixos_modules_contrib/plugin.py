import os.path
import nixops


@nixops.plugins.hookimpl
def nixexprs():
    cwd = os.path.dirname(os.path.abspath(__file__))
    return [os.path.join(cwd, "nix")]
