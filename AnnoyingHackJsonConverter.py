import json


def convert_to_json(obj):
    """
    This class shouldn't exist?
    I got the idea from the famous StackOverflow Question: https://stackoverflow.com/q/3768895/1185717
    and the answer https://stackoverflow.com/a/64469761/1185717 which points out that you can just use
    the builtin `vars` as the converter. Why doesn't python just do this?
    Anyway this is here so I could plug in a fake API response and watch the LoggingLogger do the logging without
    hitting the openai API and waiting for a response, etc.
    """
    if isinstance(obj, dict):
        return json.dumps(obj)
    else:
        return json.dumps(obj, default=vars)
