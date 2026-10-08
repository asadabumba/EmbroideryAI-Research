# Final public release evidence audit

Date: 2026-10-08

## Release decision

The public snapshot is suitable for human review and publication as a research portfolio. It is not a production serializer, a complete native implementation, or a redistribution of proprietary software.

```text
NATIVE_SEMANTICS_PROVEN = false
production_authority = false
PRODUCTION_AUTHORITY = false
full native Region5 semantic regeneration = NOT PROVEN
production writer = DISABLED
```

## 1. Public snapshot

Repository-neutral audited snapshot path:

```text
<public-repository-root>
```

The publication-clean snapshot is preserved at the repository root. Public source code, documentation, and commands do not depend on a machine-specific filesystem path.

Final public file count: **36**, excluding `.venv`, caches, bytecode, build output, and generated package metadata.

## 2. Validation results

| Check | Result |
|---|---|
| Tests | **PASS — 29 passed** |
| Ruff | **PASS — All checks passed** |
| `compileall` | **PASS** |
| Local-path scan | **PASS — no machine-specific user path or staging-directory name detected** |
| Secret scan | **PASS — no credentials, private keys, access tokens, credential URLs, or private network addresses detected** |
| Proprietary-artifact scan | **PASS — no proprietary executable, library, dump, debug database, model, or embroidery-design artifact detected** |
| Documentation-link check | **PASS — all relative documentation links resolve** |
| Focused preserved PF17 static tests | **PASS — 14 passed** |

Validation commands for the public snapshot:

```bash
python -m pytest -q
python -m ruff check .
python -m compileall -q .
```

## 3. StateStore evidence conclusion

### e1.5 ordering evidence

The archived e1.5 import writer constructs the exported `StateSettingIter(StateStore const&)` and then advances, dereferences, and serializes entries in iterator order. This proves that the e1.5 writer emits the StateStore's existing iterator/storage order.

It does **not** independently prove the e1.5 comparator, duplicate policy, or the e4.2 implementation.

### e4.2 `StateStore::PutStateSetting`

The preserved e4.2 body at mod1 RVA `0x17C7B0` constructs a setting with separate ID and value bytes, calls the lower-bound helper at `0x17B070`, and inserts through the helper at `0x17B1B0`.

The lower-bound comparator directly establishes:

- native NeedlePos order first;
- state ID order second;
- state value is not part of the key;
- insertion occurs before the first equivalent key;
- a newly inserted exact-key duplicate therefore precedes older equivalents in storage.

This supports the scoped public wording:

```text
e4.2 StateStore insertion/storage order: PROVEN within PutStateSetting
e1.5 writer traversal of existing StateStore order: PROVEN
e4.2 writer traversal of StateStore: NOT PROVEN by this preserved evidence
cross-version comparator identity: NOT CLAIMED
```

### Round-trip ordering

The public Region5 codec preserves caller-supplied record order during deterministic encode/decode round trips. That public behavior does not prove that every native Region5 record corresponds one-to-one with a StateStore entry or that the e4.2 writer consumes the store identically to e1.5.

## 4. PF17 machine-family conclusion

The source closure remains correctly attributed to **SchiffliMachine**, not Barudan Z:

```text
Schiffli source MacroFunction tag byte1 0xA5
  -> primary selector 0x17
  -> secondary selector 0x18
  -> type-3 expansion request tag 0x1700
  -> PhysicalMachine::AddComponent
  -> PhysicalFunction.FunctionTag.byte1 0x17
```

The preserved ZTC counterexample maps the same source byte `0xA5` to `0x06/0x07`, proving that the mapping is machine-family-specific.

The Barudan Z evidence is a **separate downstream consumer/status path**:

- property ID `0x7F0` is bound to `TID_EMCH_BORER_NEEDLE`;
- the configured value is stored at `BarudanZMachine+0x354` / `BarudanMachineValues+0x14`;
- that configured borer-needle index is **PROVEN**;
- the PF17-derived `BarudanZStatus+0x48` value is compared with it;
- interpreting `BarudanZStatus+0x48` as the current/selected needle-slot index is **STRONGLY SUPPORTED**;
- the inspected Barudan Z source translator has no PF17-producing branch.

Therefore the Barudan evidence does not supersede or reattribute the Schiffli PF17 producer rule.

## 5. Major public claim hierarchy

| Major claim | Final classification | Scope |
|---|---|---|
| Region5 physical record grammar | **PROVEN** | Physical encoding only |
| Public physical record round trip | **PROVEN** | Preserves valid caller-supplied order and bytes |
| Native writer structure | **PROVEN** | Structural emission behavior; not semantic tuple generation |
| e4.2 StateStore insertion/storage order | **PROVEN** | `PutStateSetting` path only |
| e1.5 writer traversal of StateStore | **PROVEN** | Existing iterator/storage order |
| e4.2 writer traversal of StateStore | **NOT PROVEN** | Not inferred from e1.5 |
| PhysicalFunction tag, marker, and MacroFunction ownership flow | **PROVEN** | Recovered construction paths |
| Schiffli A5 to primary 17 / secondary 18 | **PROVEN** | Narrow e4.2 subclass/source domain |
| ZTC A5 to primary 06 / secondary 07 | **PROVEN** | Counterexample to a global A5 rule |
| Barudan Z configured borer-needle index | **PROVEN** | Property and field binding |
| `BarudanZStatus+0x48` as selected/current needle slot | **STRONGLY SUPPORTED** | Exact source-level member name unresolved |
| Barudan Z downstream PF17 status behavior | **PARTIAL** | Local count/delta and borer comparison established; complete Region5 consequence unresolved |
| Other machine-family status strategies | **PARTIAL** | Selected paths recovered; no complete cross-family closure claimed |
| Pocket table-driven strategy | **NOT PROVEN** | Current public evidence does not justify a closed claim |
| Full native Region5 semantic regeneration | **NOT PROVEN** | Source-independent tuple production remains incomplete |
| Production writer authority | **NOT PROVEN / DISABLED** | `production_authority = false` |

## 6. Public implementation conclusion

The reviewed modules are presented as independent public implementations or deterministic sanitized models:

- `region5.py` — deterministic physical codec; explicitly not semantic regeneration or a production writer;
- `state_store.py` — synthetic e4.2 insertion/storage-order model; explicitly not the proprietary native container or writer;
- `machine_rules.py` — narrow, fail-closed machine-family mappings with unsupported inputs rejected;
- `evidence.py` — independent provenance vocabulary for scoped claims;
- `dst.py` — independent offline parser using documented behavior and synthetic fixtures.

No module claims to reproduce proprietary native implementation code. No target-derived generator, recovered binary bytes, runtime dump, or proprietary source was added.

## 7. README positioning

The README continues to emphasize reverse engineering, binary analysis, Windows x64 ABI reasoning, static analysis, deterministic format reconstruction, provenance tracking, fail-closed behavior, Python tooling, and reproducible tests.

It does not claim that the system is fully reverse engineered, production-ready, or a complete native implementation.

Recommended GitHub description:

> Research tooling for reverse engineering native embroidery formats, machine-state semantics, and deterministic Region5 reconstruction.

## 8. License

```text
License: MIT
```

The project owner explicitly selected the MIT License. The repository includes the standard MIT text in `LICENSE` with copyright year 2026 and holder Rudolf. `pyproject.toml` and `CITATION.cff` record the same license identifier.

## 9. Remaining blockers

There are no evidence, test, artifact, secret, license, or documentation blockers to human review and GitHub publication.

```text
READY_FOR_GITHUB = YES
```
