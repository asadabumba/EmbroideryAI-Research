# PF17 source rule: Schiffli producer and Barudan Z consumer

## Classification

**PROVEN**, within a narrow e4.2 x64 `SchiffliMachine` domain. This result does not prove full Region5 semantic regeneration and does not authorize a production writer.

The machine-family attribution is explicit: **SchiffliMachine is the proven native source producer in this closure. BarudanZMachine is a separately recovered downstream PF17 consumer/status evaluator, not the producer established by this rule.**

## Source-to-destination chain

```text
SchiffliMachine source MacroFunction.FunctionTag.byte1 == 0xA5
  -> primary expansion selector 0x17
  -> secondary expansion selector 0x18
  -> applicable type-3 MacroExpansionRequest carries tag word 0x1700
  -> PhysicalMachine::AddComponent(tag, current NeedlePos, source MacroFunction, flag)
  -> PhysicalFunction.FunctionTag.byte1 == 0x17
```

The word `0x1700` is the little-endian two-byte FunctionTag with byte 1 equal to `0x17`.

## ABI and ownership concepts

`PhysicalMachine::AddComponent` receives the machine object, FunctionTag, NeedlePos, MacroFunction, and a boolean flag under the Windows x64 ABI. The path:

- allocates and initializes a PhysicalFunction;
- copies the complete FunctionTag;
- resolves the current NeedlePos to a shared StitchMarker;
- retains the marker in the PhysicalFunction;
- associates the PhysicalFunction with the source MacroFunction;
- submits the normal insertion through a transaction-mediated path.

A direct insertion variant constructs the same core object but bypasses transaction/history participation. Copy, replay, direct API, and import paths can carry `0x17`, but they do not independently establish its native source rule.

## Machine-specific dispatch

The source mapping is not global. A separate `ZTCMachine` dispatcher maps the same source byte differently:

```text
ZTC source 0xA5 -> primary 0x06 / secondary 0x07
```

This counterexample falsifies the rule “source `0xA5` always means PF17.” The correct statement is machine-family-specific.

## Marker multiplicity

The expansion process may emit zero, one, or multiple applicable requests depending on source pattern and state. Multiple PhysicalFunctions can share one marker when their current NeedlePos is unchanged; later position updates can produce different markers. No universal one-source-to-one-PF17 cardinality is claimed.

## Downstream boundary

A recovered Barudan Z status path can count predecessor markers containing PF17 and apply a local count-and-delta rule. Property ID `0x7F0` is bound to `TID_EMCH_BORER_NEEDLE`; the value is loaded into `BarudanZMachine+0x354` / `BarudanMachineValues+0x14` and compared with the PF17-derived `BarudanZStatus+0x48` value. The configured borer-needle field is proven; interpreting `BarudanZStatus+0x48` as the current/selected needle-slot index is strongly supported. Barudan Z's inspected source translator has no PF17 branch. This downstream rule therefore does not make Barudan Z a native PF17 producer, and it does not close final Region5 tuple generation.

## Evidence and publication boundary

The private research used validated function boundaries, ABI reconstruction, vtable/RTTI identity, import resolution, backward slicing, and behavioral regression checks. Raw binaries, memory ranges, hashes, local directories, and environment-specific details are not included here.

## Limitations

- The rule is bounded to the analyzed software family/version and machine subclass.
- No trustworthy business-semantic name for source byte `0xA5` is claimed.
- The rule selects an expansion pair; it does not prove a fixed number of resulting functions.
- Complete machine-state-to-Region5 tuple production remains unresolved.
- `NATIVE_SEMANTICS_PROVEN = false` project-wide.
- `PRODUCTION_AUTHORITY = false`.
