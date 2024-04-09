import subprocess

subprocess.run(["daphne", "web_core.asgi:application"])
