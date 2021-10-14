import subprocess
from Manjaro.CLI import color, Utils

def database():
    Utils.spawn_cmd(["pacman-mirrors", "--fasttrack"])


def keyring():
    Utils.spawn_cmd(["pacman-key", "--refresh-keys"])
    Utils.spawn_cmd(["pacman-key", "--populate", "archlinux", "manjaro"])
