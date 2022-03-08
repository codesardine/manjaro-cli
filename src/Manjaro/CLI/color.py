from clint.textui import puts, colored, indent


def title():
    with indent(3):
        print()
        puts(colored.green("MANJARO CLI"))

def action(msg):
    with indent(3, quote=">>"):
        puts(colored.magenta(msg))

def white(msg):
    puts(colored.white(f"Description:  {msg}"))


def red(msg):
    puts(colored.red(f"Package:      {msg}"))


def cyan(msg):
    puts(colored.cyan(f"Title:        {msg}"))

def yellow(msg):
    puts(colored.yellow(msg))
