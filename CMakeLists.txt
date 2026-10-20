cmake_minimum_required(VERSION 3.25)
project(hgraph_lang VERSION 0.0.0 LANGUAGES C CXX)

include(CTest)
include(GNUInstallDirs)
include(CMakePackageConfigHelpers)
set(HGRAPH_LANG_RELEASE_VERSION "${PROJECT_VERSION}" CACHE STRING "HGL toolchain release version")
# The compiler is a downstream SDK consumer. No runtime source tree is used.
find_package(hgraph CONFIG REQUIRED)
add_subdirectory(language)

configure_package_config_file(cmake/hgraph_langConfig.cmake.in
    "${CMAKE_CURRENT_BINARY_DIR}/hgraph_langConfig.cmake"
    INSTALL_DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/hgraph_lang")
write_basic_package_version_file("${CMAKE_CURRENT_BINARY_DIR}/hgraph_langConfigVersion.cmake"
    VERSION "${HGRAPH_LANG_RELEASE_VERSION}" COMPATIBILITY SameMajorVersion)
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/hgraph_langConfig.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/hgraph_langConfigVersion.cmake"
    DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/hgraph_lang" COMPONENT Development)
