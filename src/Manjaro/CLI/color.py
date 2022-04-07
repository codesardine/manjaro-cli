from clint.textui import puts, colored, indent


def title():
    with indent(3):
        print()
        puts(colored.green("MANJARO CLI"))

def action(msg):
    with indent(3, quote=">>"):
        puts(colored.magenta(msg))

def white(msg, description=True):
    if description:
        puts(colored.white(f"Description:  {msg}"))
    else:
        puts(colored.white(msg))

def red(msg):
    puts(colored.red(msg))

def cyan(msg):
    puts(colored.cyan(f"Title:        {msg}"))

def yellow(msg):
    puts(colored.yellow(f"Package:      {msg}"))
