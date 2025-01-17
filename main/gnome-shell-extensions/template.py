pkgname = "gnome-shell-extensions"
pkgver = "45.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "gettext", "glib-devel"]
depends = [f"gnome-shell~{pkgver[:-2]}", "nautilus", "gnome-menus"]
pkgdesc = "Optional extensions for GNOME shell"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/GnomeShell/Extensions"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "239bf89ff52794f8d5e86acd85fbfe5c24be8ce167c57690db2efd587c339fd6"
