from conans import ConanFile, CMake, tools
import os

class AlphaConan(ConanFile):
    name = "alpha"
    version = "1.0.0"

#    def requirements(self):
#        self.requires()

    def build(self):
        #self.run("cmake -B _build  .")
        #self.run("cmake --build _build")
        cmake = CMake(self)
        cmake.configure(source_folder="/home/user/conan-playground/alpha", build_folder="./_build/")
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.h",  dst="include", keep_path=False)
        self.copy("*.so", dst="lib", src="_build", keep_path=False)
