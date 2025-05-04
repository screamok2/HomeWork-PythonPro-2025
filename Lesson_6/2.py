GLOBAL_CONFIG = {"feature_a": True,
                 "max_retries": 3
                 }

class Configuration:
    def __init__(self, updates: dict, validator=None):
        self.updates = updates
        self.validator = validator
        self.original_config = {}

    def __enter__(self):
        global GLOBAL_CONFIG
        self.original_config = GLOBAL_CONFIG.copy()
        if self.validator:
            if not self.validator(self.updates):
                raise ValueError

        GLOBAL_CONFIG.update(self.updates)
        return GLOBAL_CONFIG

    def __exit__(self, exc_type, exc_value, traceback):
        global GLOBAL_CONFIG
        GLOBAL_CONFIG = self.original_config


def validate_config(config):
    # Ensure max_retries >= 0
    return config.get("max_retries", 0) >= 0


print("Before: " , GLOBAL_CONFIG)


with Configuration({"feature_a": False,"max_retries": 9}, validator=validate_config):
    print("Updated:", GLOBAL_CONFIG)
