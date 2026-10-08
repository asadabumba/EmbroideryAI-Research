# Portfolio perspective

## What can a company learn about this engineer from this repository?

### Reverse engineering

The project demonstrates disciplined recovery of x64 control flow, ABI arguments, vtables, RTTI, indirect calls, object ownership, and machine-specific dispatch without treating guessed labels as facts.

### Systems thinking

The work separates source semantics, object ownership, state ordering, physical serialization, and validation. This prevents a local byte-level success from being mistaken for a complete system model.

### Binary formats and Python

The public package provides deterministic codecs and parsers with explicit domain checks, canonical encoding, malformed-input rejection, typed data models, and synthetic examples.

### Testing and debugging

Tests target original failure mechanisms: ambiguous encodings, invalid widths, duplicate-order behavior, unsupported source mappings, and stateful command transitions. Counterexamples are retained rather than explained away.

### Evidence discipline

Every major conclusion is classified as proven, strongly supported, partial, hypothetical, or not proven; inconclusive experiments remain explicitly inconclusive. Private runtime failures are not converted into semantic evidence, and target-derived reconstruction is kept separate from native semantics.

### Working with incomplete information

The repository presents unfinished boundaries directly. The engineering signal is not “everything is solved”; it is the ability to narrow uncertainty, preserve provenance, design falsifiable tests, and avoid unsupported production claims.

### Communication

The documentation gives hiring managers a short path through architecture, verified results, limitations, reproducibility, and future milestones while preserving technical depth for specialist reviewers.

## Publication state

The public snapshot is licensed under the MIT License. Proprietary binaries, runtime captures, customer material, and private research evidence remain excluded.
