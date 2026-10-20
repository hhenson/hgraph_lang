#pragma once

#include <string_view>

#ifndef HGL_RELEASE_VERSION
#define HGL_RELEASE_VERSION "0.0.0"
#endif

namespace hgl {
    inline constexpr std::string_view release_version_string = HGL_RELEASE_VERSION;
}
