# hgraph_lang

The public C++ implementation of the HGL language: compiler, command-line
tools, native-module support, tests and distribution tooling. It consumes the
installed [hgraph C++ SDK](https://github.com/hhenson/hgraph); hgraph does not
depend on this project.

## Build

Install the hgraph SDK and its dependencies, then configure this project:

```sh
git submodule update --init --recursive
cmake --preset release -DCMAKE_PREFIX_PATH=/path/to/hgraph-sdk
cmake --build --preset release --parallel
ctest --preset release
cmake --install build --prefix /path/to/hgraph-lang
```

The compiler requires C++23, CMake 3.25 or newer, clang-format, and simdjson
(the native hgraph SDK normally resolves it). Parser and
line-editor dependencies are pinned in `language/CMakeLists.txt`. Use
`HGL_ENABLE_LINE_EDITING=OFF` for a plain-input REPL.

The executable remains `hgl`; generated modules and native authoring retain
their existing APIs. [Language documentation](language/README.md), the
[shared specification](https://github.com/hhenson/hgraph_spec), and the
[portable standard library](https://github.com/hhenson/hgraph_std) retain their
own boundaries. Runtime conformance belongs to the runtime; compiler
conformance belongs here.

Catalogue review takes runtime sources explicitly as evidence:

```sh
python3 tools/hgl_catalogue.py --runtime-source /path/to/hgraph --check
```

[SOURCE.json](SOURCE.json) records the original hgraph revision, file locations
and hashes. Existing source history remains available in that repository.
