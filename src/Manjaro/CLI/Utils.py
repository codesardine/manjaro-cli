from Manjaro.CLI import color
import subprocess


def spawn_cmd(cmd):
    subprocess.run(cmd)


def wrong_syntax(cmd):
    from Manjaro.CLI.Utils import spawn_cmd
    from Manjaro.CLI import color
    color.action(f"WRONG SYNTAX, manjaro {cmd} --help")
    spawn_cmd(["manjaro", cmd, "--help"])


class Progress():
    def __init__(self):
        self.action = ""
        

prog = Progress()


def on_msg_emit(self, action=None, progress=None, status=None, details=[], message=None):
    global prog   
    if action and action != prog.action:
        prog.action = action
        if status and action and message:
            print(status, action)
        elif action:
            print(action)
    elif message:
        print(message)
