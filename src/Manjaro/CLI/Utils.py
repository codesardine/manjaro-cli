from Manjaro.CLI import color
import subprocess
import click

def spawn_cmd(cmd):
    subprocess.run(cmd)

def wrong_syntax(cmd):
    from Manjaro.CLI.Utils import spawn_cmd
    from Manjaro.CLI import color
    color.action(f"WRONG SYNTAX, manjaro {cmd} --help")
    spawn_cmd(["manjaro", cmd, "--help"])


def action_progress(self, transaction, action, status, progress, data):
    fill_char = click.style(">", fg="green")
    empty_char = click.style(" ")
    with click.progressbar(
            label=action,
            length=100,
            fill_char=fill_char,
            empty_char=empty_char,
            show_eta=False) as progress_bar:
        result = float(progress) * 100
        if result >= 96:
            result = 100
            progress_bar.update(result)
            color.red(f"\n{action} Finished")

        progress_bar.update(result)


def hook_progress(self, transaction, action, details, status, progress, data):
    fill_char = click.style(">", fg="green")
    empty_char = click.style(" ")
    with click.progressbar(
            label=action,
            length=100,
            fill_char=fill_char,
            empty_char=empty_char,
            show_eta=False) as progress_bar:
        result = float(progress) * 100
        if result >= 96:
            result = 100
            progress_bar.update(result)
            color.red(f"\n{action} Finished")

        progress_bar.update(result)
