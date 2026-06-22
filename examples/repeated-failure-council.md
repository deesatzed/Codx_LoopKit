# Example: Repeated Failure Council

Trigger:

```text
The same test failed twice after two patches.
```

Expected Codex behavior:

```text
Council Trigger: repeated verifier failure.

Opposer: The likely issue is that we are patching symptoms.
First Principles: The proof requires the behavior, not the current implementation shape.
Expander: A smaller adapter-level fix may avoid broad refactor.
Outsider: The failing assertion names the contract directly.
Implementer: Inspect the tested public API, then patch only that boundary.

Final Ruling: Stop changing internals until the public contract is mapped.
Next Step: Read the failing test and the exported API together.
```
