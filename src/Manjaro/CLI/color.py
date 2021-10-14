from clint.textui import puts, colored, indent


def title():
    with indent(3):
        print()
        puts(colored.green("MANJARO CLI"))

def action(msg):
    with indent(3, quote=">>"):
        puts(colored.magenta(msg))

def white(msg):
    with indent(2):
        puts(colored.white(msg))


def red(msg):
    with indent(2):
        puts(colored.red(msg))


def cyan(msg):
    with indent(2):
        puts(colored.cyan(msg))

def yellow(msg):
    with indent(2):
        puts(colored.yellow(msg))
