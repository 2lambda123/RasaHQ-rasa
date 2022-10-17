---
sidebar_label: rasa.core.policies.rule_policy
title: rasa.core.policies.rule_policy
---
## InvalidRule Objects

```python
class InvalidRule(RasaException)
```

Exception that can be raised when rules are not valid.

## RulePolicy Objects

```python
@DefaultV1Recipe.register(
    DefaultV1Recipe.ComponentType.POLICY_WITHOUT_END_TO_END_SUPPORT, is_trainable=True
)
class RulePolicy(MemoizationPolicy)
```

Policy which handles all the rules.

#### supported\_data

```python
 | @staticmethod
 | supported_data() -> SupportedData
```

The type of data supported by this policy.

**Returns**:

  The data type supported by this policy (ML and rule data).

#### get\_default\_config

```python
 | @staticmethod
 | get_default_config() -> Dict[Text, Any]
```

Returns the default config (see parent class for full docstring).

#### \_\_init\_\_

```python
 | __init__(config: Dict[Text, Any], model_storage: ModelStorage, resource: Resource, execution_context: ExecutionContext, featurizer: Optional[TrackerFeaturizer] = None, lookup: Optional[Dict] = None) -> None
```

Initializes the policy.

#### raise\_if\_incompatible\_with\_domain

```python
 | @classmethod
 | raise_if_incompatible_with_domain(cls, config: Dict[Text, Any], domain: Domain) -> None
```

Checks whether the domains action names match the configured fallback.

**Arguments**:

- `config` - configuration of a `RulePolicy`
- `domain` - a domain

**Raises**:

  `InvalidDomain` if this policy is incompatible with the domain

#### train

```python
 | train(training_trackers: List[TrackerWithCachedStates], domain: Domain, **kwargs: Any, ,) -> Resource
```

Trains the policy on given training trackers.

**Arguments**:

- `training_trackers` - The list of the trackers.
- `domain` - The domain.
  

**Returns**:

  The resource which can be used to load the trained policy.

#### predict\_action\_probabilities

```python
 | predict_action_probabilities(tracker: DialogueStateTracker, domain: Domain, rule_only_data: Optional[Dict[Text, Any]] = None, **kwargs: Any, ,) -> PolicyPrediction
```

Predicts the next action (see parent class for more information).

#### persist

```python
 | persist() -> None
```

Persists trained `RulePolicy`.

