pkgname = "vulkan-tools"
pkgver = "1.3.268"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-Wno-dev",
    "-DVULKAN_HEADERS_INSTALL_DIR=/usr",
    "-DBUILD_CUBE=ON",
]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf", "glslang-progs"]
makedepends = [
    "vulkan-headers",
    "vulkan-loader-devel",
    "libxkbcommon-devel",
    "libxcb-devel",
    "libxrandr-devel",
    "wayland-devel",
    "wayland-protocols",
    "linux-headers",
]
pkgdesc = "Official Vulkan tools and utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = (
    f"https://github.com/KhronosGroup/Vulkan-Tools/archive/v{pkgver}.tar.gz"
)
sha256 = "07b08b45812da1e82921ac707076558ec9b2f6f00eefefb69b911a1ba0715294"
# FIXME: vkcube etc fail
hardening = ["vis", "!cfi"]
# no test suite
options = ["!cross", "!check"]
