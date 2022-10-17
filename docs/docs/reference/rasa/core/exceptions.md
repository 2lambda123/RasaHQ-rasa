---
sidebar_label: rasa.core.exceptions
title: rasa.core.exceptions
---
## AgentNotReady Objects

```python
class AgentNotReady(RasaCoreException)
```

Raised if someone tries to use an agent that is not ready.

An agent might be created, e.g. without an processor attached. But
if someone tries to parse a message with that agent, this exception
will be thrown.

#### \_\_init\_\_

```python
 | __init__(message: Text) -> None
```

Initialize message attribute.

## ChannelConfigError Objects

```python
class ChannelConfigError(RasaCoreException)
```

Raised if a channel is not configured correctly.

## InvalidTrackerFeaturizerUsageError Objects

```python
class InvalidTrackerFeaturizerUsageError(RasaCoreException)
```

Raised if a tracker featurizer is incorrectly used.

