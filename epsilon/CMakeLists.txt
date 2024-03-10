project("epsilon")

get_filename_component(CONANBUILDINFO_DIR "${CMAKE_BINARY_DIR}" PATH)
include(${CONANBUILDINFO_DIR}/conanbuildinfo.cmake)
option(BUILD_SHARED_LIBS "Build using shared libraries" ON)
add_library(epsilon src.cpp)
target_include_directories(epsilon PRIVATE
    ${CONAN_INCLUDE_DIRS_ALPHA}
    ${CONAN_INCLUDE_DIRS_DELTA})
target_link_directories(epsilon PRIVATE
    ${CONAN_LIB_DIRS_ALPHA}
    ${CONAN_LIB_DIRS_DELTA})

set_target_properties(epsilon PROPERTIES PUBLIC_HEADER epsilon.h)
install(TARGETS epsilon PUBLIC_HEADER DESTINATION include)
