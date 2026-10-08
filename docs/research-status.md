# Research status

## Status table

| Area | Classification | Public conclusion |
|---|---|---|
| Region5 physical grammar | PROVEN | Canonical ULEB32 of uint32(int32), followed by two raw bytes |
| Region5 record round trip | PROVEN | Exact for valid physical records; semantic meaning is not implied |
| Writer structure | PROVEN | Structural emission path recovered; semantic tuple production remains incomplete |
| e4.2 StateStore insertion/storage order | PROVEN | `PutStateSetting` lower-bound order uses native NeedlePos then ID; value is excluded; a new exact-key duplicate is inserted before older equivalents |
| e1.5 writer traversal | PROVEN | The writer constructs a `StateSettingIter` from the StateStore and serializes entries in existing iterator/storage order |
| e4.2 writer traversal | NOT PROVEN | The preserved `PutStateSetting` body proves insertion/storage behavior, not the e4.2 writer's consumption path |
| PhysicalFunction marker ownership | PROVEN | PhysicalFunctions retain shared StitchMarkers selected by NeedlePos |
| MacroFunction physical-component ownership | PROVEN | Ownership/list linkage is distinct from FunctionStore insertion |
| Schiffli source A5 to PF17 | PROVEN | Narrow e4.2 native producer rule: A5 selects primary 17 / secondary 18 |
| ZTC source A5 mapping | PROVEN | Counterexample maps to 06/07, not 17/18 |
| Barudan Z downstream PF17 history rule | PARTIAL | Local PF17-consuming count-and-delta behavior and the configured borer slot are proven; this is not a Barudan Z PF17 source rule and the complete Region5 consequence remains unresolved |
| Direct machine-state strategies | PARTIAL | Current publishable evidence does not establish a closed count |
| Pocket table-driven strategy | INCONCLUSIVE | Current checkpoint does not justify a CLOSED claim |
| Other machine-family strategies | PARTIAL | Dispatch structures exist, exact tuple rules remain incomplete |
| Full native Region5 semantic regeneration | NOT PROVEN | Source-independent tuple production is incomplete |
| Production writer | DISABLED | `PRODUCTION_AUTHORITY = false` |

## Global flags

```text
NATIVE_SEMANTICS_PROVEN = false
REGION5_NATIVE_SEMANTICS_PROVEN = false
PRODUCTION_AUTHORITY = false
```

## What changed for publication

The public snapshot preserves verified conclusions while removing private paths, hashes, capture directories, proprietary artifact inventories, raw evidence, runtime orchestration, and retrospective generators. No private claim was promoted during sanitization.
