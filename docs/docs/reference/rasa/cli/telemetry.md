---
sidebar_label: rasa.cli.telemetry
title: rasa.cli.telemetry
---
#### add\_subparser

```python
add_subparser(subparsers: SubParsersAction, parents: List[argparse.ArgumentParser]) -> None
```

Add all telemetry tracking parsers.

**Arguments**:

- `subparsers` - subparser we are going to attach to
- `parents` - Parent parsers, needed to ensure tree structure in argparse

#### inform\_about\_telemetry

```python
inform_about_telemetry(_: argparse.Namespace) -> None
```

Inform user about telemetry tracking.

#### disable\_telemetry

```python
disable_telemetry(_: argparse.Namespace) -> None
```

Disable telemetry tracking.

#### enable\_telemetry

```python
enable_telemetry(_: argparse.Namespace) -> None
```

Enable telemetry tracking.

