project("alpha")

option(BUILD_SHARED_LIBS "Build using shared libraries" ON)
add_library(alpha src.cpp)

set_target_properties(alpha PROPERTIES PUBLIC_HEADER alpha.h)
install(TARGETS alpha PUBLIC_HEADER DESTINATION include)
