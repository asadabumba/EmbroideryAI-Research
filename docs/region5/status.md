# Region5 semantic status

## Closed boundary

The physical record grammar is proven. The e4.2 `PutStateSetting` insertion/storage rule and the e1.5 writer's traversal of existing iterator order are also proven within their separate versioned scopes. They are represented by deterministic public models and tests.

## Open boundary

The unresolved problem is native production of complete `(first, second, third)` records from arbitrary source designs and machine families. The remaining work includes:

- exact source of each state ID;
- exact source and narrowing rules for each value;
- machine-family dispatch and table semantics;
- complete NeedlePos-to-record relationships;
- validation on unseen source cases without target-derived lookup.

## Machine-specific behavior

The Schiffli/ZTC `0xA5` counterexample proves that source-tag interpretation depends on the machine family. Rules must be recovered and tested per subclass; a shared numeric tag does not imply shared semantics.

## Publication flags

```text
NATIVE_SEMANTICS_PROVEN = false
PRODUCTION_AUTHORITY = false
```

The public codec can round-trip physical data, but no public production writer is enabled.
