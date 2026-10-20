# Language distribution

The language package consumes the separately installed hgraph SDK. Its CMake
package is `hgraph_lang`; `find_package(hgraph_lang CONFIG REQUIRED)` loads
`hgl_add_module()` and the native authoring targets. The executable is `hgl`.

- `conanfile.py` packages the compiler and requires `hgraph/0.8.34`.
- `docker/Dockerfile` builds that dependency from the extraction's pinned
  public source revision, installs the SDK, then independently builds the
  language package against it. The final image contains both installations.
- `smoke/consumer` builds and evaluates a generated module through the
  installed public CMake packages.
- `archive/homebrew` preserves the former, unshipped combined SDK/compiler
  formula and tap draft. It is historical preparation; establishing separate
  SDK and language formulas remains a release decision.

Build locally after shared-source setup:

```sh
python3 tools/shared_artifacts.py
docker build -f packaging/docker/Dockerfile -t hgraph-lang:local .
docker run --rm -v "$PWD/packaging/smoke:/work" hgraph-lang:local hgl test smoke.hgl
```

No workflow publishes a package, image, bottle or release.
