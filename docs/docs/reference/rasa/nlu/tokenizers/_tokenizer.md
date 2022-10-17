---
sidebar_label: rasa.nlu.tokenizers._tokenizer
title: rasa.nlu.tokenizers._tokenizer
---
## Token Objects

```python
class Token()
```

#### set

```python
 | set(prop: Text, info: Any) -> None
```

Set property value.

#### get

```python
 | get(prop: Text, default: Optional[Any] = None) -> Any
```

Returns token value.

#### fingerprint

```python
 | fingerprint() -> Text
```

Returns a stable hash for this Token.

## Tokenizer Objects

```python
class Tokenizer(Component)
```

Base class for tokenizers.

#### \_\_init\_\_

```python
 | __init__(component_config: Dict[Text, Any] = None) -> None
```

Construct a new tokenizer using the WhitespaceTokenizer framework.

#### tokenize

```python
 | tokenize(message: Message, attribute: Text) -> List[Token]
```

Tokenizes the text of the provided attribute of the incoming message.

#### train

```python
 | train(training_data: TrainingData, config: Optional[RasaNLUModelConfig] = None, **kwargs: Any, ,) -> None
```

Tokenize all training data.

#### process

```python
 | process(message: Message, **kwargs: Any) -> None
```

Tokenize the incoming message.

