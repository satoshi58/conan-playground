from conans import ConanFile, CMake, tools
import os

class GammaConan(ConanFile):
    name = "gamma"
    version = "1.0.0"
    generators = "cmake"

    def requirements(self):
        self.requires("alpha/1.0.0")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="/home/user/conan-playground/gamma", build_folder="./_build/")
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.h",  dst="include", keep_path=False)
        self.copy("*.so", dst="lib", src="_build", keep_path=False)
