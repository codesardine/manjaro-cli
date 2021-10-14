import subprocess
from Manjaro.CLI import color, Utils

def database():
    Utils.spawn_cmd(["pacman-mirrors", "--fasttrack"])
