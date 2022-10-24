---
sidebar_label: rasa.shared.nlu.training_data.formats.dialogflow
title: rasa.shared.nlu.training_data.formats.dialogflow
---
## DialogflowReader Objects

```python
class DialogflowReader(TrainingDataReader)
```

Reader for NLU training data.

#### read

```python
def read(filename: Union[Text, Path], **kwargs: Any) -> "TrainingData"
```

Loads training data stored in the Dialogflow data format.

