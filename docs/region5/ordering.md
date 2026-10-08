# Region5-related ordering

## e4.2 `StateStore::PutStateSetting`

Direct static evidence from the preserved e4.2 `PutStateSetting` body proves that it constructs a setting with separate ID and value bytes, obtains a lower-bound insertion position, and inserts at that position. The recovered insertion/storage key is:

```text
(NeedlePos ascending, state ID ascending)
```

Here `NeedlePos ascending` means the native two-part NeedlePos comparison observed in the e4.2 comparator, not an assumed scalar representation. The state value is not read by the comparator. Lower-bound insertion places a new setting before the first equivalent key, so newly inserted exact-key duplicates precede older equivalents in storage.

This establishes **e4.2 insertion/storage order within the recovered `PutStateSetting` path**. It does not by itself prove how every e4.2 writer traverses the store.

## e1.5 writer traversal

The archived e1.5 import writer constructs the exported `StateSettingIter(StateStore const&)`, then repeatedly dereferences, serializes, and advances that iterator. This proves that the e1.5 writer emits the store's existing iterator/storage order.

The e1.5 writer evidence is not used to infer the e4.2 comparator. Conversely, the e4.2 comparator evidence is not presented as direct proof of the e4.2 writer path.

## Public model and round trip

`state_store.py` is a deterministic synthetic model of the proven e4.2 insertion/storage rule. It is not the proprietary native container or writer. `region5.py` preserves the order of records supplied to it during encode/decode round trips; that public invariant does not independently prove native StateStore-to-Region5 semantics.

## Distinct PhysicalFunction orders

PhysicalFunction analysis exposed two separate orderings:

- the MacroFunction component chain appends at the tail and preserves creation order;
- FunctionStore lower-bound insertion places a new equal-position/equal-type entry before older equivalent entries.

These structures should not be conflated.

## What is not proven

- that every Region5 record directly corresponds one-to-one with a StateStore entry;
- that the archived e1.5 comparator and e4.2 comparator are identical;
- the e4.2 native writer's exact traversal path;
- a complete source-level rule for every state ID and value;
- a universal ordering rule across unrelated containers;
- full semantic regeneration from source designs.
