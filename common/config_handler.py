import yaml
import os

def load_config(config_name='config.yaml'):
    """Loads the configuration file and returns the config for the active environment."""
    # Build the absolute path to the config file
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', config_name)

    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    # Get the active environment from an OS environment variable, or use the default
    env_name = os.getenv('TEST_ENV', config['default_env'])

    # Return the configuration for the specified environment
    return config[env_name]

# Load the configuration once and make it available for import
config = load_config()