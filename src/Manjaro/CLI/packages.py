from Manjaro.SDK import PackageManager
from Manjaro.CLI import color, Utils

PackageManager.Pamac._on_emit_action_progress = Utils.action_progress
PackageManager.Pamac._on_emit_hook_progress = Utils.hook_progress
pamac = PackageManager.Pamac()


def _check_plugin_support(format=""):
    def _create_new_instance():
        import sys, subprocess
        subprocess.run(sys.argv)
        sys.exit()

    if format == "flatpak" and not pamac.config.get_support_flatpak():
        color.action("Instaling Flatpak Plugin")
        pamac.add_pkgs_to_install(["libpamac-flatpak-plugin"])
        pamac.run()
        _create_new_instance()

    elif format == "snap" and not pamac.config.get_support_snap():
        color.action("Instaling Snap Plugin")
        pamac.add_pkgs_to_install(["libpamac-snap-plugin"])
        pamac.run()
        _create_new_instance()


def install_pkg(pkgs):
    color.action("Instaling and upgrading packages")
    _list = pkgs.split(" ")
    return pamac.add_pkgs_to_install(_list)


def install_flatpaks(pkgs):
    color.action("Instaling and upgrading flatpaks")
    _list = []
    for p in pkgs.split(" "):
        pkg_object = pamac.search_flatpaks(p)
        for pkg in pkg_object:
            if pkg.get_name() == p:
                _list.append(pkg)
    
    pamac.add_pkgs_to_install(_list, pkg_format="flatpaks")


def install_snaps(pkgs):
    color.action("Instaling and upgrading snaps")
    _list = []
    for p in pkgs.split(" "):
        pkg_object = pamac.search_snaps(p)
        for pkg in pkg_object:
            if pkg.get_name() == p:
                _list.append(pkg)

    pamac.add_pkgs_to_install(_list, pkg_format="snaps")


def install_appimages(pkgs):
    color.action("Instaling Appimages")
    _list = []
    for p in pkgs.split(" "):
        _list.append(p)
    pamac.add_pkgs_to_install(_list, pkg_format="appimages")


def remove_snaps(pkgs):
    color.action("Removing snaps")
    _list = []
    for p in pkgs.split(" "):
        pkg_object = pamac.search_snaps(p)
        for pkg in pkg_object:
            if pkg.get_name() == p:
                _list.append(pkg)

    pamac.add_pkgs_to_remove(_list, pkg_format="snaps")


def remove_flatpaks(pkgs):
    color.action("Removing flatpaks")
    _list = []
    for p in pkgs.split(" "):
        pkg_object = pamac.search_flatpaks(p)
        for pkg in pkg_object:
            if pkg.get_name() == p:
                _list.append(pkg)
    
    pamac.add_pkgs_to_remove(_list, pkg_format="flatpaks")


def remove_pkgs(pkgs):
    color.action("Removing packages")
    _list = pkgs.split(" ")
    pamac.add_pkgs_to_remove(_list)


def Search_pkgs(pkgs):
    color.action("Native Packages Search Results".upper())
    _list = pkgs.split(" ")
    for pkg in _list:
        p = pamac.search_pkgs(pkg)
        if p:
            for i in p:
                color.yellow(i.get_name())
                title = i.get_app_name()
                if title:
                    color.cyan(title)

                desc = i.get_desc()
                if desc:
                    color.white(desc)
        else:
            color.red("Not Found".upper())
        print()


def Search_snaps(snaps):
    color.action("Snaps Search Results".upper())
    _list = snaps.split(" ")
    for pkg in _list:
        p = pamac.search_snaps(pkg)
        if p:
            for i in p:
                color.yellow(i.get_name())
                title = i.get_app_name()
                if title:
                    color.cyan(title)

                desc = i.get_desc()
                if desc:
                    color.white(desc)
        else:
            color.red("Not Found")
        print()


def Search_flatpaks(flatpaks):
    color.action("Flatpak Search Results".upper())
    _list = flatpaks.split(" ")
    for pkg in _list:
        p = pamac.search_flatpaks(pkg)
        if p:
            for i in p:
                color.yellow(i.get_name())
                title = i.get_app_name()
                if title:
                    color.cyan(title)

                desc = i.get_desc()
                if desc:
                    color.white(desc)
        else:
            color.red("Not Found")
        print()


def Search_appimages(appimages):
    color.action("Appimage Search Results".upper())
    _list = appimages.split(" ")
    for pkg in _list:
        p = pamac.appimage.search(pkg)
        if p:
            for i in p:
                d = pamac.appimage.get_details(i)
                color.yellow(d["name"])
                title = d["title"]
                if title:
                    color.cyan(title)

                desc = d["description"]
                if desc:
                    color.white(desc)
        else:
            color.red("Not Found")
        print()
