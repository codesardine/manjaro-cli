from Manjaro.CLI import color
import click
color.title()
        
@click.group()
def cli():
    pass

@click.command(help="Search software on any package format")
@click.option("-a", help="search all formats")
@click.option("-n", help="search native package")
@click.option("-f", help="search flatpak")
@click.option("-s", help="search snap")
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
@click.option("-o", help="Set open source graphic drivers", is_flag=True, is_eager=True, default=False)
@click.option("-p", help="Set proprietary graphic drivers", is_flag=True, is_eager=True, default=False)
def drivers(o, p):
    from Manjaro.SDK import Hardware
    if o:
        Hardware.Graphics.set_open()

    elif p:
        Hardware.Graphics.set_proprietary()

    else:
        from Manjaro.CLI.Utils import wrong_syntax
        wrong_syntax("drivers")

@click.command(help="Display system information")
@click.option("-g", help="Graphic drivers", is_flag=True, is_eager=True, default=False)
@click.option("-b", help="Current branch", is_flag=True, is_eager=True, default=False)
@click.option("-e", is_flag=True, default=False, is_eager=True, help="error messages")
@click.option("-w", is_flag=True, default=False, is_eager=True, help="warning messages")
@click.option("-i", is_flag=True, default=False, is_eager=True, help="information messages")
@click.option("-d", is_flag=True, default=False, is_eager=True, help="debug messages")
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
@click.option("-d", is_flag=True, default=False, is_eager=True, help="package database")
def refresh(d):
    if d:
        from Manjaro.CLI import Refresh
        Refresh.database()
    else:
        from Manjaro.CLI.Utils import wrong_syntax
        wrong_syntax("info")

@click.command(help="Set current software branch")
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

@click.command(help="Install software packages")
@click.option("-n", help="install native packages")
@click.option("-f", help="install flatpaks")
@click.option("-s", help="install snaps")
def install(n, f, s):
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

@click.command(help="Remove software packages")
@click.option("-n", help="install native packages")
@click.option("-f", help="install flatpaks")
@click.option("-s", help="install snaps")
def remove(n, f, s):
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
