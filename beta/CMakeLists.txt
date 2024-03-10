project("beta")

get_filename_component(CONANBUILDINFO_DIR "${CMAKE_BINARY_DIR}" PATH)
include(${CONANBUILDINFO_DIR}/conanbuildinfo.cmake)
option(BUILD_SHARED_LIBS "Build using shared libraries" ON)
add_library(beta src.cpp)
target_include_directories(beta PRIVATE ${CONAN_INCLUDE_DIRS_ALPHA})
target_link_directories(beta PRIVATE ${CONAN_LIB_DIRS_ALPHA})

set_target_properties(beta PROPERTIES PUBLIC_HEADER beta.h)
install(TARGETS beta PUBLIC_HEADER DESTINATION include)
