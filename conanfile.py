"""The HGL toolchain consumes the separately packaged hgraph SDK."""
import os

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import get
from conan.tools.system.package_manager import (
    Apk, Apt, Brew, Chocolatey, Dnf, PacMan, Pkg, Yum, Zypper,
)

LEXY_URL = "https://github.com/foonathan/lexy/archive/refs/tags/v2025.05.0.tar.gz"
LEXY_SHA256 = "ae867846b890b7564d633cf28d39dfc4938fe7c54515126f720c1762de5eab30"
ISOCLINE_URL = "https://github.com/daanx/isocline/archive/refs/tags/v1.1.0.tar.gz"
ISOCLINE_SHA256 = "1e5f0efa2b719c3e1d292f501e5329e141a039deefc801099f8bbb9a50255531"


class HgraphLangConan(ConanFile):
    name = "hgraph_lang"
    version = "0.0.0"
    package_type = "application"
    license = "MIT"
    url = "https://github.com/hhenson/hgraph_lang"
    description = "HGL compiler and native module tooling"
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = (
        "CMakeLists.txt", "cmake/*", "language/*", "LICENSE",
        "external/hgraph_std/hgl/*",
    )

    def requirements(self):
        self.requires("hgraph/0.8.34", transitive_headers=True, transitive_libs=True)

    def layout(self):
        cmake_layout(self)

    def source(self):
        get(self, LEXY_URL, sha256=LEXY_SHA256, strip_root=True, destination="lexy")
        get(self, ISOCLINE_URL, sha256=ISOCLINE_SHA256, strip_root=True, destination="isocline")

    def system_requirements(self):
        for manager, package in (
            (Apt, "clang-format"), (Dnf, "clang-tools-extra"),
            (Yum, "clang-tools-extra"), (Apk, "clang-extra-tools"),
            (PacMan, "clang"), (Zypper, "clang-tools"), (Pkg, "llvm"),
            (Brew, "clang-format"), (Chocolatey, "llvm"),
        ):
            manager(self).install([package], update=True, host_package=False)

    def generate(self):
        CMakeDeps(self).generate()
        toolchain = CMakeToolchain(self)
        toolchain.cache_variables["BUILD_TESTING"] = False
        toolchain.cache_variables["HGRAPH_LANG_RELEASE_VERSION"] = str(self.version)
        for dependency in ("LEXY", "ISOCLINE"):
            toolchain.cache_variables[f"FETCHCONTENT_SOURCE_DIR_{dependency}"] = os.path.join(
                self.source_folder, dependency.lower())
        toolchain.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        CMake(self).install()

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "none")
        self.cpp_info.builddirs = ["lib/cmake/hgraph_lang", "lib/cmake/hgl"]
        self.cpp_info.bindirs = ["bin"]
