project("delta")

get_filename_component(CONANBUILDINFO_DIR "${CMAKE_BINARY_DIR}" PATH)
include(${CONANBUILDINFO_DIR}/conanbuildinfo.cmake)
option(BUILD_SHARED_LIBS "Build using shared libraries" ON)
add_library(delta src.cpp)
target_include_directories(delta PRIVATE
    ${CONAN_INCLUDE_DIRS_BETA}
    ${CONAN_INCLUDE_DIRS_GAMMA})
target_link_directories(delta PRIVATE
    ${CONAN_LIB_DIRS_BETA}
    ${CONAN_LIB_DIRS_GAMMA})

set_target_properties(delta PROPERTIES PUBLIC_HEADER delta.h)
install(TARGETS delta PUBLIC_HEADER DESTINATION include)
