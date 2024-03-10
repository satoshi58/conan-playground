project("gamma")

get_filename_component(CONANBUILDINFO_DIR "${CMAKE_BINARY_DIR}" PATH)
include(${CONANBUILDINFO_DIR}/conanbuildinfo.cmake)
option(BUILD_SHARED_LIBS "Build using shared libraries" ON)
add_library(gamma src.cpp)
target_include_directories(gamma PRIVATE ${CONAN_INCLUDE_DIRS_ALPHA})
target_link_directories(gamma PRIVATE ${CONAN_LIB_DIRS_ALPHA})

set_target_properties(gamma PROPERTIES PUBLIC_HEADER gamma.h)
install(TARGETS gamma PUBLIC_HEADER DESTINATION include)
