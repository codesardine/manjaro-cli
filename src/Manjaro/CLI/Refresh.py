import subprocess
from Manjaro.CLI import color

def database(refresh):
    if refresh == "database":
        subprocess.run(["pacman-mirrors", "--fasttrack"])
        subprocess.run(["pacman", "-Syy"])
    else:
        color.red("Use -d or database")

