# Methodology

## Static discovery

The research begins with exhaustive references rather than guessed function names:

- enumerate direct and indirect xrefs;
- validate function ownership with x64 `.pdata` / `RUNTIME_FUNCTION` metadata;
- distinguish entries from interior instructions and switch-table data;
- reconstruct Windows x64 register and stack arguments;
- resolve imported calls through IAT entries and exact module identity;
- identify classes through vtables, Complete Object Locators, and RTTI descriptors.

## Dataflow reconstruction

For a candidate semantic rule:

1. Identify the source field.
2. Follow the field through machine-specific dispatch.
3. Track immediate values, pointers, and tag words across ABI boundaries.
4. Separate construction from copy, replay, import, or deserialization paths.
5. Bind the result to a concrete destination field.
6. Search for a counterexample in another machine family.

The PF17 closure follows this pattern from a source MacroFunction tag, through expansion requests, into `PhysicalMachine::AddComponent`, and finally to the PhysicalFunction tag field.

## Source-vs-target separation

A rule is native only if it is derived from source structures or independently established native behavior. The following are retrospective controls, not native semantics:

- target signatures;
- expected output bytes;
- lookup tables fitted from known targets;
- copied templates;
- target-derived topology;
- state-specific corrections selected by the expected output.

Retrospective controls can localize a problem, but cannot authorize production writing.

## Provenance classification

- **PROVEN:** direct scoped evidence, identity checks, and adversarial review support the claim.
- **STRONGLY SUPPORTED:** evidence converges but one link remains indirect or incomplete.
- **PARTIAL:** bounded subclaims are established, but the complete behavior remains unresolved.
- **HYPOTHESIS:** the claim is falsifiable and awaiting sufficient evidence.
- **NOT PROVEN:** available evidence does not establish the stated claim.
- **INCONCLUSIVE:** the experiment cannot support a semantic conclusion.

Instrumentation failure, timeout, missing output, failed attachment, or malformed capture remains technical evidence and is classified as inconclusive for semantics.

## Adversarial falsification

Review actively searches for:

- target leakage and overfitting;
- stale or substituted artifacts;
- wrong module/build identity;
- incorrect pointer, RVA, or function-boundary interpretation;
- copy/replay paths mistaken for native producers;
- vacuous tests;
- unsupported generalization across machine families.

The ZTC `0xA5 -> 0x06/0x07` mapping is a concrete counterexample that prevents promotion of the Schiffli PF17 rule into a universal mapping.

## Regression testing

Public tests execute only offline behavior with synthetic fixtures. They cover canonical encodings, malformed data, duplicate ordering, source-tag counterexamples, provenance categories, and machine-state transitions. Private runtime tests and proprietary evidence are intentionally excluded.
