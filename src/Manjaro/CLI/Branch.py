from Manjaro.CLI import color
from Manjaro.SDK.Branches import Branch

def info():
    current_branch = Branch().get_branch()
    color.action(f"Current branch is {current_branch}")
    return current_branch

def staging():
    current_branch = info()
    if current_branch != "staging":
        color.action(f"Setting branch to staging")
        Branch().set_branch_mirrors("stable-staging")
    

def stable():
    current_branch = info()
    if current_branch != "stable":
        color.action(f"Setting branch to stable")
        Branch().set_branch_mirrors("stable")
    

def testing():
    current_branch = info()
    if current_branch != "testing":
        color.action(f"Setting branch to testing")
        Branch().set_branch_mirrors("testing")
    

def unstable():
    current_branch = info()
    if current_branch != "unstable":
        color.action(f"Setting branch to unstable")
        Branch().set_branch_mirrors("unstable")
