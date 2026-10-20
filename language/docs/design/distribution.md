# Distribution and deployment

The public `hgraph_lang` project owns the compiler, command-line tools,
language tests, native module support and language distribution inputs. It
consumes the installed public hgraph SDK. The runtime package does not depend
on this project and carries no compiler build option.

## Package boundary

`find_package(hgraph_lang CONFIG REQUIRED)` resolves the hgraph SDK and exposes
`hgl_add_module()` and the existing `hgl::` native authoring targets. Builds
use the SDK's exported include paths and link requirements; no runtime source
checkout is required. Compiler catalogue tooling may take a separate runtime
checkout as audit evidence through `--runtime-source`.

An installation contains:

```text
bin/hgl
include/hgl/
lib/libhgl_*
lib/cmake/hgl/
lib/cmake/hgraph_lang/
share/hgl/
```

The runtime SDK remains separately installed, possibly in the same prefix.
When consuming a PyArrow-backed SDK, configure with
`HGRAPH_USE_PYARROW_ARROW=ON` and the matching `Python_EXECUTABLE`.

## Versions and distribution inputs

The compiler reports its own `HGRAPH_LANG_RELEASE_VERSION` and the runtime API
version separately. `0.0.0` denotes an unversioned development build; creating
this repository does not publish a tagged release.

The Conan recipe requires the matching hgraph SDK. The container recipe builds
the pinned runtime as a separate dependency, then builds this package against
its installation. Both use the same installed consumer smoke case. CI builds
and tests; it does not publish packages or images.

The former combined-distribution plan is retained in
[the earlier record](distribution-before-extraction.md) and
[the original RFC](native-distribution-before-extraction.rst). Those plans and
the archived Homebrew draft describe the earlier combined package, not the
current project boundary. New native channel releases remain separate work.
