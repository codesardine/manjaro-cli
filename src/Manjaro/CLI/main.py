from Manjaro.CLI import color
import click
color.title()
        
@click.group()
def cli():
    pass

@click.command(help="Search Software On Any Package Format")
@click.option("-a", help="Search All formats")
@click.option("-n", help="Search Native Package")
@click.option("-f", help="Search Flatpak")
@click.option("-s", help="Search Snap")
def search(a, s, n, f):
    if a or s or n or f:
        if a:
            from Manjaro.CLI.packages import _check_plugin_support, Search_snaps, Search_flatpaks, Search_pkgs
            _check_plugin_support(format="flatpak")
            _check_plugin_support(format="snap")
            Search_pkgs(a)
            Search_flatpaks(a)
            Search_snaps(a)
        if n:
            from Manjaro.CLI.packages import Search_pkgs
            Search_pkgs(n)

        if f:
            from Manjaro.CLI.packages import _check_plugin_support, Search_flatpaks
            _check_plugin_support(format="flatpak")
            Search_flatpaks(f)
        if s:
            from Manjaro.CLI.packages import _check_plugin_support, Search_snaps
            _check_plugin_support(format="snap")
            Search_snaps(s)
    else:
        from Manjaro.CLI.Utils import wrong_syntax
        wrong_syntax("search")    

@click.command(help="Set Drivers")
@click.option("-o", help="Set Open Source Graphic Grivers", is_flag=True, is_eager=True, default=False)
@click.option("-p", help="Set Proprietary Graphic Grivers", is_flag=True, is_eager=True, default=False)
def drivers(o, p):
    from Manjaro.SDK import Hardware
    if o:
        Hardware.Graphics.set_open()

    elif p:
        Hardware.Graphics.set_proprietary()

    else:
        from Manjaro.CLI.Utils import wrong_syntax
        wrong_syntax("drivers")

@click.command(help="Display System Information")
@click.option("-g", help="Graphic Drivers", is_flag=True, is_eager=True, default=False)
@click.option("-b", help="Current Branch", is_flag=True, is_eager=True, default=False)
@click.option("-e", is_flag=True, default=False, is_eager=True, help="Error Messages")
@click.option("-w", is_flag=True, default=False, is_eager=True, help="Warning Messages")
@click.option("-i", is_flag=True, default=False, is_eager=True, help="Information Messages")
@click.option("-d", is_flag=True, default=False, is_eager=True, help="Debug Messages")
def info(g, b, e, w, i, d):
    if g:
        from Manjaro.SDK import Hardware
        Hardware.Info().graphics_driver()
    elif b:
        from Manjaro.CLI import Branch
        Branch.info()
    elif e:
        from Manjaro.CLI.Diagnose import error
        error()
    elif w:
        from Manjaro.CLI.Diagnose import warning
        warning()
    elif i:
        from Manjaro.CLI.Diagnose import info
        info()
    elif d:
        from Manjaro.CLI.Diagnose import debug
        debug()
    else:
        from Manjaro.CLI.Utils import wrong_syntax
        wrong_syntax("info")

@click.command(help="Refresh reload data")
@click.option("-d", is_flag=True, default=False, is_eager=True, help="Mirrors")
@click.option("-k", is_flag=True, default=False, is_eager=True, help="Keyring")
def refresh(d, k):
    from Manjaro.CLI import Refresh
    if d:
        Refresh.database()
    if k:
        Refresh.keyring()
    else:
        from Manjaro.CLI.Utils import wrong_syntax
        wrong_syntax("info")

@click.command(help="Set Current Software Branch")
@click.option("-s", is_flag=True, default=False, is_eager=True, help="Set Stable Branch")
@click.option("-g", is_flag=True, default=False, is_eager=True, help="Set Staging Branch")
@click.option("-t", is_flag=True, default=False, is_eager=True, help="Set Testing Branch")
@click.option("-u", is_flag=True, default=False, is_eager=True, help="Set Unstable Branch")
def branch(s, g, t, u):
    from Manjaro.CLI import Branch
    if s:
        Branch.stable()
    elif g:
        Branch.staging()
    elif t:
        Branch.testing()
    elif u:
        Branch.unstable()
    else:
        from Manjaro.CLI.Utils import wrong_syntax
        wrong_syntax("branch")

@click.command(help="Install Software Packages")
@click.option("-n", help="Install Native packages")
@click.option("-f", help="Install Flatpaks")
@click.option("-s", help="Install Snaps")
def install(n, f, s):
    if n or f or s:
        from Manjaro.CLI.packages import pamac
        if n:
            from Manjaro.CLI.packages import install_pkg
            install_pkg(n)
        if s:
            from Manjaro.CLI.packages import _check_plugin_support, install_snaps
            _check_plugin_support(format="snap")
            install_snaps(s)
        if f:
            from Manjaro.CLI.packages import _check_plugin_support, install_flatpaks
            _check_plugin_support(format="flatpak")
            install_flatpaks(f)
        pamac.run()
    else:
        from Manjaro.CLI.Utils import wrong_syntax
        wrong_syntax("install")

@click.command(help="Remove Roftware Packages")
@click.option("-n", help="Remove Native Packages")
@click.option("-f", help="Remove Flatpaks")
@click.option("-s", help="Remove Snaps")
def remove(n, f, s):
    if n or f or s:
        from Manjaro.CLI.packages import pamac
        if n:
            from Manjaro.CLI.packages import remove_pkgs
            remove_pkgs(n)
        if s:
            from Manjaro.CLI.packages import _check_plugin_support, remove_snaps
            _check_plugin_support(format="snap")
            remove_snaps(s)
        if f:
            from Manjaro.CLI.packages import _check_plugin_support, remove_flatpaks
            _check_plugin_support(format="flatpak")
            remove_flatpaks(f)
        pamac.run()
    else:
        from Manjaro.CLI.Utils import wrong_syntax
        wrong_syntax("remove")

cmds = (
    drivers,
    info,
    search,
    refresh,
    branch,
    install,
    remove
)
for cmd in cmds:
    cli.add_command(cmd)
