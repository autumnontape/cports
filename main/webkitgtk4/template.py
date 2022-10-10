# mirrors the gtk3 webkitgtk template
pkgname = "webkitgtk4"
pkgver = "2.38.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DPORT=GTK", "-DCMAKE_SKIP_RPATH=ON",
    f"-DCMAKE_LINKER={self.profile().triplet}-clang",
    # -DUSE_*
    "-DUSE_SOUP2=OFF",
    "-DUSE_GTK4=ON",
    "-DUSE_LD_LLD=ON",
    "-DUSE_WOFF2=ON",
    "-DUSE_WPE_RENDERER=ON",
    # -DENABLE_*
    "-DENABLE_DOCUMENTATION=OFF",
    "-DENABLE_SAMPLING_PROFILER=OFF", # unavailable on musl
    "-DENABLE_MINIBROWSER=ON",
    "-DENABLE_INTROSPECTION=ON",
    "-DENABLE_WAYLAND_TARGET=ON",
    "-DENABLE_X11_TARGET=ON",
    "-DENABLE_BUBBLEWRAP_SANDBOX=ON",
    # conflicts with the gtk3 one
    "-DENABLE_WEBDRIVER=OFF",
]
hostmakedepends = [
    "cmake", "ninja", "pkgconf", "perl", "python", "ruby", "gperf", "flex",
    "gettext-tiny", "glib-devel", "geoclue", "wayland-progs", "bubblewrap",
    "xdg-dbus-proxy", "gobject-introspection",
]
makedepends = [
    "libwpe-devel", "wpebackend-fdo-devel", "libpsl-devel", "geoclue-devel",
    "libgcrypt-devel", "libsecret-devel", "at-spi2-core-devel", "icu-devel",
    "libnotify-devel", "hyphen-devel", "woff2-devel", "libmanette-devel",
    "lcms2-devel",  "libjpeg-turbo-devel", "libpng-devel", "libwebp-devel",
    "openjpeg-devel", "libxml2-devel", "libtasn1-devel", "sqlite-devel",
    "harfbuzz-devel", "freetype-devel", "gtk4-devel", "libsoup-devel",
    "gstreamer-devel", "gst-plugins-base-devel", "gst-plugins-bad-devel",
    "libxslt-devel", "icu-devel", "enchant-devel", "libseccomp-devel",
    "libxt-devel", "libxcomposite-devel", "libxdamage-devel", "mesa-devel",
    "libxkbcommon-devel", "wayland-devel", "elogind-devel", "wayland-protocols",
]
depends = ["bubblewrap", "xdg-dbus-proxy"]
pkgdesc = "GTK4 port of the WebKit browser engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later AND BSD-2-Clause"
url = "https://webkitgtk.org"
source = f"{url}/releases/webkitgtk-{pkgver}.tar.xz"
sha256 = "f9ce6375a3b6e1329b0b609f46921e2627dc7ad6224b37b967ab2ea643bc0fbd"
debug_level = 1 # otherwise LTO link runs out of memory + fat debuginfo
tool_flags = {
    "CFLAGS": ["-DNDEBUG"],
    "CXXFLAGS": [
        # also silence some really loud warnings...
        "-DNDEBUG", "-Wno-deprecated-declarations", "-Wno-deprecated-copy"
    ],
}
env = {
    # WebKitCCache.cmake
    "CCACHE_SLOPPINESS": "time_macros,include_file_mtime"
}
# huge testsuite
options = ["!check"]

# riscv64 uses llint but no jit yet
match self.profile().arch:
    case "x86_64" | "aarch64":
        configure_args += ["-DENABLE_JIT=ON", "-DENABLE_C_LOOP=OFF"]
    case "riscv64":
        configure_args += ["-DENABLE_JIT=OFF", "-DENABLE_C_LOOP=OFF"]
    case _:
        configure_args += ["-DENABLE_JIT=OFF", "-DENABLE_C_LOOP=ON"]

# LTO broken on aarch64 (JIT segfault) and on riscv64 (broken in LLVM)
match self.profile().arch:
    case "aarch64" | "riscv64":
        options += ["!lto"]
    case _:
        configure_args += ["-DLTO_MODE=thin"]

def post_install(self):
    self.install_license("Source/WebCore/LICENSE-APPLE")
    self.install_license("Source/WebCore/LICENSE-LGPL-2.1")
    self.install_license("Source/WebCore/LICENSE-LGPL-2")

@subpackage("webkitgtk4-devel")
def _devel(self):
    return self.default_devel()