FLOW_DECORATORS = []
STEP_DECORATORS = []


def get_plugin_cli():
    """
    Return list of click multi-commands to extend metaflow CLI
    with a "sample" command.
    """

    from .sample.sample import cli

    return [cli]
