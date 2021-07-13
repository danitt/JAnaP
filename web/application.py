import os
import inspect
import sys

# TODO: Determine why this change was made
import matplotlib
matplotlib.use('TkAgg')

import werkzeug.serving
import thread

import controllers
import controllers.configuration

# Get the default configuration file location
absolute_location = os.path.abspath(inspect.getfile(inspect.currentframe()))
absolute_path = os.path.dirname(absolute_location)
absolute_root_path = os.path.abspath(os.path.join(absolute_path, ".."))

# Load configuration from default location
local_config_file = os.path.join(absolute_root_path, "node.conf.local")
if os.path.isfile(local_config_file):
    config_file = local_config_file
else:
    config_file = os.path.join(absolute_root_path, "node.conf")
controllers.configuration.parse_config_file(config_file)

# Add the code path to the system path
code_dir = controllers.configuration.NodeConfiguration.Paths.code_root
sys.path.insert(0, code_dir) 

# Optionally override host path
APP_HOST = os.getenv('APP_HOST', '127.0.0.1')

import controllers.worker

if __name__ == "__main__":
    
    if not werkzeug.serving.is_running_from_reloader():
        thread.start_new_thread(controllers.worker.background_thread, ())

    controllers.app.secret_key = os.urandom(12)
    controllers.app.run(debug=True, host=APP_HOST)
