Parallel HGL authoring
----------------------

The HGL authoring milestone keeps existing C++ registrations in place.
``external/hgraph_spec_audit/catalogue/README.md`` is the maintained migration inventory;
`The language migration catalogue <https://github.com/hhenson/hgraph_lang/blob/main/language/docs/design/migration-catalogue.md>`_ records source and review drift. Declarations,
registration templates and expanded registry signatures are separate evidence.
A completed domain has a compiled HGL body or a binding to an HGL-exposed
native value function. A graph wrapper around a temporal operator stays pending.
Production replacement is a separate decision.

Scalar stream state, folds, arithmetic, conversions, collection queries and
calendar projections live in the parallel ``hgraph.std`` and
``hgraph.operators`` modules. Overload-specific aliases preserve algorithms
whose signatures cannot yet be consolidated. The catalogue names those aliases
and the remaining lifecycle, error, type and structural limitations.

Native ``signal`` arguments project the common endpoint. The C++ emitter
unwraps structural typed-view facades through their public ``base()`` accessor
when passing them to a native ``TSInputView`` parameter. Boolean set iteration
also converts C++ Boolean proxy references to the declared HGL Boolean value
before passing them to typed output/native operations. This permits metadata
queries before payload validity without reading or copying the payload.

Acceptance includes public C++ parity tests, source HGL tests and an installed
SDK consumer that recompiles the installed native and standard source parts.
The imported-module scripted tests use a dedicated CLI test host linked with
the native value provider; the build-time compiler remains independent of the
library it generates. The design record is
`migration-catalogue.md <https://github.com/hhenson/hgraph_lang/blob/main/language/docs/design/migration-catalogue.md>`_.
