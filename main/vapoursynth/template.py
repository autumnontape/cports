pkgname = "vapoursynth"
pkgver = "64"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "gmake",
    "pkgconf",
    "automake",
    "libtool",
    "nasm",
    "python-cython",
]
makedepends = ["python-devel", "zimg-devel"]
pkgdesc = "Video processing framework"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.vapoursynth.com"
source = f"https://github.com/vapoursynth/vapoursynth/archive/R{pkgver}.tar.gz"
sha256 = "29e7972eace52bb83365cf9a14a5552df444090391f032de23b589ed8ff64213"


@subpackage("vapoursynth-devel")
def _devel(self):
    # libvapoursynth.so should be in main package, don't use default_devel
    return [
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/lib/*.a",
        "usr/lib/libvapoursynth-script.so",
    ]
