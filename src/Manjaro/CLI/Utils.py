import subprocess

def spawn_cmd(cmd):
    subprocess.run(cmd)

def wrong_syntax(cmd):
    from Manjaro.CLI.Utils import spawn_cmd
    from Manjaro.CLI import color
    color.action(f"WRONG SYNTAX, manjaro {cmd} --help")
    spawn_cmd(["manjaro", cmd, "--help"])
