---
sidebar_label: rasa.cli.run
title: rasa.cli.run
---
#### add\_subparser

```python
def add_subparser(subparsers: SubParsersAction,
                  parents: List[argparse.ArgumentParser]) -> None
```

Add all run parsers.

**Arguments**:

- `subparsers` - subparser we are going to attach to
- `parents` - Parent parsers, needed to ensure tree structure in argparse

#### run

```python
def run(args: argparse.Namespace) -> None
```

Entrypoint for `rasa run`.

**Arguments**:

- `args` - The CLI arguments.

