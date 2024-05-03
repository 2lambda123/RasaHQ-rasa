All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](https://semver.org/) starting with version 1.0.

<!-- You should **NOT** be adding new change log entries to this file, this
file is managed by ``towncrier``.

You **may** edit previous change logs to fix problems like typo corrections or such.
You can find more information on how to add a new change log entry at
https://github.com/RasaHQ/rasa-private/tree/main/changelog/ . -->

<!-- TOWNCRIER -->

## [3.8.5] - 2024-05-03
                       
Rasa Pro 3.8.5 (2024-05-03)                            
### Bugfixes
- [#575](https://github.com/rasahq/rasa/issues/575): Trigger `pattern_internal_error` if collection does not exist in a Qdrant vector store.


## [3.8.4] - 2024-04-30
                       
Rasa Pro 3.8.4 (2024-04-30)                            
### Improvements
- [#542](https://github.com/rasahq/rasa/issues/542): Added support for NLU Triggers by supporting uploading the NLU files for CALM Assistants


## [3.8.3] - 2024-04-26
                       
Rasa Pro 3.8.3 (2024-04-26)                            
### Improvements
- [#538](https://github.com/rasahq/rasa/issues/538): * Throw validation error and exit when duplicate responses are found across domains. This is a breaking change, as it will cause training to fail if duplicate responses are found. If you have duplicate responses in your training data, you will need to remove them before training.
  * Update domain importing to ignore the warnings about duplicates when merging with the default flow domain

### Bugfixes
- [#515](https://github.com/rasahq/rasa/issues/515): Use AzureChatOpenAI class instead of AzureOpenAI class to instantiate openai models deployed in Azure. This fixes the usage of gpt-3.5-turbo model in Azure.
- [#518](https://github.com/rasahq/rasa/issues/518): Fixes validation to catch empty placeholders in response that dumps entire context.
- [#532](https://github.com/rasahq/rasa/issues/532): Fix security vulnerabilities by updating poetry environment:
  fonttools, CVE-2023-45139, from 4.40.0 to 4.43.0
  aiohttp, CVE-2024-27306, from 3.9.3 to 3.9.4
  dnspython, CVE-2023-29483, from 2.3.0 to 2.6.1
  pymongo, CVE-2024-21506, from 4.3.3 to 4.6.3
- [#540](https://github.com/rasahq/rasa/issues/540): Numbers that are part of the body of the LLM answer in EnterpriseSearch should not be matched as citation references in the postprocessing method.
- [#552](https://github.com/rasahq/rasa/issues/552): Errors from the Flow Retrieval API are now both logged and thrown. When such errors occur, an ErrorCommand is emitted by the Command Generator.


## [3.8.2] - 2024-04-25
                       
Rasa Pro 3.8.2 (2024-04-25)                            
### Bugfixes
- [#1013](https://github.com/rasahq/rasa/issues/1013): Add the currently active flow as well as the called flow (if present) to the 
  list of available flows for the `LLMCommandGenerator`.
- [#533](https://github.com/rasahq/rasa/issues/533): Fix custom prompt not read from the model resource path for LLMCommandGenerator.


## [3.8.1] - 2024-04-17
                       
Rasa Pro 3.8.1 (2024-04-17)                            
### Improvements
- [#441](https://github.com/rasahq/rasa/issues/441): Adjusted chat widget behavior to remain open when clicking outside the chat box area.
- [#468](https://github.com/rasahq/rasa/issues/468): Improve debug logs to include information about evaluation of `if-else` conditions in flows at runtime.
- [#893](https://github.com/rasahq/rasa/issues/893): Remove the `ContextualResponseRephraser` from the tutorial template to keep it simple as it is not needed anymore.

### Bugfixes
- [#441](https://github.com/rasahq/rasa/issues/441): Introduced support for numbered Markdown lists.
- [#481](https://github.com/rasahq/rasa/issues/481): Added support for uploading assistants with default domain directory.

### Miscellaneous internal changes
- [#403](https://github.com/rasahq/rasa/issues/403), [#436](https://github.com/rasahq/rasa/issues/436), [#452](https://github.com/rasahq/rasa/issues/452), [#457](https://github.com/rasahq/rasa/issues/457), [#475](https://github.com/rasahq/rasa/issues/475), [#501](https://github.com/rasahq/rasa/issues/501)


## [3.8.0] - 2024-04-03

Rasa Pro 3.8.0 (2024-04-03)
### Features
- [#324](https://github.com/rasahq/rasa/issues/324): Introduces **semantic retrieval of flows** at runtime to reduce the size of the prompt sent to the LLM by utilizing similarity between vector embeddings. It enables the assistant to scale to a large number of flows.

  Flow retrieval is **enabled by default**. To configure it, you can modify the settings under the `flow_retrieval`
  property of `LLMCommandGenerator` component. For detailed configuration options, refer to our
  [documentation](https://rasa.com/docs/rasa-pro/concepts/dialogue-understanding#customizing-flow-retrieval).

  Introduces `always_include_in_prompt` field to the
  [flow definition](https://rasa.com/docs/rasa-pro/concepts/flows/#flow-properties).
  If field is set to `true` and the [flow guard](https://rasa.com/docs/rasa-pro/concepts/starting-flows/#flow-guards)
  defined in the `if` field evaluates to `true`, the flow will be included in the prompt.
- [#697](https://github.com/rasahq/rasa/issues/697): Introduction of coexistence between CALM and NLU-based assistants.
  Coexistence allows you to use policies from both CALM and NLU-based assistants in a single assistant. This allows migrating from NLU-based paradigm to CALM in an iterative fashion.

- [#762](https://github.com/rasahq/rasa/issues/762): Introduction of `call` step.
  You can use a `call` step to embed another flow.
  When the execution reaches a `call` step, Rasa starts the called flow.
  Once the called flow is complete, the execution continues with the calling flow.

### Improvements
- [#214](https://github.com/rasahq/rasa/issues/214): Instrument the `command_processor` module, in particular the following functions:
  - `execute_commands`
  - `clean_up_commands`
  - `validate_state_of_commands`
  - `remove_duplicated_set_slots`
- [#231](https://github.com/rasahq/rasa/issues/231): Improve the instrumentation of `LLMCommandGenerator`:
  - extract more LLM configuration parameters, e.g. `type`, `temperature`, `request-timeout`, `engine` and `deployment` (the latter 2 being only for the Azure OpenAI service).
  - instrument the private method `_check_commands_against_startable_flows` to track the commands with which the LLM responded, as well as the startable flow ids.
- [#238](https://github.com/rasahq/rasa/issues/238): Instrument `flow_executor.py` module, in particular these functions:
  - `advance_flows()`: extract `available_actions` tracing tag
  - `advance_flows_until_next_action()`: extract action name and score, metadata and prediction events as tracing tags from the returned prediction value
  - `run_step()`: extract step custom id, description and current flow id.
- [#241](https://github.com/rasahq/rasa/issues/241): Instrument `Policy._prediction()` method for each of the policy subclasses.
- [#247](https://github.com/rasahq/rasa/issues/247): Instrument `IntentlessPolicy` methods such as:
  - `find_closest_response`: extract the `response` and `score` from the returned tuple;
  - `select_response_examples`: extract the `ai_response_examples` from returned value;
  - `select_few_shot_conversations`: extract the `conversation_samples` from returned value;
  - `extract_ai_responses`: extract the `ai_responses` from returned value;
  - `generate_answer`: extract the `llm_response` from returned value.
- [#251](https://github.com/rasahq/rasa/issues/251): 1. Instrument `InformationRetrieval.search` method for supported vector stores: extract query and document metadata tracing attributes.
  2. Instrument `EnterpriseSearchPolicy._generate_llm_answer` method: extract LLM config tracing attributes.
  3. Extract dialogue stack current context in the following functions:
  - `rasa.dialogue_understanding.processor.command_processor.clean_up_commands`
  - `rasa.core.policies.flows.flow_executor.advance_flows`
  - `rasa.core.policies.flows.flow_executor.run_step`
- [#253](https://github.com/rasahq/rasa/issues/253): 1. Instrument `NLUCommandAdapter.predict_commands` method and extract the `commands` from the returned value, as well as the user message `intent`.
  2. Improve LLM config tracing attribute extraction for `ContextualResponseRephraser`.
- [#257](https://github.com/rasahq/rasa/issues/257): Add new config boolean property `trace_prompt_tokens` that would enable the tracing of the length of the prompt tokens for the following components:
  - `LLMCommandGenerator`
  - `EnterpriseSearchPolicy`
  - `IntentlessPolicy`
  - `ContextualResponseRephraser`
- [#274](https://github.com/rasahq/rasa/issues/274): Enable execution of single E2E tests by including the test case name in the path to test cases, like so: `path/to/test_cases.yml::test_case_name` or `path/to/folder_containing_test_cases::test_case_name`.
- [#277](https://github.com/rasahq/rasa/issues/277): Implement `MetricInstrumentProvider` interface whose role is to:
  - register instruments during metrics configuration
  - retrieve the appropriate instrument to record measurements in the relevant instrumentation code section
- [#279](https://github.com/rasahq/rasa/issues/279): Enabled the setting of a minimum similarity score threshold for retrieved documents in Enterprise Search's `vector_store` with the addition of the `threshold` property. If no documents are retrieved, it triggers Pattern Cannot Handle. This feature is supported in Milvus and Qdrant vector stores.
- [#282](https://github.com/rasahq/rasa/issues/282): Record measurements for the following metrics in the instrumentation code:
  - CPU usage of the `LLMCommandGenerator`
  - memory usage of `LLMCommandGenerator`
  - prompt token usage of `LLMCommandGenerator`
  - method call duration for LLM specific calls (in `LLMCommandGenerator`, `EnterpriseSearchPolicy`, `IntentlessPolicy`, `ContextualResponseRephraser`)
  - rasa client request duration
  - rasa client request body size

  Instrument `EndpointConfig.request()` method call in order to measure the client request metrics.
- [#307](https://github.com/rasahq/rasa/issues/307): Improvements around default behaviour of `ChitChatAnswerCommand()`:
  - The command processor will issue `CannotHandleCommand()` instead of the `ChitChatCommand()` when `pattern_chitchat` uses
  an action step `action_trigger_chitchat` without the `IntentlessPolicy` being configured. During training a warning is
  raised.
  - Changed the default pattern_chitchat to:
  ```yaml
  pattern_chitchat:
    description: handle interactions with the user that are not task-oriented
    name: pattern chitchat
    steps:
      - action: action_trigger_chitchat
  ```
  - Default rasa init template for CALM comes with `IntentlessPolicy` added to pipeline.
- [#311](https://github.com/rasahq/rasa/issues/311): Add support for OTLP Collector as metrics receiver which can forward metrics to the chosen metrics backend, e.g. Prometheus.
- [#342](https://github.com/rasahq/rasa/issues/342): Enable document source citation for Enterprise Search knowledge answers by setting the boolean `citation_enabled: true` property in the `config.yml` file:

  ```yaml
  policies:
    - name: EnterpriseSearchPolicy
      citation_enabled: true
  ```
- [#405](https://github.com/rasahq/rasa/issues/405): Add telemetry events for flow retrieval and call step
- [#410](https://github.com/rasahq/rasa/issues/410): Tighten python dependency constraints in `pyproject.toml`, hence reducing the installation time to
  around 20 minutes with `pip` (and no caching enabled).
- [#420](https://github.com/rasahq/rasa/issues/420): Improved tracing clarity of the Contextual Response Rephraser by adding the `_create_history` method span, including its LLM configuration attributes.
- [#682](https://github.com/rasahq/rasa/issues/682): Users now have enhanced control over the debugging process of LLM-driven components. This update introduces a fine-grained, customizable logging that can be controlled through specific environment variables.

  For example, set the `LOG_LEVEL_LLM` environment variable to enable detailed logging at the desired level for all the LLM components or specify the component you are debugging:

  ## Example configuration
  ```bash
  export LOG_LEVEL_LLM=DEBUG
  export LOG_LEVEL_LLM_COMMAND_GENERATOR=INFO
  export LOG_LEVEL_LLM_ENTERPRISE_SEARCH=INFO
  export LOG_LEVEL_LLM_INTENTLESS_POLICY=DEBUG
  export LOG_LEVEL_LLM_PROMPT_REPHRASER=DEBUG
  ```
- [#780](https://github.com/rasahq/rasa/issues/780): If the user wants to chat with the assistant at the end of `rasa init`,
  we are now calling `rasa inspect` instead of `rasa shell`.
- [#827](https://github.com/rasahq/rasa/issues/827): A slot can now be collected via an action `action_ask_<slot-name>` instead of the utterance
  `utter_ask_<slot-name>` in a collect step.
  You can either define an utterance or an action for the collect step in your flow.
  Make sure to add your custom action `action_ask_<slot-name>` to the domain file.
- [#953](https://github.com/rasahq/rasa/issues/953): Validate the configuration of the coexistence router before the actual training starts.
- [#966](https://github.com/rasahq/rasa/issues/966): Improved error handling in Enterprise Search Policy, changed the prompt to improve formatting of documents and ensured empty slots are not added to the prompt.
- [#390](https://github.com/rasahq/rasa-private/issues/390): Implement asynchronous graph execution. CALM assistants rely on a lot
  of I/O calls (e.g. to a LLM service), which impaired performances. With this change, we've improved the response time performance
  by 10x. All policies and components now support async calling.
- [#184](https://github.com/rasahq/rasa-private/issues/184): Merge `rasa` and `rasa-plus` packages into one. As a result, we renamed
  the Python package to `rasa-pro` and the Docker image to `rasa-pro`. Please head over to the migration guide
  [here](https://rasa.com/docs/rasa-pro/migration-guide#installation) for installation,
  and [here](https://rasa.com/docs/rasa-pro/migration-guide#component-yaml-configuration-changes) for the necessary configuration updates.

### Bugfixes
- [#232](https://github.com/rasahq/rasa/issues/232): Updated pillow and jinja2 packages to address security vulnerabilities.
- [#273](https://github.com/rasahq/rasa/issues/273): Fix OpenTelemetry `Invalid type NoneType for attribute value` warning.
- [#309](https://github.com/rasahq/rasa/issues/309): Add support for `metadata_payload_key` for Qdrant Vector Store with an error message if `content_payload_key` or `metadata_payload_key` are incorrect
- [#310](https://github.com/rasahq/rasa/issues/310): Changed the ordering of returned events to order by ID (previously timestamp) in SQL Tracker Store
- [#319](https://github.com/rasahq/rasa/issues/319): Improved the end-to-end test comparison mechanism to accurately handle and strip trailing newline characters from expected bot responses, preventing false negatives due to formatting mismatches.
- [#346](https://github.com/rasahq/rasa/issues/346): Fixed a bug that caused inaccurate search results in Enterprise Search when a bot message appeared before the last user message.
- [#347](https://github.com/rasahq/rasa/issues/347): Fixes flow guards pypredicate evaluatation bug: pypredicate was evaluated with `Slot` instances instead of slot values
- [#383](https://github.com/rasahq/rasa/issues/383): Post-process source citations in Enterprise Search Policy responses so that they are enumerated in the correct order.
- [#398](https://github.com/rasahq/rasa/issues/398): Resolves issue causing the `FlowRetrieval.populate` to always use default embeddings.
- [#407](https://github.com/rasahq/rasa/issues/407): Fix the bug with the validation of routing setup crashing when the pipeline is not specified (null)
- [#408](https://github.com/rasahq/rasa/issues/408): Remove conversation turns prior to a restart when creating a conversation transcript for an LLM call.

  This helps in cases where the prior conversation is not relevant for the
  current session. Information which should be carried to the next session
  should explicitly be stored in slots.
- [#415](https://github.com/rasahq/rasa/issues/415): Add tracker back to the LLMCommandGenerator.parse_command to ensure compatibility with custom command generator built
  with 3.7.
- [#419](https://github.com/rasahq/rasa/issues/419): Move coexistence routing setup validation from `rasa.validator.Validator` to
  `rasa.engine.validation`. This gave access to graph schema which allowed for
  validation checks of subclassed routers.
- [#427](https://github.com/rasahq/rasa/issues/427): Fixes a bug in determining the name of the model based on provided parameters.
- [#592](https://github.com/rasahq/rasa/issues/592): `LogisticRegressionClassifier` checks if training examples are present during training and logs a
  warning in case no training examples are provided.
- [#771](https://github.com/rasahq/rasa/issues/771): Fixes the bug that resulted in an infinite loop on a collect step in a flow with a flow guard set to `if: False`.
- [#778](https://github.com/rasahq/rasa/issues/778): Fix training the enterprise search policy multiple times with a different
  source folder name than the default name "docs".
- [#871](https://github.com/rasahq/rasa/issues/871): Log message `llm_command_generator.predict_commands.finished` is set to debug log by default.
  To enable logging of the `LLMCommandGenerator` set `LOG_LEVEL_LLM_COMMAND_GENERATOR` to `INFO`.
- [#892](https://github.com/rasahq/rasa/issues/892): Improvements and fixes to cleaning up commands:

  - Clean up predicted `StartFlow` commands from the `LLMCommandGenerator` if the flow, that should
  be started, is already active.
  - Clean up predicted SetSlot commands from the `LLMCommandGenerator` if the value of the slot is
  already set on the tracker.
  - Use string comparison for slot values to make sure to capture cases when the `LLMCommandGenerator`
  predicted a string value but the value set on the tracker is, for example, an integer value.
- [#907](https://github.com/rasahq/rasa/issues/907): Remove `context` from list of `restricted` slots
- [#931](https://github.com/rasahq/rasa/issues/931): Improved handling of categorical slots with text values when using CALM.

  Slot values extracted by the command generator (LLM) will be stored in the
  same casing as the casing used to define the categorical slot values in the
  domain. E.g. A categorical slot defined to store the values ["A", "B"]
  will store "A" if the LLM predicts the slot to be filled with "a". Previously,
  this would have stored "a".

### Miscellaneous internal changes
- [#227](https://github.com/rasahq/rasa/issues/227), [#236](https://github.com/rasahq/rasa/issues/236), [#280](https://github.com/rasahq/rasa/issues/280), [#322](https://github.com/rasahq/rasa/issues/322), [#325](https://github.com/rasahq/rasa/issues/325), [#385](https://github.com/rasahq/rasa/issues/385), [#386](https://github.com/rasahq/rasa/issues/386), [#424](https://github.com/rasahq/rasa/issues/424)


## [3.7.9] - 2024-03-26

Rasa Pro 3.7.9 (2024-03-26)
### Improvements
- [#359](https://github.com/rasahq/rasa/issues/359): Add validations for flow ID to allow only alphanumeric characters, underscores, and hyphens except for the first character.

### Bugfixes
- [#310](https://github.com/rasahq/rasa/issues/310): Changed the ordering of returned events to order by ID (previously timestamp) in SQL Tracker Store
- [#352](https://github.com/rasahq/rasa/issues/352): Fixes flow guards pypredicate evaluatation bug: pypredicate was evaluated with `Slot` instances instead of slot values
- [#369](https://github.com/rasahq/rasa/issues/369): Improved handling of categorical slots with text values when using CALM.

  Slot values extracted by the command generator (LLM) will be stored in the
  same casing as the casing used to define the categorical slot values in the
  domain. E.g. A categorical slot defined to store the values ["A", "B"]
  will store "A" if the LLM predicts the slot to be filled with "a". Previously,
  this would have stored "a".
- [#871](https://github.com/rasahq/rasa/issues/871): Log message `llm_command_generator.predict_commands.finished` is set to debug log by default.
  To enable logging of the `LLMCommandGenerator` set `LOG_LEVEL_LLM_COMMAND_GENERATOR` to `INFO`.
- [#892](https://github.com/rasahq/rasa/issues/892): Improvements and fixes to cleaning up commands:

  - Clean up predicted `StartFlow` commands from the `LLMCommandGenerator` if the flow, that should
  be started, is already active.
  - Clean up predicted SetSlot commands from the `LLMCommandGenerator` if the value of the slot is
  already set on the tracker.
  - Use string comparison for slot values to make sure to capture cases when the `LLMCommandGenerator`
  predicted a string value but the value set on the tracker is, for example, an integer value.

## [3.7.8] - 2024-02-28

Rasa Pro 3.7.8 (2024-02-28)
### Improvements
- [#259](https://github.com/rasahq/rasa/issues/259): Improved UX around ClarifyCommand by checking options for existence and ordering them. Also, now dropping Clarify commands if there are any other commands to prevent two questions or statements to be uttered at the same time.
- [#266](https://github.com/rasahq/rasa/issues/266): LLMCommandGenerator returns CannotHandle() command when is encountered with scenarios where
  it is unable to predict a valid command.

### Bugfixes
- [#228](https://github.com/rasahq/rasa/issues/228): Replace categorical slot values in a predicate with lower case replacements. This fixes the case sensitive slot comparisons in flow guards, branches in flows and slot rejections.
- [#270](https://github.com/rasahq/rasa/issues/270): Modify flows YAML schema to make next step mandatory to noop step.
- [#272](https://github.com/rasahq/rasa/issues/272): Flush messages when Kafka producer is closed. This is to ensure that all messages in the producer's internal queue are sent to the broker.
  Ensure to import all pattern stack frame subclasses of `DialogueStackFrame` when retrieving tracker from the tracker store, a required step during `rasa export`.
- [#1060](https://github.com/rasahq/rasa-plus/issues/1060): Add support for `metadata_payload_key` for Qdrant Vector Store with an error message if `content_payload_key` or `metadata_payload_key` are incorrect


## [3.7.7] - 2024-02-06

Rasa Pro 3.7.7 (2024-02-06)
### Bugfixes
- [#232](https://github.com/rasahq/rasa/issues/232): Updated pillow and jinja2 packages to address security vulnerabilities.


## [3.7.6] - 2024-02-01

Rasa Pro 3.7.6 (2024-02-01)
### Bugfixes
- [#144](https://github.com/rasahq/rasa/issues/144): Fix reported issue, e.g. https://github.com/RasaHQ/rasa/issues/5461 in Rasa Pro:
  Do not unpack json payload if `data` key is not present in the response custom output payloads when using socketio channel.
  This allows assistants which use custom output payloads to work with the Rasa Inspector debugging tool.
- [#206](https://github.com/rasahq/rasa/issues/206): Make flow description a required property in the flow json schema.
- [#778](https://github.com/rasahq/rasa/issues/778): Fix training the enterprise search policy multiple times with a different
  source folder name than the default name "docs".

### Miscellaneous internal changes
- [#223](https://github.com/rasahq/rasa/issues/223)


## [3.7.5] - 2024-01-24

Rasa Pro 3.7.5 (2024-01-24)
### Improvements
- [#193](https://github.com/rasahq/rasa/issues/193): Add new embedding types: `huggingface` and `huggingface_bge`. These new types import the `HuggingFaceEmbeddings` and `HuggingFaceBgeEmbeddings` embedding classes from Langchain.

### Bugfixes
- [#189](https://github.com/rasahq/rasa/issues/189): Fixes a bug that caused the `full_retrieval_intent_name` key to be missing in the published event. Rasa Analytics makes use of this key to get the Retrieval Intent Name
- [#196](https://github.com/rasahq/rasa/issues/196): Pin `grpcio` indirect dependency to `1.56.2` to address [CVE-2023-33953](https://www.cve.org/CVERecord?id=CVE-2023-33953)
  Pin `aiohttp` to version `3.9.0` to address [CVE-2023-49081](https://www.cve.org/CVERecord?id=CVE-2023-49081)
- [#771](https://github.com/rasahq/rasa/issues/771): Fixes the bug that resulted in an infinite loop on a collect step in a flow with a flow guard set to `if: False`.
- [#1029](https://github.com/rasahq/rasa-plus/issues/1029): Changed the parameters request timeout to 10 seconds and maximum number of retries to 1 for the default LLM used by Enterprise Search Policy. Any error during vector search or LLM API calls should now trigger the pattern `pattern_internal_error`. Updated the default enterprise search policy prompt to respond more succinctly to queries.


## [3.7.4] - 2024-01-03

Rasa Pro 3.7.4 (2024-01-03)
### Improvements
- [#142](https://github.com/rasahq/rasa/issues/142): Add embeddings type `azure` to simplify azure configurations, particularly when using Enterprise Search Policy

### Bugfixes
- [#161](https://github.com/rasahq/rasa/issues/161): Add a validation in `rasa data validate` to check the LinkFlowStep refers to a valid flow ID


## [3.7.3] - 2023-12-21

Rasa Pro 3.7.3 (2023-12-21)
### Improvements
- [#133](https://github.com/rasahq/rasa/issues/133): Persist prompt as part of the model and reread prompt from the model storage instead of original file path during loading. Impacts LLMCommandGenerator.
- [#141](https://github.com/rasahq/rasa/issues/141): Replaced soon to be depracted text-davinci-003 model with gpt-3.5-turbo. Affects components - LLM Intent Classifier and Contextual Response Rephraser.

### Bugfixes
- [#990](https://github.com/rasahq/rasa-plus/issues/990): Fix stale cache of local knowledge base used by EnterpriseSearchPolicy by implementing the `fingerprint_addon` class method.

### Miscellaneous internal changes
- [#140](https://github.com/rasahq/rasa/issues/140), [#143](https://github.com/rasahq/rasa/issues/143), [#149](https://github.com/rasahq/rasa/issues/149), [#712](https://github.com/rasahq/rasa/issues/712)


## [3.7.2] - 2023-12-07

Rasa Pro 3.7.2 (2023-12-07)
### Bugfixes
- [#967](https://github.com/rasahq/rasa-plus/issues/967): Fix propagation of context across rasa spans when running `rasa run --enable-api` in the case when no additional tracing context is passed to rasa.
- [#980](https://github.com/rasahq/rasa-plus/issues/980): Fixed a bug in policy invocation that made Enterprise Search Policy and `action_trigger_search` behaved strangely when used with rules and stories
- [#984](https://github.com/rasahq/rasa-plus/issues/984): Updated aiohttp, cryptography and langchain to address security vulnerabilities.

### Miscellaneous internal changes
- [#992](https://github.com/rasahq/rasa-plus/issues/992)


## [3.7.1] - 2023-12-01

Rasa Pro 3.7.1 (2023-12-01)
### Improvements
- [#966](https://github.com/rasahq/rasa-plus/issues/966): Improved error handling in Enterprise Search Policy, changed the prompt to improve formatting of documents and ensured empty slots are not added to the prompt


## [3.7.0] - 2023-11-22

Rasa Pro 3.7.0 (2023-11-22)
### Features
- [#893](https://github.com/rasahq/rasa-plus/issues/893): Added Enterprise Search Policy that uses an LLM with conversation context and relevant knowledge base documents to generate rephrased responses. The LLM is prompted to answer the user questions given the chat transcript, documents retrived from a document search and the slot values so far. This policy supports an in-memory Faiss vector store and connecting to instances of Milvus or Qdrant vector store.

### Improvements
- [#12480](https://github.com/rasahq/rasa/issues/12480): Skip executing the pipeline when the user message is of the form /intent or /intent + entities.
- [#12514](https://github.com/rasahq/rasa/issues/12514): Remove tensorflow-addons from dependencies as it is now deprecated.
- [#12533](https://github.com/rasahq/rasa/issues/12533): Add building multi-platform Docker image (amd64/arm64)
- [#12543](https://github.com/rasahq/rasa/issues/12543): Switch struct log to `FilteringBoundLogger` in order to retain log level set in the config.
- [#12558](https://github.com/rasahq/rasa/issues/12558): Added metadata as an additional argument as an additional parameter to an
  `Action`s `run` method.

  Added an additional default action called `action_send_text` which allows
  a policy to respond with a text. The text is passed to the action using the
  metadata, e.g. `metadata={"message": {"text": "Hello"}}`.

  Added LLM utility functions.
- [#12704](https://github.com/rasahq/rasa/issues/12704): Passed request headers from REST channel.
- [#12778](https://github.com/rasahq/rasa/issues/12778): Added additional method `fingerprint_addon` to the `GraphComponent` interface to allow inclusion of external data into the fingerprint calculation of a component
- [#12901](https://github.com/rasahq/rasa/issues/12901): Added Schema file and schema validation for flows.
- [#1557](https://github.com/rasahq/rasa/issues/1557): Added environment variables to configure JWT and auth token.
  For JWT the following environment variables are available:
  - JWT_SECRET
  - JWT_METHOD
  - JWT_PRIVATE_KEY

  For auth token the following environment variable is available:
  - AUTH_TOKEN
- [#33](https://github.com/rasahq/rasa/issues/33): Add skip question command
- [#41](https://github.com/rasahq/rasa/issues/41): Update the CALM starter template by:
  - adding the following flows from the financial chatbot:
    - add_contact.yml
    - remove_contact.yml
    - list_contacts.yml
  - using multiple modules (in the form of yml files) to segregate the flows (a good model to be followed)
  - adding e2e tests:
    - happy paths
    - cancelations
    - corrections
- [#74](https://github.com/rasahq/rasa/issues/74): - Enhanced the Rasa error pattern for accommodating various error types.
  - Upgraded the LLMCommandGenerator for processing the new 'user_input' configuration section. This update includes handling of messages that surpass the defined character limit.

  **Configuration Update:**

  The LLMCommandGenerator now supports a user-defined character limit via the 'user_input' configuration:

  ```yaml
    - name: LLMCommandGenerator
      llm:
        ...
      user_input:
        max_characters: 500
  ```

  **Default Behavior:**

  In the absence of a specified limit, it defaults to a 420-character cap.
  To bypass the limit entirely, set the 'max_characters' value to -1.
- [#90](https://github.com/rasahq/rasa/issues/90): - Bot now returns a default message in response to an empty user message. This improves user experience by providing
  feedback even when no input is detected.
  - `LLMCommandGenerator` behavior updated. It now returns an `ErrorCommand` for empty user messages.
  - Updated default error pattern and added the default utterance in `default_flows_for_patterns.yml`
- [#1230](https://github.com/rasahq/rasa-plus/issues/1230): Add support for Vault namespaces.
  To use namespace set either:
  * `VAULT_NAMESPACE` environment variable
  * `namespace` property in `secrets_manager` section at `endpoints.yaml`
- [#669](https://github.com/rasahq/rasa-plus/issues/669): Added Rasa Labs LLM components. Added components are:
  - `LLMIntentClassifier`
  - `IntentlessPolicy`
  - `ContextualResponseRephraser`
- [#772](https://github.com/rasahq/rasa-plus/issues/772): Made it possible for the Rasa REST channel to accept OpenTelemetry tracing context.
- [#773](https://github.com/rasahq/rasa-plus/issues/773): Improved the naming of trace spans and added more trace tags.
- [#827](https://github.com/rasahq/rasa-plus/issues/827): Add `slot_was_not_set` to E2E testing for asserting that a slot was not set and that a slot was not set with a specific value.
- [#850](https://github.com/rasahq/rasa-plus/issues/850): Introduced the rasa studio download command, enabling data retrieval from the studio.
  Implemented the option to refresh the Keycloak token.
  Expanded the functionality of RasaPrimitiveStorageMapper with the addition of flows.
  Added flows support to `rasa studio train`.
- [#898](https://github.com/rasahq/rasa-plus/issues/898): Instrument `LLMCommandGenerator._generate_action_list_using_llm` and `Command.run_command_on_tracker` methods.
- [#917](https://github.com/rasahq/rasa-plus/issues/917): Added the default values for the number of tokens generated by the LLM (`max_tokens`)
- [#918](https://github.com/rasahq/rasa-plus/issues/918): Make the instrumentation of `Command.run_command_on_tracker` method applicable to all subclasses of the `Command` class`
- [#920](https://github.com/rasahq/rasa-plus/issues/920): Instrument `ContextualResponseRephraser._generate_llm_response` and `ContextualResponseRephraser.generate` methods.
- [#925](https://github.com/rasahq/rasa-plus/issues/925): Extract commands as tracing attributes from message input when previous node was the `LLMCommandGenerator`.
- [#927](https://github.com/rasahq/rasa-plus/issues/927): Rename `rasa chat` command to `rasa inspect` and rename channel name to `inspector`.
- [#935](https://github.com/rasahq/rasa-plus/issues/935): Extract `events` and `optional_events` when `GraphNode` is `FlowPolicy`.

### Bugfixes
- [#100](https://github.com/rasahq/rasa/issues/100): uvloop is disabled by default on apple silicon machines
- [#12516](https://github.com/rasahq/rasa/issues/12516): Add `rasa_events` to the list of anonymizable structlog keys and rename structlog keys.
- [#12521](https://github.com/rasahq/rasa/issues/12521): Introduce a validation step in `rasa data validate` and `rasa train` commands to identify non-existent paths and empty domains.
- [#12556](https://github.com/rasahq/rasa/issues/12556): Rich responses containing buttons with parentheses characters are now correctly parsed.
  Previously any characters found between the first identified pair of `()` in response button took precedence.
- [#12735](https://github.com/rasahq/rasa/issues/12735): Resolve dependency incompatibility: Pin  version of `dnspython` to ==2.3.0.
- [#12790](https://github.com/rasahq/rasa/issues/12790): Fixed `KeyError` which resulted when `domain_responses` doesn't exist as a keyword argument while using a custom action dispatcher with nlg server.
- [#1762](https://github.com/rasahq/rasa/issues/1762): Fixed incompatibility with latest python-socketio release.

  The python-socketio released a backwards incompatible change on their minor
  release. This fix addresses this and makes the code compatible with prior and
  the new python-socketio version.

  https://github.com/miguelgrinberg/python-socketio/blob/main/CHANGES.md
- [#779](https://github.com/rasahq/rasa-plus/issues/779): Fixed the `404 Not Found` Github actions error while removing packages.
- [#827](https://github.com/rasahq/rasa-plus/issues/827): Corrected E2E diff behavior to prevent it from going out of sync when more than one turn difference exists between actual and expected events.
  Fixed E2E tests from propagating errors when events and test steps did not have the same length.
  Fixed the issue where E2E tests couldn't locate slot events that were not arranged chronologically.
  Resolved the problem where E2E tests were incorrectly diffing user utter events when they were not in the correct order.
- [#890](https://github.com/rasahq/rasa-plus/issues/890): Fixed E2E runner wrongly selecting the first available bot utterance when generating the test fail diff.
- [#943](https://github.com/rasahq/rasa-plus/issues/943): Updated werkzeug and urllib3 to address security vulnerabilities.
- [#950](https://github.com/rasahq/rasa-plus/issues/950): Fix cases when E2E test runner crashes when there is no response from the bot.

### Improved Documentation
- [#12371](https://github.com/rasahq/rasa/issues/12371): Update wording in Rasa Pro installation page.
- [#12677](https://github.com/rasahq/rasa/issues/12677): Updated docs on sending Conversation Events to Multiple DBs.
- [#12685](https://github.com/rasahq/rasa/issues/12685): Corrected [action server api](https://rasa.com/docs/rasa/pages/action-server-api/) sample in docs.
- [#12703](https://github.com/rasahq/rasa/issues/12703): Document support for Vault namespaces.
- [#12721](https://github.com/rasahq/rasa/issues/12721): Updated tracing documentation to include tracing in the action server and the REST Channel.

### Miscellaneous internal changes
- [#900](https://github.com/rasahq/rasa-plus/issues/900)

## [3.6.13] - 2023-10-23

Rasa Pro 3.6.13 (2023-10-23)
### Bugfixes
- [#12927](https://github.com/rasahq/rasa/issues/12927): Fix wrong conflicts that occur when rasa validate stories is run with slots that have active_loop set to null in mapping conditions.


## [3.6.12] - 2023-10-10

Rasa Pro 3.6.12 (2023-10-10)
### Improvements
- [#856](https://github.com/rasahq/rasa-plus/issues/856): Added `username` to the connection parameters for `ConcurrentRedisLockStore`.

### Bugfixes
- [#12904](https://github.com/rasahq/rasa/issues/12904): Refresh headers used in requests (e.g. action server requests) made by `EndpointConfig` using its `headers` attribute.
- [#12906](https://github.com/rasahq/rasa/issues/12906): Upgrade `pillow` to `10.0.1` to address security vulnerability CVE-2023-4863 found in `10.0.0` version.
- [#867](https://github.com/rasahq/rasa-plus/issues/867): Fix setuptools security vulnerability CVE-2022-40897 in Docker build by updating setuptools in poetry's environment.


## [3.6.11] - 2023-10-05

Rasa Pro 3.6.11 (2023-10-05)
### Bugfixes
- [#12722](https://github.com/rasahq/rasa/issues/12722): Intent names will not be falsely abbreviated in interactive training (fixes OSS-413).

  This will also fix a bug where forced user utterances (using the regex matcher) will
  be reverted even though they are present in the domain.
- [#12886](https://github.com/rasahq/rasa/issues/12886): Cache `EndpointConfig` session object using `cached_property` decorator instead of recreating this object on every request.
  Initialize these connection pools for action server and model server endpoints as part of the Sanic `after_server_start` listener.
  Also close connection pools during Sanic `after_server_stop` listener.


## [3.6.10] - 2023-09-26

Rasa Pro 3.6.10 (2023-09-26)
### Improvements
- [#12827](https://github.com/rasahq/rasa/issues/12827): Improved handling of last batch during DIET and TED training. The last batch is discarded if it contains less than half a batch size of data.
- [#12852](https://github.com/rasahq/rasa/issues/12852): Added `username` to the connection parameters for `RedisLockStore` and `RedisTrackerStore`
- [#1493](https://github.com/rasahq/rasa/issues/1493): Telemetry data is only send for licensed users.

### Improved Documentation
- [#12868](https://github.com/rasahq/rasa/issues/12868): Remove the Playground from docs.


## [3.6.9] - 2023-09-15

Rasa Pro 3.6.9 (2023-09-15)
### Improvements
- [#12778](https://github.com/rasahq/rasa/issues/12778): Added additional method `fingerprint_addon` to the `GraphComponent` interface to allow inclusion of external data into the fingerprint calculation of a component

### Bugfixes
- [#12790](https://github.com/rasahq/rasa/issues/12790): Fixed `KeyError` which resulted when `domain_responses` doesn't exist as a keyword argument while using a custom action dispatcher with nlg server.


## [3.6.8] - 2023-08-30

Rasa Pro 3.6.8 (2023-08-30)
### Bugfixes
- [#784](https://github.com/rasahq/rasa-plus/issues/784): Fix E2E testing diff algorithm to support the following use cases:
  - asserting a slot was not set under a `slot_was_set` block
  - asserting multiple slot names and/or values under a `slot_was_set` block
  Additionally, the diff algorithm has been improved to show a higher fidelity result.


## [3.6.7] - 2023-08-29

Rasa Pro 3.6.7 (2023-08-29)
### Bugfixes
- [#12768](https://github.com/rasahq/rasa/issues/12768): Updated certifi, cryptography, and scipy packages to address security vulnerabilities.
- [#795](https://github.com/rasahq/rasa-plus/issues/795): Updated setuptools and wheel to address security vulnerabilities.


## [3.6.6] - 2023-08-23

Rasa Pro 3.6.6 (2023-08-23)
### Bugfixes
- [#12755](https://github.com/rasahq/rasa/issues/12755): Updated setuptools and wheel to address security vulnerabilities.


## [3.6.5] - 2023-08-17

Rasa Pro 3.6.5 (2023-08-17)
### Improvements
- [#12696](https://github.com/rasahq/rasa/issues/12696): Use the same session across requests in `RasaNLUHttpInterpreter`

### Bugfixes
- [#12737](https://github.com/rasahq/rasa/issues/12737): Resolve dependency incompatibility: Pin  version of `dnspython` to ==2.3.0.
- [#774](https://github.com/rasahq/rasa-plus/issues/774): Fix the issue in `rasa test e2e` where test diff inaccurately displayed actual event transcripts, leading to the duplication of `BotUtter`` or `UserUtter`` events. This occurred specifically when `SetSlot`` events took place that were not explicitly defined in the Test Cases.

### Improved Documentation
- [#12712](https://github.com/rasahq/rasa/issues/12712): Updated PII docs with new section on how to use Rasa X/Enterprise with PII management solution, and a new note on debug
  logs being displayed after the bot message with `rasa shell`.


## [3.6.4] - 2023-07-21

Rasa Pro 3.6.4 (2023-07-21)
### Bugfixes
- [#12575](https://github.com/rasahq/rasa/issues/12575): Extract conditional response variation and channel variation filtering logic into a separate component.
  Enable usage of this component in the NaturalLanguageGenerator subclasses (e.g. CallbackNaturalLanguageGenerator, TemplatedNaturalLanguageGenerator).
  Amend nlg_request_format to include a single response ID string field, instead of a list of IDs.
- [#123](https://github.com/rasahq/rasa-plus/issues/123): Added details to the logs of successful and failed cases of running the markers upload command.

### Improved Documentation
- [#12663](https://github.com/rasahq/rasa/issues/12663): Updated commands with square brackets e.g (`pip install rasa[spacy]`) to use quotes (`pip install 'rasa[spacy]'`) for compatibility with zsh in docs.


## [3.6.3] - 2023-07-20

Rasa Pro 3.6.3 (2023-07-20)
### Improvements
- [#12637](https://github.com/rasahq/rasa/issues/12637): Added a human readable component to structlog using the `event_info` key and made it the default rendered key if present.

### Bugfixes
- [#12638](https://github.com/rasahq/rasa/issues/12638): Fix the issue with the most recent model not being selected if the owner or permissions where modified on the model file.
- [#12661](https://github.com/rasahq/rasa/issues/12661): Fixed `BlockingIOError` which occured as a result of too large data passed to strulogs.
- [#746](https://github.com/rasahq/rasa-plus/issues/746): Fixed the error handling mechanism in `rasa test e2e` to quickly detect and communicate errors when the action server, defined in endpoints.yaml, is not available.
- [#747](https://github.com/rasahq/rasa-plus/issues/747): Allow hyphens `-` to be present in e2e test slot names.
- [#748](https://github.com/rasahq/rasa-plus/issues/748): Resolved issues in `rasa test e2e` where errors occurred when the bot concluded the conversation with `SetSlot` events while there were remaining steps in the test case.
  Corrected the misleading error message '- No slot set' to '- Slot types do not match' in `rasa test e2e` when a type mismatch occurred during testing.

### Improved Documentation
- [#12659](https://github.com/rasahq/rasa/issues/12659): Update action server documentation with new capability to extend Sanic features by using plugins.
  Update rasa-sdk dependency to version 3.6.1.
- [#12663](https://github.com/rasahq/rasa/issues/12663): Updated commands with square brackets e.g (`pip install rasa[spacy]`) to use quotes (`pip install 'rasa[spacy]'`) for compatibility with zsh in docs.


## [3.6.2] - 2023-07-06

Rasa Pro 3.6.2 (2023-07-06)
### Improvements
- [#651](https://github.com/rasahq/rasa-plus/issues/651): Add building Docker container for arm64 (e.g. to allow running Rasa inside docker on M1/M2).

  Bumped the version of OpenTelemetry to meet the requirement of protobuf 4.x.

### Bugfixes
- [#12602](https://github.com/rasahq/rasa/issues/12602): Resolves the issue of importing TensorFlow on Docker for ARM64 architecture.


## [3.6.1] - 2023-07-03

Rasa Pro 3.6.1 (2023-07-03)
### Improvements
- [#12533](https://github.com/rasahq/rasa/issues/12533): Add building multi-platform Docker image (amd64/arm64)
- [#12543](https://github.com/rasahq/rasa/issues/12543): Switch struct log to `FilteringBoundLogger` in order to retain log level set in the config.
- [#12560](https://github.com/rasahq/rasa/issues/12560): Add new anonymizable structlog keys.

### Bugfixes
- [#12516](https://github.com/rasahq/rasa/issues/12516): Add `rasa_events` to the list of anonymizable structlog keys and rename structlog keys.
- [#12521](https://github.com/rasahq/rasa/issues/12521): Introduce a validation step in `rasa data validate` and `rasa train` commands to identify non-existent paths and empty domains.
- [#12556](https://github.com/rasahq/rasa/issues/12556): Rich responses containing buttons with parentheses characters are now correctly parsed.
  Previously any characters found between the first identified pair of `()` in response button took precedence.
- [#702](https://github.com/rasahq/rasa-plus/issues/702): Add PII bugfixes (e.g. handling None values and casting data types to string before being passed to the anonymizer) after testing manually with Audiocodes channel.

### Improved Documentation
- [#12371](https://github.com/rasahq/rasa/issues/12371): Update wording in Rasa Pro installation page.
- [#12505](https://github.com/rasahq/rasa/issues/12505): Document new PII Management section.
- [#12527](https://github.com/rasahq/rasa/issues/12527): Added Documentation for Realtime Markers Section.
- [#12579](https://github.com/rasahq/rasa/issues/12579): Add "Rasa Pro Change Log" to documentation.
- [#12581](https://github.com/rasahq/rasa/issues/12581): Document new Load Testing Guidelines section.
- [#12597](https://github.com/rasahq/rasa/issues/12597): Changes the formatting of realtime markers documentation page


## [3.6.0] - 2023-06-14

Rasa Pro 3.6.0 (2023-06-14)
### Deprecations and Removals
- [#12355](https://github.com/rasahq/rasa/issues/12355): Removed Python 3.7 support as [it reaches its end of life in June 2023](https://devguide.python.org/versions/)

### Features
- [#644](https://github.com/rasahq/rasa-plus/issues/644): Implemented PII (Personally Idenfiable Information) management using Microsoft Presidio as the entity analyzer and
  anonymization engine.
  The feature covers the following:
  - anonymization of Rasa events (`UserUttered`, `BotUttered`, `SlotSet`, `EntitiesAdded`) before they are streamed to
  Kafka event broker anonymization topics specified in `endpoints.yml`.
  - anonymization of Rasa logs that expose PII data

  The main components of the feature are:
  - anonymization rules that define in `endpoints.yml` the PII entities to be anonymized and the anonymization method to be used
  - anonymization executor that executes the anonymization rules on a given text
  - anonymization orchestrator that orchestrates the execution of the anonymization rules and publishes
  the anonymized event to the matched Kafka topic.
  - anonymization pipeline that contains a list of orchestrators and is registered to a singleton provider component,
  which gets invoked in hook calls in Rasa Open Source when the pipeline must be retrieved for anonymizing events and logs.

  Please read through the PII Management section in the official documentation to learn how to get started.
- [#685](https://github.com/rasahq/rasa-plus/issues/685): Implemented support for real time evaluation of Markers with the Analytics
  Data Pipeline, enabling you to gain valuable insights and enhance the performance of your Rasa
  Assistant.

  For this feature, we've added support for `rasa markers upload` command. Running this command validates the marker configuration file against the domain file and uploads the configuration to Analytics Data Pipeline.

### Improvements
- [#11222](https://github.com/rasahq/rasa/issues/11222): Add optional property `ids` to the nlg server request body.
  IDs will be transmitted to the NLG server and can be used to identify the response variation that should be used.
- [#11775](https://github.com/rasahq/rasa/issues/11775): Add building Docker container for arm64 (e.g. to allow running Rasa inside docker on M1/M2).
- [#12162](https://github.com/rasahq/rasa/issues/12162): Add support for Location data from Whatsapp on Twilio Channel
- [#12324](https://github.com/rasahq/rasa/issues/12324): Add validation to `rasa train` to align validation expectations with `rasa data validate`.
  Add `--skip-validation` flag to disable validation and `--fail-on-validation-warnings`, `--validation-max-history` to `rasa train` to have the same options as `rasa data validate`.
- [#12453](https://github.com/rasahq/rasa/issues/12453): Updated tensorflow to version 2.11.1 for all platforms except Apple Silicon which stays on 2.11.0 as 2.11.1 is not available yet
- [#12454](https://github.com/rasahq/rasa/issues/12454): Slot mapping conditions accept `active_loop` specified as `null` in those cases when slots with this mapping condition
  should be filled only outside form contexts.
- [#12487](https://github.com/rasahq/rasa/issues/12487): Add an optional `description` key to the Markers Configuration format. This can be used to add documentation and context about marker's usage. For example, a `markers.yml` can look like

  ``` yaml
  marker_name_provided:
    description: “Name slot has been set”
    slot_was_set: name

  marker_mood_expressed:
    description: “Unhappy or Great Mood was expressed”
    or:
      - intent: mood_unhappy
      - intent: mood_great
  ```
- [#630](https://github.com/rasahq/rasa-plus/issues/630): Add `rasa marker upload` command to upload markers to the Rasa Pro Services.
  Usage: `rasa marker upload --config=<path-to-config-file> -d=<path-to-domain-file> -rasa-pro-services-url=<url>`.
- [#670](https://github.com/rasahq/rasa-plus/issues/670): Enhance the validation of the `anonymization` key in `endpoints.yaml` by introducing checks for required fields and duplicate IDs.

### Bugfixes
- [#12467](https://github.com/rasahq/rasa/issues/12467): Fix running custom form validation to update required slots at form activation when prefilled slots consist only of slots
  that are not requested by the form.
- [#638](https://github.com/rasahq/rasa-plus/issues/638): Anonymize `rasa_events` structlog key.
- [#646](https://github.com/rasahq/rasa-plus/issues/646): Fixes issue with uploading locally trained model to a cloud rasa-plus instance where the conversation does not
  go as expected because slots don't get set correctly, e.g. an error is logged `Tried to set non existent slot 'placeholder_slot_name'. Make sure you added all your slots to your domain file.`.
  This is because the updated domain during the cloud upload did not get passed to the wrapped tracker store of the `AuthRetryTrackerStore` rasa-plus component.
  The fix was to add domain property and setter methods to the `AuthRetryTrackerStore` component.
- [#684](https://github.com/rasahq/rasa-plus/issues/684): When using `rasa studio upload`, if no specific `intents` or `entities` are specified by the user, the update will now include all available `intents` or `entities`.

### Improved Documentation
- [#12145](https://github.com/rasahq/rasa/issues/12145): Explicitly set Node.js version to 12.x in order to run Docusaurus.
- [#12160](https://github.com/rasahq/rasa/issues/12160): Update obselete commands in docs README.
- [#12168](https://github.com/rasahq/rasa/issues/12168): Correct docker image name for `deploy-rasa-pro-services` in docs.
- [#12169](https://github.com/rasahq/rasa/issues/12169): Update Compatibility Matrix.
- [#12266](https://github.com/rasahq/rasa/issues/12266): Implement `rasa data split stories` to split stories data into train/test parts.
- [#12362](https://github.com/rasahq/rasa/issues/12362): Updated [knowledge base action docs](https://rasa.com/docs/rasa-pro/action-server/knowledge-bases) to reflect the improvements made in `knowledge base actions` in Rasa Pro 3.6 version. This enhancement now allows users to query for the `object` attribute without the need for users to request a list of `objects` of a particular `object type` beforehand. The docs update mentions this under `:::info New in 3.6` section.
- [#12504](https://github.com/rasahq/rasa/issues/12504): Fix dead link in Analytics documentation.

### Miscellaneous internal changes
- [#12291](https://github.com/rasahq/rasa/issues/12291), [#12329](https://github.com/rasahq/rasa/issues/12329), [#12332](https://github.com/rasahq/rasa/issues/12332), [#12365](https://github.com/rasahq/rasa/issues/12365), [#12372](https://github.com/rasahq/rasa/issues/12372), [#12386](https://github.com/rasahq/rasa/issues/12386), [#12492](https://github.com/rasahq/rasa/issues/12492), [#619](https://github.com/rasahq/rasa-plus/issues/619)


## [3.5.12] - 2023-06-23

Rasa Pro 3.5.12 (2023-06-23)
### Bugfixes
- [#12534](https://github.com/rasahq/rasa/issues/12534): Rich responses containing buttons with parentheses characters are now correctly parsed.
  Previously any characters found between the first identified pair of `()` in response button took precedence.

### Miscellaneous internal changes
- [#12512](https://github.com/rasahq/rasa/issues/12512)


## [3.5.11] - 2023-06-08

Rasa Pro 3.5.11 (2023-06-08)
### Bugfixes
- [#12467](https://github.com/rasahq/rasa/issues/12467): Fix running custom form validation to update required slots at form activation when prefilled slots consist only of slots
  that are not requested by the form.


## [3.5.10] - 2023-05-23

Rasa Pro 3.5.10 (2023-05-23)
### Improved Documentation
- [#12437](https://github.com/rasahq/rasa/issues/12437): Added documentation for spaces alpha


## [3.5.9] - 2023-05-19

Rasa Pro 3.5.9 (2023-05-19)

No significant changes.


## [3.5.8] - 2023-05-12

Rasa Pro 3.5.8 (2023-05-12)
### Bugfixes
- [#12361](https://github.com/rasahq/rasa/issues/12361): Explicitly handled `BufferError exception - Local: Queue full` in Kafka producer.


## [3.5.7] - 2023-05-09

Rasa Pro 3.5.7 (2023-05-09)
### Bugfixes
- [#12314](https://github.com/rasahq/rasa/issues/12314): `SlotSet` events will be emitted when the value set by the custom action is the same as the existing value of the slot. This was fixed for `AugmentedMemoizationPolicy` to work properly with truncated trackers.

  To restore the previous behaviour, the custom action can return a SlotSet only if the slot value has changed. For example,

  ```
  class CustomAction(Action):
      def name(self) -> Text:
          return "custom_action"

      def run(self, dispatcher: CollectingDispatcher,
              tracker: Tracker,
              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          # current value of the slot
          slot_value = tracker.get_slot('my_slot')

          # value of the entity
          # this is parsed from the user utterance
          entity_value = next(tracker.get_latest_entity_values("entity_name"), None)

          if slot_value != entity_value:
            return[SlotSet("my_slot", entity_value)]
  ```


## [3.5.6] - 2023-04-28

Rasa Pro 3.5.6 (2023-04-28)
### Bugfixes
- [#12280](https://github.com/rasahq/rasa/issues/12280): Addresses Regular Expression Denial of Service vulnerability in slack connector (https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS)
- [#12325](https://github.com/rasahq/rasa/issues/12325): Fix parsing of RabbitMQ URL provided in `endpoints.yml` file to include vhost path and query parameters.
  Re-allows inclusion of credentials in the URL as a regression fix (this was supported in 2.x).


## [3.5.5] - 2023-04-20

Rasa Pro 3.5.5 (2023-04-20)
### Bugfixes
- [#12268](https://github.com/rasahq/rasa/issues/12268): Allow slot mapping parameter `intent` to accept a list of intent names (as strings), in addition to accepting an intent name as a single string.
- [#12271](https://github.com/rasahq/rasa/issues/12271): Fix `BlockingIOError` when running `rasa shell` on utterances with more than 5KB of text.
- [#12286](https://github.com/rasahq/rasa/issues/12286): Use `ruamel.yaml` round-trip loader in order to preserve all comments after appending `assistant_id` to `config.yml`.
- [#12295](https://github.com/rasahq/rasa/issues/12295): Fix `AttributeError: 'NoneType' object has no attribute 'send_response'` caused by retrieving tracker via `GET /conversations/{conversation_id}/tracker` endpoint when `action_session_start` is customized in a custom action.
  This was addressed by passing an instance of `CollectingOutputChannel` to the method retrieving the tracker from the `MessageProcessor`.

### Improved Documentation
- [#12272](https://github.com/rasahq/rasa/issues/12272): Updated AWS model loading documentation to indicate what should `AWS_ENDPOINT_URL` environment variable be set to.
  Added integration test for AWS model loading.
- [#12279](https://github.com/rasahq/rasa/issues/12279): Updated Rasa Pro Services documentation to add `KAFKA_SSL_CA_LOCATION` environment variable. Allows connections over SSL to Kafka
- [#12290](https://github.com/rasahq/rasa/issues/12290): Added note to CLI documentation to address encoding and color issues on certain Windows terminals

### Miscellaneous internal changes
- [#12267](https://github.com/rasahq/rasa/issues/12267)


## [3.5.4] - 2023-04-05

Rasa Pro 3.5.4 (2023-04-05)
### Bugfixes
- [#12226](https://github.com/rasahq/rasa/issues/12226): Fix issue with failures while publishing events to RabbitMQ after a RabbitMQ restart.
  The fix consists of pinning `aio-pika` dependency to `8.2.3`, since this issue was introduced in `aio-pika` v`8.2.4`.
- [#12232](https://github.com/rasahq/rasa/issues/12232): Patch redis Race Conditiion vulnerability.

### Miscellaneous internal changes
- [#12230](https://github.com/rasahq/rasa/issues/12230), [#12238](https://github.com/rasahq/rasa/issues/12238)


## [3.5.3] - 2023-03-30

Rasa Pro 3.5.3 (2023-03-30)
### Improved Documentation
- [#12209](https://github.com/rasahq/rasa/issues/12209): Add new Rasa Pro page in docs, together with minimal content changes.


## [3.5.2] - 2023-03-30

Rasa Pro 3.5.2 (2023-03-30)
### Improvements
- [#12144](https://github.com/rasahq/rasa/issues/12144): Add a self-reference of the synonym in the EntitySynonymMapper to handle entities extracted in a casing different to synonym case. (For example if a synonym `austria` is added, entities extracted with any alternate casing of the synonym will also be mapped to `austria`). It addresses ATO-616

### Bugfixes
- [#12189](https://github.com/rasahq/rasa/issues/12189): Make custom actions inheriting from rasa-sdk `FormValidationAction` parent class an exception of the `selective_domain` rule and always send them domain.
- [#12193](https://github.com/rasahq/rasa/issues/12193): Fix 2 issues detected with the HTTP API:
  - The `GET /conversations/{conversation_id}/tracker` endpoint was not returning the tracker with all sessions when `include_events` query parameter was set to `ALL`.
  The fix constituted in using `TrackerStore.retrieve_full_tracker` method instead of `TrackerStore.retrieve` method in the function handling the `GET /conversations/{conversation_id}/tracker` endpoint.
  Implemented or updated this method across all tracker store subclasses.
  - The `GET /conversations/{conversation_id}/story` endpoint was not returning all the stories for all sessions when `all_sessions` query parameter was set to `true`.
  The fix constituted in using all events of the tracker to be converted in stories instead of only the `applied_events`.

### Improved Documentation
- [#12110](https://github.com/rasahq/rasa/issues/12110): Add documentation for secrets managers.


## [3.5.1] - 2023-03-24

Rasa Pro 3.5.1 (2023-03-24)
### Bugfixes
- [#12174](https://github.com/rasahq/rasa/issues/12174): Fixes training `DIETCLassifier` on the GPU.

  A deterministic GPU implementation of SparseTensorDenseMatmulOp is not currently available

### Improved Documentation
- [#12127](https://github.com/rasahq/rasa/issues/12127): Updated `Test your assistant` section to describe the new end-to-end testing feature.
  Also updated CLI and telemetry reference docs.
- [#12169](https://github.com/rasahq/rasa/issues/12169): Update Compatibility Matrix.


## [3.5.0] - 2023-03-21

Rasa Pro 3.5.0 (2023-03-21)
### Features
- [#12053](https://github.com/rasahq/rasa/issues/12053): Add a new required key (`assistant_id`) to `config.yml` to uniquely identify assistants in deployment.
  The assistant identifier is extracted from the model metadata and added to the metadata of all dialogue events.
  Re-training will be required to include the assistant id in the event metadata.

  If the assistant identifier is missing from the `config.yml` or the default identifier value is not replaced, a random
  identifier is generated during each training.

  An assistant running without an identifier will issue a warning that dialogue events without identifier metadata will be
  streamed to the event broker.
- [#309](https://github.com/rasahq/rasa-plus/issues/309): End-to-end testing is an enhanced and comprehensive CLI-based testing tool that allows you to test conversation scenarios with different pre-configured contexts, execute custom actions, verify response texts or names, and assert when slots are filled. It is available ysing the new `rasa test e2e` command.
- [#342](https://github.com/rasahq/rasa-plus/issues/342): You can now store your assistant's secrets in an external credentials manager. In this release, Rasa Pro currently supports credentials manager for the Tracker Store with HashiCorp Vault.

### Improvements
- [#11998](https://github.com/rasahq/rasa/issues/11998): Add capability to send compressed body in HTTP request to action server.
  Use COMPRESS_ACTION_SERVER_REQUEST=True to turn the feature on.

### Bugfixes
- [#12136](https://github.com/rasahq/rasa/issues/12136): Address potentially missing events with Pika consumer due to weak references on asynchronous tasks,
  as specifcied in [Python official documentation](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task).
- [#12155](https://github.com/rasahq/rasa/issues/12155): Sets a global seed for numpy, TensorFlow, keras, Python and CuDNN, to ensure consistent random number generation.

### Improved Documentation
- [#11893](https://github.com/rasahq/rasa/issues/11893): Clarify in the docs, how rules are designed and how to use this behaviour to abort a rule

### Miscellaneous internal changes
- [#11924](https://github.com/rasahq/rasa/issues/11924), [#11926](https://github.com/rasahq/rasa/issues/11926), [#12006](https://github.com/rasahq/rasa/issues/12006), [#12022](https://github.com/rasahq/rasa/issues/12022), [#12092](https://github.com/rasahq/rasa/issues/12092), [#12135](https://github.com/rasahq/rasa/issues/12135), [#12137](https://github.com/rasahq/rasa/issues/12137), [#12140](https://github.com/rasahq/rasa/issues/12140), [#12154](https://github.com/rasahq/rasa/issues/12154)


## [3.4.14] - 2023-06-08

Rasa Pro 3.4.14 (2023-06-08)
### Bugfixes
- [#12467](https://github.com/rasahq/rasa/issues/12467): Fix running custom form validation to update required slots at form activation when prefilled slots consist only of slots
  that are not requested by the form.


## [3.4.13] - 2023-05-19

Rasa Pro 3.4.13 (2023-05-19)

No significant changes.


## [3.4.12] - 2023-05-12

Rasa Pro 3.4.12 (2023-05-12)
### Bugfixes
- [#12361](https://github.com/rasahq/rasa/issues/12361): Explicitly handled `BufferError exception - Local: Queue full` in Kafka producer.


## [3.4.11] - 2023-05-09

Rasa Pro 3.4.11 (2023-05-09)
### Bugfixes
- [#12325](https://github.com/rasahq/rasa/issues/12325): Fix parsing of RabbitMQ URL provided in `endpoints.yml` file to include vhost path and query parameters.
  Re-allows inclusion of credentials in the URL as a regression fix (this was supported in 2.x).
- [#12364](https://github.com/rasahq/rasa/issues/12364): `SlotSet` events will be emitted when the value set by the custom action is the same as the existing value of the slot. This was fixed for `AugmentedMemoizationPolicy` to work properly with truncated trackers.

  To restore the previous behaviour, the custom action can return a SlotSet only if the slot value has changed. For example,

  ```
  class CustomAction(Action):
      def name(self) -> Text:
          return "custom_action"

      def run(self, dispatcher: CollectingDispatcher,
              tracker: Tracker,
              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          # current value of the slot
          slot_value = tracker.get_slot('my_slot')

          # value of the entity
          # this is parsed from the user utterance
          entity_value = next(tracker.get_latest_entity_values("entity_name"), None)

          if slot_value != entity_value:
            return[SlotSet("my_slot", entity_value)]
  ```

### Miscellaneous internal changes
- [#12267](https://github.com/rasahq/rasa/issues/12267)


## [3.4.10] - 2023-04-17

Rasa Pro 3.4.10 (2023-04-17)
### Miscellaneous internal changes
- [#12255](https://github.com/rasahq/rasa/issues/12255)


## [3.4.9] - 2023-04-05
### Miscellaneous internal changes
- [#12234](https://github.com/rasahq/rasa/issues/12234)


## [3.4.8] - 2023-04-03

Rasa Pro 3.4.8 (2023-04-03)
### Bugfixes
- [#12186](https://github.com/rasahq/rasa/issues/12186): Fix issue with failures while publishing events to RabbitMQ after a RabbitMQ restart.
  The fix consists of pinning `aio-pika` dependency to `8.2.3`, since this issue was introduced in `aio-pika` v`8.2.4`.


## [3.4.7] - 2023-03-30

Rasa Pro 3.4.7 (2023-03-30)
### Improvements
- [#12144](https://github.com/rasahq/rasa/issues/12144): Add a self-reference of the synonym in the EntitySynonymMapper to handle entities extracted in a casing different to synonym case. (For example if a synonym `austria` is added, entities extracted with any alternate casing of the synonym will also be mapped to `austria`). It addresses ATO-616

### Bugfixes
- [#12139](https://github.com/rasahq/rasa/issues/12139): Fix 2 issues detected with the HTTP API:
  - The `GET /conversations/{conversation_id}/tracker` endpoint was not returning the tracker with all sessions when `include_events` query parameter was set to `ALL`.
  The fix constituted in using `TrackerStore.retrieve_full_tracker` method instead of `TrackerStore.retrieve` method in the function handling the `GET /conversations/{conversation_id}/tracker` endpoint.
  Implemented or updated this method across all tracker store subclasses.
  - The `GET /conversations/{conversation_id}/story` endpoint was not returning all the stories for all sessions when `all_sessions` query parameter was set to `true`.
  The fix constituted in using all events of the tracker to be converted in stories instead of only the `applied_events`.
- [#12189](https://github.com/rasahq/rasa/issues/12189): Make custom actions inheriting from rasa-sdk `FormValidationAction` parent class an exception of the `selective_domain` rule and always send them domain.


## [3.4.6] - 2023-03-16

Rasa Pro 3.4.6 (2023-03-16)
### Bugfixes
- [#12098](https://github.com/rasahq/rasa/issues/12098): Fixes CountVectorFeaturizer to train when min_df != 1.


## [3.4.5] - 2023-03-09

Rasa Pro 3.4.5 (2023-03-09)
### Bugfixes
- [#12059](https://github.com/rasahq/rasa/issues/12059): Check unresolved slots before initiating model training.
- [#12096](https://github.com/rasahq/rasa/issues/12096): Fixes the bug when a slot (with `from_intent` mapping which contains no input for `intent` parameter) will no longer fill for any intent that is not under the `not_intent` parameter.
- [#12099](https://github.com/rasahq/rasa/issues/12099): Fix validation metrics calculation when batch_size is dynamic.

### Improved Documentation
- [#12062](https://github.com/rasahq/rasa/issues/12062): Add a link to an existing docs section on how to test the audio channel on `localhost`.


## [3.4.4] - 2023-02-17

Rasa Pro 3.4.4 (2023-02-17)
### Improvements
- [#11997](https://github.com/rasahq/rasa/issues/11997): Add capability to send compressed body in HTTP request to action server.
  Use COMPRESS_ACTION_SERVER_REQUEST=True to turn the feature on.

### Bugfixes
- [#12052](https://github.com/rasahq/rasa/issues/12052): Fix the error which resulted during merging multiple domain files where at least one of them contains custom actions that explicitly need `send_domain` set as True in the domain.


## [3.4.3] - 2023-02-14

Rasa Pro 3.4.3 (2023-02-14)
### Improvements
- [#12001](https://github.com/rasahq/rasa/issues/12001): Add support for custom RulePolicy.
- [#12013](https://github.com/rasahq/rasa/issues/12013): Add capability to select which custom actions should receive domain when they are invoked.

### Bugfixes
- [#11942](https://github.com/rasahq/rasa/issues/11942): Fix calling the form validation action twice for the same user message triggering a form.
- [#12033](https://github.com/rasahq/rasa/issues/12033): Fix conditional response does not check other conditions if first condition matches.

### Improved Documentation
- [#11976](https://github.com/rasahq/rasa/issues/11976): Add section in tracker store docs to document the fallback tracker store mechanism.


## [3.4.2] - 2023-01-27

Rasa Pro 3.4.2 (2023-01-27)
### Bugfixes
- [#11926](https://github.com/rasahq/rasa/issues/11926): Decision to publish docs should not consider next major and minor alpha release versions.
- [#11968](https://github.com/rasahq/rasa/issues/11968): Exit training/running Rasa model when SpaCy runtime version is not compatible with the specified SpaCy model version.
- [#11971](https://github.com/rasahq/rasa/issues/11971): The new custom logging feature was not working due to small syntax issue in the argparse level.

  Previously, the file name passed using the argument --logging-config-file was never retrieved so it never creates the new custom config file with the desired formatting.

### Miscellaneous internal changes
- [#11924](https://github.com/rasahq/rasa/issues/11924)


## [3.4.1] - 2023-01-19

Rasa Pro 3.4.1 (2023-01-19)
### Bugfixes
- [#11923](https://github.com/rasahq/rasa/issues/11923): Changed categorical slot comparison to be case insensitive.
- [#11929](https://github.com/rasahq/rasa/issues/11929): Exit training when transformer_size is not divisible by the number_of_attention_heads parameter and update the transformer documentations.

### Improved Documentation
- [#11899](https://github.com/rasahq/rasa/issues/11899): Update compatibility matrix between Rasa-plus and Rasa Pro services.


## [3.4.0] - 2022-12-14

Rasa Pro 3.4.0 (2022-12-14)
### Features
- [#11087](https://github.com/rasahq/rasa/issues/11087): Add metadata to Websocket channel. Messages can now include a `metadata` object which will be included as metadata to Rasa.  The metadata can be supplied on a user configurable key with the `metadata_key` setting in the `socketio` section of the `credentials.yml`.
- [#185](https://github.com/rasahq/rasa-plus/issues/185): Use a new IVR Channel to connect your assistant to AudioCodes VoiceAI Connect.

### Improvements
- [#11517](https://github.com/rasahq/rasa/issues/11517): Added `./docker/Dockerfile_pretrained_embeddings_spacy_it` to include Spacy's Italian pre-trained model `it_core_news_md`.
- [#11765](https://github.com/rasahq/rasa/issues/11765): Replace `kafka-python` dependency with `confluent-kafka` async Producer API.
- [#11773](https://github.com/rasahq/rasa/issues/11773): Add support for Python 3.10 version.
- [#2546](https://github.com/rasahq/rasa/issues/2546): Added CLI option `--logging-config-file` to enable configuration of custom logs formatting.

### Bugfixes
- [#11869](https://github.com/rasahq/rasa/issues/11869): Implements a new CLI option `--jwt-private-key` required to have complete support for asymmetric algorithms as specified
  originally in the docs.


### Improved Documentation
- [#11766](https://github.com/rasahq/rasa/issues/11766): Clarify in the documentation how to write testing stories if a user presses a button with payload.
- [#11801](https://github.com/rasahq/rasa/issues/11801): Clarify prioritisation of used slot asking option in forms in documentation.

### Miscellaneous internal changes
- [#11742](https://github.com/rasahq/rasa/issues/11742), [#11800](https://github.com/rasahq/rasa/issues/11800), [#11817](https://github.com/rasahq/rasa/issues/11817), [#11877](https://github.com/rasahq/rasa/issues/11877)

## [3.3.8] - 2023-04-06
### Miscellaneous internal changes
- [#12235](https://github.com/rasahq/rasa/issues/12235)


## [3.3.7] - 2023-03-31
### Improvements
- [#12144](https://github.com/rasahq/rasa/issues/12144): Add a self-reference of the synonym in the EntitySynonymMapper to handle entities extracted in a casing different to synonym case. (For example if a synonym `austria` is added, entities extracted with any alternate casing of the synonym will also be mapped to `austria`). It addresses ATO-616

### Bugfixes
- [#12187](https://github.com/rasahq/rasa/issues/12187): Fix issue with failures while publishing events to RabbitMQ after a RabbitMQ restart.
  The fix consists of pinning `aio-pika` dependency to `8.2.3`, since this issue was introduced in `aio-pika` v`8.2.4`.
- [#12192](https://github.com/rasahq/rasa/issues/12192): Fix 2 issues detected with the HTTP API:
  - The `GET /conversations/{conversation_id}/tracker` endpoint was not returning the tracker with all sessions when `include_events` query parameter was set to `ALL`.
  The fix constituted in using `TrackerStore.retrieve_full_tracker` method instead of `TrackerStore.retrieve` method in the function handling the `GET /conversations/{conversation_id}/tracker` endpoint.
  Implemented or updated this method across all tracker store subclasses.
  - The `GET /conversations/{conversation_id}/story` endpoint was not returning all the stories for all sessions when `all_sessions` query parameter was set to `true`.
  The fix constituted in using all events of the tracker to be converted in stories instead of only the `applied_events`.

## [3.3.6] - 2023-03-09

Rasa Pro 3.3.6 (2023-03-09)
### Bugfixes
- [#12103](https://github.com/rasahq/rasa/issues/12103): Fixes the bug when a slot (with `from_intent` mapping which contains no input for `intent` parameter) will no longer fill for any intent that is not under the `not_intent` parameter.
- [#12117](https://github.com/rasahq/rasa/issues/12117): Fix validation metrics calculation when batch_size is dynamic.


## [3.3.5] - 2023-02-21

No significant changes.


## [3.3.4] - 2023-02-14

Rasa Pro 3.3.4 (2023-02-14)
### Improvements
- [#11996](https://github.com/rasahq/rasa/issues/11996): Add capability to send compressed body in HTTP request to action server.
Use COMPRESS_ACTION_SERVER_REQUEST=True to turn the feature on.
- [#12001](https://github.com/rasahq/rasa/issues/12001): Add support for custom RulePolicy.

## [3.3.3] - 2022-12-01

### Bugfixes
- [#11792](https://github.com/rasahq/rasa/issues/11792): Bypass Windows path length restrictions upon saving and reading a model archive in `rasa.engine.storage.LocalModelStorage`.

### Improvements
- [#11819](https://github.com/rasahq/rasa/issues/11819): Updated tensorflow to 2.8.4.

## [3.3.2] - 2022-11-30
### Improvements
- [#11762](https://github.com/rasahq/rasa/issues/11762): Added support for camembert french bert model

### Bugfixes
- [#11818](https://github.com/rasahq/rasa/issues/11818): Fixes `RuntimeWarning: coroutine 'Bot.set_webhook' was never awaited` issue encountered when starting the rasa server,
  which caused the Telegram bot to be unresponsive.

### Improved Documentation
- [#11768](https://github.com/rasahq/rasa/issues/11768): The documentation was updated for Buttons using messages that start with '/'.
  Previously, it wrongly stated that messages with '/' bypass NLU, which is not the case.
- [#11799](https://github.com/rasahq/rasa/issues/11799): Add documentation for Rasa Pro Services upgrades.


## [3.3.1] - 2022-11-09
### Improved Documentation
- [#11721](https://github.com/rasahq/rasa/issues/11721): Add docs on how to set up additional data lakes for Rasa Pro analytics pipeline.
- [#11724](https://github.com/rasahq/rasa/issues/11724): Update migration guide and form docs with prescriptive recommendation on how to implement dynamic forms with custom slot mappings.

### Improvements
- [#11732](https://github.com/rasahq/rasa/issues/11732): Updated numpy and scikit learn version to fix vulnerabilities of those dependencies

## [3.3.0] - 2022-10-24
### Features
- [#3](https://github.com/rasahq/rasa-plus/issues/3): Tracing capabilities for your Rasa Pro assistant. Distributed tracing tracks requests as they flow through a distributed system (in this case: a Rasa assistant), sending data about the requests to a tracing backend which collects all trace data and enables inspecting it. With this version of the Tracing feature, Rasa Pro supports OpenTelemetry.
- [#92](https://github.com/rasahq/rasa-plus/issues/92): `ConcurrentRedisLockStore` is a new lock store that uses Redis as a persistence layer and is safe for use with multiple Rasa server replicas.

### Improvements
- [#11561](https://github.com/rasahq/rasa/issues/11561): Added option `--offset-timestamps-by-seconds` to offset the timestamp of events when using `rasa export`
- [#11578](https://github.com/rasahq/rasa/issues/11578): Rasa supports native installations on Apple Silicon (M1 / M2). Please
  follow the installation instructions and take a look at the limitations.
- [#11596](https://github.com/rasahq/rasa/issues/11596): Caching `Message` and `Features` fingerprints unless they are altered, saving up to 2/3 of fingerprinting time in our tests.
- [#11598](https://github.com/rasahq/rasa/issues/11598): Added package versions of component  dependencies as an additional part of fingerprinting calculation. Upgrading an dependency will thus lead to a retraining of the component in the future. Also, by changing fingerprint calculation, the next training after this change will be a complete retraining.
- [#11623](https://github.com/rasahq/rasa/issues/11623): Export events continuously rather than loading all events in memory first when
  using `rasa export`. Events will be streamed right from the start rather
  than loading all events first and pushing them to the broker afterwards.
- [#11568](https://github.com/rasahq/rasa/issues/11568): Adds new dependency pluggy, with which it was possible to implement new plugin functionality.
  This plugin manager enables the extension and/or enhancement of the Rasa command line interface with functionality made available in the rasa-plus package.

### Bugfixes
- [#11575](https://github.com/rasahq/rasa/issues/11575): Fix `BlockingIOError` when running `rasa interactive`, after the upgrade of `prompt-toolkit` dependency.
- [#11395](https://github.com/rasahq/rasa/issues/11395): Fixes a bug that lead to initial slot values being incorporated into all rules by default, thus breaking most rules when the slot value changed from its initial value
- [#11429](https://github.com/rasahq/rasa/issues/11429): Made logistic regression classifier output a proper intent ranking and made ranking length configurable

### Deprecations and Removals
- [#11190](https://github.com/rasahq/rasa/issues/11190): Remove code related to Rasa X local mode as it is deprecated and scheduled for removal.

### Miscellaneous internal changes
- [#11548](https://github.com/rasahq/rasa/issues/11548)


## [3.2.13] - 2023-03-09

Rasa 3.2.13 (2023-03-09)
### Bugfixes
- [#12099](https://github.com/rasahq/rasa/issues/12099): Fix validation metrics calculation when batch_size is dynamic.
- [#12102](https://github.com/rasahq/rasa/issues/12102): Fixes the bug when a slot (with `from_intent` mapping which contains no input for `intent` parameter) will no longer fill for any intent that is not under the `not_intent` parameter.


## [3.2.12] - 2023-02-21
### Features
- [#11087](https://github.com/rasahq/rasa/issues/11087): Add metadata to Websocket channel. Messages can now include a `metadata` object which will be included as metadata to Rasa.  The metadata can be supplied on a user configurable key with the `metadata_key` setting in the `socketio` section of the `credentials.yml`.

### Improvements
- [#11995](https://github.com/rasahq/rasa/issues/11995): Add capability to send compressed body in HTTP request to action server.
Use COMPRESS_ACTION_SERVER_REQUEST=True to turn the feature on.

### Bugfixes
- [#11926](https://github.com/rasahq/rasa/issues/11926): Decision to publish docs should not consider next major and minor alpha release versions.


## [3.2.11] - 2022-12-05
### Improvements
- [#11596](https://github.com/rasahq/rasa/issues/11596): Caching `Message` and `Features` fingerprints unless they are altered, saving up to 2/3 of fingerprinting time in our tests.

### Bugfixes
- [#11829](https://github.com/rasahq/rasa/issues/11829): Implements a new CLI option `--jwt-private-key` required to have complete support for asymmetric algorithms as specified
  originally in the docs.


## [3.2.10] - 2022-09-29
### Bugfixes
- [#11588](https://github.com/rasahq/rasa/issues/11588): Fixes scenarios in which a slot with `from_trigger_intent` mapping that specifies an `active_loop` condition was being filled despite that `active_loop` not being activated.
  In addition, fixes scenario in which a slot with `from_trigger_intent` mapping without a specified `active_loop` mapping condition is only filled if the form gets activated.
  Removes unnecessary validation warning that a slot with `from_trigger_intent` and a mapping condition should be included in the form's required_slots.
- [#ato-161](https://github.com/rasahq/rasa/issues/ato-161): Fixed a bug where `DIETClassier` crashed during training
  when both masked language modelling and evaluation
  during training were used.

### Improved Documentation
- [#11571](https://github.com/rasahq/rasa/issues/11571): Rasa SDK documentation lives now in Rasa Open Source documentation under the _Rasa SDK_ category.

### Miscellaneous internal changes
- [#11552](https://github.com/rasahq/rasa/issues/11552)


## [3.2.9] - 2022-09-09

Yanked.


## [3.2.8] - 2022-09-08
### Bugfixes
- [#11540](https://github.com/rasahq/rasa/issues/11540): Fix bug where `KeywordIntentClassifier` overrides preceding intent classifiers' predictions
  although the `KeyWordIntentClassifier` was not matching any keywords.


## [3.2.7] - 2022-08-31
### Improvements
- [#11448](https://github.com/rasahq/rasa/issues/11448): Improve `rasa data validate` command so that it uses custom importers when they are defined in config file.

### Bugfixes
- [#11311](https://github.com/rasahq/rasa/issues/11311): Re-instates the REST channel metadata feature.  Metadata can be provided on the `metadata` key.


## [3.2.6] - 2022-08-12
### Bugfixes
- [#11433](https://github.com/rasahq/rasa/issues/11433): This fix makes sure that when a Domain object is loaded from multiple files where one file specifies a custom session config and the rest do not, the default session configuration does not override the custom session config.

### Miscellaneous internal changes
- [#11426](https://github.com/rasahq/rasa/issues/11426), [#11434](https://github.com/rasahq/rasa/issues/11434)


## [3.2.5] - 2022-08-05
### Bugfixes
- [#11294](https://github.com/rasahq/rasa/issues/11294): Fix `KeyError` which resulted when `action_two_stage_fallback` got executed in a project whose domain contained slot mappings.
- [#11390](https://github.com/rasahq/rasa/issues/11390): Fixes regression in which slot mappings were prioritized according to reverse order as they were listed in the domain, instead of in order from first to last, as was implicitly expected in `2.x`.
  Clarifies this implicit priority order in the docs.
- [#11394](https://github.com/rasahq/rasa/issues/11394): Enables the dispatching of bot messages returned as events by slot validation actions.


## [3.2.4] - 2022-07-21
### Bugfixes
- [#11061](https://github.com/rasahq/rasa/issues/11061): Added session_config key as valid domain key during domain loading from directory containing a separate domain file with session configuration.
- [#11362](https://github.com/rasahq/rasa/issues/11362): Run default action `action_extract_slots` after a custom action returns a `UserUttered` event to fill any applicable slots.
- [#11368](https://github.com/rasahq/rasa/issues/11368): Handle the case when an `EndpointConfig` object is given as parameter to the `AwaitableTrackerStore.create()` method.


## [3.2.3] - 2022-07-18
### Bugfixes
- [#11305](https://github.com/rasahq/rasa/issues/11305): - Fixed error in creating response when slack sends retry messages. Assigning `None` to `response.text` caused `TypeError: Bad body type. Expected str, got NoneType`.
  - Fixed Slack triggering timeout after 3 seconds if the action execution is too slow. Running `on_new_message` as an asyncio background task instead of a blocking await fixes this by immediately returning a response with code 200.
- [#11326](https://github.com/rasahq/rasa/issues/11326): Revert change in #10295 that removed running the form validation action on activation of the form before the loop is active.
- [#11333](https://github.com/rasahq/rasa/issues/11333): `SlotSet` events will be emitted when the value set by the current user turn is the same as the existing value.

  Previously, `ActionExtractSlots` would not emit any `SlotSet` events if the new value was the same as the existing
  one. This caused the augmented memoization policy to lose these slot values when truncating the tracker.


## [3.2.2] - 2022-07-05
### Improved Documentation
- [#11207](https://github.com/rasahq/rasa/issues/11207): Update documentation for customizable classes such as tracker stores, event brokers and lock stores.

### Miscellaneous internal changes
- [#11296](https://github.com/rasahq/rasa/issues/11296)


## [3.2.1] - 2022-06-17
### Bugfixes
- [#10430](https://github.com/rasahq/rasa/issues/10430): Fix failed check in `rasa data validate` that verifies forms in rules or stories are consistent with the domain when the rule or story contains a default action as `active_loop` step.


## [3.2.0] - 2022-06-14
### Deprecations and Removals
- [#10989](https://github.com/rasahq/rasa/issues/10989): [NLU training data](https://rasa.com/docs/rasa-pro/nlu-based-assistants/nlu-training-data) in JSON format is deprecated and will be
  removed in Rasa Open Source 4.0.
  Please use `rasa data convert nlu -f yaml --data <path to NLU data>` to convert your
  NLU JSON data to YAML format before support for NLU JSON data is removed.

### Improvements
- [#10696](https://github.com/rasahq/rasa/issues/10696): Make `TrackerStore` interface methods asynchronous and supply an `AwaitableTrackerstore` wrapper for custom tracker stores which do not implement the methods as asynchronous.
- [#10897](https://github.com/rasahq/rasa/issues/10897): Added flag `use_gpu` to `TEDPolicy` and `UnexpecTEDIntentPolicy` that can be used to enable training on CPU even when a GPU is available.
- [#11102](https://github.com/rasahq/rasa/issues/11102): Add `--endpoints` command line parameter to `rasa train` parser.

### Bugfixes
- [#11129](https://github.com/rasahq/rasa/issues/11129): The azure botframework channel now validates the incoming JSON Web Tokens (including signature).

  Previously, JWTs were not validated at all.
- [#9386](https://github.com/rasahq/rasa/issues/9386): `rasa shell` now outputs custom json unicode characters instead of `\uxxxx` codes

### Improved Documentation
- [#11130](https://github.com/rasahq/rasa/issues/11130): Clarify aspects of the API spec
  GET /status endpoint: Correct response schema for model_id - a string, not an object.

  GET /conversations/{conversation_id}/tracker: Describe each of the enum options for include_events query parameter

  POST & PUT /conversations/{conversation_id}/tracker/eventss: Events schema added for each event type

  GET /conversations/{conversation_id}/story: Clarified the all_sessions query parameter and default behaviour.

  POST /model/test/intents : Remove JSON payload option since it is not supported

  POST /model/parse: Explain what emulation_mode is and how it affects response results

### Miscellaneous internal changes
- [#11088](https://github.com/rasahq/rasa/issues/11088), [#11123](https://github.com/rasahq/rasa/issues/11123), [#9093](https://github.com/rasahq/rasa/issues/9093), [#9099](https://github.com/rasahq/rasa/issues/9099)

## [3.1.7] - 2022-08-30
### Miscellaneous internal changes
- [#11522](https://github.com/rasahq/rasa/issues/11522)


## [3.1.6] - 2022-07-20
### Bugfixes
- [#11362](https://github.com/rasahq/rasa/issues/11362): Run default action `action_extract_slots` after a custom action returns a `UserUttered` event to fill any applicable slots.


## [3.1.5] - 2022-07-15
### Bugfixes
- [#11333](https://github.com/rasahq/rasa/issues/11333): `SlotSet` events will be emitted when the value set by the current user turn is the same as the existing value.

  Previously, `ActionExtractSlots` would not emit any `SlotSet` events if the new value was the same as the existing
  one. This caused the augmented memoization policy to lose these slot values when truncating the tracker.


## [3.1.4] - 2022-06-21                          No significant changes.
Upgrade dependent libraries with security vulnerabilities (Pillow, TensorFlow, ujson).

## [3.1.3] - 2022-06-17
### Bugfixes
- [#11129](https://github.com/rasahq/rasa/issues/11129): The azure botframework channel now validates the incoming JSON Web Tokens (including signature).

  Previously, JWTs were not validated at all.
- [#11197](https://github.com/rasahq/rasa/issues/11197): Backports fix for failed check in `rasa data validate` that verifies forms in rules or stories are consistent with the domain when the rule or story contains a default action as `active_loop` step.


## [3.1.2] - 2022-06-08
### Miscellaneous internal changes
- [#11156](https://github.com/rasahq/rasa/issues/11156), [#11173](https://github.com/rasahq/rasa/issues/11173)


## [3.1.1] - 2022-06-03
### Bugfixes
- [#10480](https://github.com/rasahq/rasa/issues/10480): Remove warning for Rasa X localmode not being supported when the `--production` flag is present.
- [#10908](https://github.com/rasahq/rasa/issues/10908): Pin requirement for `scipy<1.8.0` since `scipy>=1.8.0` is not backward compatible with `scipy<1.8.0` and additionally requires Python>=3.8, while Rasa supports Python 3.7 as well.
- [#11149](https://github.com/rasahq/rasa/issues/11149): Fix the extraction of values for slots with mapping conditions from trigger intents that activate a form, which was possible in `2.x`.


## [3.1.0] - 2022-03-25
### Features
- [#10203](https://github.com/rasahq/rasa/issues/10203): Add configuration options (via env variables) for library logging.
- [#10473](https://github.com/rasahq/rasa/issues/10473): Support other recipe types.

  This pull request also adds support for graph recipes, see details at
  https://rasa.com/docs/rasa/model-configuration and check Graph Recipe page.

  Graph recipe is a raw format for specifying executed graph directly. This is
  useful if you need a more powerful way to specify your model creation.
- [#10545](https://github.com/rasahq/rasa/issues/10545): Added optional `ssl_keyfile`, `ssl_certfile`, and `ssl_ca_certs` parameters to the Redis tracker store.
- [#10650](https://github.com/rasahq/rasa/issues/10650): Added `LogisticRegressionClassifier` to the NLU classifiers.

  This model is lightweight and might help in early prototyping. The training times typically decrease substantially, but the accuracy might be a bit lower too.
- [#8762](https://github.com/rasahq/rasa/issues/8762): Added support for Python 3.9.

### Improvements
- [#10378](https://github.com/rasahq/rasa/issues/10378): Bump TensorFlow version to 2.7.

  :::caution
  We can't guarantee the exact same output and hence model performance if your
  configuration uses `LanguageModelFeaturizer`. This applies to the case where the
  model is re-trained with the new rasa open source version without changing the
  configuration, random seeds, and data as well as to the case where a model trained with
  a previous version of rasa open source is loaded with this new version for inference.

  We suggest training a new model if you are upgrading to this version of Rasa Open Source.
- [#10444](https://github.com/rasahq/rasa/issues/10444): Make `rasa data validate` check for duplicated intents, forms, responses
  and slots when using domains split between multiple files.
- [#10899](https://github.com/rasahq/rasa/issues/10899): Add an `influence_conversation` flag to entites to provide a shorthand for ignoring an entity for all intents.
- [#9789](https://github.com/rasahq/rasa/issues/9789): Add `--request-timeout` command line argument to `rasa shell`, allowing users to configure the time a request can take before it's terminated.

### Bugfixes
- [#10376](https://github.com/rasahq/rasa/issues/10376): Validate regular expressions in nlu training data configuration.
- [#10409](https://github.com/rasahq/rasa/issues/10409): Unset the default values for `num_threads` and `finetuning_epoch_fraction` to `None` in order
  to fix cases when CLI defaults override the data from config.
- [#10447](https://github.com/rasahq/rasa/issues/10447): Update `rasa data validate` to not fail when `active_loop` is `null`
- [#10570](https://github.com/rasahq/rasa/issues/10570): Fixes Domain loading when domain config uses multiple yml files.

  Previously not all configures attributes were necessarily known when merging Domains, and in the case of `entities` were not being properly assigned to `intents`.
- [#10606](https://github.com/rasahq/rasa/issues/10606): Fix `max_history` truncation in `AugmentedMemoizationPolicy` to preserve the most recent `UserUttered` event.
  Previously, `AugmentedMemoizationPolicy` failed to predict next action after long sequences of actions (longer than `max_history`) because the policy did not have access to the most recent user message.
- [#10634](https://github.com/rasahq/rasa/issues/10634): Add `RASA_ENVIRONMENT` header in Kafka only if the environmental variable is set.
- [#10767](https://github.com/rasahq/rasa/issues/10767): Merge domain entities as lists of dicts, not lists of lists to support entity roles and groups across multiple domains.
- [#9351](https://github.com/rasahq/rasa/issues/9351): Add an option to specify `--domain` for `rasa test nlu` CLI command.

### Improved Documentation
- [#10553](https://github.com/rasahq/rasa/issues/10553): Fixed an over-indent in the Tokenizers section of the Components page of the docs.

### Miscellaneous internal changes
- [#10143](https://github.com/rasahq/rasa/issues/10143), [#10507](https://github.com/rasahq/rasa/issues/10507), [#10568](https://github.com/rasahq/rasa/issues/10568), [#10601](https://github.com/rasahq/rasa/issues/10601), [#10658](https://github.com/rasahq/rasa/issues/10658), [#10746](https://github.com/rasahq/rasa/issues/10746), [#10807](https://github.com/rasahq/rasa/issues/10807), [#9094](https://github.com/rasahq/rasa/issues/9094), [#9096](https://github.com/rasahq/rasa/issues/9096), [#9097](https://github.com/rasahq/rasa/issues/9097), [#9098](https://github.com/rasahq/rasa/issues/9098)


## [3.0.10] - 2022-03-15## [3.0.10] - 2022-03-15
### Bugfixes
- [#10675](https://github.com/rasahq/rasa/issues/10675): Fix broken conversion from Rasa JSON NLU data to Rasa YAML NLU data.


## [3.0.9] - 2022-03-11
### Bugfixes
- [#10412](https://github.com/rasahq/rasa/issues/10412): Fix Socket IO connection issues by upgrading sanic to v21.12.

  The bug is caused by [an invalid function signature](https://github.com/sanic-org/sanic/issues/2272) and is fixed in [v21.12](https://sanic.readthedocs.io/en/v21.12.1/sanic/changelog.html#version-21-12-0).

  This update brings some deprecations in `sanic`:

  - Sanic and Blueprint may no longer have arbitrary properties attached to them
      - Fixed this by moving user defined properties to the `instance.ctx` object
  - Sanic and Blueprint forced to have compliant names
      - Fixed this by using string literal names instead of the module's name via _\_name\_\_
  - `sanic.exceptions.abort` is Deprecated
      - Fixed by replacing it with `sanic.exceptions.SanicException`
  - `sanic.response.StreamingHTTPResponse` is deprecated
      - Fixed by replacing it with sanic.response.ResponseStream
- [#10447](https://github.com/rasahq/rasa/issues/10447): Update `rasa data validate` to not fail when `active_loop` is `null`

### Improved Documentation
- [#10798](https://github.com/rasahq/rasa/issues/10798): Updated the `model_confidence` parameter in `TEDPolicy` and `DIETClassifier`. The `linear_norm` is removed
  as it is no longer supported.
- [#10940](https://github.com/rasahq/rasa/issues/10940): Added an additional step to `Receiving Messages` section in slack.mdx documentation. After a slack update this
  additional step is needed to allow direct messages to the bot.
- [#10957](https://github.com/rasahq/rasa/issues/10957): Backport the updated deployment docs to 3.0.x.


## [3.0.8] - 2022-02-11
### Improvements
- [#10394](https://github.com/rasahq/rasa/issues/10394): Allow single tokens in rasa end-to-end test files to be annotated with multiple entities.

  Some entity extractors (s.a. `RegexEntityExtractor`) can generate multiple entities from a single expression. Before this change, `rasa test` would fail in this case, because test stories could not be annotated correctly.
  New annotation option is
  ```YAML
  stories:
    - story: Some story
      steps:
        - user: |
            cancel my [iphone][{"entity":"iphone", "value":"iphone"},{"entity":"smartphone", "value":"true"}{"entity":"mobile_service", "value":"true"}]
          intent: cancel_contract
  ```

### Bugfixes
- [#10865](https://github.com/rasahq/rasa/issues/10865): Fixed a bug where the `POST /conversations/<conversation_id>/tracker/events` endpoint repeated
  session start events when appending events to a new tracker.


## [3.0.7] - 2022-02-09
### Bugfixes
- [#10516](https://github.com/rasahq/rasa/issues/10516): Checkpoint weights were never loaded before. Implements overwriting checkpoint weights to the final model weights after training of `DIETClassifier`, `ResponseSelector` and `TEDPolicy`.
- [#10782](https://github.com/rasahq/rasa/issues/10782): Allow arbitrary keys under each slot in the domain to allow for custom slot types.
- [#10840](https://github.com/rasahq/rasa/issues/10840): Fix issue with missing running event loop in `MainThread` when starting Rasa Open
  Source for Rasa X with JWT secrets.


## [3.0.6] - 2022-01-28
### Deprecations and Removals
- [#10590](https://github.com/rasahq/rasa/issues/10590): Removed CompositionView.

### Bugfixes
- [#10504](https://github.com/rasahq/rasa/issues/10504): Fixes a bug which was caused by `DIETClassifier` (`ResponseSelector`, `SklearnIntentClassifier` and `CRFEntityExtractor` have the same issue) trying to process message which didn't have required features. Implements removing unfeaturized messages for the above-mentioned components before training and prediction.
- [#10540](https://github.com/rasahq/rasa/issues/10540): Enable slots with `from_entity` mapping that are not part of a form's required slots to be set during active loop.
- [#10673](https://github.com/rasahq/rasa/issues/10673): Catch `ValueError` for any port values that cannot be cast to integer and re-raise as `RasaException` during the initialisation of `SQLTrackerStore`.
- [#10728](https://github.com/rasahq/rasa/issues/10728): Use `tf.function` for model prediction to improve inference speed.
- [#10761](https://github.com/rasahq/rasa/issues/10761): Tie prompt-toolkit to ^2.0 to fix `rasa-shell`.

### Improved Documentation
- [#10536](https://github.com/rasahq/rasa/issues/10536): Update dynamic form behaviour docs section with an example on how to override `required_slots` in case of removal of a form required slot.


## [3.0.5] - 2022-01-19
### Bugfixes
- [#10519](https://github.com/rasahq/rasa/issues/10519): Corrects `transformer_size` parameter value (`None` by default) with a default size during loading in case `ResponseSelector` contains transformer layers.

### Miscellaneous internal changes
- [#10385](https://github.com/rasahq/rasa/issues/10385), [#592](https://github.com/rasahq/rasa/issues/592)


## [3.0.4] - 2021-12-22


### Miscellaneous internal changes
- [#10572](https://github.com/rasahq/rasa/issues/10572)


## [3.0.3] - 2021-12-16
### Bugfixes
- [#10448](https://github.com/rasahq/rasa/issues/10448): Copy lookup tables to train and test folds in cross validation. Before, the generated folds did not have a copy of
  the lookup tables from the original NLU data, so that `RegexEntityExtractor` could not recognize any entities during
  the evaluation.
- [#7645](https://github.com/rasahq/rasa/issues/7645): Do not print warning when subintent actions have response.

### Miscellaneous internal changes
- [#9945](https://github.com/rasahq/rasa/issues/9945)


## [3.0.2] - 2021-12-09
### Bugfixes
- [#10374](https://github.com/rasahq/rasa/issues/10374): Update SQLAlchemy version to a compatible one in case other dependencies force
  a lower version.
- [#10391](https://github.com/rasahq/rasa/issues/10391): Fix overriding of default config with custom config containing nested dictionaries. Before,
   the keys of a nested dictionary in the default config that were not specified in the
  custom config got lost.
- [#10401](https://github.com/rasahq/rasa/issues/10401): Add `UserWarning` to alert users trying to run `rasa x` CLI command with rasa version 3.0 or higher that rasa-x currently doesn't support rasa 3.x.

### Improved Documentation
- [#10291](https://github.com/rasahq/rasa/issues/10291): Added note to the slot mappings section of the migration guide to recommend checking dynamic form behavior on migrated assistants.


## [3.0.1] - 2021-12-02
### Bugfixes
- [#10235](https://github.com/rasahq/rasa/issues/10235): Fix previous slots getting filled after a restart. Previously events were
  searched from oldest to newest which meant we would find first occurrence of a
  message and use slots from thereafter. Now we use the last utterance or the
  restart event.

### Miscellaneous internal changes
- [#10405](https://github.com/rasahq/rasa/issues/10405)


## [3.0.0] - 2021-11-23
### Deprecations and Removals
- [#6487](https://github.com/rasahq/rasa/issues/6487): Remove backwards compatibility code with Rasa Open Source 1.x, Rasa Enterprise 0.35, and other outdated
  backwards compatibility code in `rasa.cli.x`, `rasa.core.utils`, `rasa.model_testing`, `rasa.model_training`
  and `rasa.shared.core.events`.
- [#8569](https://github.com/rasahq/rasa/issues/8569): Removed Python 3.6 support as [it reaches its end of life in December 2021](https://www.python.org/dev/peps/pep-0494/#lifespan).
- [#8862](https://github.com/rasahq/rasa/issues/8862): Follow through on removing deprecation warnings for synchronous `EventBroker` methods.
- [#8864](https://github.com/rasahq/rasa/issues/8864): Follow through on deprecation warnings for policies and policy ensembles.
- [#8867](https://github.com/rasahq/rasa/issues/8867): Follow through on deprecation warnings for `rasa.shared.data`.
- [#8868](https://github.com/rasahq/rasa/issues/8868): Follow through on deprecation warnings for the `Domain`. Most importantly this will
  enforce the schema of the [`forms` section](https://rasa.com/docs/rasa-pro/nlu-based-assistants/forms) in the domain file.
  This further includes the removal of the `UnfeaturizedSlot` type.
- [#8869](https://github.com/rasahq/rasa/issues/8869): Remove deprecated `change_form_to` and `set_form_validation` methods from `DialogueStateTracker`.
- [#8870](https://github.com/rasahq/rasa/issues/8870): Remove the support of Markdown training data format. This includes:
  - reading and writing of story files in Markdown format
  - reading and writing of NLU data in Markdown format
  - reading and writing of retrieval intent data in Markdown format
  - all the Markdown examples and tests that use Markdown
- [#8871](https://github.com/rasahq/rasa/issues/8871): Removed automatic renaming of deprecated action
  `action_deactivate_form` to `action_deactivate_loop`.
  `action_deactivate_form` will just be treated like other
  non-existing actions from now on.
- [#8872](https://github.com/rasahq/rasa/issues/8872): Remove deprecated `sorted_intent_examples` method from `TrainingData`.
- [#8873](https://github.com/rasahq/rasa/issues/8873): Raising `RasaException` instead of deprecation warning when using
  `class_from_module_path` for loading types other than classes.
- [#8874](https://github.com/rasahq/rasa/issues/8874): Specifying the `retrieve_events_from_previous_conversation_sessions` kwarg for the any `TrackerStore` was deprecated and has now been removed.
  Please use the `retrieve_full_tracker()` method instead.

  Deserialization of pickled trackers was deprecated and has now been removed.
  Rasa will perform any future save operations of trackers using json serialisation.

  Removed catch for missing (deprecated) `session_date` when saving trackers in `DynamoTrackerStore`.
- [#8879](https://github.com/rasahq/rasa/issues/8879): Removed the deprecated dialogue policy state featurizers: `BinarySingleStateFeature` and `LabelTokenizerSingleStateFeaturizer`.

  Removed the deprecated method `encode_all_actions` of `SingleStateFeaturizer`. Use `encode_all_labels` instead.
- [#8880](https://github.com/rasahq/rasa/issues/8880): Follow through with removing deprecated policies: `FormPolicy`, `MappingPolicy`, `FallbackPolicy`, `TwoStageFallbackPolicy`, and `SklearnPolicy`.

  Remove warning about default value of `max_history` in MemoizationPolicy. The default value is now `None`.
- [#8881](https://github.com/rasahq/rasa/issues/8881): Follow through on deprecation warnings and remove code, tests, and docs for `ConveRTTokenizer`, `LanguageModelTokenizer` and `HFTransformersNLP`.
- [#8883](https://github.com/rasahq/rasa/issues/8883): `rasa.shared.nlu.training_data.message.Message` method `get_combined_intent_response_key` has been removed. `get_full_intent` should now be used in its place.
- [#8974](https://github.com/rasahq/rasa/issues/8974): Intent IDs sent with events (to kafka and elsewhere) have been removed, intent
  names can be used instead (or if numerical values are needed for backwards
  compatibility, one can also hash the names to get previous ID values, ie.
  `hash(intent_name)` is the old ID values). Intent IDs have been removed because
  they were providing no extra value and integers that large were problematic for
  some event broker implementations.
- [#9236](https://github.com/rasahq/rasa/issues/9236): Remove `loop` argument from `train` method in `rasa`.
  This argument became redundant when Python 3.6 support was dropped as `asyncio.run` became available in Python 3.7.
- [#9390](https://github.com/rasahq/rasa/issues/9390): Remove `template_variables` and `e2e` arguments from `get_stories` method of `TrainingDataImporter`.
  This argument was used in Markdown data format and became redundant once Markdown was removed.
- [#9399](https://github.com/rasahq/rasa/issues/9399): `weight_sparsity` has been removed. Developers should replace it with `connection_density` in the following way: `connection_density` = 1-`weight_sparsity`.

  `softmax` is not available as a `loss_type` anymore.

  The `linear_norm` option has been removed as possible value for `model_confidence`. Please, use `softmax` instead.

  `minibatch` has been removed as a value for `tensorboard_log_level`, use `batch` instead.

  Removed deprecation warnings related to the removed component config values.
- [#9404](https://github.com/rasahq/rasa/issues/9404): Follow through on removing deprecation warnings raised in these modules:

  - `rasa/server.py`

  - `rasa/core/agent.py`

  - `rasa/core/actions/action.py`

  - `rasa/core/channels/mattermost.py`

  - `rasa/core/nlg/generator.py`

  - `rasa/nlu/registry.py`
- [#9432](https://github.com/rasahq/rasa/issues/9432): Remove deprecation warnings associated with the `"number_additional_patterns"` parameter of
  `rasa.nlu.featurizers.sparse_featurizer.regex_featurizer.RegexFeaturizer`.
  This parameter is no longer needed for incremental training.

  Remove deprecation warnings associated with the `"additional_vocabulary_size"` parameter of
  `rasa.nlu.featurizers.sparse_featurizer.count_vectors_featurizer.CountVectorsFeaturizer`.
  This parameter is no longer needed for incremental training.

  Remove deprecated functions `training_states_actions_and_entities` and
  `training_states_and_actions` from `rasa.core.featurizers.tracker_featurizers.TrackerFeaturizer`.
  Use `training_states_labels_and_entities` and `training_states_and_labels` instead.
- [#9455](https://github.com/rasahq/rasa/issues/9455): Follow through on deprecation warning for `NGramFeaturizer`
- [#9598](https://github.com/rasahq/rasa/issues/9598): The CLI commands `rasa data convert config` and `rasa data convert responses` which
  converted from the Rasa Open Source 1 to the Rasa Open Source 2 formats were removed.
  Please use a Rasa Open Source 2 installation to convert your training data before
  moving to Rasa Open Source 3.
- [#9766](https://github.com/rasahq/rasa/issues/9766): `rasa.core.agent.Agent.visualize` was removed. Please use `rasa visualize` or
  `rasa.core.visualize.visualize` instead.
- [#9972](https://github.com/rasahq/rasa/issues/9972): Removed slot auto-fill functionality, making the key invalid to use in the domain file.
  The `auto_fill` parameter was also removed from the constructor of the `Slot` class.
  In order to continue filling slots with entities of the same name, you now have to define a `from_entity` mapping in the `slots` section of the domain.
  To learn more about how to migrate your 2.0 assistant, please read the migration guide.

### Features
- [#10150](https://github.com/rasahq/rasa/issues/10150): Training data version upgraded from `2.0` to `3.0` due to breaking changes to format in Rasa Open Source 3.0
- [#10170](https://github.com/rasahq/rasa/issues/10170): A new experimental feature called `Markers` has been added.
  `Markers` allow you to define points of interest in conversations as a set of conditions that need to be met.
  A new command `rasa evaluate markers` allows you to apply these conditions to your existing tracker stores
  and outputs the points at which the conditions were satisfied.
- [#9803](https://github.com/rasahq/rasa/issues/9803): Rasa Open Source now uses the [model configuration](https://rasa.com/docs/rasa-pro/nlu-based-assistants/model-configuration) to build a

  [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph).
  This graph describes the dependencies between the items in your model configuration and
  how data flows between them. This has two major benefits:

  - Rasa Open Source can use the computational graph to optimize the execution of your
    model. Examples for this are efficient caching of training steps or executing
    independent steps in parallel.
  - Rasa Open Source can represent different model architectures flexibly. As long as the
    graph remains acyclic Rasa Open Source can in theory pass any data to any graph
    component based on the model configuration without having to tie the underlying
    software architecture to the used model architecture.

  This change required changes to custom policies and custom NLU components. See the
  documentation for a detailed
  [migration guide](https://rasa.com/docs/rasa-pro/migration-guide#custom-policies-and-custom-components).
- [#9972](https://github.com/rasahq/rasa/issues/9972): Added explicit mechanism for slot filling that allows slots to be set and/or updated throughout the conversation.
  This mechanism is enabled by defining global slot mappings in the `slots` section of the domain file.

  In order to support this new functionality, implemented a new default action: `action_extract_slots`. This new action runs after each user turn and checks if any slots can be filled with information extracted from the last user message based on defined slot mappings.

  Since slot mappings were moved away from the `forms` section of the domain file, converted the form's `required_slots` to a list of slot names.
  In order to restrict certain mappings to a form, you can now use the `conditions` key in the mapping to define the applicable `active_loop`, like so:
  ```yaml
  slots:
    location:
      type: text
      influence_conversation: false
      mappings:
      - type: from_entity
        entity: city
        conditions:
        - active_loop: booking_form
  ```
  To learn more about how to migrate your 2.0 assistant, please read the migration guide.

### Improvements
- [#10189](https://github.com/rasahq/rasa/issues/10189): Updated the `/status` endpoint response payload, and relevant documentation, to return/reflect the updated 3.0 keys/values.
- [#7619](https://github.com/rasahq/rasa/issues/7619): Bump TensorFlow version to 2.6.

    This update brings some security benefits (see TensorFlow
    [release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.6.0)
    for details). However, internal experiments suggest that it is also associated with
    increased train and inference time, as well as increased memory usage.

    You can read more about why we decided to update TensorFlow, and what the expected
    impact is [here](https://rasa.com/blog/let-s-talk-about-tensorflow-2-6/).

    If you experience a significant increase in train time, inference time, and/or memory
    usage, please let us know in the [forum](https://forum.rasa.com/t/feedback-upgrading-to-tensorflow-2-6/48331).

    Users can no longer set `TF_DETERMINISTIC_OPS=1` if they are using GPU(s) because a
    `tf.errors.UnimplementedError` will be thrown by TensorFlow (read more
    [here](https://github.com/tensorflow/tensorflow/releases/tag/v2.6.0)).

    :::caution
    This **breaks backward compatibility of previously trained models**.
    It is not possible to load models trained with previous versions of Rasa Open Source. Please re-train
    your assistant before trying to use this version.
- [#8057](https://github.com/rasahq/rasa/issues/8057): Added authentication support for connecting to external RabbitMQ servers.
  Currently user has to hardcode a username and a password in a URL in order to connect to an external RabbitMQ server.
- [#8459](https://github.com/rasahq/rasa/issues/8459): 1) Failed test stories will display full retrieval intents.

  2) Retrieval intents will be extracted during action prediction in test stories so that we won't have unnecessary mismatches anymore.

  Let's take this example story:
  ```yaml
  - story: test story
    steps:
    - user: |
        what is your name?
      intent: chitchat/ask_name
    - action: utter_chitchat/ask_name
    - intent: bye
    - action: utter_bye
  ```

  Before:
  ```yaml
    steps:
    - intent: chitchat   # 1) intent is not displayed in it's original form
    - action: utter_chitchat/ask_name  # predicted: utter_chitchat
                    # 2) retrieval intent is not extracted during action prediction and we have a mismatch

    - intent: bye  # some other fail
    - action: utter_bye # some other fail
  ```

  Both 1) and 2) problems are solved.

  Now:
  ```yaml
    steps:
    - intent: chitchat/ask_name
    - action: utter_chitchat/ask_name
    - intent: bye  # some other fail
    - action: utter_bye # some other fail
  ```
- [#8469](https://github.com/rasahq/rasa/issues/8469): Added `-i` command line option to make RASA listen on a specific ip-address instead of any network interface
- [#8760](https://github.com/rasahq/rasa/issues/8760): `rasa data validate` now checks that forms referenced in `active_loop` directives are defined in the domain
- [#8914](https://github.com/rasahq/rasa/issues/8914): Every conversation event now includes in its metadata the ID of the model which loaded at the time it was created.
- [#8924](https://github.com/rasahq/rasa/issues/8924): Send indices of user message tokens along with the `UserUttered` event through the event broker to Rasa X.
- [#8929](https://github.com/rasahq/rasa/issues/8929): Added optional flag to convert intent ID hashes from integer to string in the `KafkaEventBroker`.
- [#8933](https://github.com/rasahq/rasa/issues/8933): Make it possible to use `or` functionality for `slot_was_set` events.
- [#9068](https://github.com/rasahq/rasa/issues/9068): Upgraded the spaCy dependency from version 3.0 to 3.1.
- [#9133](https://github.com/rasahq/rasa/issues/9133): Implemented `fingerprint` methods in these classes:

  - `Event`
  - `Slot`
  - `DialogueStateTracker`
- [#9193](https://github.com/rasahq/rasa/issues/9193): Added debug message that logs when a response condition is used.
- [#9485](https://github.com/rasahq/rasa/issues/9485): The naming scheme for trained models was changed. Unless you provide a
  `--fixed-model-name` to `rasa train`, Rasa Open Source will now generate a new model
  name using the schema `<timestamp>-<random name>.tar.gz`, e.g.
  - `20211018-094821-composite-pita.tar.gz` (for a model containing a trained NLU and dialogue model)
  - `nlu-20211018-094821-composite-pita.tar.gz` (for a model containing only a trained NLU model but not a dialogue model)
  - `core-20211018-094821-composite-pita.tar.gz` (for a model containing only a trained dialogue model but no NLU model)
- [#9604](https://github.com/rasahq/rasa/issues/9604): Due to changes in the model architecture the behavior of `rasa train --dry-run` changed.
  The exit codes now have the following meaning:

  * `0` means that the model does not require an expensive retraining. However, the
    responses might still require updating by running `rasa train`
  * `1` means that one or multiple components require to be retrained.
  * `8` means that the `--force` flag was used and hence any cached results are ignored
    and the entire model is retrained.
- [#9642](https://github.com/rasahq/rasa/issues/9642): Machine learning components like `DIETClassifier`, `ResponseSelector` and `TEDPolicy` using a `ranking_length` parameter will no longer report renormalised
  confidences for the top predictions by default.

  A new parameter `renormalize_confidences` is added to these components which if set to `True`, renormalizes the confidences of top `ranking_length` number of predictions to sum up to 1. The default value is `False`, which means no renormalization will be applied by default. It is advised to leave it to `False` but if you are trying to reproduce the results from previous versions of Rasa Open Source, you can set it to `True`.

  Renormalization will only be applied if `model_confidence=softmax` is used.

### Bugfixes
- [#10079](https://github.com/rasahq/rasa/issues/10079): Fixed validation behavior and logging output around unused intents and utterances.
- [#8614](https://github.com/rasahq/rasa/issues/8614): `rasa test nlu --cross-validation` uses autoconfiguration when no pipeline is defined instead of failing
- [#9195](https://github.com/rasahq/rasa/issues/9195): Update DynamoDb tracker store to correctly retrieve all `sender_ids` from a DynamoDb table.
- [#9629](https://github.com/rasahq/rasa/issues/9629): Fix for `failed_test_stories.yml` not printing the correct message when the extracted entity
  specified in a test story is incorrect.
- [#9852](https://github.com/rasahq/rasa/issues/9852): Fix CVE-2021-41127

### Improved Documentation
- [#10095](https://github.com/rasahq/rasa/issues/10095): Added new docs for Markers.
- [#10230](https://github.com/rasahq/rasa/issues/10230): Update pip in same command which installs rasa and clarify supported version in
  docs.
- [#8568](https://github.com/rasahq/rasa/issues/8568): Update `pika` consumer code in Event Brokers documentation.
- [#8930](https://github.com/rasahq/rasa/issues/8930): Adds documentation on how to use `CRFEntityExtractor` with features from a dense featurizer (e.g. `LanguageModelFeaturizer`).
- [#9366](https://github.com/rasahq/rasa/issues/9366): Updated docs (Domain, Forms, Default Actions, Migration Guide, CLI) to provide more detail over the new slot mappings changes.
- [#9711](https://github.com/rasahq/rasa/issues/9711): Updated documentation publishing mechanisms to build one version of [the documentation](https://rasa.com/docs/rasa)
  for each major version of Rasa Open Source, starting from 2.x upwards. Previously, we were building one
  version of the documentation for each minor version of Rasa Open Source, resulting in a poor user
  experience and high maintenance costs.

### Miscellaneous internal changes
- [#10065](https://github.com/rasahq/rasa/issues/10065), [#10084](https://github.com/rasahq/rasa/issues/10084), [#10086](https://github.com/rasahq/rasa/issues/10086), [#10131](https://github.com/rasahq/rasa/issues/10131), [#9078](https://github.com/rasahq/rasa/issues/9078), [#9131](https://github.com/rasahq/rasa/issues/9131), [#9135](https://github.com/rasahq/rasa/issues/9135), [#9557](https://github.com/rasahq/rasa/issues/9557)


## [2.8.16] - 2021-12-09
### Improvements
- [#10413](https://github.com/rasahq/rasa/issues/10413): The value of the `RASA_ENVIRONMENT` environmental variable is sent as a header in messages logged by `KafkaEventBroker`.
  This value was previously only made available by `PikaEventConsumer`.

### Bugfixes
- [#10458](https://github.com/rasahq/rasa/issues/10458): Make `action_metadata` json serializable and make it available on the tracker. This is a backport of a fix in 3.0.0.


## [2.8.15] - 2021-11-25
### Bugfixes
- [#10381](https://github.com/rasahq/rasa/issues/10381): Validate regular
  expressions in nlu training data configuration.

## [2.8.14] - 2021-11-18
### Bugfixes
- [#10241](https://github.com/rasahq/rasa/issues/10241): Bump TensorFlow version to 2.6.2. _We have plans to port this
  change to 3.x (see [this issue](https://github.com/RasaHQ/rasa/issues/10378))_.
- [#10257](https://github.com/rasahq/rasa/issues/10257): Downgrade google-auth to <2.

## [2.8.13] - 2021-11-11
### Bugfixes
- [#9949](https://github.com/rasahq/rasa/issues/9949): Fixed new intent creation in `rasa interactive` command. Previously, this failed with 500
  from the server due to `UnexpecTEDIntentPolicy` trying to predict with the new intent not in
  domain.
- [#9982](https://github.com/rasahq/rasa/issues/9982): Install mitie library when preparing test runs. This step was missing before
  and tests were thus failing as we have many tests which rely on mitie library.
  Previously, `make install-full` was required.

### Miscellaneous internal changes
- [#10146](https://github.com/rasahq/rasa/issues/10146), [#9989](https://github.com/rasahq/rasa/issues/9989)


## [2.8.12] - 2021-10-21
### Bugfixes
- [#9771](https://github.com/rasahq/rasa/issues/9771): Fixed a bug where `rasa test --fail-on-prediction-errors` would raise a
  `WrongPredictionException` for entities which were actually predicted correctly.

  This happened in two ways:
  1. if for a user message some entities were extracted multiple times (by multiple entity
  extractors) but listed only once in the test story,
  2. if the order in which entities from a message were extracted didn't match the order
  in which they were listed in the test story.

### Improved Documentation
- [#9691](https://github.com/rasahq/rasa/issues/9691): Improve the documentation for training `TEDPolicy` with data augmentation.


## [2.8.11] - 2021-10-20
### Bugfixes
- [#9858](https://github.com/rasahq/rasa/issues/9858): Updates dependency on `sanic-jwt` (1.5.0 -> ">=1.6.0, <1.7.0")

  This removes the need to pin the version of `pyjwt` as the newer version of `sanic-jwt`
  manages this properly.


## [2.8.10] - 2021-10-14
### Bugfixes
- [#5657](https://github.com/rasahq/rasa/issues/5657): Add List handling in the `send_custom_json` method on `channels/facebook.py`.
  Bellow are some examples that could cause en error before.

  Example 1: when the whole json is a List
  ```
  [
      {
          "blocks": {
              "type": "progression_bar",
              "text": {"text": "progression 1", "level": "1"},
          }
      },
      {"sender": {"id": "example_id"}},
  ]
  ```

  Example 2: instead of being a Dict, *blocks* is a List when there are 2 *type*
  keys under it
  ```
  {
      "blocks": [
          {"type": "title", "text": {"text": "Conversation progress"}},
          {
              "type": "progression_bar",
              "text": {"text": "Look how far we are...", "level": "1"},
          },
      ]
  }
  ```
- [#7676](https://github.com/rasahq/rasa/issues/7676): Fixed bug when using wit.ai training data to train.
  Training failed with an error similarly to this:

  ```bash
    File "./venv/lib/python3.8/site-packages/rasa/nlu/classifiers/diet_classifier.py", line 803, in train
      self.check_correct_entity_annotations(training_data)
    File "./venv/lib/python3.8/site-packages/rasa/nlu/extractors/extractor.py", line 418, in check_correct_entity_annotations
      entities_repr = [
    File "./venv/lib/python3.8/site-packages/rasa/nlu/extractors/extractor.py", line 422, in <listcomp>
      entity[ENTITY_ATTRIBUTE_VALUE],
  KeyError: 'value'
  ```
- [#9851](https://github.com/rasahq/rasa/issues/9851): Fix CVE-2021-41127


## [2.8.9] - 2021-10-08
### Improvements
- [#7619](https://github.com/rasahq/rasa/issues/7619): Bump TensorFlow version to 2.6.

  This update brings some security benefits (see TensorFlow
  [release notes](https://github.com/tensorflow/tensorflow/releases/tag/v2.6.0)
  for details). However, internal experiments suggest that it is also associated with
  increased train and inference time, as well as increased memory usage.

  You can read more about why we decided to update TensorFlow, and what the expected
  impact is [here](https://rasa.com/blog/let-s-talk-about-tensorflow-2-6/).

  If you experience a significant increase in train time, inference time, and/or memory
  usage, please let us know in the [forum](https://forum.rasa.com/t/feedback-upgrading-to-tensorflow-2-6/48331).

  Users can no longer set `TF_DETERMINISTIC_OPS=1` if they are using GPU(s) because a
  `tf.errors.UnimplementedError` will be thrown by TensorFlow (read more
  [here](https://github.com/tensorflow/tensorflow/releases/tag/v2.6.0)).

  :::caution
  This **breaks backward compatibility of previously trained models**.
  It is not possible to load models trained with previous versions of Rasa Open Source. Please re-train
  your assistant before trying to use this version.

  :::
## [2.8.8] - 2021-10-06


### Improvements
- [#7250](https://github.com/rasahq/rasa/issues/7250): Added a function to display the actual text of a Token when inspecting
  a Message in a pipeline, making it easier to debug.

### Improved Documentation
- [#9780](https://github.com/rasahq/rasa/issues/9780): Removing the experimental feature warning for `conditional response variations` from the Rasa docs.
  The behaviour of the feature remains unchanged.
- [#9782](https://github.com/rasahq/rasa/issues/9782): Updates [quick install documentation](https://rasa.com/docs/rasa-pro/installation/python/installation) with optional venv step, better pip install instructions, & M1 warning


## [2.8.7] - 2021-09-20
### Bugfixes
- [#9678](https://github.com/rasahq/rasa/issues/9678): Explicitly set the upper limit for currently compatible TensorFlow versions.


## [2.8.6] - 2021-09-09
### Bugfixes
- [#9302](https://github.com/rasahq/rasa/issues/9302): Fix rules not being applied when a featurised categorical slot has as one of its allowed
  values `none`, `NoNe`, `None` or a similar value.


## [2.8.5] - 2021-09-06
### Bugfixes
- [#9476](https://github.com/rasahq/rasa/issues/9476): AugmentedMemoizationPolicy is accelerated for large trackers
- [#9542](https://github.com/rasahq/rasa/issues/9542): Bump tensorflow to 2.3.4 to address security vulnerabilities


## [2.8.4] - 2021-09-02
### Improvements
- [#5546](https://github.com/rasahq/rasa/issues/5546): Increase speed of augmented lookup for `AugmentedMemoizationPolicy`

### Bugfixes
- [#7362](https://github.com/rasahq/rasa/issues/7362): Fix `--data` being treated as if non-optional on sub-commands of `rasa data convert`
- [#9490](https://github.com/rasahq/rasa/issues/9490): Fixes bug where `hide_rule_turn` was defaulting to `None` when ActionExecuted was deserialised.

### Miscellaneous internal changes
- [#8682](https://github.com/rasahq/rasa/issues/8682)


## [2.8.3] - 2021-08-19
### Bugfixes
- [#7695](https://github.com/rasahq/rasa/issues/7695): Ignore checking that intent is in domain for E2E story utterances when running `rasa data validate`. Previously data validation would fail on E2E stories.


## [2.8.2] - 2021-08-04
### Bugfixes
- [#9203](https://github.com/rasahq/rasa/issues/9203): Fixes a bug which caused training of `UnexpecTEDIntentPolicy` to crash when end-to-end training stories were included in the training data.

  Stories with end-to-end training data will now be skipped for the training of `UnexpecTEDIntentPolicy`.

### Improved Documentation
- [#8024](https://github.com/rasahq/rasa/issues/8024): Removing the experimental feature warning for the `story validation` tool from the rasa docs.
  The behaviour of the feature remains unchanged.
- [#8791](https://github.com/rasahq/rasa/issues/8791): Removing the experimental feature warning for `entity roles and groups` from the rasa docs,
  and from the code where it previously appeared as a print statement.
  The behaviour of the feature remains otherwise unchanged.


## [2.8.1] - 2021-07-22
### Improvements
- [#9085](https://github.com/rasahq/rasa/issues/9085): Add support for `cafile` parameter in `endpoints.yaml`.
  This will load a custom local certificate file and use it when making requests to that endpoint.

  For example:

  ```yaml
  action_endpoint:
    url: https://localhost:5055/webhook
    cafile: ./cert.pem
  ```

  This means that requests to the action server `localhost:5055` will use the certificate `cert.pem` located in the current working directory.

### Bugfixes
- [#9182](https://github.com/rasahq/rasa/issues/9182): Fixes wrong overriding of `epochs` parameter when `TEDPolicy` or `UnexpecTEDIntentPolicy` is not loaded in finetune mode.


## [2.8.0] - 2021-07-12
### Deprecations and Removals
- [#9045](https://github.com/rasahq/rasa/issues/9045): The option `model_confidence=linear_norm` is deprecated and will be removed in Rasa Open Source `3.0.0`.

  Rasa Open Source `2.3.0` introduced `linear_norm` as a possible value for `model_confidence`
  parameter in machine learning components such as `DIETClassifier`, `ResponseSelector` and `TEDPolicy`.
  Based on user feedback, we have identified multiple problems with this option.
  Therefore, `model_confidence=linear_norm` is now deprecated and
  will be removed in Rasa Open Source `3.0.0`. If you were using `model_confidence=linear_norm` for any of the mentioned components,
  we recommend to revert it back to `model_confidence=softmax` and re-train the assistant. After re-training,
  we also recommend to [re-tune the thresholds for fallback components](https://rasa.com/docs/rasa-pro/nlu-based-assistants/fallback-handoff#fallbacks).
- [#9091](https://github.com/rasahq/rasa/issues/9091): The fallback mechanism for spaCy models has now been removed in Rasa `3.0.0`.

  Rasa Open Source `2.5.0` introduced support for spaCy 3.0. This introduced a
  breaking feature because models would no longer be manually linked. To make
  the transition smooth Rasa would rely on the `language` parameter in the
  `config.yml` to fallback to a medium spaCy model if no model was configured
  for the `SpacyNLP` component. In Rasa Open Source `3.0.0` and onwards the
  `SpacyNLP` component will require the model name (like `"en_core_web_md"`)
  to be passed explicitly.

### Features
- [#8724](https://github.com/rasahq/rasa/issues/8724): Added `sasl_mechanism` as an optional configurable parameters for the [Kafka Producer](https://rasa.com/docs/rasa-pro/production/event-brokers#kafka-event-broker).
- [#8913](https://github.com/rasahq/rasa/issues/8913): Introduces a new policy called [`UnexpecTEDIntentPolicy`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/policies#unexpected-intent-policy).

  `UnexpecTEDIntentPolicy` helps you review conversations
   and also allows your bot to react to unexpected user turns in conversations.
   It is an auxiliary policy that should only be used in conjunction with
   at least one other policy, as the only action that it can trigger
   is the special and newly introduced
   [`action_unlikely_intent`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/default-actions#action_unlikely_intent) action.

   The auto-configuration will include `UnexpecTEDIntentPolicy` in your
   configuration automatically, but you can also include it yourself
   in the `policies` section of the configuration:

   ```
   policies:
     - name: UnexpecTEDIntentPolicy
       epochs: 200
       max_history: 5
   ```

  As part of the feature, it also introduces:

  - [`IntentMaxHistoryTrackerFeaturizer`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/policies#3-intent-max-history)
    to featurize the trackers for `UnexpecTEDIntentPolicy`.
  - `MultiLabelDotProductLoss` to support `UnexpecTEDIntentPolicy`'s multi-label training objective.
  - A new default action called [`action_unlikely_intent`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/default-actions#action_unlikely_intent).


  `rasa test` command has also been adapted to `UnexpecTEDIntentPolicy`:

  - If a test story contains `action_unlikely_intent` and the policy ensemble does not trigger it, this leads to
    a test error (wrongly predicted action) and the corresponding story will be logged in `failed_test_stories.yml`.
  - If the story does not contain `action_unlikely_intent` and Rasa Open Source does predict it then
    the prediction of `action_unlikely_intent` will be ignored for the evaluation (and hence not lead
    to a prediction error) but the story will be logged in a file called `stories_with_warnings.yml`.


  The `rasa data validate` command will warn if `action_unlikely_intent` is
  included in the training stories. Accordingly, `YAMLStoryWriter` and `MarkdownStoryWriter` have been updated to not dump `action_unlikely_intent` when writing stories to a file.

  :::caution
  The introduction of a new default action **breaks backward compatibility of previously trained models**.
  It is not possible to load models trained with previous versions of Rasa Open Source. Please re-train
  your assistant before trying to use this version.

  :::

### Improvements
- [#8127](https://github.com/rasahq/rasa/issues/8127): Added detailed json schema validation for `UserUttered`, `SlotSet`, `ActionExecuted` and `EntitiesAdded` events both sent and received from the action server, as well as covered at high-level the validation of the rest of the 20 events.
  In case the events are invalid, a `ValidationError` will be raised.
- [#8232](https://github.com/rasahq/rasa/issues/8232): Users don't need to specify an additional buffer size for sparse featurizers anymore during incremental training.

  Space for new sparse features are created dynamically inside the downstream machine learning
  models - `DIETClassifier`, `ResponseSelector`. In other words, no extra buffer is created in
  advance for additional vocabulary items and space will be dynamically allocated for them inside the model.

  This means there's no need to specify `additional_vocabulary_size` for [`CountVectorsFeaturizer`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#countvectorsfeaturizer) or
  `number_additional_patterns` for [`RegexFeaturizer`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#regexfeaturizer). These parameters are now deprecated.

  **Before**
  ```yaml
  pipeline:
    - name: "WhitespaceTokenizer"
    - name: "RegexFeaturizer"
      number_additional_patterns: 100
    - name: "CountVectorsFeaturizer"
      additional_vocabulary_size: {text: 100, response: 20}
  ```

  **Now**
  ```yaml
  pipeline:
    - name: "WhitespaceTokenizer"
    - name: "RegexFeaturizer"
    - name: "CountVectorsFeaturizer"
  ```

  Also, all custom layers specifically built for machine learning models - `RasaSequenceLayer`, `RasaFeatureCombiningLayer`
  and `ConcatenateSparseDenseFeatures` now inherit from `RasaCustomLayer` so that they support flexible incremental training out of the box.
- [#8295](https://github.com/rasahq/rasa/issues/8295): Speed up the contradiction check of the [`RulePolicy`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/policies#rule-policy)
  by a factor of 3.
- [#8801](https://github.com/rasahq/rasa/issues/8801): Change the confidence score assigned by [`FallbackClassifier`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#fallbackclassifier) to fallback intent to be the same as the fallback threshold.
- [#8926](https://github.com/rasahq/rasa/issues/8926): Issue a UserWarning if a specified **domain folder** contains files that look like YML files but cannot be parsed successfully.
  Only invoked if user specifies a folder path in `--domain` paramater. Previously those invalid files in the specified folder were silently ignored.
  **Does not apply** to individually specified domain YAML files, e.g. `--domain /some/path/domain.yml`, those being invalid will still raise an exception.

### Bugfixes
- [#8711](https://github.com/rasahq/rasa/issues/8711): Fix for unnecessary retrain and duplication of folders in the model

### Miscellaneous internal changes
- [#8241](https://github.com/rasahq/rasa/issues/8241), [#8525](https://github.com/rasahq/rasa/issues/8525), [#8694](https://github.com/rasahq/rasa/issues/8694), [#8704](https://github.com/rasahq/rasa/issues/8704)


## [2.7.2] - 2021-08-09
### Bugfixes
- [#7695](https://github.com/rasahq/rasa/issues/7695): Ignore checking that intent is in domain for E2E story utterances when running `rasa data validate`. Previously data validation would fail on E2E stories.
- [#8711](https://github.com/rasahq/rasa/issues/8711): Fix for unnecessary retrain and duplication of folders in the model


## [2.7.1] - 2021-06-16


### Bugfixes
- [#7286](https://github.com/rasahq/rasa/issues/7286): Best model checkpoint allows for metrics to be equal to previous best if at least one
  metric improves, rather than strict improvement for each metric.
- [#8200](https://github.com/rasahq/rasa/issues/8200): Fixes a bug where multiple plots overlap each other and are rendered incorrectly when comparing performance across multiple NLU pipelines.
- [#8812](https://github.com/rasahq/rasa/issues/8812): Don't evaluate entities if no entities present in test data.

  Also, catch exception in `plot_paired_histogram` when data is empty.


## [2.7.0] - 2021-06-03


### Improvements
- [#7691](https://github.com/rasahq/rasa/issues/7691): Changed the default config to train the `RulePolicy` before the `TEDPolicy`.
  This means that conflicting rule/stories will be identified before a potentially slow training of the `TEDPolicy`.
- [#7799](https://github.com/rasahq/rasa/issues/7799): Updated validator used by `rasa data validate` to verify that actions used in stories and rules are present in the domain and that form slots match domain slots.
- [#7912](https://github.com/rasahq/rasa/issues/7912): Rename `plot_histogram` to `plot_paired_histogram` and fix missing bars in the plot.
- [#8225](https://github.com/rasahq/rasa/issues/8225): Changed --data option type in the ``rasa data validate``` command to allow more than one path to be passed.

### Bugfixes
- [#8152](https://github.com/rasahq/rasa/issues/8152): The file `failed_test_stories.yml` (generated by `rasa test`) now also includes the wrongly predicted entity as a comment next to the entity of a user utterance.
  Additionally, the comment printed next to the intent of a user utterance is printed only if the intent was wrongly predicted (irrelevantly if there was a wrongly predicted entity or not in the specific user utterance).
- [#8309](https://github.com/rasahq/rasa/issues/8309): Added check in PikaEventBroker constructor: if port cannot be cast to integer, raise RasaException
- [#8388](https://github.com/rasahq/rasa/issues/8388): Fixed bug where missing intent warnings appear when running `rasa test`
- [#8611](https://github.com/rasahq/rasa/issues/8611): Update `should_retrain` function to return the correct fingerprint comparison result
  even when there is a problem with model unpacking.
- [#8719](https://github.com/rasahq/rasa/issues/8719): Handle correctly Telegram edited message.

### Miscellaneous internal changes
- [#8591](https://github.com/rasahq/rasa/issues/8591), [#8641](https://github.com/rasahq/rasa/issues/8641), [#8654](https://github.com/rasahq/rasa/issues/8654), [#8658](https://github.com/rasahq/rasa/issues/8658), [#8802](https://github.com/rasahq/rasa/issues/8802)


## [2.6.3] - 2021-05-28


### Bugfixes
- [#8046](https://github.com/rasahq/rasa/issues/8046): `ResponseSelector` can now be trained with the transformer enabled (i.e. when a positive
  `number_of_transformer_layers` is provided) even if one doesn't specify the transformer's
  size. Previously, not specifying `transformer_size` led to an error.
- [#8386](https://github.com/rasahq/rasa/issues/8386): Return `EntityEvaluationResult` during evaluation of test stories only if `parsed_message` is not `None`.
- [#8546](https://github.com/rasahq/rasa/issues/8546): Ignore `OSError` in Sentry reporting.
- [#8547](https://github.com/rasahq/rasa/issues/8547): Replaced `ValueError` with `RasaException` in TED model `_check_data` method.
- [#8639](https://github.com/rasahq/rasa/issues/8639): Changed import to fix agent creation in Jupyter.

### Miscellaneous internal changes
- [#7906](https://github.com/rasahq/rasa/issues/7906), [#8544](https://github.com/rasahq/rasa/issues/8544), [#8725](https://github.com/rasahq/rasa/issues/8725), [#8726](https://github.com/rasahq/rasa/issues/8726), [#8727](https://github.com/rasahq/rasa/issues/8727), [#8728](https://github.com/rasahq/rasa/issues/8728)


## [2.6.2] - 2021-05-18


### Bugfixes
- [#8364](https://github.com/rasahq/rasa/issues/8364): Fixed a bug where [`ListSlot`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/domain#list-slot)s were filled with single items
  in case only one matching entity was extracted for this slot.

  Values applied to [`ListSlot`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/domain#list-slot)s will be converted to a `List`
  in case they aren't one.
- [#8581](https://github.com/rasahq/rasa/issues/8581): Fix bug with false rule conflicts

  This essentially reverts [PR 8446](https://github.com/RasaHQ/rasa/pull/8446/files), except for the tests.
  The PR is redundant due to [PR 8646](https://github.com/RasaHQ/rasa/pull/8646/files).
- [#8590](https://github.com/rasahq/rasa/issues/8590): Handle `AttributeError ` thrown by empty slot mappings in domain form through refactoring.
- [#8631](https://github.com/rasahq/rasa/issues/8631): Fixed incorrect `The action 'utter_<response selector intent>' is used in the stories, but is not a valid utterance action`
  error when running `rasa data validate` with response selector responses in the domain file.

### Improved Documentation
- [#8079](https://github.com/rasahq/rasa/issues/8079): Added a note to clarify best practice for resetting all slots after form deactivation.

### Miscellaneous internal changes
- [#8587](https://github.com/rasahq/rasa/issues/8587)


## [2.6.1] - 2021-05-11


### Bugfixes
- [#7908](https://github.com/rasahq/rasa/issues/7908): Made `SchemaError` message available to validator so that the reason why reason schema validation fails during `rasa data validate` is displayed when response `text` value is `null`.
  Added warning message when deprecated MappingPolicy format is used in the domain.
- [#8623](https://github.com/rasahq/rasa/issues/8623): When there are multiple entities in a user message, they will get sorted when creating a
  representation of the current dialogue state.

  Previously, the ordering was random, leading to inconsistent state representations. This
  would sometimes lead to memoization policies failing to recall a memorised action.


## [2.6.0] - 2021-05-06


### Deprecations and Removals
- [#261](https://github.com/rasahq/rasa/issues/261): In forms, the keyword `required_slots` should always precede the definition of slot mappings and the lack of it is deprecated.
  Please see the [migration guide](https://rasa.com/docs/rasa-pro/migration-guide) for more information.
- [#8428](https://github.com/rasahq/rasa/issues/8428): `rasa.data.get_test_directory`, `rasa.data.get_core_nlu_directories`, and
  `rasa.shared.nlu.training_data.training_data.TrainingData::get_core_nlu_directories`
  are deprecated and will be removed in Rasa Open Source 3.0.0.
- [#8498](https://github.com/rasahq/rasa/issues/8498): Update the minimum compatible model version to "2.6.0".
  This means all models trained with an earlier version will have to be retrained.

### Features
- [#8103](https://github.com/rasahq/rasa/issues/8103): Feature enhancement enabling JWT authentication for the Socket.IO channel. Users can define `jwt_key` and `jwt_method` as parameters in their credentials file for authentication.
- [#8180](https://github.com/rasahq/rasa/issues/8180): Allows a Rasa bot to be connected to a Twilio Voice channel. More details in the [Twilio Voice docs](https://rasa.com/docs/rasa-pro/connectors/twilio-voice)
- [#8532](https://github.com/rasahq/rasa/issues/8532): Conditional response variations are supported in the `domain.yml` without requiring users to write custom actions code.

  A condition can be a list of slot-value mapping constraints.

### Improvements
- [#261](https://github.com/rasahq/rasa/issues/261): Added an optional `ignored_intents` parameter in forms.

  - To use it, add the `ignored_intents` parameter  in your `domain.yml` file after the forms name and provide a list of intents to ignore. Please see [Forms](https://rasa.com/docs/rasa-pro/nlu-based-assistants/forms) for more information.
  - This can be used in case the user never wants to fill any slots of a form with the specified intent, e.g. chitchat.
- [#5786](https://github.com/rasahq/rasa/issues/5786): Add function to carry `max_history` to featurizer
- [#7589](https://github.com/rasahq/rasa/issues/7589): Improved the machine learning models' codebase by factoring out shared feature-processing
  logic into three custom layer classes:
  - `ConcatenateSparseDenseFeatures` combines multiple sparse and dense feature tensors
  into one.
  - `RasaFeatureCombiningLayer` additionally combines sequence-level and sentence-level
  features.
  - `RasaSequenceLayer` is used for attributes with sequence-level features; it
  additionally embeds the combined features with a transformer and facilitates masked
  language modeling.
- [#7685](https://github.com/rasahq/rasa/issues/7685): Added the following usability improvements with respect to entities getting extracted multiple times:
  * Added warnings for competing entity extractors at training time and for overlapping entities at inference time
  * Improved docs to help users handle overlapping entity problems.
- [#7999](https://github.com/rasahq/rasa/issues/7999): Replace `weight_sparsity` with `connection_density` in all transformer-based models and add guarantees about internal layers.

  We rename `DenseWithSparseWeights` into `RandomlyConnectedDense`, and guarantee that even at density zero the output is dense and every input is connected to at least one output. The former `weight_sparsity` parameter of DIET, TED, and the ResponseSelector, is now roughly equivalent to `1 - connection_density`, except at very low densities (high sparsities).

  All layers and components that used to have a `sparsity` argument (`Ffnn`, `TransformerRasaModel`, `MultiHeadAttention`, `TransformerEncoderLayer`, `TransformerEncoder`) now have a `density` argument instead.
- [#8074](https://github.com/rasahq/rasa/issues/8074): Rasa test now prints a warning if the test stories contain bot utterances that are not part of the domain.
- [#8263](https://github.com/rasahq/rasa/issues/8263): Updated `asyncio.Task.all_tasks` to `asyncio.all_tasks`, with a fallback for python 3.6, which raises an AttributeError for `asyncio.all_tasks`. This removes the deprecation warning for the `Task.all_tasks` usage.
- [#8461](https://github.com/rasahq/rasa/issues/8461): Change variable name from `i` to `array_2D`
- [#8560](https://github.com/rasahq/rasa/issues/8560): Implement a new interface `run_inference` inside `RasaModel` which performs batch inferencing through tensorflow models.

  `rasa_predict` inside `RasaModel` has been made a private method now by changing it to `_rasa_predict`.

### Bugfixes
- [#7005](https://github.com/rasahq/rasa/issues/7005): Fixed a bug for plotting trackers with non-ascii texts during interactive training by enforcing utf-8 encoding
- [#7589](https://github.com/rasahq/rasa/issues/7589): Fix masked language modeling in DIET to only apply masking to token-level
  (sequence-level) features. Previously, masking was applied to both token-level and
  sentence-level features.
- [#8300](https://github.com/rasahq/rasa/issues/8300): Make it possible to use `null` entities in stories.
- [#8333](https://github.com/rasahq/rasa/issues/8333): Introduce a `skip_validation` flag in order to speed up reading YAML files that were already validated.
- [#8341](https://github.com/rasahq/rasa/issues/8341): Fixed a bug in interactive training that
  lead to crashes for long Chinese, Japanese,
  or Korean user or bot utterances.


## [2.5.2] - 2021-06-16


### Features
- [#8892](https://github.com/rasahq/rasa/issues/8892): Added `sasl_mechanism` as an optional configurable parameters for the [Kafka Producer](https://rasa.com/docs/rasa-pro/production/event-brokers#kafka-event-broker).


## [2.5.1] - 2021-04-28


### Bugfixes
- [#8446](https://github.com/rasahq/rasa/issues/8446): Fixed prediction for rules with multiple entities.
- [#8545](https://github.com/rasahq/rasa/issues/8545): Mitigated Matplotlib backend issue using lazy configuration
  and added a more explicit error message to guide users.


## [2.5.0] - 2021-04-12


### Deprecations and Removals
- [#8141](https://github.com/rasahq/rasa/issues/8141): The following import abbreviations were removed:
  * `rasa.core.train`: Please use `rasa.core.train.train` instead.
  * `rasa.core.visualize`: Please use `rasa.core.visualize.visualize` instead.
  * `rasa.nlu.train`: Please use `rasa.nlu.train.train` instead.
  * `rasa.nlu.test`: Please use `rasa.nlu.test.run_evaluation` instead.
  * `rasa.nlu.cross_validate`: Please use `rasa.nlu.test.cross_validate` instead.

### Features
- [#7869](https://github.com/rasahq/rasa/issues/7869): Upgraded Rasa to be compatible with spaCy 3.0.

  This means that we can support more features for more languages but there are also a few changes.

  SpaCy 3.0 deprecated the `spacy link <language model>` command so that means that from now on [the
  full model name](https://spacy.io/models) needs to be used in the `config.yml` file.

  **Before**

  Before you could run `spacy link en en_core_web_md` and then we would be able
  to pick up the correct model from the `language` parameter.

  ```yaml
  language: en

  pipeline:
     - name: SpacyNLP
  ```

  **Now**

  This behavior will be deprecated and instead you'll want to be explicit in `config.yml`.

  ```yaml
  language: en

  pipeline:
     - name: SpacyNLP
       model: en_core_web_md
  ```

  **Fallback**

  To make the transition easier, Rasa will try to fall back to a medium spaCy model when-ever
  a compatible language is configured for the entire pipeline in `config.yml` even if you don't
  specify a `model`. This fallback behavior is temporary and will be deprecated in Rasa 3.0.0.

  We've updated our docs to reflect these changes. All examples now show a direct link to the
  correct spaCy model. We've also added a warning to the [SpaCyNLP](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#spacynlp)
  docs that explains the fallback behavior.

### Improvements
- [#4280](https://github.com/rasahq/rasa/issues/4280): Improved CLI startup time.
- [#4596](https://github.com/rasahq/rasa/issues/4596): Add `augmentation` and `num_threads` arguments to API `POST /model/train`

  Fix boolean casting issue for `force_training` and `save_to_default_model_directory` arguments
- [#7477](https://github.com/rasahq/rasa/issues/7477): Add minimum compatible version to --version command
- [#7660](https://github.com/rasahq/rasa/issues/7660): Updated warning for unexpected slot events during prediction time to Rasa Open Source
  2.0 YAML training data format.
- [#7701](https://github.com/rasahq/rasa/issues/7701): Hide dialogue turns predicted by `RulePolicy` in the tracker states
  for ML-only policies like `TEDPolicy`
  if those dialogue turns only appear as rules in the training data and do not appear in stories.

  Add `set_shared_policy_states(...)` method to all policies.
  This method sets `_rule_only_data` dict with keys:
  - `rule_only_slots`: Slot names, which only occur in rules but not in stories.
  - `rule_only_loops`: Loop names, which only occur in rules but not in stories.

  This information is needed for correct featurization to hide dialogue turns that appear only in rules.
- [#8208](https://github.com/rasahq/rasa/issues/8208): Faster reading of YAML NLU training data files.
- [#8335](https://github.com/rasahq/rasa/issues/8335): Added partition_by_sender flag to [Kafka Producer](https://rasa.com/docs/rasa-pro/production/event-brokers#kafka-event-broker) to optionally associate events with Kafka partition based on sender_id.

### Bugfixes
- [#7260](https://github.com/rasahq/rasa/issues/7260): Fixed the 'loading model' message which was logged twice when using `rasa run`.
- [#7379](https://github.com/rasahq/rasa/issues/7379): Change training data validation to only count nlu training examples.
- [#7450](https://github.com/rasahq/rasa/issues/7450): Rule tracker states no longer include the initial value of slots.
  Rules now only require slot values when explicitly stated in the rule.
- [#7640](https://github.com/rasahq/rasa/issues/7640): `rasa test`, `rasa test core` and `rasa test nlu` no longer show temporary paths
  in case there are issues in the test files.
- [#7690](https://github.com/rasahq/rasa/issues/7690): Resolved memory problems with dense features and `CRFEntityExtractor`
- [#7916](https://github.com/rasahq/rasa/issues/7916): Handle empty intent and entity mapping in the `domain`.

  There is now an InvalidDomain exception raised if in the `domain.yml` file there are empty intent or entity mappings.
  An example of empty intent and entity mappings is the following :
  ```yaml-rasa
  intents:
    - greet:
    - goodbye:

  entities:
    - cuisine:
    - number:
  ```
- [#8102](https://github.com/rasahq/rasa/issues/8102): Fixed a bug in a form where slot mapping doesn't work if the predicted intent name is substring for another intent name.
- [#8114](https://github.com/rasahq/rasa/issues/8114): Fixes bug where stories could not be retrieved if entities had no start or end.
- [#8178](https://github.com/rasahq/rasa/issues/8178): Catch ChannelNotFoundEntity exception coming from the pika broker and raise as ConnectionException.
- [#8337](https://github.com/rasahq/rasa/issues/8337): Fix bug with NoReturn throwing an exception in Python 3.7.0 when running `rasa train`
- [#8382](https://github.com/rasahq/rasa/issues/8382): Throw `RasaException` instead of `ValueError` in situations when environment variables
  specified in YAML cannot be expanded.
- [#8343](https://github.com/rasahq/rasa/issues/8343): Updated python-engineio version for compatibility with python-socketio

### Miscellaneous internal changes
- [#6511](https://github.com/rasahq/rasa/issues/6511), [#7640](https://github.com/rasahq/rasa/issues/7640), [#7827](https://github.com/rasahq/rasa/issues/7827), [#8056](https://github.com/rasahq/rasa/issues/8056), [#8117](https://github.com/rasahq/rasa/issues/8117), [#8141](https://github.com/rasahq/rasa/issues/8141), [#8240](https://github.com/rasahq/rasa/issues/8240)


## [2.4.3] - 2021-03-26


### Bugfixes
- [#8114](https://github.com/rasahq/rasa/issues/8114): Fixes bug where stories could not be retrieved if entities had no start or end.


## [2.4.2] - 2021-03-25


### Bugfixes
- [#7835](https://github.com/rasahq/rasa/issues/7835): Fix `UnicodeException` in `is_key_in_yaml`.
- [#8258](https://github.com/rasahq/rasa/issues/8258): Fixed the bug that events from previous conversation sessions would be re-saved in the [`SQLTrackerStore`](https://rasa.com/docs/rasa-pro/production/tracker-stores#sqltrackerstore) or [`MongoTrackerStore`](https://rasa.com/docs/rasa-pro/production/tracker-stores#mongotrackerstore) when `retrieve_events_from_previous_conversation_sessions` was true.


## [2.4.1] - 2021-03-23


### Bugfixes
- [#8194](https://github.com/rasahq/rasa/issues/8194): Fix `TEDPolicy` training e2e entities when no entities are present in the stories
  but there are entities in the domain.
- [#8198](https://github.com/rasahq/rasa/issues/8198): Fixed missing model configuration file validation.
- [#8223](https://github.com/rasahq/rasa/issues/8223): In Rasa 2.4.0, support for using `template` in `utter_message` when handling a custom action was wrongly deprecated. Both `template` and `response` are now supported, though note that `template` will be deprecated at Rasa 3.0.0.


## [2.4.0] - 2021-03-11


### Deprecations and Removals
- [#6484](https://github.com/rasahq/rasa/issues/6484): NLG Server
  - Changed request format to send `response` as well as `template` as a field. The `template` field will be removed in Rasa Open Source 3.0.0.

  `rasa.core.agent`
  - The terminology `template` is deprecated and replaced by `response`. Support for `template` from the NLG response will be removed in Rasa Open Source 3.0.0. Please see [here](https://rasa.com/docs/rasa-pro/production/nlg) for more details.

  `rasa.core.nlg.generator`
  - `generate()` now takes in  `utter_action` as a parameter.
  - The terminology `template` is deprecated and replaced by `response`. Support for `template` in the `NaturalLanguageGenerator` will be removed in Rasa Open Source 3.0.0.

  `rasa.shared.core.domain`
  - The property `templates` is deprecated. Use `responses` instead. It will be removed in Rasa Open Source 3.0.0.
  - `retrieval_intent_templates` will be removed in Rasa Open Source 3.0.0. Please use `retrieval_intent_responses` instead.
  - `is_retrieval_intent_template` will be removed in Rasa Open Source 3.0.0. Please use `is_retrieval_intent_response` instead.
  - `check_missing_templates` will be removed in Rasa Open Source 3.0.0. Please use `check_missing_responses` instead.

  Response Selector
  - The field `template_name` will be deprecated in Rasa Open Source 3.0.0. Please use `utter_action` instead. Please see [here](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#selectors) for more details.
  - The field `response_templates` will be deprecated in Rasa Open Source 3.0.0. Please use `responses` instead. Please see [here](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#selectors) for more details.

### Improvements
- [#7022](https://github.com/rasahq/rasa/issues/7022): The following endpoints now require the existence of the conversation for the specified conversation ID, raising an exception and returning a 404 status code.

  * `GET /conversations/<conversation_id:path>/story`

  * `POST /conversations/<conversation_id:path>/execute`

  * `POST /conversations/<conversation_id:path>/predict`
- [#7438](https://github.com/rasahq/rasa/issues/7438): Simplify our training by overwriting `train_step` instead of `fit` for our custom models.

  This allows us to use the build-in callbacks from Keras, such as the
  [Tensorboard Callback](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TensorBoard),
  which offers more functionality compared to what we had before.

    :::warning
    If you want to use Tensorboard for `DIETClassifier`, `ResponseSelector`, or `TEDPolicy` and log metrics after
    every (mini)batch, please use 'batch' instead of 'minibatch' as 'tensorboard_log_level'.
- [#7578](https://github.com/rasahq/rasa/issues/7578): When `TED` is configured to extract entities `rasa test` now evaluates them against the labels in the test stories. Results are saved in `/results` along with the results for the NLU components that extract entities.
- [#7680](https://github.com/rasahq/rasa/issues/7680): We're now running integration tests for Rasa Open Source, with initial coverage for `SQLTrackerStore` (with PostgreSQL),
  `RedisLockStore` (with Redis) and `PikaEventBroker` (with RabbitMQ). The integration tests are now part of our
  CI, and can also be ran locally using `make test-integration`
  (see [Rasa Open Source README](https://github.com/RasaHQ/rasa#running-the-integration-tests) for more information).
- [#7763](https://github.com/rasahq/rasa/issues/7763): Allow tests to be located anywhere, not just in `tests` directory.
- [#7893](https://github.com/rasahq/rasa/issues/7893): Model configuration files are now validated whether they match the expected schema.
- [#7952](https://github.com/rasahq/rasa/issues/7952): Speed up `YAMLStoryReader.is_key_in_yaml` function by making it to check if key is in YAML without
  actually parsing the text file.
- [#7953](https://github.com/rasahq/rasa/issues/7953): Speed up YAML parsing by reusing parsers, making the process of environment variable interpolation optional,
  and by not adding duplicating implicit resolvers and YAML constructors to `ruamel.yaml`
- [#7955](https://github.com/rasahq/rasa/issues/7955): Drastically improved finger printing time for large story graphs
- [#8000](https://github.com/rasahq/rasa/issues/8000): Remove console logging of conversation level F1-score and precision since these calculations were not meaningful.

  Add conversation level accuracy to core policy results logged to file in `story_report.json` after running `rasa test core` or `rasa test`.
- [#8100](https://github.com/rasahq/rasa/issues/8100): Improved the [lock store](https://rasa.com/docs/rasa-pro/production/lock-stores) debug log message when the process has to
  queue because other messages have to be processed before this item.

### Bugfixes
- [#4612](https://github.com/rasahq/rasa/issues/4612): Fixed the bug that OR statements in stories would break the check whether a model needs to be retrained
- [#7063](https://github.com/rasahq/rasa/issues/7063): Update the spec of `POST /model/test/intents` and add tests for cases when JSON is provided.

  Fix the incorrect temporary file extension for the data that gets extracted from the payload provided
  in the body of `POST /model/test/intents` request.
- [#7113](https://github.com/rasahq/rasa/issues/7113): Fix for the cli command `rasa data convert config` when migrating Mapping Policy and no rules.

  Making `rasa data convert config` migrate correctly the Mapping Policy when no rules are available. It updates the `config.yml` file by removing the `MappingPolicy` and adding the `RulePolicy` instead. Also, it creates the `data/rules.yml` file even if empty in the case of no available rules.
- [#7470](https://github.com/rasahq/rasa/issues/7470): Allow to have slots with values that result to a dictionary under the key `slot_was_set` (in `stories.yml` file).

  An example would be to have the following story step in `stories.yml`:
  ```yaml
  - slot_was_set:
      - some_slot:
          some_key: 'some_value'
          other_key: 'other_value'
  ```
  This would be allowed if the `some_slot` is also set accordingly in the `domain.yml` with type `any`.
- [#7662](https://github.com/rasahq/rasa/issues/7662): Update the fingerprinting function to recognize changes in lookup files.
- [#7932](https://github.com/rasahq/rasa/issues/7932): Fixed a bug when interpolating environment variables in YAML files which included `$` in their value.
  This led to the following stack trace:

  ```
  ValueError: Error when trying to expand the environment variables in '${PASSWORD}'. Please make sure to also set these environment variables: '['$qwerty']'.
  (13 additional frame(s) were not displayed)
  ...
    File "rasa/utils/endpoints.py", line 26, in read_endpoint_config
      content = rasa.shared.utils.io.read_config_file(filename)
    File "rasa/shared/utils/io.py", line 527, in read_config_file
      content = read_yaml_file(filename)
    File "rasa/shared/utils/io.py", line 368, in read_yaml_file
      return read_yaml(read_file(filename, DEFAULT_ENCODING))
    File "rasa/shared/utils/io.py", line 349, in read_yaml
      return yaml_parser.load(content) or {}
    File "rasa/shared/utils/io.py", line 314, in env_var_constructor
      " variables: '{}'.".format(value, not_expanded)
  ```
- [#7949](https://github.com/rasahq/rasa/issues/7949): The REQUESTED_SLOT always belongs to the currently active form.

  Previously it was possible that after form switching, the REQUESTED_SLOT was for the previous form.
- [#96](https://github.com/rasahq/rasa/issues/96): Update the `LanguageModelFeaturizer` tests to reflect new default model weights for `bert`, and skip all `bert` tests
  with default model weights on CI, run `bert` tests with `bert-base-uncased` on CI instead.

### Improved Documentation
- [#8080](https://github.com/rasahq/rasa/issues/8080): Update links to Sanic docs in the documentation.
- [#8109](https://github.com/rasahq/rasa/issues/8109): Update Rasa Playground to correctly use `tracking_id` when calling API methods.

### Miscellaneous internal changes
- [#6484](https://github.com/rasahq/rasa/issues/6484), [#7737](https://github.com/rasahq/rasa/issues/7737), [#7879](https://github.com/rasahq/rasa/issues/7879), [#8016](https://github.com/rasahq/rasa/issues/8016)


## [2.3.5] - 2021-06-16


### Features
- [#8860](https://github.com/rasahq/rasa/issues/8860): Added `sasl_mechanism` as an optional configurable parameters for the [Kafka Producer](https://rasa.com/docs/rasa-pro/production/event-brokers#kafka-event-broker).

### Improvements
- [#7955](https://github.com/rasahq/rasa/issues/7955): Drastically improved finger printing time for large story graphs
- [#8100](https://github.com/rasahq/rasa/issues/8100): Improved the [lock store](https://rasa.com/docs/rasa-pro/production/lock-stores) debug log message when the process has to
  queue because other messages have to be processed before this item.

### Bugfixes
- [#4612](https://github.com/rasahq/rasa/issues/4612): Fixed the bug that OR statements in stories would break the check whether a model needs to be retrained
- [#8649](https://github.com/rasahq/rasa/issues/8649): Updated `python-engineio` dependency version for compatibility with `python-socketio`.

### Improved Documentation
- [#8080](https://github.com/rasahq/rasa/issues/8080): Update links to Sanic docs in the documentation.


## [2.3.4] - 2021-02-26


### Bugfixes
- [#8014](https://github.com/rasahq/rasa/issues/8014): Setting `model_confidence=cosine` in `DIETClassifier`, `ResponseSelector` and `TEDPolicy` is deprecated and will no longer be available. This was introduced in Rasa Open Source version `2.3.0` but post-release experiments suggest that using cosine similarity as model's confidences can change the ranking of predicted labels which is wrong.

  `model_confidence=inner` is deprecated and is replaced by `model_confidence=linear_norm` as the former produced an unbounded range of confidences which broke the logic of assistants in various other places.

  We encourage you to try `model_confidence=linear_norm` which will produce a linearly normalized version of dot product similarities with each value in the range `[0,1]`. This can be done with the following config:
  ```yaml
  - name: DIETClassifier
    model_confidence: linear_norm
    constrain_similarities: True
  ```
  This should ease up [tuning fallback thresholds](https://rasa.com/docs/rasa-pro/nlu-based-assistants/fallback-handoff#fallbacks) as confidences for wrong predictions are better distributed across the range `[0, 1]`.

  If you trained a model with `model_confidence=cosine` or `model_confidence=inner` setting using previous versions of Rasa Open Source, please re-train by either removing the `model_confidence` option from the configuration or setting it to `linear_norm`.

  `model_confidence=cosine` is removed from the configuration generated by [auto-configuration](https://rasa.com/docs/rasa-pro/nlu-based-assistants/model-configuration#suggested-config).


## [2.3.3] - 2021-02-25


### Bugfixes
- [#8001](https://github.com/rasahq/rasa/issues/8001): Fixed bug where the conversation does not lock before handling a reminder event.


## [2.3.2] - 2021-02-22


### Bugfixes
- [#7972](https://github.com/rasahq/rasa/issues/7972): Fix a bug where, if a user injects an intent using the HTTP API, slot auto-filling is not performed on the entities provided.


## [2.3.1] - 2021-02-17


### Bugfixes
- [#7970](https://github.com/rasahq/rasa/issues/7970): Fixed a YAML validation error which happened when executing multiple validations
  concurrently. This could e.g. happen when sending concurrent requests to server
  endpoints which process YAML training data.


## [2.3.0] - 2021-02-11


### Improvements
- [#5673](https://github.com/rasahq/rasa/issues/5673): Expose diagnostic data for action and NLU predictions.

  Add `diagnostic_data` field to the Message
  and Prediction objects, which contain
  information about attention weights and other intermediate results of the inference computation.
  This information can be used for debugging and fine-tuning, e.g. with [RasaLit](https://github.com/RasaHQ/rasalit).

  For examples of how to access the diagnostic data, see [here](https://gist.github.com/JEM-Mosig/c6e15b81ee70561cb72e361aff310d7e).
- [#5986](https://github.com/rasahq/rasa/issues/5986): Using the `TrainingDataImporter` interface to load the data in `rasa test core`.

  Failed test stories are now referenced by their absolute path instead of the relative path.
- [#7292](https://github.com/rasahq/rasa/issues/7292): Improve error handling and Sentry tracking:
  - Raise `MarkdownException` when training data in Markdown format cannot be read.
  - Raise `InvalidEntityFormatException` error instead of `json.JSONDecodeError` when entity format is in valid
    in training data.
  - Gracefully handle empty sections in endpoint config files.
  - Introduce `ConnectionException` error and raise it when `TrackerStore` and `EventBroker`
    cannot connect to 3rd party services, instead of raising exceptions from 3rd party libraries.
  - Improve `rasa.shared.utils.common.class_from_module_path` function by making sure it always returns a class.
    The function currently raises a deprecation warning if it detects an anomaly.
  - Ignore `MemoryError` and `asyncio.CancelledError` in Sentry.
  - `rasa.shared.utils.validation.validate_training_data` now raises a `SchemaValidationError` when validation fails
    (this error inherits `jsonschema.ValidationError`, ensuring backwards compatibility).
- [#7303](https://github.com/rasahq/rasa/issues/7303): Allow `PolicyEnsemble` in cases where calling individual policy's `load` method returns `None`.
- [#7420](https://github.com/rasahq/rasa/issues/7420): User message metadata can now be accessed via the default slot
  `session_started_metadata` during the execution of a
  [custom `action_session_start`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/default-actions#customization).

  ```python
  from typing import Any, Text, Dict, List
  from rasa_sdk import Action, Tracker
  from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType

  class ActionSessionStart(Action):
      def name(self) -> Text:
          return "action_session_start"

      async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
      ) -> List[Dict[Text, Any]]:
          metadata = tracker.get_slot("session_started_metadata")

          # Do something with the metadata
          print(metadata)

          # the session should begin with a `session_started` event and an `action_listen`
          # as a user message follows
          return [SessionStarted(), ActionExecuted("action_listen")]
  ```
- [#7579](https://github.com/rasahq/rasa/issues/7579): Add BILOU tagging schema for entity extraction in end-to-end TEDPolicy.
- [#7616](https://github.com/rasahq/rasa/issues/7616): Added two new parameters `constrain_similarities` and `model_confidence` to machine learning (ML) components - [DIETClassifier](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#dietclassifier), [ResponseSelector](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#dietclassifier) and [TEDPolicy](https://rasa.com/docs/rasa-pro/nlu-based-assistants/policies#ted-policy).

  Setting `constrain_similarities=True` adds a sigmoid cross-entropy loss on all similarity values to restrict them to an approximate range in `DotProductLoss`. This should help the models to perform better on real world test sets.
  By default, the parameter is set to `False` to preserve the old behaviour, but users are encouraged to set it to `True` and re-train their assistants as it will be set to `True` by default from Rasa Open Source 3.0.0 onwards.

  Parameter `model_confidence` affects how model's confidence for each label is computed during inference. It can take three values:
  1. `softmax` - Similarities between input and label embeddings are post-processed with a softmax function, as a result of which confidence for all labels sum up to 1.
  2. `cosine` - Cosine similarity between input label embeddings. Confidence for each label will be in the range `[-1,1]`.
  3. `inner` - Dot product similarity between input and label embeddings. Confidence for each label will be in an unbounded range.

  Setting `model_confidence=cosine` should help users tune the fallback thresholds of their assistant better. The default value is `softmax` to preserve the old behaviour, but we recommend using `cosine` as that will be the new default value from Rasa Open Source 3.0.0 onwards. The value of this option does not affect how confidences are computed for entity predictions in `DIETClassifier` and `TEDPolicy`.

  With both the above recommendations, users should configure their ML component, e.g. `DIETClassifier`, as
  ```yaml
  - name: DIETClassifier
    model_confidence: cosine
    constrain_similarities: True
    ...
  ```
  Once the assistant is re-trained with the above configuration, users should also tune fallback confidence thresholds.

  Configuration option `loss_type=softmax` is now deprecated and will be removed in Rasa Open Source 3.0.0 . Use `loss_type=cross_entropy` instead.

  The default [auto-configuration](https://rasa.com/docs/rasa-pro/nlu-based-assistants/model-configuration#suggested-config) is changed to use `constrain_similarities=True` and `model_confidence=cosine` in ML components so that new users start with the recommended configuration.

  **EDIT**: Some post-release experiments revealed that using `model_confidence=cosine` is wrong as it can change the order of predicted labels. That's why this option was removed in Rasa Open Source version `2.3.3`. `model_confidence=inner` is deprecated as it produces an unbounded range of confidences which can break the logic of assistants in various other places. Please use `model_confidence=linear_norm` which will produce a linearly normalized version of dot product similarities with each value in the range `[0,1]`. Please read more about this change under the notes for release `2.3.4`.

- [#7817](https://github.com/rasahq/rasa/issues/7817): Use simple random uniform distribution of integers in negative sampling, because
  negative sampling with `tf.while_loop` and random shuffle inside creates a memory leak.
- [#7848](https://github.com/rasahq/rasa/issues/7848): Added support to configure `exchange_name` for [pika event broker](https://rasa.com/docs/rasa-pro/production/event-brokers#pika-event-broker).
- [#7867](https://github.com/rasahq/rasa/issues/7867): If `MaxHistoryTrackerFeaturizer` is used, invert the dialogue sequence before passing
  it to the transformer so that the last dialogue input becomes the first one and
  therefore always have the same positional encoding.

### Bugfixes
- [#7420](https://github.com/rasahq/rasa/issues/7420): Fixed an error when using the endpoint `GET /conversations/<conversation_id:path>/story`
  with a tracker which contained slots.
- [#7707](https://github.com/rasahq/rasa/issues/7707): Add the option to configure whether extracted entities should be split by comma (`","`) or not to TEDPolicy. Fixes
  crash when this parameter is accessed during extraction.
- [#7710](https://github.com/rasahq/rasa/issues/7710): When switching forms, the next form will always correctly ask for the first required slot.

  Before, the next form did not ask for the slot if it was the same slot as the requested slot of the previous form.
- [#7749](https://github.com/rasahq/rasa/issues/7749): Fix the bug when `RulePolicy` handling loop predictions are overwritten by e2e `TEDPolicy`.
- [#7751](https://github.com/rasahq/rasa/issues/7751): When switching forms, the next form is cleanly activated.

  Before, the next form was correctly activated, but the previous form had wrongly uttered
  the response that asked for the requested slot when slot validation for that slot
  had failed.
- [#7829](https://github.com/rasahq/rasa/issues/7829): Fix a bug in incremental training when passing a specific model path with the `--finetune` argument.
- [#7867](https://github.com/rasahq/rasa/issues/7867): Fix the role of `unidirectional_encoder` in TED. This parameter is only applied to
  transformers for `text`, `action_text` and `label_action_text`.

### Miscellaneous internal changes
- [#7420](https://github.com/rasahq/rasa/issues/7420), [#7515](https://github.com/rasahq/rasa/issues/7515), [#7574](https://github.com/rasahq/rasa/issues/7574), [#7601](https://github.com/rasahq/rasa/issues/7601)


## [2.2.10] - 2021-02-08


### Improvements
- [#7069](https://github.com/rasahq/rasa/issues/7069): Updated error message when using incompatible model versions.

### Bugfixes
- [#7885](https://github.com/rasahq/rasa/issues/7885): Limit `numpy` version to `< 1.2` as `tensorflow` is not compatible with `numpy`
  versions `>= 1.2`. `pip` versions `<= 20.2` don't resolve dependencies conflicts
  correctly which could result in an incompatible `numpy` version and the following
  error:

  ```bash
  NotImplementedError: Cannot convert a symbolic Tensor (strided_slice_6:0) to a numpy array. This error may indicate that you're trying to pass a Tensor to a NumPy call, which is not supported
  ```


## [2.2.9] - 2021-02-02


### Bugfixes
- [#7861](https://github.com/rasahq/rasa/issues/7861): Correctly include the `confused_with` field in the test report for the
  [`POST /model/test/intents`](/pages/http-api#operation/testModelIntent) endpoint.


## [2.2.8] - 2021-01-28


### Bugfixes
- [#7764](https://github.com/rasahq/rasa/issues/7764): Fixes a bug in [forms](https://rasa.com/docs/rasa-pro/nlu-based-assistants/forms) where the next slot asked was not consistent after returning to a form from an unhappy path.


## [2.2.7] - 2021-01-25


### Improvements
- [#7731](https://github.com/rasahq/rasa/issues/7731): Add support for in `RasaYAMLWriter` for writing intent and example metadata back
  into NLU YAML files.

### Bugfixes
- [#4311](https://github.com/rasahq/rasa/issues/4311): Fixed a bug with `Domain.is_domain_file()` that could raise an Exception in case the potential domain file is not a valid YAML.


## [2.2.6] - 2021-01-21


### Bugfixes
- [#7717](https://github.com/rasahq/rasa/issues/7717): Fix wrong warning `The method 'EventBroker.close' was changed to be asynchronous` when
  the `EventBroker.close` was actually asynchronous.
- [#7720](https://github.com/rasahq/rasa/issues/7720): Fix incremental training for cases when training data does not contain entities but `DIETClassifier` is configured to perform entity recognition also.

  Now, the instance of `RasaModelData` inside `DIETClassifier` does not contain `entities` as a feature for training if there is no training data present for entity recognition.


## [2.2.5] - 2021-01-12


### Bugfixes
- [#7603](https://github.com/rasahq/rasa/issues/7603): Fixed key-error bug on `rasa data validate stories`.

### Miscellaneous internal changes
- [#7711](https://github.com/rasahq/rasa/issues/7711)


## [2.2.4] - 2021-01-08


### Improvements
- [#7520](https://github.com/rasahq/rasa/issues/7520): Improve the warning in case the [RulePolicy](https://rasa.com/docs/rasa-pro/nlu-based-assistants/policies#rule-policy) or the deprecated
  [MappingPolicy](https://rasa.com/docs/rasa/2.x/policies#mapping-policy) are missing
  from the model's `policies` configuration. Changed the info log to a warning as one
  of this policies should be added to the model configuration.

### Bugfixes
- [#7692](https://github.com/rasahq/rasa/issues/7692): Explicitly specify the `crypto` extra dependency of `pyjwt` to ensure that the
  `cryptography` dependency is installed. `cryptography` is strictly required to be able
  to be able to verify JWT tokens.


## [2.2.3] - 2021-01-06


### Bugfixes
- [#7622](https://github.com/rasahq/rasa/issues/7622): Correctly retrieve intent ranking from `UserUttered` even during default affirmation
  action implementation.
- [#7684](https://github.com/rasahq/rasa/issues/7684): Fixed a problem when using the `POST /model/test/intents` endpoint together with a
  [model server](https://rasa.com/docs/rasa-pro/production/model-storage#load-model-from-server). The error looked as follows:

  ```
  ERROR    rasa.core.agent:agent.py:327 Could not load model due to Detected inconsistent loop usage. Trying to schedule a task on a new event loop, but scheduler was created with a different event loop. Make sure there is only one event loop in use and that the scheduler is running on that one.
  ```

  This also fixes a problem where testing a model from a model server would change the
  production model.


## [2.2.2] - 2020-12-21


### Bugfixes
- [#7592](https://github.com/rasahq/rasa/issues/7592): Fixed incompatibility between Rasa Open Source 2.2.x and Rasa X < 0.35.


## [2.2.1] - 2020-12-17


### Bugfixes
- [#7557](https://github.com/rasahq/rasa/issues/7557): Fixed a problem where a [form](https://rasa.com/docs/rasa-pro/nlu-based-assistants/forms) wouldn't reject when the
  `FormValidationAction` re-implemented `required_slots`.
- [#7585](https://github.com/rasahq/rasa/issues/7585): Fixed an error when using the [SQLTrackerStore](https://rasa.com/docs/rasa-pro/production/tracker-stores#sqltrackerstore)
  with a Postgres database and the parameter `login_db` specified.

  The error was:

  ```bash
  psycopg2.errors.SyntaxError: syntax error at end of input
  rasa-production_1  | LINE 1: SELECT 1 FROM pg_catalog.pg_database WHERE datname = ?
  ```


## [2.2.0] - 2020-12-16


### Deprecations and Removals
- [#6410](https://github.com/rasahq/rasa/issues/6410): `Domain.random_template_for` is deprecated and will be removed in Rasa Open Source
  3.0.0. You can alternatively use the `TemplatedNaturalLanguageGenerator`.

  `Domain.action_names` is deprecated and will be removed in Rasa Open Source
  3.0.0. Please use `Domain.action_names_or_texts` instead.
- [#7458](https://github.com/rasahq/rasa/issues/7458): Interfaces for `Policy.__init__` and `Policy.load` have changed.
  See [migration guide](https://rasa.com/docs/rasa-pro/migration-guide#rasa-21-to-rasa-22) for details.
- [#7495](https://github.com/rasahq/rasa/issues/7495): Deprecate training and test data in Markdown format. This includes:
  - reading and writing of story files in Markdown format
  - reading and writing of NLU data in Markdown format
  - reading and writing of retrieval intent data in Markdown format

  Support for Markdown data will be removed entirely in Rasa Open Source 3.0.0.

  Please convert your existing Markdown data by using the commands
  from the [migration guide](https://rasa.com/docs/rasa-pro/migration-guide#rasa-21-to-rasa-22):

  ```bash
  rasa data convert nlu -f yaml --data={SOURCE_DIR} --out={TARGET_DIR}
  rasa data convert nlg -f yaml --data={SOURCE_DIR} --out={TARGET_DIR}
  rasa data convert core -f yaml --data={SOURCE_DIR} --out={TARGET_DIR}
  ```
- [#7529](https://github.com/rasahq/rasa/issues/7529): `Domain.add_categorical_slot_default_value`, `Domain.add_requested_slot`
  and `Domain.add_knowledge_base_slots` are deprecated and will be removed in Rasa Open
  Source 3.0.0. Their internal versions are now called during the Domain creation.
  Calling them manually is no longer required.

### Features
- [#6971](https://github.com/rasahq/rasa/issues/6971): Incremental training of models in a pipeline is now supported.

  If you have added new NLU training examples or new stories/rules for
  dialogue manager, you don't need to train the pipeline from scratch.
  Instead, you can initialize the pipeline with a previously trained model
  and continue finetuning the model on the complete dataset consisting of
  new training examples. To do so, use `rasa train --finetune`. For more
  detailed explanation of the command, check out the docs on [incremental
  training](https://rasa.com/docs/rasa-pro/command-line-interface#incremental-training).

  Added a configuration parameter `additional_vocabulary_size` to
  [`CountVectorsFeaturizer`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#countvectorsfeaturizer)
  and `number_additional_patterns` to [`RegexFeaturizer`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#regexfeaturizer).
  These parameters are useful to configure when using incremental training for your pipelines.
- [#7408](https://github.com/rasahq/rasa/issues/7408): Add the option to use cross-validation to the
  [`POST /model/test/intents`](/pages/http-api#operation/testModelIntent) endpoint.
  To use cross-validation specify the query parameter `cross_validation_folds` in addition
  to the training data in YAML format.

  Add option to run NLU evaluation
  ([`POST /model/test/intents`](/pages/http-api#operation/testModelIntent)) and
  model training ([`POST /model/train`](/pages/http-api#operation/trainModel))
  asynchronously.
  To trigger asynchronous processing specify
  a callback URL in the query parameter `callback_url` which Rasa Open Source should send
  the results to. This URL will also be called in case of errors.
- [#7496](https://github.com/rasahq/rasa/issues/7496): Make [TED Policy](https://rasa.com/docs/rasa-pro/nlu-based-assistants/policies#ted-policy) an end-to-end policy. Namely, make it possible to train TED on stories that contain
  intent and entities or user text and bot actions or bot text.
  If you don't have text in your stories, TED will behave the same way as before.
  Add possibility to predict entities using TED.

  Here's an example of a dialogue in the Rasa story format:

  ```rasa-yaml
  stories:
  - story: collect restaurant booking info  # name of the story - just for debugging
    steps:
    - intent: greet                          # user message with no entities
    - action: utter_ask_howcanhelp           # action that the bot should execute
    - intent: inform                         # user message with entities
      entities:
      - location: "rome"
      - price: "cheap"
    - bot: On it                             # actual text that bot can output
    - action: utter_ask_cuisine
    - user: I would like [spanish](cuisine). # actual text that user input
    - action: utter_ask_num_people
  ```

  Some model options for `TEDPolicy` got renamed.
  Please update your configuration files using the following mapping:

  |      Old model option       |                  New model option                      |
  |-----------------------------|--------------------------------------------------------|
  |transformer_size             |dictionary “transformer_size” with keys                 |
  |                             |“text”, “action_text”, “label_action_text”, “dialogue”  |
  |number_of_transformer_layers |dictionary “number_of_transformer_layers” with keys     |
  |                             |“text”, “action_text”, “label_action_text”, “dialogue”  |
  |dense_dimension              |dictionary “dense_dimension” with keys                  |
  |                             |“text”, “action_text”, “label_action_text”, “intent”,   |
  |                             |“action_name”, “label_action_name”, “entities”, “slots”,|
  |                             |“active_loop”                                           |

### Improvements
- [#3998](https://github.com/rasahq/rasa/issues/3998): Added a message showing the location where the failed stories file was saved.
- [#7232](https://github.com/rasahq/rasa/issues/7232): Add support for the top-level response keys `quick_replies`, `attachment` and `elements` refered to in `rasa.core.channels.OutputChannel.send_reponse`, as well as `metadata`.
- [#7257](https://github.com/rasahq/rasa/issues/7257): Changed the format of the histogram of confidence values for both correct and incorrect predictions produced by running `rasa test`.
- [#7284](https://github.com/rasahq/rasa/issues/7284): Run [`bandit`](https://bandit.readthedocs.io/en/latest/) checks on pull requests.
  Introduce `make static-checks` command to run all static checks locally.
- [#7397](https://github.com/rasahq/rasa/issues/7397): Add `rasa train --dry-run` command that allows to check if training needs to be performed
  and what exactly needs to be retrained.
- [#7408](https://github.com/rasahq/rasa/issues/7408): [`POST /model/test/intents`](/pages/http-api#operation/testModelIntent) now returns
  the `report` field for `intent_evaluation`, `entity_evaluation` and
  `response_selection_evaluation` as machine-readable JSON payload instead of string.
- [#7436](https://github.com/rasahq/rasa/issues/7436): Make `rasa data validate stories` work for end-to-end.

  The `rasa data validate stories` function now considers the tokenized user text instead of the plain text that is part of a state.
  This is closer to what Rasa Core actually uses to distinguish states and thus captures more story structure problems.

### Bugfixes
- [#6804](https://github.com/rasahq/rasa/issues/6804): Rename `language_list` to `supported_language_list` for `JiebaTokenizer`.
- [#7244](https://github.com/rasahq/rasa/issues/7244): A `float` slot returns unambiguous values - `[1.0, <value>]` if successfully converted, `[0.0, 0.0]` if not.
  This makes it possible to distinguish an empty float slot from a slot set to `0.0`.
  :::caution
  This change is model-breaking. Please retrain your models.
  :::
- [#7306](https://github.com/rasahq/rasa/issues/7306): Fix an erroneous attribute for Redis key prefix in `rasa.core.tracker_store.RedisTrackerStore`: 'RedisTrackerStore' object has no attribute 'prefix'.
- [#7407](https://github.com/rasahq/rasa/issues/7407): Remove token when its text (for example, whitespace) can't be tokenized by LM tokenizer (from `LanguageModelFeaturizer`).
- [#7408](https://github.com/rasahq/rasa/issues/7408): Temporary directories which were created during requests to the [HTTP API](https://rasa.com/docs/rasa-pro/production/http-api)
  are now cleaned up correctly once the request was processed.
- [#7422](https://github.com/rasahq/rasa/issues/7422): Add option `use_word_boundaries` for `RegexFeaturizer` and `RegexEntityExtractor`. To correctly process languages such as Chinese that don't use whitespace for word separation, the user needs to add the `use_word_boundaries: False` option to those two components.
- [#7529](https://github.com/rasahq/rasa/issues/7529): Correctly fingerprint the default domain slots. Previously this led to the issue
  that `rasa train core` would always retrain the model even if the training data hasn't
  changed.

### Improved Documentation
- [#7313](https://github.com/rasahq/rasa/issues/7313): Return the "Migrate from" entry to the docs sidebar.

### Miscellaneous internal changes
- [#7167](https://github.com/rasahq/rasa/issues/7167)


## [2.1.3] - 2020-12-04


### Improvements
- [#7426](https://github.com/rasahq/rasa/issues/7426): Removed `multidict` from the project dependencies. `multidict` continues to be a second
  order dependency of Rasa Open Source but will be determined by the dependencies which
  use it instead of by Rasa Open Source directly.

  This resolves issues like the following:

  ```bash
  sanic 20.9.1 has requirement multidict==5.0.0, but you'll have multidict 4.6.0 which is incompatible.
  ```

### Bugfixes
- [#7316](https://github.com/rasahq/rasa/issues/7316): `SingleStateFeaturizer` checks whether it was trained with `RegexInterpreter` as
  nlu interpreter. If that is the case, `RegexInterpreter` is used during prediction.
- [#7390](https://github.com/rasahq/rasa/issues/7390): Make sure the `responses` are synced between NLU training data and the Domain even if there're no retrieval intents in the NLU training data.
- [#7417](https://github.com/rasahq/rasa/issues/7417): Categorical slots will have a default value set when just updating nlg data in the domain.

  Previously this resulted in `InvalidDomain` being thrown.
- [#7418](https://github.com/rasahq/rasa/issues/7418): - Preserve `domain` slot ordering while dumping it back to the file.
  - Preserve multiline `text` examples of `responses` defined in `domain` and `NLU` training data.


## [2.1.2] - 2020-11-27


### Bugfixes
- [#7235](https://github.com/rasahq/rasa/issues/7235): Slots that use `initial_value` won't cause rule contradiction errors when `conversation_start: true` is used. Previously, two rules that differed only in their use of `conversation_start` would be flagged as contradicting when a slot used `initial_value`.

  In checking for incomplete rules, an action will be required to have set _only_ those slots that the same action has set in another rule. Previously, an action was expected to have set also slots which, despite being present after this action in another rule, were not actually set by this action.
- [#7345](https://github.com/rasahq/rasa/issues/7345): Fixed Rasa Open Source not being able to fetch models from certain URLs.


## [2.1.1] - 2020-11-23


### Bugfixes
- [#7338](https://github.com/rasahq/rasa/issues/7338): Sender ID is correctly set when copying the tracker and sending it to the action server (instead of sending the `default` value). This fixes a problem where the action server would only retrieve trackers with a `sender_id` `default`.


## [2.1.0] - 2020-11-17


### Deprecations and Removals
- [#7136](https://github.com/rasahq/rasa/issues/7136): The [`Policy`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/policies) interface was changed to return a `PolicyPrediction` object when
  `predict_action_probabilities` is called. Returning a list of probabilities directly
  is deprecated and support for this will be removed in Rasa Open Source 3.0.

  You can adapt your custom policy by wrapping your probabilities in a `PolicyPrediction`
  object:

  ```python
  from rasa.core.policies.policy import Policy, PolicyPrediction
  # ... other imports

  def predict_action_probabilities(
          self,
          tracker: DialogueStateTracker,
          domain: Domain,
          interpreter: NaturalLanguageInterpreter,
          **kwargs: Any,
      ) -> PolicyPrediction:
      probabilities = ... # an action prediction of your policy
      return PolicyPrediction(probabilities, "policy_name", policy_priority=self.priority)
  ```

  The same change was applied to the `PolicyEnsemble` interface. Instead of returning
  a tuple of action probabilities and policy name, it is now returning a
  `PolicyPrediction` object. Support for the old `PolicyEnsemble` interface will be
  removed in Rasa Open Source 3.0.

  :::caution
  This change is model-breaking. Please retrain your models.

  :::
- [#7263](https://github.com/rasahq/rasa/issues/7263): The [Pika Event Broker](https://rasa.com/docs/rasa-pro/production/event-brokers#pika-event-broker) no longer supports
  the environment variables `RABBITMQ_SSL_CA_FILE` and `RABBITMQ_SSL_KEY_PASSWORD`.
  You can alternatively specify `RABBITMQ_SSL_CA_FILE` in the RabbitMQ connection URL as
  described in the
  [RabbitMQ documentation](https://www.rabbitmq.com/uri-query-parameters.html).

  ```yaml-rasa title="endpoints.yml
  event_broker:
   type: pika
   url: "amqps://user:password@host?cacertfile=path_to_ca_cert&password=private_key_password"
   queues:
   - my_queue

  ```

  Support for `RABBITMQ_SSL_KEY_PASSWORD` was removed entirely.

  The method [`Event Broker.close`](https://rasa.com/docs/rasa-pro/production/event-brokers) was changed to be asynchronous.
  Support for synchronous implementations will be removed in Rasa Open Source 3.0.0.
  To adapt your implementation add the `async` keyword:

  ```python
  from rasa.core.brokers.broker import EventBroker

  class MyEventBroker(EventBroker):

      async def close(self) -> None:
          # clean up event broker resources
  ```

### Features
- [#7136](https://github.com/rasahq/rasa/issues/7136): [Policies](https://rasa.com/docs/rasa-pro/nlu-based-assistants/policies) can now return obligatory and optional events as part of their
  prediction. Obligatory events are always applied to the current conversation tracker.
  Optional events are only applied to the conversation tracker in case the policy wins.

### Improvements
- [#4341](https://github.com/rasahq/rasa/issues/4341): Changed `Agent.load` method to support `pathlib` paths.
- [#5715](https://github.com/rasahq/rasa/issues/5715): If you are using the feature [Entity Roles and Groups](https://rasa.com/docs/rasa-pro/nlu-based-assistants/nlu-training-data#entities-roles-and-groups), you should now also list the roles and groups
  in your domain file if you want roles and groups to influence your conversations. For example:
  ```yaml-rasa
  entities:
    - city:
        roles:
          - from
          - to
    - name
    - topping:
        groups:
          - 1
          - 2
    - size:
        groups:
          - 1
          - 2
  ```

  Entity roles and groups can now influence dialogue predictions. For more information see the section
  [Entity Roles and Groups influencing dialogue predictions](https://rasa.com/docs/rasa-pro/nlu-based-assistants/nlu-training-data#entity-roles-and-groups-influencing-dialogue-predictions).
- [#6285](https://github.com/rasahq/rasa/issues/6285): Predictions of the [`FallbackClassifier`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#fallbackclassifier) are
  ignored when
  [evaluating the NLU model](https://rasa.com/docs/rasa-pro/nlu-based-assistants/testing-your-assistant#evaluating-an-nlu-model)
  Note that the `FallbackClassifier` predictions still apply to
  [test stories](https://rasa.com/docs/rasa-pro/nlu-based-assistants/testing-your-assistant#writing-test-stories).
- [#6474](https://github.com/rasahq/rasa/issues/6474): Adapt the training data reader and emulator for wit.ai to their latest format.
  Update the instructions in the
  migrate from wit.ai documentation
  to run Rasa Open Source in wit.ai emulation mode.
- [#6498](https://github.com/rasahq/rasa/issues/6498): Adding configurable prefixes to Redis [Tracker](https://rasa.com/docs/rasa-pro/production/tracker-stores) and [Lock Stores](https://rasa.com/docs/rasa-pro/production/lock-stores) so that a single Redis instance (and logical DB) can support multiple conversation trackers and locks.
  By default, conversations will be prefixed with `tracker:...` and all locks prefixed with `lock:...`. Additionally, you can add an alphanumeric-only `prefix: value` in `endpoints.yml` such that keys in redis will take the form `value:tracker:...` and `value:lock:...` respectively.
- [#6571](https://github.com/rasahq/rasa/issues/6571): Log the model's relative path when using CLI commands.
- [#6852](https://github.com/rasahq/rasa/issues/6852): Adds the option to configure whether extracted entities should be split by comma (`","`) or not. The default behaviour is `True` - i.e. split any list of extracted entities by comma. This makes sense for a list of ingredients in a recipie, for example `"avocado, tofu, cauliflower"`, however doesn't make sense for an address such as `"Schönhauser Allee 175, 10119 Berlin, Germany"`.

  In the latter case, add a new option to your config, e.g. if you are using the `DIETClassifier` this becomes:

  ```yaml
  ...
  - name: DIETClassifier
    split_entities_by_comma: False
  ...
  ```

  in which case, none of the extracted entities will be split by comma. To switch it on/off for specific entity types you can use:

  ```yaml
  ...
  - name: DIETClassifier
    split_entities_by_comma:
      address: True
      ingredient: False
  ...
  ```

  where both `address` and `ingredient` are two entity types.

  This feature is also available for `CRFEntityExtractor`.
- [#6860](https://github.com/rasahq/rasa/issues/6860): Fetching test stories from the HTTP API endpoint
  `GET /conversations/<conversation_id>/story` no longer triggers an update
  of the
  [conversation session](https://rasa.com/docs/rasa-pro/nlu-based-assistants/domain#session-configuration).

  Added a new boolean query parameter `all_sessions` (default: `false`) to the
  [HTTP API](https://rasa.com/docs/rasa-pro/production/http-api) endpoint for fetching test stories
  (`GET /conversations/<conversation_id>/story`).

  When setting `?all_sessions=true`, the endpoint returns test stories for all
  conversation sessions for `conversation_id`.
  When setting `?all_sessions=all_sessions`, or when omitting the `all_sessions`
  parameter, a single test story is returned for `conversation_id`. In cases where
  multiple conversation sessions exist, only the last story is returned.

  Specifying the `retrieve_events_from_previous_conversation_sessions`
  kwarg for the [Tracker Store](https://rasa.com/docs/rasa-pro/production/tracker-stores) class is deprecated and will be
  removed in Rasa Open Source 3.0. Please use the `retrieve_full_tracker()` method
  instead.
- [#6865](https://github.com/rasahq/rasa/issues/6865): Improve the `rasa data convert nlg` command and introduce the `rasa data convert responses` command
  to simplify the migration from pre-2.0 response selector format to the new format.
- [#6966](https://github.com/rasahq/rasa/issues/6966): Added warning for when an option is provided for a [component](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components) that is not listed as a key in the defaults for that component.
- [#6977](https://github.com/rasahq/rasa/issues/6977): [Forms](https://rasa.com/docs/rasa-pro/nlu-based-assistants/forms) no longer reject their execution before a potential custom
  action for validating / extracting slots was executed.
  Forms continue to reject in two cases automatically:
  - A slot was requested to be filled, but no slot mapping applied to the latest user
    message and there was no custom action for potentially extracting other slots.
  - A slot was requested to be filled, but the custom action for validating / extracting
    slots didn't return any slot event.

  Additionally you can also reject the form execution manually by returning a
  `ActionExecutionRejected` event within your custom action for validating / extracting
  slots.
- [#7027](https://github.com/rasahq/rasa/issues/7027): Remove dependency between `ConveRTTokenizer` and `ConveRTFeaturizer`. The `ConveRTTokenizer` is now deprecated, and the
  `ConveRTFeaturizer` can be used with any other `Tokenizer`.

  Remove dependency between `HFTransformersNLP`, `LanguageModelTokenizer`, and `LanguageModelFeaturizer`. Both
  `HFTransformersNLP` and `LanguageModelTokenizer` are now deprecated. `LanguageModelFeaturizer` implements the behavior
  of the stack and can be used with any other `Tokenizer`.
- [#7061](https://github.com/rasahq/rasa/issues/7061): Gray out "Download" button in Rasa Playground when the project is not yet ready to be downloaded.
- [#7068](https://github.com/rasahq/rasa/issues/7068): Slot mappings for [Forms](https://rasa.com/docs/rasa-pro/nlu-based-assistants/forms) in the domain are now optional. If you do not
  provide any slot mappings as part of the domain, you need to provide
  [custom slot mappings](https://rasa.com/docs/rasa-pro/nlu-based-assistants/forms#custom-slot-mappings) through a custom action.
  A form without slot mappings is specified as follows:

  ```rasa-yaml
  forms:
    my_form:
      # no mappings
  ```

  The action for [forms](https://rasa.com/docs/rasa-pro/nlu-based-assistants/forms) can now be overridden by defining a custom action
  with the same name as the form. This can be used to keep using the deprecated
  Rasa Open Source `FormAction` which is implemented within the Rasa SDK. Note that it is
  **not** recommended to override the form action for anything else than using the
  deprecated Rasa SDK `FormAction`.
- [#7102](https://github.com/rasahq/rasa/issues/7102): Changed the default model weights loaded for `HFTransformersNLP` component.

  Use a [language agnostic sentence embedding model](https://tfhub.dev/google/LaBSE/1)
  as the default model. These model weights should help improve performance on
  intent classification and response selection.
- [#7122](https://github.com/rasahq/rasa/issues/7122): Add validations for [slot mappings](https://rasa.com/docs/rasa-pro/nlu-based-assistants/forms#slot-mappings).
  If a slot mapping is not valid, an `InvalidDomain` error is raised.
- [#7132](https://github.com/rasahq/rasa/issues/7132): Adapt the training data reader and emulator for LUIS to
  [their latest format](https://westcentralus.dev.cognitive.microsoft.com/docs/services/luis-endpoint-api-v3-0/)
  and add support for roles.
  Update the instructions in the
  "Migrate from LUIS" documentation page
  to reflect the recent changes made to the UI of LUIS.
- [#7160](https://github.com/rasahq/rasa/issues/7160): Adapt the training data reader and emulator for DialogFlow to
  [their latest format](https://cloud.google.com/dialogflow/es/docs/reference/rest/v2/DetectIntentResponse)
  and add support for regex entities.
- [#7263](https://github.com/rasahq/rasa/issues/7263): The [Pika Event Broker](https://rasa.com/docs/rasa-pro/production/event-brokers#pika-event-broker) was reimplemented with
  the `[aio-pika` library[(https://aio-pika.readthedocs.io/en/latest/). Messages will
  now be published to RabbitMQ asynchronously which improves the prediction performance.
- [#7278](https://github.com/rasahq/rasa/issues/7278): The confidence of the [`FallbackClassifier`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#fallbackclassifier)
  predictions is set to `1 - top intent confidence`.

### Bugfixes
- [#5974](https://github.com/rasahq/rasa/issues/5974): `ActionRestart` will now trigger `ActionSessionStart` as a followup action.
- [#6582](https://github.com/rasahq/rasa/issues/6582): Fixed a bug with `rasa data split nlu` which caused the resulting train / test ratio to sometimes differ from the ratio specified by the user or by default.

  The splitting algorithm ensures that every intent and response class appears in both the training and the test set. This means that each split must contain at least as many examples as there are classes, which for small datasets can contradict the requested training fraction. When this happens, the command issues a warning to the user that the requested training fraction can't be satisfied.
- [#6721](https://github.com/rasahq/rasa/issues/6721): Fixed bug where slots with `influence_conversation=false` affected the action
  prediction if they were set manually using the
  `POST /conversations/<conversation_id/tracker/events` endpoint in the
  [HTTP API](https://rasa.com/docs/rasa-pro/production/http-api).
- [#6760](https://github.com/rasahq/rasa/issues/6760): Update Pika event broker to be a separate process and make it use a
  `multiprocessing.Queue` to send and process messages. This change should help
  avoid situations when events stop being sent after a while.
- [#6973](https://github.com/rasahq/rasa/issues/6973): Ignore rules when validating stories
- [#6986](https://github.com/rasahq/rasa/issues/6986): - Updated Slack Connector for new Slack Events API
- [#7001](https://github.com/rasahq/rasa/issues/7001): Update Rasa Playground "Download" button to work correctly depending on the current chat state.
- [#7002](https://github.com/rasahq/rasa/issues/7002): Test stories can now contain both: normal intents and retrieval intents. The `failed_test_stories.yml`, generated by `rasa test`, also specifies the full retrieval intent now.
  Previously `rasa test` would fail on test stories that specified retrieval intents.
- [#7031](https://github.com/rasahq/rasa/issues/7031): The converter tool is now able to convert test stories that contain a number as entity type.
- [#7034](https://github.com/rasahq/rasa/issues/7034): The converter tool now converts test stories and stories that contain full retrieval intents correctly.
  Previously the response keys were deleted during conversion to YAML.
- [#7204](https://github.com/rasahq/rasa/issues/7204): The slack connector requires a configuration for `slack_signing_secret` to make
  the connector more secure. The configuration value needs to be added to your
  `credentials.yml` if you are using the slack connector.
- [#7246](https://github.com/rasahq/rasa/issues/7246): Fixed model fingerprinting - it should avoid some more unecessary retrainings now.
- [#7253](https://github.com/rasahq/rasa/issues/7253): Fixed a problem when slots of type `text` or `list` were referenced by name only in
  the training data and this was treated as an empty value. This means that the two
  following stories are equivalent in case the slot type is `text`:

  ```yaml
  stories:
  - story: Story referencing slot by name
    steps:
    - intent: greet
    - slot_was_set:
      - name

  - story: Story referencing slot with name and value
    steps:
    - intent: greet
    - slot_was_set:
      - name: "some name"

  ```

  Note that you still need to specify values for all other slot types as only `text`
  and `list` slots are featurized in a binary fashion.

### Improved Documentation
- [#6973](https://github.com/rasahq/rasa/issues/6973): Correct data validation docs

### Miscellaneous internal changes
- [#6470](https://github.com/rasahq/rasa/issues/6470), [#7015](https://github.com/rasahq/rasa/issues/7015), [#7090](https://github.com/rasahq/rasa/issues/7090)


## [2.0.8] - 2020-11-26


### Bugfixes
- [#7235](https://github.com/rasahq/rasa/issues/7235): Slots that use `initial_value` won't cause rule contradiction errors when `conversation_start: true` is used. Previously, two rules that differed only in their use of `conversation_start` would be flagged as contradicting when a slot used `initial_value`.

  In checking for incomplete rules, an action will be required to have set _only_ those slots that the same action has set in another rule. Previously, an action was expected to have set also slots which, despite being present after this action in another rule, were not actually set by this action.


## [2.0.7] - 2020-11-24


### Bugfixes
- [#5974](https://github.com/rasahq/rasa/issues/5974): `ActionRestart` will now trigger `ActionSessionStart` as a followup action.
- [#7317](https://github.com/rasahq/rasa/issues/7317): Fixed Rasa Open Source not being able to fetch models from certain URLs.

  This addresses an issue introduced in 2.0.3 where `rasa-production` could not use the models from `rasa-x` in Rasa X server mode.
- [#7316](https://github.com/rasahq/rasa/issues/7316): `SingleStateFeaturizer` checks whether it was trained with `RegexInterpreter` as
  NLU interpreter. If that is the case, `RegexInterpreter` is used during prediction.


## [2.0.6] - 2020-11-10


### Bugfixes
- [#6629](https://github.com/rasahq/rasa/issues/6629): Fixed a bug that occurred when setting multiple Sanic workers in combination with a custom [Lock Store](https://rasa.com/docs/rasa-pro/production/lock-stores). Previously, if the number was set higher than 1 and you were using a custom lock store, it would reject because of a strict check to use a [Redis Lock Store](https://rasa.com/docs/rasa-pro/production/lock-stores#redislockstore).
- [#7176](https://github.com/rasahq/rasa/issues/7176): Fixed a bug in the [`TwoStageFallback`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/fallback-handoff#two-stage-fallback) action which
  reverted too many events after the user successfully rephrased.


## [2.0.5] - 2020-11-10


### Bugfixes
- [#7200](https://github.com/rasahq/rasa/issues/7200): Fix a bug because of which only one retrieval intent was present in `all_retrieval_intent` key of the output of `ResponseSelector` even if there were multiple retrieval intents present in the training data.


## [2.0.4] - 2020-11-08


### Bugfixes
- [#7140](https://github.com/rasahq/rasa/issues/7140): Fixed error when starting Rasa X locally without a proper git setup.
- [#7186](https://github.com/rasahq/rasa/issues/7186): Properly validate incoming webhook requests for the Slack connector to be authentic.


## [2.0.3] - 2020-10-29


### Bugfixes
- [#7089](https://github.com/rasahq/rasa/issues/7089): Fix [ConveRTTokenizer](https://rasa.com/docs/rasa/2.x/components#converttokenizer) failing because of wrong model URL by making the `model_url` parameter of `ConveRTTokenizer` mandatory.

  Since the ConveRT model was taken [offline](https://github.com/RasaHQ/rasa/issues/6806), we can no longer use
  the earlier public URL of the model. Additionally, since the licence for the model is unknown,
  we cannot host it ourselves. Users can still use the component by setting `model_url` to a community/self-hosted
  model URL or path to a local directory containing model files. For example:
  ```yaml
  pipeline:
      - name: ConveRTTokenizer
        model_url: <remote/local path to model>
  ```
- [#7108](https://github.com/rasahq/rasa/issues/7108): Update example formbot to use `FormValidationAction` for slot validation


## [2.0.2] - 2020-10-22


### Bugfixes
- [#6691](https://github.com/rasahq/rasa/issues/6691): Fix description of previous event in output of `rasa data validate stories`
- [#7053](https://github.com/rasahq/rasa/issues/7053): Fixed command line coloring for windows command lines running an encoding other than `utf-8`.

### Miscellaneous internal changes
- [#7057](https://github.com/rasahq/rasa/issues/7057)


## [2.0.1] - 2020-10-20


### Bugfixes
- [#7018](https://github.com/rasahq/rasa/issues/7018): Create correct `KafkaProducer` for `PLAINTEXT` and `SASL_SSL` security protocols.
- [#7033](https://github.com/rasahq/rasa/issues/7033): - Fix `YAMLStoryReader` not being able to represent [`OR` statements](https://rasa.com/docs/rasa-pro/nlu-based-assistants/stories#or-statements) in conversion mode.
  - Fix `MarkdownStoryWriter` not being able to write stories with `OR` statements (when loaded in conversion mode).


## [2.0.0] - 2020-10-07


### Deprecations and Removals
- [#5757](https://github.com/rasahq/rasa/issues/5757): Removed previously deprecated packages `rasa_nlu` and `rasa_core`.

  Use imports from `rasa.core` and `rasa.nlu` instead.
- [#5758](https://github.com/rasahq/rasa/issues/5758): Removed previously deprecated classes:
  - event brokers (`EventChannel` and `FileProducer`, `KafkaProducer`,
    `PikaProducer`, `SQLProducer`)
  - intent classifier `EmbeddingIntentClassifier`
  - policy `KerasPolicy`

  Removed previously deprecated methods:
  - `Agent.handle_channels`
  - `TrackerStore.create_tracker_store`

  Removed support for pipeline templates in `config.yml`

  Removed deprecated training data keys `entity_examples` and `intent_examples` from
  json training data format.
- [#5834](https://github.com/rasahq/rasa/issues/5834): Removed `restaurantbot` example as it was confusing and not a great way to build a bot.
- [#6296](https://github.com/rasahq/rasa/issues/6296): `LabelTokenizerSingleStateFeaturizer` is deprecated. To replicate `LabelTokenizerSingleStateFeaturizer` functionality,
  add a `Tokenizer`  with `intent_tokenization_flag: True` and `CountVectorsFeaturizer` to the NLU pipeline.
  An example of elements to be added to the pipeline is shown in the improvement changelog 6296`.

  `BinarySingleStateFeaturizer` is deprecated and will be removed in the future. We recommend to switch to `SingleStateFeaturizer`.
- [#6354](https://github.com/rasahq/rasa/issues/6354): Specifying the parameters `force` and `save_to_default_model_directory` as part of the
  JSON payload when training a model using `POST /model/train` is now deprecated.
  Please use the query parameters `force_training` and `save_to_default_model_directory`
  instead. See the [API documentation](/pages/http-api) for more information.
- [#6409](https://github.com/rasahq/rasa/issues/6409): The conversation event `form` was renamed to `active_loop`. Rasa Open Source
  will continue to be able to read and process old `form` events. Note that
  serialized trackers will no longer have the `active_form` field. Instead the
  `active_loop` field will contain the same information. Story representations
  in Markdown and YAML will use `active_loop` instead of `form` to represent the
  event.
- [#6453](https://github.com/rasahq/rasa/issues/6453): Removed support for `queue` argument in `PikaEventBroker` (use `queues` instead).

  Domain file:
  - Removed support for `templates` key (use `responses` instead).
  - Removed support for string `responses` (use dictionaries instead).

  NLU `Component`:
  - Removed support for `provides` attribute, it's not needed anymore.
  - Removed support for `requires` attribute (use `required_components()` instead).

  Removed `_guess_format()` utils method from `rasa.nlu.training_data.loading` (use `guess_format` instead).

  Removed several config options for [TED Policy](https://rasa.com/docs/rasa-pro/nlu-based-assistants/policies#ted-policy), [DIETClassifier](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#dietclassifier) and [ResponseSelector](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#responseselector):
  - `hidden_layers_sizes_pre_dial`
  - `hidden_layers_sizes_bot`
  - `droprate`
  - `droprate_a`
  - `droprate_b`
  - `hidden_layers_sizes_a`
  - `hidden_layers_sizes_b`
  - `num_transformer_layers`
  - `num_heads`
  - `dense_dim`
  - `embed_dim`
  - `num_neg`
  - `mu_pos`
  - `mu_neg`
  - `use_max_sim_neg`
  - `C2`
  - `C_emb`
  - `evaluate_every_num_epochs`
  - `evaluate_on_num_examples`

  Please check the documentation for more information.
- [#6463](https://github.com/rasahq/rasa/issues/6463): The conversation event `form_validation` was renamed to `loop_interrupted`.
  Rasa Open Source will continue to be able to read and process old `form_validation`
  events.
- [#6658](https://github.com/rasahq/rasa/issues/6658): `SklearnPolicy` was deprecated. `TEDPolicy` is the preferred machine-learning policy for dialogue models.
- [#6809](https://github.com/rasahq/rasa/issues/6809): [Slots](https://rasa.com/docs/rasa-pro/nlu-based-assistants/domain#slots) of type `unfeaturized` are
  now deprecated and will be removed in Rasa Open Source 3.0. Instead you should use
  the property `influence_conversation: false` for every slot type as described in the
  [migration guide](https://rasa.com/docs/rasa-pro/migration-guide#unfeaturized-slots).
- [#6934](https://github.com/rasahq/rasa/issues/6934): [Conversation sessions](https://rasa.com/docs/rasa-pro/nlu-based-assistants/domain#session-configuration) are now enabled by default
  if your [Domain](https://rasa.com/docs/rasa-pro/nlu-based-assistants/domain) does not contain a session configuration.
  Previously a missing session configuration was treated as if conversation sessions
  were disabled. You can explicitly disable conversation sessions using the following
  snippet:

  ```yaml-rasa title="domain.yml"
  session_config:
    # A session expiration time of `0`
    # disables conversation sessions
    session_expiration_time: 0
  ```
- [#6952](https://github.com/rasahq/rasa/issues/6952): Using the [default action](https://rasa.com/docs/rasa-pro/nlu-based-assistants/default-actions) `action_deactivate_form` to deactivate
  the currently active loop / [Form](https://rasa.com/docs/rasa-pro/nlu-based-assistants/forms) is deprecated.
  Please use `action_deactivate_loop` instead.

### Features
- [#4745](https://github.com/rasahq/rasa/issues/4745): Added template name to the metadata of bot utterance events.

  `BotUttered` event contains a `template_name` property in its metadata for any
  new bot message.
- [#5086](https://github.com/rasahq/rasa/issues/5086): Added a `--num-threads` CLI argument that can be passed to `rasa train`
  and will be used to train NLU components.
- [#5510](https://github.com/rasahq/rasa/issues/5510): You can now define what kind of features should be used by what component
  (see [Choosing a Pipeline](https://rasa.com/docs/rasa-pro/nlu-based-assistants/tuning-your-model)).

  You can set an alias via the option `alias` for every featurizer in your pipeline.
  The `alias` can be anything, by default it is set to the full featurizer class name.
  You can then specify, for example, on the
  [DIETClassifier](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#dietclassifier) what features from which
  featurizers should be used.
  If you don't set the option `featurizers` all available features will be used.
  This is also the default behavior.
  Check components to see what components have the option
  `featurizers` available.

  Here is an example pipeline that shows the new option.
  We define an alias for all featurizers in the pipeline.
  All features will be used in the `DIETClassifier`.
  However, the `ResponseSelector` only takes the features from the
  `ConveRTFeaturizer` and the `CountVectorsFeaturizer` (word level).

  ```
  pipeline:
  - name: ConveRTTokenizer
  - name: ConveRTFeaturizer
    alias: "convert"
  - name: CountVectorsFeaturizer
    alias: "cvf_word"
  - name: CountVectorsFeaturizer
    alias: "cvf_char"
    analyzer: char_wb
    min_ngram: 1
    max_ngram: 4
  - name: RegexFeaturizer
    alias: "regex"
  - name: LexicalSyntacticFeaturizer
    alias: "lsf"
  - name: DIETClassifier:
  - name: ResponseSelector
    epochs: 50
    featurizers: ["convert", "cvf_word"]
  - name: EntitySynonymMapper
  ```

  :::caution
  This change is model-breaking. Please retrain your models.

  :::
- [#5837](https://github.com/rasahq/rasa/issues/5837): Added `--port` commandline argument to the interactive learning mode to allow
  changing the port for the Rasa server running in the background.
- [#5957](https://github.com/rasahq/rasa/issues/5957): Add new entity extractor `RegexEntityExtractor`. The entity extractor extracts entities using the lookup tables
  and regexes defined in the training data. For more information see [RegexEntityExtractor](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#regexentityextractor).
- [#5996](https://github.com/rasahq/rasa/issues/5996): Introduced a new `YAML` format for Core training data and implemented a parser
  for it. Rasa Open Source can now read stories in both `Markdown` and `YAML` format.
- [#6020](https://github.com/rasahq/rasa/issues/6020): You can now enable threaded message responses from Rasa through the Slack connector.
  This option is enabled using an optional configuration in the credentials.yml file

  ```yaml
      slack:
        slack_token:
        slack_channel:
        use_threads: True
  ```

  Button support has also been added in the Slack connector.
- [#6065](https://github.com/rasahq/rasa/issues/6065): Add support for [rules](https://rasa.com/docs/rasa-pro/nlu-based-assistants/rules) data and [forms](https://rasa.com/docs/rasa-pro/nlu-based-assistants/forms) in YAML
  format.
- [#6066](https://github.com/rasahq/rasa/issues/6066): The NLU `interpreter` is now passed to the [Policies](https://rasa.com/docs/rasa-pro/nlu-based-assistants/policies) during training and
  inference time. Note that this requires an additional parameter `interpreter` in the
  method `predict_action_probabilities` of the `Policy` interface. In case a
  custom `Policy` implementation doesn't provide this parameter Rasa Open Source
  will print a warning and omit passing the `interpreter`.
- [#6088](https://github.com/rasahq/rasa/issues/6088): Added the new dialogue policy RulePolicy which will replace the old “rule-like”
  policies [Mapping Policy](https://rasa.com/docs/rasa/2.x/policies#mapping-policy),
  [Fallback Policy](https://rasa.com/docs/rasa/2.x/policies#fallback-policy),
  [Two-Stage Fallback Policy](https://rasa.com/docs/rasa/2.x/policies#two-stage-fallback-policy), and
  [Form Policy](https://rasa.com/docs/rasa/2.x/policies#form-policy). These policies are now
  deprecated and will be removed in the future. Please see the
  [rules documentation](https://rasa.com/docs/rasa-pro/nlu-based-assistants/rules) for more information.

  Added new NLU component [FallbackClassifier](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#fallbackclassifier)
  which predicts an intent `nlu_fallback` in case the confidence was below a given
  threshold. The intent `nlu_fallback` may
  then be used to write stories / rules to handle the fallback in case of low NLU
  confidence.

  ```yaml-rasa
  pipeline:
  - # Other NLU components ...
  - name: FallbackClassifier
    # If the highest ranked intent has a confidence lower than the threshold then
    # the NLU pipeline predicts an intent `nlu_fallback` which you can then be used in
    # stories / rules to implement an appropriate fallback.
    threshold: 0.5
  ```
- [#6132](https://github.com/rasahq/rasa/issues/6132): Added possibility to split the domain into separate files. All YAML files
  under the path specified with `--domain` will be scanned for domain
  information (e.g. intents, actions, etc) and then combined into a single domain.

  The default value for `--domain` is still `domain.yml`.
- [#6275](https://github.com/rasahq/rasa/issues/6275): Add optional metadata argument to `NaturalLanguageInterpreter`'s parse method.
- [#6354](https://github.com/rasahq/rasa/issues/6354): The Rasa Open Source API endpoint `POST /model/train` now supports training data in YAML
  format. Please specify the header `Content-Type: application/yaml` when
  training a model using YAML training data.
  See the [API documentation](/pages/http-api) for more information.
- [#6374](https://github.com/rasahq/rasa/issues/6374): Added a YAML schema and a writer for 2.0 Training Core data.
- [#6404](https://github.com/rasahq/rasa/issues/6404): Users can now use the ``rasa data convert {nlu|core} -f yaml`` command to convert training data from Markdown format to YAML format.
- [#6536](https://github.com/rasahq/rasa/issues/6536): Add option `use_lemma` to `CountVectorsFeaturizer`. By default it is set to `True`.

  `use_lemma` indicates whether the featurizer should use the lemma of a word for counting (if available) or not.
  If this option is set to `False` it will use the word as it is.

### Improvements
- [#4536](https://github.com/rasahq/rasa/issues/4536): Add support for Python 3.8.
- [#5368](https://github.com/rasahq/rasa/issues/5368): Changed the project structure for Rasa projects initialized with the
  [CLI](https://rasa.com/docs/rasa-pro/command-line-interface) (using the `rasa init` command):
  `actions.py` -> `actions/actions.py`. `actions` is now a Python package (it contains
  a file `actions/__init__.py`). In addition, the `__init__.py` at the
  root of the project has been removed.
- [#5481](https://github.com/rasahq/rasa/issues/5481): `DIETClassifier` now also assigns a confidence value to entity predictions.
- [#5637](https://github.com/rasahq/rasa/issues/5637): Added behavior to the `rasa --version` command. It will now also list information
  about the operating system, python version and `rasa-sdk`. This will make it easier
  for users to file bug reports.
- [#5743](https://github.com/rasahq/rasa/issues/5743): Support for additional training metadata.

  Training data messages now to support kwargs and the Rasa JSON data reader
  includes all fields when instantiating a training data instance.
- [#5748](https://github.com/rasahq/rasa/issues/5748): Standardize testing output. The following test output can be produced for intents,
  responses, entities and stories:
  - report: a detailed report with testing metrics per label (e.g. precision,
    recall, accuracy, etc.)
  - errors: a file that contains incorrect predictions
  - successes: a file that contains correct predictions
  - confusion matrix: plot of confusion matrix
  - histogram: plot of confidence distribution (not available for stories)
- [#5756](https://github.com/rasahq/rasa/issues/5756): To avoid the problem of our entity extractors predicting entity labels for
  just a part of the words, we introduced a cleaning method after the prediction
  was done. We should avoid the incorrect prediction in the first place.
  To achieve this we will not tokenize words into sub-words anymore.
  We take the mean feature vectors of the sub-words as the feature vector of the word.

  :::caution
  This change is model breaking. Please, retrain your models.

  :::
- [#5759](https://github.com/rasahq/rasa/issues/5759): Move option `case_sensitive` from the tokenizers to the featurizers.
  - Remove the option from the `WhitespaceTokenizer` and `ConveRTTokenizer`.
  - Add option `case_sensitive` to the `RegexFeaturizer`.
- [#5766](https://github.com/rasahq/rasa/issues/5766): If a user sends a voice message to the bot using Facebook, users messages was set to the attachments URL. The same is now also done for the rest of attachment types (image, video, and file).
- [#5794](https://github.com/rasahq/rasa/issues/5794): Creating a `Domain` using `Domain.fromDict` can no longer alter the input dictionary.
  Previously, there could be problems when the input dictionary was re-used for other
  things after creating the `Domain` from it.
- [#5805](https://github.com/rasahq/rasa/issues/5805): The debug-level logs when instantiating an
  [SQLTrackerStore](https://rasa.com/docs/rasa-pro/production/tracker-stores#sqltrackerstore)
  no longer show the password in plain text. Now, the URL is displayed with the password
  hidden, e.g. `postgresql://username:***@localhost:5432`.
- [#5855](https://github.com/rasahq/rasa/issues/5855): Shorten the information in tqdm during training ML algorithms based on the log
  level. If you train your model in debug mode, all available metrics will be
  shown during training, otherwise, the information is shorten.
- [#5913](https://github.com/rasahq/rasa/issues/5913): Ignore conversation test directory `tests/` when importing a project
  using `MultiProjectImporter` and `use_e2e` is `False`.
  Previously, any story data found in a project subdirectory would be imported
  as training data.
- [#5985](https://github.com/rasahq/rasa/issues/5985): Implemented model checkpointing for DIET (including the response selector) and TED. The best model during training will be stored instead of just the last model. The model is evaluated on the basis of `evaluate_every_number_of_epochs` and `evaluate_on_number_of_examples`.

  Checkpointing is enabled iff the following is set for the models in the `config.yml` file:
  * `checkpoint_model: True`
  * `evaluate_on_number_of_examples > 0`

  The model is stored to whatever location has been specified with the `--out` parameter when calling `rasa train nlu/core ...`.
- [#6024](https://github.com/rasahq/rasa/issues/6024): `rasa data split nlu` now makes sure that there is at least one example per
  intent and response in the test data.
- [#6039](https://github.com/rasahq/rasa/issues/6039): The method `ensure_consistent_bilou_tagging` now also considers the confidence values of the predicted tags
  when updating the BILOU tags.
- [#6045](https://github.com/rasahq/rasa/issues/6045): We updated the way how we save and use features in our NLU pipeline.

  The message object now has a dedicated field, called `features`, to store the
  features that are generated in the NLU pipeline. We adapted all our featurizers in a
  way that sequence and sentence features are stored independently. This allows us to
  keep different kind of features for the sequence and the sentence. For example, the
  `LexicalSyntacticFeaturizer` does not produce any sentence features anymore as our
  experiments showed that those did not bring any performance gain just quite a lot of
  additional values to store.

  We also modified the DIET architecture to process the sequence and sentence
  features independently at first. The features are concatenated just before
  the transformer.

  We also removed the `__CLS__` token again. Our Tokenizers will not
  add this token anymore.

  :::caution
  This change is model-breaking. Please retrain your models.

  :::
- [#6052](https://github.com/rasahq/rasa/issues/6052): Add endpoint kwarg to `rasa.jupyter.chat` to enable using a custom action server while chatting with a model in a jupyter notebook.
- [#6055](https://github.com/rasahq/rasa/issues/6055): Support for rasa conversation id with special characters on the server side - necessary for some channels (e.g. Viber)
- [#6123](https://github.com/rasahq/rasa/issues/6123): Add support for proxy use in [slack](https://rasa.com/docs/rasa-pro/connectors/slack) input channel.
- [#6134](https://github.com/rasahq/rasa/issues/6134): Log the number of examples per intent during training. Logging can be enabled using `rasa train --debug`.
- [#6237](https://github.com/rasahq/rasa/issues/6237): Support for other remote storages can be achieved by using an external library.
- [#6273](https://github.com/rasahq/rasa/issues/6273): Add `output_channel` query param to `/conversations/<conversation_id>/tracker/events` route, along with boolean `execute_side_effects` to optionally schedule/cancel reminders, and forward bot messages to output channel.
- [#6276](https://github.com/rasahq/rasa/issues/6276): Allow Rasa to boot when model loading exception occurs. Forward HTTP Error responses to standard log output.
- [#6294](https://github.com/rasahq/rasa/issues/6294): Rename `DucklingHTTPExtractor` to `DucklingEntityExtractor`.
- [#6296](https://github.com/rasahq/rasa/issues/6296): * Modified functionality of `SingleStateFeaturizer`.

    `SingleStateFeaturizer` uses trained NLU `Interpreter` to featurize intents and action names.
    This modified `SingleStateFeaturizer` can replicate `LabelTokenizerSingleStateFeaturizer` functionality.
    This component is deprecated from now on.
    To replicate `LabelTokenizerSingleStateFeaturizer` functionality,
    add a `Tokenizer`  with `intent_tokenization_flag: True` and `CountVectorsFeaturizer` to the NLU pipeline.
    Please update your configuration file.

    For example:
      ```yaml
      language: en
      pipeline:
        - name: WhitespaceTokenizer
          intent_tokenization_flag: True
        - name: CountVectorsFeaturizer
      ```

    Please train both NLU and Core (using `rasa train`) to use a trained tokenizer and featurizer for core featurization.

    The new `SingleStateFeaturizer` stores slots, entities and forms in sparse features for more lightweight storage.

    `BinarySingleStateFeaturizer` is deprecated and will be removed in the future.
    We recommend to switch to `SingleStateFeaturizer`.

  * Modified `TEDPolicy` to handle sparse features. As a result, `TEDPolicy` may require more epochs than before to converge.

  * Default TEDPolicy featurizer changed to `MaxHistoryTrackerFeaturizer` with infinite max history (takes all dialogue turns into account).
  * Default batch size for TED increased from [8,32] to [64, 256]
- [#6323](https://github.com/rasahq/rasa/issues/6323): [Response selector templates](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#responseselector) now support all features that
  domain utterances do. They use the yaml format instead of markdown now.
  This means you can now use buttons, images, ... in your FAQ or chitchat responses
  (assuming they are using the response selector).

  As a consequence, training data form in markdown has to have the file
  suffix `.md` from now on to allow proper file type detection-
- [#6457](https://github.com/rasahq/rasa/issues/6457): Support for test stories written in yaml format.
- [#6466](https://github.com/rasahq/rasa/issues/6466): [Response Selectors](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#responseselector) are now trained on retrieval intent labels by default instead of the actual response text. For most models, this should improve training time and accuracy of the `ResponseSelector`.

  If you want to revert to the pre-2.0 default behavior, add the `use_text_as_label=true` parameter to your `ResponseSelector` component.

  You can now also have multiple response templates for a single sub-intent of a retrieval intent. The first response template
  containing the text attribute is picked for training(if `use_text_as_label=True`) and a random template is picked for bot's utterance just as how other `utter_` templates are picked.

  All response selector related evaluation artifacts - `report.json, successes.json, errors.json, confusion_matrix.png` now use the sub-intent of the retrieval intent as the target and predicted labels instead of the actual response text.

  The output schema of `ResponseSelector` has changed - `full_retrieval_intent` and `name` have been deprecated in favour
  of `intent_response_key` and `response_templates` respectively. Additionally a key `all_retrieval_intents`
  is added to the response selector output which will hold a list of all retrieval intents(faq,chitchat, etc.)
  that are present in the training data.An example output looks like this -
  ```
  "response_selector": {
      "all_retrieval_intents": ["faq"],
      "default": {
        "response": {
          "id": 1388783286124361986, "confidence": 1.0, "intent_response_key": "faq/is_legit",
          "response_templates": [
            {
              "text": "absolutely",
              "image": "https://i.imgur.com/nGF1K8f.jpg"
            },
            {
              "text": "I think so."
            }
          ],
        },
        "ranking": [
          {
            "id": 1388783286124361986,
            "confidence": 1.0,
            "intent_response_key": "faq/is_legit"
          },
        ]
  ```

  An example bot demonstrating how to use the `ResponseSelector` is added to the `examples` folder.
- [#6472](https://github.com/rasahq/rasa/issues/6472): Do not modify conversation tracker's ``latest_input_channel`` property when using ``POST /trigger_intent`` or ``ReminderScheduled``.
- [#6555](https://github.com/rasahq/rasa/issues/6555): Do not set the output dimension of the `sparse-to-dense` layers to the same dimension as the dense features.

  Update default value of `dense_dimension` and `concat_dimension` for `text` in `DIETClassifier` to 128.
- [#6591](https://github.com/rasahq/rasa/issues/6591): Retrieval actions with `respond_` prefix are now replaced with usual utterance actions with `utter_` prefix.

  If you were using retrieval actions before, rename all of them to start with `utter_` prefix. For example, `respond_chitchat` becomes `utter_chitchat`.
  Also, in order to keep the response templates more consistent, you should now add the `utter_` prefix to all response templates defined for retrieval intents. For example, a response template `chitchat/ask_name` becomes `utter_chitchat/ask_name`. Note that the NLU examples for this will still be under `chitchat/ask_name` intent.
  The example `responseselectorbot` should help clarify these changes further.
- [#6613](https://github.com/rasahq/rasa/issues/6613): Added telemetry reporting. Rasa uses telemetry to report anonymous usage information.
  This information is essential to help improve Rasa Open Source for all users.
  Reporting will be opt-out. More information can be found in our
  [telemetry documentation](https://rasa.com/docs/rasa-pro/telemetry/telemetry).
- [#6757](https://github.com/rasahq/rasa/issues/6757): Update `extract_other_slots` method inside `FormAction` to fill a slot from an entity
  with a different name if corresponding slot mapping of `from_entity` type is unique.
- [#6809](https://github.com/rasahq/rasa/issues/6809): [Slots](https://rasa.com/docs/rasa-pro/nlu-based-assistants/domain#slots) of any type can now be ignored during a conversation.
  To do so, specify the property `influence_conversation: false` for the slot.

  ```yaml
  slot:
    a_slot:
      type: text
      influence_conversation: false
  ```

  The property `influence_conversation` is set to `true` by default. See the
  [documentation for slots](https://rasa.com/docs/rasa-pro/nlu-based-assistants/domain#slots) for more information.

  A new slot type [`any`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/domain#any-slot) was added. Slots of this type can store
  any value. Slots of type `any` are always ignored during conversations.
- [#6856](https://github.com/rasahq/rasa/issues/6856): Improved exception handling within Rasa Open Source.

  All exceptions that are somewhat expected (e.g. errors in file formats like
  configurations or training data) will share a common base class
  `RasaException`.

  ::warning Backwards Incompatibility
  Base class for the exception raised when an action can not be found has been changed
  from a `NameError` to a `ValueError`.
  ::

  Some other exceptions have also slightly changed:
  - raise `YamlSyntaxException` instead of YAMLError (from ruamel) when
    failing to load a yaml file with information about the line where loading failed
  - introduced `MissingDependencyException` as an exception raised if packages
    need to be installed
- [#6900](https://github.com/rasahq/rasa/issues/6900): Debug logs from `matplotlib` libraries are now hidden by default and are configurable with the `LOG_LEVEL_LIBRARIES` environment variable.
- [#6943](https://github.com/rasahq/rasa/issues/6943): Update `KafkaEventBroker` to support `SASL_SSL` and `PLAINTEXT` protocols.

### Bugfixes
- [#3597](https://github.com/rasahq/rasa/issues/3597): Fixed issue where temporary model directories were not removed after pulling from a model server.

  If the model pulled from the server was invalid, this could lead to large amounts of local storage usage.
- [#5038](https://github.com/rasahq/rasa/issues/5038): Fixed a bug in the `CountVectorsFeaturizer` which resulted in the very first
  message after loading a model to be processed incorrectly due to the vocabulary
  not being loaded yet.
- [#5135](https://github.com/rasahq/rasa/issues/5135): Fixed Rasa shell skipping button messages if buttons are attached to
  a message previous to the latest.
- [#5385](https://github.com/rasahq/rasa/issues/5385): Stack level for `FutureWarning` updated to level 2.
- [#5453](https://github.com/rasahq/rasa/issues/5453): If custom utter message contains no value or integer value, then it fails
  returning custom utter message. Fixed by converting the template to type string.
- [#5617](https://github.com/rasahq/rasa/issues/5617): Don't create TensorBoard log files during prediction.
- [#5638](https://github.com/rasahq/rasa/issues/5638): Fixed DIET breaking with empty spaCy model.
- [#5737](https://github.com/rasahq/rasa/issues/5737): Pinned the library version for the Azure
  [Cloud Storage](https://rasa.com/docs/rasa-pro/production/model-storage#load-model-from-cloud) to 2.1.0 since the
  persistor is currently not compatible with later versions of the azure-storage-blob
  library.
- [#5755](https://github.com/rasahq/rasa/issues/5755): Remove `clean_up_entities` from extractors that extract pre-defined entities.
  Just keep the clean up method for entity extractors that extract custom entities.
- [#5792](https://github.com/rasahq/rasa/issues/5792): Fixed issue where the `DucklingHTTPExtractor` component would
  not work if its `url` contained a trailing slash.
- [#5808](https://github.com/rasahq/rasa/issues/5808): Changed to variable `CERT_URI` in `hangouts.py` to a string type
- [#5850](https://github.com/rasahq/rasa/issues/5850): Slots will be correctly interpolated for `button` responses.

  Previously this resulted in no interpolation due to a bug.
- [#5905](https://github.com/rasahq/rasa/issues/5905): Remove option `token_pattern` from `CountVectorsFeaturizer`.
  Instead all tokenizers now have the option `token_pattern`.
  If a regular expression is set, the tokenizer will apply the token pattern.
- [#5921](https://github.com/rasahq/rasa/issues/5921): Allow user to retry failed file exports in interactive training.
- [#5964](https://github.com/rasahq/rasa/issues/5964): Fixed a bug when custom metadata passed with the utterance always restarted the session.
- [#5998](https://github.com/rasahq/rasa/issues/5998): `WhitespaceTokenizer` does not remove vowel signs in Hindi anymore.
- [#6042](https://github.com/rasahq/rasa/issues/6042): Convert entity values coming from `DucklingHTTPExtractor` to string
  during evaluation to avoid mismatches due to different types.
- [#6053](https://github.com/rasahq/rasa/issues/6053): Update `FeatureSignature` to store just the feature dimension instead of the
  complete shape. This change fixes the usage of the option `share_hidden_layers`
  in the `DIETClassifier`.
- [#6087](https://github.com/rasahq/rasa/issues/6087): Unescape the `\n, \t, \r, \f, \b` tokens on reading nlu data from markdown files.

  On converting json files into markdown, the tokens mentioned above are espaced. These tokens need to be unescaped on loading the data from markdown to ensure that the data is treated in the same way.
- [#6120](https://github.com/rasahq/rasa/issues/6120): Fix the way training data is generated in rasa test nlu when using the `-P` flag.
  Each percentage of the training dataset used to be formed as a part of the last
  sampled training dataset and not as a sample from the original training dataset.
- [#6143](https://github.com/rasahq/rasa/issues/6143): Prevent `WhitespaceTokenizer` from outputting empty list of tokens.
- [#6198](https://github.com/rasahq/rasa/issues/6198): Add `EntityExtractor` as a required component for `EntitySynonymMapper` in a pipeline.
- [#6222](https://github.com/rasahq/rasa/issues/6222): Better handling of input sequences longer than the maximum sequence length that the `HFTransformersNLP` models can handle.

  During training, messages with longer sequence length should result in an error, whereas during inference they are
  gracefully handled but a debug message is logged. Ideally, passing messages longer than the acceptable maximum sequence
  lengths of each model should be avoided.
- [#6231](https://github.com/rasahq/rasa/issues/6231): When using the `DynamoTrackerStore`, if there are more than 100 DynamoDB tables, the tracker could attempt to re-create an existing table if that table was not among the first 100 listed by the dynamo API.
- [#6282](https://github.com/rasahq/rasa/issues/6282): Fixed a deprication warning that pops up due to changes in numpy
- [#6291](https://github.com/rasahq/rasa/issues/6291): Update `rasabaster` to fix an issue with syntax highlighting on "Prototype an Assistant" page.

  Update default stories and rules on "Prototype an Assistant" page.
- [#6419](https://github.com/rasahq/rasa/issues/6419): Fixed a bug in the `serialise` method of the `EvaluationStore` class which resulted in a wrong end-to-end evaluation of the predicted entities.
- [#6535](https://github.com/rasahq/rasa/issues/6535): [Forms](https://rasa.com/docs/rasa-pro/nlu-based-assistants/forms) with slot mappings defined in `domain.yml` must now be a
  dictionary (with form names as keys). The previous syntax where `forms` was simply a
  list of form names is still supported.
- [#6577](https://github.com/rasahq/rasa/issues/6577): Remove BILOU tag prefix from role and group labels when creating entities.
- [#6601](https://github.com/rasahq/rasa/issues/6601): Fixed a bug in the featurization of the boolean slot type. Previously, to set a slot value to "true",
  you had to set it to "1", which is in conflict with the documentation. In older versions `true`
  (without quotes) was also possible, but now raised an error during yaml validation.
- [#6603](https://github.com/rasahq/rasa/issues/6603): Fixed a bug in rasa interactive. Now it exports the stories and nlu training data as yml file.
- [#6711](https://github.com/rasahq/rasa/issues/6711): Fixed slots not being featurized before first user utterance.

  Fixed AugmentedMemoizationPolicy to forget the first action on the first going back
- [#6741](https://github.com/rasahq/rasa/issues/6741): Fixed the remote URL of ConveRT model as it was recently updated by its authors.
- [#6755](https://github.com/rasahq/rasa/issues/6755): Treat the length of OOV token as 1 to fix token align issue when OOV occurred.
- [#6757](https://github.com/rasahq/rasa/issues/6757): Fixed the bug when entity was extracted even
  if it had a role or group but roles or groups were not expected.
- [#6803](https://github.com/rasahq/rasa/issues/6803): Fixed the bug that caused `supported_language_list` of `Component` to not work correctly.

  To avoid confusion, only one of `supported_language_list` and `not_supported_language_list` can be set to not `None` now
- [#6897](https://github.com/rasahq/rasa/issues/6897): Fixed issue where responses including `text: ""` and no `custom` key would incorrectly fail domain validation.
- [#6898](https://github.com/rasahq/rasa/issues/6898): Fixed issue where extra keys other than `title` and `payload` inside of `buttons` made a response fail domain validation.
- [#6919](https://github.com/rasahq/rasa/issues/6919): Do not filter training data in model.py but on component side.
- [#6929](https://github.com/rasahq/rasa/issues/6929): Check if a model was provided when executing `rasa test core`.
  If not, print a useful error message and stop.
- [#6805](https://github.com/rasahq/rasa/issues/6805): Transfer only response templates for retrieval intents from domain to NLU Training Data.

  This avoids retraining the NLU model if one of the non retrieval intent response templates are edited.

### Improved Documentation
- [#4441](https://github.com/rasahq/rasa/issues/4441): Added documentation on `ambiguity_threshold` parameter in Fallback Actions page.
- [#4605](https://github.com/rasahq/rasa/issues/4605): Remove outdated whitespace tokenizer warning in Testing Your Assistant documentation.
- [#5640](https://github.com/rasahq/rasa/issues/5640): Updated Facebook Messenger channel docs with supported attachment information
- [#5675](https://github.com/rasahq/rasa/issues/5675): Update `rasa shell` documentation to explain how to recreate external
  channel session behavior.
- [#5811](https://github.com/rasahq/rasa/issues/5811): Event brokers documentation should say `url` instead of `host`.
- [#5952](https://github.com/rasahq/rasa/issues/5952): Update `rasa init` documentation to include `tests/conversation_tests.md`
  in the resulting directory tree.
- [#6819](https://github.com/rasahq/rasa/issues/6819): Update ["Validating Form Input" section](https://rasa.com/docs/rasa-pro/nlu-based-assistants/forms#validating-form-input) to include details about
  how `FormValidationAction` class makes it easier to validate form slots in custom actions and how to use it.
- [#6823](https://github.com/rasahq/rasa/issues/6823): Update the examples in the API docs to use YAML instead of Markdown

### Miscellaneous internal changes
- [#5784](https://github.com/rasahq/rasa/issues/5784), [#5788](https://github.com/rasahq/rasa/issues/5788), [#6199](https://github.com/rasahq/rasa/issues/6199), [#6403](https://github.com/rasahq/rasa/issues/6403), [#6735](https://github.com/rasahq/rasa/issues/6735)


## [1.10.26] - 2021-06-17

### Features
- [#8876](https://github.com/rasahq/rasa/issues/8876): Added `sasl_mechanism` as an optional configurable parameter for the [Kafka Producer](https://rasa.com/docs/rasa-pro/production/event-brokers#kafka-event-broker).


## [1.10.25] - 2021-04-14

### Features
- [#8429](https://github.com/rasahq/rasa/issues/8429): Added `partition_by_sender` flag to Kafka Producer to optionally associate events with Kafka partition based on sender_id.

### Improvements
- [#8345](https://github.com/rasahq/rasa/issues/8345): Improved the [lock store](https://rasa.com/docs/rasa-pro/production/lock-stores) debug log message when the process has to queue because other messages have to be processed before this item.


## [1.10.24] - 2021-03-29

### Bugfixes
- [#8019](https://github.com/rasahq/rasa/issues/8019): Added `group_id` parameter back to `KafkaEventBroker` to fix error when instantiating event broker with a config containing the `group_id` parameter which is only relevant to the event consumer


## [1.10.23] - 2021-02-22

### Bugfixes
- [#7895](https://github.com/rasahq/rasa/issues/7895): Fixed bug where the conversation does not lock before handling a reminder event.


## [1.10.22] - 2021-02-05

### Bugfixes
- [#7772](https://github.com/rasahq/rasa/issues/7754): Backported the Rasa Open Source 2 `PikaEventBroker` implementation to address
  problems when using it with multiple Sanic workers.

## [1.10.21] - 2021-02-01

### Improvements
- [#7439](https://github.com/rasahq/rasa/issues/7439): The `url` option now supports a list of servers `url: ['10.0.0.158:32803','10.0.0.158:32804']`.
  Removed `group_id` because it is not a valid Kafka producer parameter.

### Bugfixes
- [#7638](https://github.com/rasahq/rasa/issues/7638): Fixed a bug that occurred when setting multiple Sanic workers in combination with a custom [Lock Store](https://rasa.com/docs/rasa-pro/production/lock-stores). Previously, if the number was set higher than 1 and you were using a custom lock store, it would reject because of a strict check to use a [Redis Lock Store](https://rasa.com/docs/rasa-pro/production/lock-stores#redislockstore).
- [#7722](https://github.com/rasahq/rasa/issues/7722): Fix a bug where, if a user injects an intent using the HTTP API, slot auto-filling is not performed on the entities provided.


## [1.10.20] - 2020-12-18

### Bugfixes

- [#7575](https://github.com/rasahq/rasa/issues/7575): Fix scikit-learn crashing during evaluation of `ResponseSelector` predictions.


## [1.10.19] - 2020-12-17

### Improvements

- [#6251](https://github.com/rasahq/rasa/issues/6251): Kafka Producer connection now remains active across sends. Added support for group and client id.
  The Kafka producer also adds support for the `PLAINTEXT` and `SASL_SSL` protocols.

  DynamoDB table exists check fixed bug when more than 100 tables exist.

- [#6814](https://github.com/rasahq/rasa/issues/6814): Replace use of `python-telegram-bot` package with `pyTelegramBotAPI`
- [#7423](https://github.com/rasahq/rasa/issues/7423): Use response selector keys (sub-intents) as labels for plotting the confusion matrix during NLU evaluation to improve readability.


## [1.10.18] - 2020-11-26

### Bugfixes
- [#7340](https://github.com/rasahq/rasa/issues/7340>): Fixed an issues with the DynamoDB TrackerStore creating a new table entry/object for each TrackerStore update. The column ``session_date`` has been deprecated and should be removed manually in existing DynamoDB tables.


## [1.10.17] - 2020-11-12

### Bugfixes
- [#7219](https://github.com/rasahq/rasa/issues/7219): Prevent the message handling process in ``PikaEventBroker`` from being terminated.


## [1.10.16] - 2020-10-15

### Bugfixes
- [#6703](https://github.com/rasahq/rasa/issues/6703): Update Pika event broker to be a separate process and make it use a
  ``multiprocessing.Queue`` to send and process messages. This change should help
  avoid situations when events stop being sent after a while.

## [1.10.15] - 2020-10-09

### Bugfixes

- [#3597](https://github.com/rasahq/rasa/issues/3597): Fixed issue where temporary model directories were not removed after pulling from a model server. If the model pulled from the server was invalid, this could lead to large amounts of local storage usage.
- [#6755](https://github.com/rasahq/rasa/issues/6755): Treat the length of OOV token as 1 to fix token align issue when OOV occurred.
- [#6899](https://github.com/rasahq/rasa/issues/6899): Fixed ``MappingPolicy`` not predicting ``action_listen`` after the mapped action while running ``rasa test``.


### Improvements

- [#6900](https://github.com/rasahq/rasa/issues/6900): Debug logs from ``matplotlib`` libraries are now hidden by default and are configurable with the ``LOG_LEVEL_LIBRARIES`` environment variable.

## [1.10.14] - 2020-09-23

### Bugfixes

- [#6741](https://github.com/rasahq/rasa/issues/6741): Fixed the remote URL of ConveRT model as it was recently updated by its authors. Also made the remote URL configurable at runtime in the corresponding tokenizer's and featurizer's configuration.

## [1.10.13] - 2020-09-22

### Bugfixes

- [#6577](https://github.com/rasahq/rasa/issues/6577): Remove BILOU tag prefix from role and group labels when creating entities.

## [1.10.12] - 2020-09-03

### Bugfixes

- [#6549](https://github.com/rasahq/rasa/issues/6549): Fix slow training of `CRFEntityExtractor` when using Entity Roles and Groups.

## [1.10.11] - 2020-08-21

### Improvements

- [#6044](https://github.com/rasahq/rasa/issues/6044): Do not deepcopy slots when instantiating trackers. This leads to a significant
  speedup when training on domains with a large number of slots.
- [#6226](https://github.com/rasahq/rasa/issues/6226): Added more debugging logs to the [Lock Stores](https://rasa.com/docs/rasa-pro/production/lock-stores) to simplify debugging in case of

  connection problems.

  Added a new parameter `socket_timeout` to the `RedisLockStore`. If Redis doesn't
  answer within `socket_timeout` seconds to requests from Rasa Open Source, an error
  is raised. This avoids seemingly infinitely blocking connections and exposes connection
  problems early.

### Bugfixes

- [#5182](https://github.com/rasahq/rasa/issues/5182): Fixed a bug where domain fields such as `store_entities_as_slots` were overridden
  with defaults and therefore ignored.
- [#6191](https://github.com/rasahq/rasa/issues/6191): If two entities are separated by a comma (or any other symbol), extract them as two separate entities.
- [#6340](https://github.com/rasahq/rasa/issues/6340): If two entities are separated by a single space and uses BILOU tagging,
  extract them as two separate entities based on their BILOU tags.


## [1.10.10] - 2020-08-04

### Bugfixes

- [#6280](https://github.com/rasahq/rasa/issues/6280): Fixed `TypeError: expected string or bytes-like object`
  issue caused by integer, boolean, and null values in templates.


## [1.10.9] - 2020-07-29

### Improvements

- [#6255](https://github.com/rasahq/rasa/issues/6255): Rasa Open Source will no longer add `responses` to the `actions` section of the
  domain when persisting the domain as a file. This addresses related problems in Rasa X
  when Integrated Version Control introduced big diffs due to the added utterances
  in the `actions` section.

### Bugfixes

- [#6160](https://github.com/rasahq/rasa/issues/6160): Consider entity roles/groups during interactive learning.


## [1.10.8] - 2020-07-15

### Bugfixes

* [#6075](https://github.com/rasahq/rasa/issues/6075): Add 'Access-Control-Expose-Headers' for 'filename' header
* [#6137](https://github.com/rasahq/rasa/issues/6137): Fixed a bug where an invalid language variable prevents rasa from finding training examples when importing Dialogflow data.


## [1.10.7] - 2020-07-07

### Features

* [#6150](https://github.com/rasahq/rasa/issues/6150): Add `not_supported_language_list` to component to be able to define languages that a component can NOT handle.

  `WhitespaceTokenizer` is not able to process languages which are not separated by whitespace. `WhitespaceTokenizer`
  will throw an error if it is used with Chinese, Japanese, and Thai.

### Bugfixes

* [#6150](https://github.com/rasahq/rasa/issues/6150): `WhitespaceTokenizer` only removes emoji if complete token matches emoji regex.


## [1.10.6] - 2020-07-06

### Bugfixes

* [#6143](https://github.com/rasahq/rasa/issues/6143): Prevent `WhitespaceTokenizer` from outputting empty list of tokens.

## [1.10.5] - 2020-07-02

### Bugfixes

* [#6119](https://github.com/rasahq/rasa/issues/6119): Explicitly remove all emojis which appear as unicode characters from the output of `regex.sub` inside `WhitespaceTokenizer`.

## [1.10.4] - 2020-07-01

### Bugfixes

* [#5998](https://github.com/rasahq/rasa/issues/5998): `WhitespaceTokenizer` does not remove vowel signs in Hindi anymore.

* [#6031](https://github.com/rasahq/rasa/issues/6031): Previously, specifying a lock store in the endpoint configuration with a type other than `redis` or `in_memory`
  would lead to an `AttributeError: 'str' object has no attribute 'type'`. This bug is fixed now.

* [#6032](https://github.com/rasahq/rasa/issues/6032): Fix `Interpreter parsed an intent ...` warning when using the `/model/parse`
  endpoint with an NLU-only model.

* [#6042](https://github.com/rasahq/rasa/issues/6042): Convert entity values coming from any entity extractor to string during evaluation to avoid mismatches due to
  different types.

* [#6078](https://github.com/rasahq/rasa/issues/6078): The assistant will respond through the webex channel to any user (room) communicating to it. Before the bot responded only to a fixed `roomId` set in the `credentials.yml` config file.

## [1.10.3] - 2020-06-12

### Improvements

* [#3900](https://github.com/rasahq/rasa/issues/3900): Reduced duplicate logs and warnings when running `rasa train`.

### Bugfixes

* [#5972](https://github.com/rasahq/rasa/issues/5972): Remove the `clean_up_entities` method from the `DIETClassifier` and `CRFEntityExtractor` as it let to incorrect
  entity predictions.

* [#5976](https://github.com/rasahq/rasa/issues/5976): Fix server crashes that occurred when Rasa Open Source pulls a model from a
  [model server](https://rasa.com/docs/rasa-pro/production/model-storage#load-model-from-server) and an exception was thrown during
  model loading (such as a domain with invalid YAML).

## [1.10.2] - 2020-06-03

### Bugfixes

* [#5521](https://github.com/rasahq/rasa/issues/5521): Responses used in ResponseSelector now support new lines with explicitly adding `\\n` between them.

* [#5758](https://github.com/rasahq/rasa/issues/5758): Fixed a bug in [`rasa export`](https://rasa.com/docs/rasa-pro/command-line-interface#rasa-export)) which caused Rasa Open Source to only migrate conversation events from the last [Session configuration](https://rasa.com/docs/rasa-pro/nlu-based-assistants/domain#session-configuration).

## [1.10.1] - 2020-05-15

### Improvements

* [#5794](https://github.com/rasahq/rasa/issues/5794): Creating a `Domain` using `Domain.fromDict` can no longer alter the input dictionary.
  Previously, there could be problems when the input dictionary was re-used for other
  things after creating the `Domain` from it.

### Bugfixes

* [#5617](https://github.com/rasahq/rasa/issues/5617): Don't create TensorBoard log files during prediction.

* [#5638](https://github.com/rasahq/rasa/issues/5638): Fix: DIET breaks with empty spaCy model

* [#5755](https://github.com/rasahq/rasa/issues/5755): Remove `clean_up_entities` from extractors that extract pre-defined entities.
  Just keep the clean up method for entity extractors that extract custom entities.

* [#5792](https://github.com/rasahq/rasa/issues/5792): Fixed issue where the `DucklingHTTPExtractor` component would
  not work if its url contained a trailing slash.

* [#5825](https://github.com/rasahq/rasa/issues/5825): Fix list index out of range error in `ensure_consistent_bilou_tagging`.

### Miscellaneous internal changes

* #5788

## [1.10.0] - 2020-04-28

### Features

* [#3765](https://github.com/rasahq/rasa/issues/3765): Add support for entities with roles and grouping of entities in Rasa NLU.

  You can now define a role and/or group label in addition to the entity type for entities.
  Use the role label if an entity can play different roles in your assistant.
  For example, a city can be a destination or a departure city.
  The group label can be used to group multiple entities together.
  For example, you could group different pizza orders, so that you know what toppings goes with which pizza and
  what size which pizza has.
  For more details see [Entities Roles and Groups](https://rasa.com/docs/rasa-pro/nlu-based-assistants/nlu-training-data#entities-roles-and-groups).

  To fill slots from entities with a specific role/group, you need to either use forms or use a custom action.
  We updated the tracker method `get_latest_entity_values` to take an optional role/group label.
  If you want to use a form, you can add the specific role/group label of interest to the slot mapping function
  `from_entity` (see [Forms](https://rasa.com/docs/rasa-pro/nlu-based-assistants/forms)).

  :::note
  Composite entities are currently just supported by the [DIETClassifier](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#dietclassifier) and [CRFEntityExtractor](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#crfentityextractor).

  :::

* [#5465](https://github.com/rasahq/rasa/issues/5465): Update training data format for NLU to support entities with a role or group label.

  You can now specify synonyms, roles, and groups of entities using the following data format:
  Markdown:

  ```
  [LA]{"entity": "location", "role": "city", "group": "CA", "value": "Los Angeles"}
  ```

  JSON:

  ```
  "entities": [
      {
          "start": 10,
          "end": 12,
          "value": "Los Angeles",
          "entity": "location",
          "role": "city",
          "group": "CA",
      }
  ]
  ```

  The markdown format `[LA](location:Los Angeles)` is deprecated. To update your training data file just
  execute the following command on the terminal of your choice:
  `sed -i -E 's/\\[([^)]+)\\]\\(([^)]+):([^)]+)\\)/[\\1]{"entity": "\\2", "value": "\\3"}/g' nlu.md`

  For more information about the new data format see [Training Data Format](https://rasa.com/docs/rasa-pro/nlu-based-assistants/training-data-format).

### Improvements

* [#2224](https://github.com/rasahq/rasa/issues/2224): Suppressed `pika` logs when establishing the connection. These log messages
  mostly happened when Rasa X and RabbitMQ were started at the same time. Since RabbitMQ
  can take a few seconds to initialize, Rasa X has to re-try until the connection is
  established.
  In case you suspect a different problem (such as failing authentication) you can
  re-enable the `pika` logs by setting the log level to `DEBUG`. To run Rasa Open
  Source in debug mode, use the `--debug` flag. To run Rasa X in debug mode, set the
  environment variable `DEBUG_MODE` to `true`.

* [#3419](https://github.com/rasahq/rasa/issues/3419): Include the source filename of a story in the failed stories

  Include the source filename of a story in the failed stories to make it easier to identify the file which contains the failed story.

* [#5544](https://github.com/rasahq/rasa/issues/5544): Add confusion matrix and “confused_with” to response selection evaluation

  If you are using ResponseSelectors, they now produce similiar outputs during NLU evaluation. Misclassfied responses are listed in a “confused_with” attribute in the evaluation report. Similiarily, a confusion matrix of all responses is plotted.

* [#5578](https://github.com/rasahq/rasa/issues/5578): Added `socketio` to the compatible channels for [Reminders and External Events](https://rasa.com/docs/rasa-pro/nlu-based-assistants/reaching-out-to-user).

* [#5595](https://github.com/rasahq/rasa/issues/5595): Update `POST /model/train` endpoint to accept retrieval action responses
  at the `responses` key of the JSON payload.

* [#5627](https://github.com/rasahq/rasa/issues/5627): All Rasa Open Source images are now using Python 3.7 instead of Python 3.6.

* [#5635](https://github.com/rasahq/rasa/issues/5635): Update dependencies based on the `dependabot` check.

* [#5636](https://github.com/rasahq/rasa/issues/5636): Add dropout between `FFNN` and `DenseForSparse` layers in `DIETClassifier`,
  `ResponseSelector` and `EmbeddingIntentClassifier` controlled by `use_dense_input_dropout` config parameter.

* [#5646](https://github.com/rasahq/rasa/issues/5646): `DIETClassifier` only counts as extractor in `rasa test` if it was actually trained for entity recognition.

* [#5669](https://github.com/rasahq/rasa/issues/5669): Remove regularization gradient for variables that don't have prediction gradient.

* [#5672](https://github.com/rasahq/rasa/issues/5672): Raise a warning in `CRFEntityExtractor` and `DIETClassifier` if entities are not correctly annotated in the
  training data, e.g. their start and end values do not match any start and end values of tokens.

* [#5690](https://github.com/rasahq/rasa/issues/5690): Add `full_retrieval_intent` property to `ResponseSelector` rankings

* [#5717](https://github.com/rasahq/rasa/issues/5717): Change default values for hyper-parameters in `EmbeddingIntentClassifier` and `DIETClassifier`

  Use `scale_loss=False` in `DIETClassifier`. Reduce the number of dense dimensions for sparse features of text from 512 to 256 in `EmbeddingIntentClassifier`.

### Bugfixes

* [#5230](https://github.com/rasahq/rasa/issues/5230): Fixed issue where posting to certain callback channel URLs would return a 500 error on successful posts due to invalid response format.

* [#5475](https://github.com/rasahq/rasa/issues/5475): One word can just have one entity label.

  If you are using, for example, `ConveRTTokenizer` words can be split into multiple tokens.
  Our entity extractors assign entity labels per token. So, it might happen, that a word, that was split into two tokens,
  got assigned two different entity labels. This is now fixed. One word can just have one entity label at a time.

* [#5509](https://github.com/rasahq/rasa/issues/5509): An entity label should always cover a complete word.

  If you are using, for example, `ConveRTTokenizer` words can be split into multiple tokens.
  Our entity extractors assign entity labels per token. So, it might happen, that just a part of a word has
  an entity label. This is now fixed. An entity label always covers a complete word.

* [#5574](https://github.com/rasahq/rasa/issues/5574): Fixed an issue that happened when metadata is passed in a new session.

  Now the metadata is correctly passed to the ActionSessionStart.

* [#5672](https://github.com/rasahq/rasa/issues/5672): Updated Python dependency `ruamel.yaml` to `>=0.16`. We recommend to use at least
  `0.16.10` due to the security issue
  [CVE-2019-20478](https://nvd.nist.gov/vuln/detail/CVE-2019-20478) which is present in
  in prior versions.

### Miscellaneous internal changes

* #5556, #5587, #5614, #5631, #5633

## [1.9.7] - 2020-04-23

### Improvements

* [#4606](https://github.com/rasahq/rasa/issues/4606): The stream reading timeout for `rasa shell\` is now configurable by using the
  environment variable \`\`RASA_SHELL_STREAM_READING_TIMEOUT_IN_SECONDS`.
  This can help to fix problems when using `rasa shell` with custom actions which run
  10 seconds or longer.

### Bugfixes

* [#5709](https://github.com/rasahq/rasa/issues/5709): Reverted changes in 1.9.6 that led to model incompatibility. Upgrade to 1.9.7 to fix
  `self.sequence_lengths_for(tf_batch_data[TEXT_SEQ_LENGTH][0]) IndexError: list index out of range`
  error without needing to retrain earlier 1.9 models.

  Therefore, all 1.9 models except for 1.9.6 will be compatible; a model trained on 1.9.6 will need
  to be retrained on 1.9.7.

## [1.9.6] - 2020-04-15

### Bugfixes

* [#5426](https://github.com/rasahq/rasa/issues/5426): Fix rasa test nlu plotting when using multiple runs.

* [#5489](https://github.com/rasahq/rasa/issues/5489): Fixed issue where `max_number_of_predictions` was not considered when running end-to-end testing.

### Miscellaneous internal changes

* #5626

## [1.9.5] - 2020-04-01

### Improvements

* [#5533](https://github.com/rasahq/rasa/issues/5533): Support for
  [PostgreSQL schemas](https://www.postgresql.org/docs/11/ddl-schemas.html) in
  [SQLTrackerStore](https://rasa.com/docs/rasa-pro/production/tracker-stores#sqltrackerstore). The `SQLTrackerStore`
  accesses schemas defined by the `POSTGRESQL_SCHEMA` environment variable if
  connected to a PostgreSQL database.

  The schema is added to the connection string option's `-csearch_path` key, e.g.
  `-options=-csearch_path=<SCHEMA_NAME>` (see the
  [PostgreSQL docs](https://www.postgresql.org/docs/11/contrib-dblink-connect.html) for more details).
  As before, if no `POSTGRESQL_SCHEMA` is defined, Rasa uses the database's default
  schema (`public`).

  The schema has to exist in the database before connecting, i.e. it needs to have been
  created with

  ```postgresql
  CREATE SCHEMA schema_name;
  ```

### Bugfixes

* [#5547](https://github.com/rasahq/rasa/issues/5547): Fixed ambiguous logging in `DIETClassifier` by adding the name of the calling class to the log message.

## [1.9.4] - 2020-03-30

### Bugfixes

* [#5529](https://github.com/rasahq/rasa/issues/5529): Fix memory leak problem on increasing number of calls to `/model/parse` endpoint.

## [1.9.3] - 2020-03-27

### Bugfixes

* [#5505](https://github.com/rasahq/rasa/issues/5505): Set default value for `weight_sparsity` in `ResponseSelector` to `0`.
  This fixes a bug in the default behavior of `ResponseSelector` which was accidentally introduced in `rasa==1.8.0`.
  Users should update to this version and re-train their models if `ResponseSelector` was used in their pipeline.

## [1.9.2] - 2020-03-26

### Improved Documentation

* [#5497](https://github.com/RasaHQ/rasa/pull/5497): Fix documentation to bring back Sara.

## [1.9.1] - 2020-03-25

### Bugfixes

* [#5492](https://github.com/rasahq/rasa/issues/5492): Fix an issue where the deprecated `queue` parameter for the [Pika Event Broker](https://rasa.com/docs/rasa-pro/production/event-brokers#pika-event-broker)
  was ignored and Rasa Open Source published the events to the `rasa_core_events`
  queue instead. Note that this does not change the fact that the `queue` argument
  is deprecated in favor of the `queues` argument.

## [1.9.0] - 2020-03-24

### Features

* [#5006](https://github.com/rasahq/rasa/issues/5006): Channel `hangouts` for Rasa integration with Google Hangouts Chat is now supported out-of-the-box.

* [#5389](https://github.com/rasahq/rasa/issues/5389): Add an optional path to a specific directory to download and cache the pre-trained model weights for [HFTransformersNLP](https://rasa.com/docs/rasa/2.x/components#hftransformersnlp).

* [#5422](https://github.com/rasahq/rasa/issues/5422): Add options `tensorboard_log_directory` and `tensorboard_log_level` to `EmbeddingIntentClassifier`,
  `DIETClasifier`, `ResponseSelector`, `EmbeddingPolicy` and `TEDPolicy`.

  By default `tensorboard_log_directory` is `None`. If a valid directory is provided,
  metrics are written during training. After the model is trained you can take a look
  at the training metrics in tensorboard. Execute `tensorboard --logdir <path-to-given-directory>`.

  Metrics can either be written after every epoch (default) or for every training step.
  You can specify when to write metrics using the variable `tensorboard_log_level`.
  Valid values are 'epoch' and 'minibatch'.

  We also write down a model summary, i.e. layers with inputs and types, to the given directory.

### Improvements

* [#4756](https://github.com/rasahq/rasa/issues/4756): Make response timeout configurable.
  `rasa run`, `rasa shell` and `rasa x` can now be started with
  `--response-timeout <int>` to configure a response timeout of `<int>` seconds.

* [#4826](https://github.com/rasahq/rasa/issues/4826): Add full retrieval intent name to message data
  `ResponseSelector` will now add the full retrieval intent name
  e.g. `faq/which_version` to the prediction, making it accessible
  from the tracker.

* [#5258](https://github.com/rasahq/rasa/issues/5258): Added `PikaEventBroker` ([Pika Event Broker](https://rasa.com/docs/rasa-pro/production/event-brokers#pika-event-broker)) support for publishing to
  multiple queues. Messages are now published to a `fanout` exchange with name
  `rasa-exchange` (see
  [exchange-fanout](https://www.rabbitmq.com/tutorials/amqp-concepts.html#exchange-fanout)
  for more information on `fanout` exchanges).

  The former `queue` key is deprecated. Queues should now be
  specified as a list in the `endpoints.yml` event broker config under a new key
  `queues`. Example config:

  ```yaml-rasa
  event_broker:
    type: pika
    url: localhost
    username: username
    password: password
    queues:
      - queue-1
      - queue-2
      - queue-3
  ```

* [#5416](https://github.com/rasahq/rasa/issues/5416): Change `rasa init` to include `tests/conversation_tests.md` file by default.

* [#5446](https://github.com/rasahq/rasa/issues/5446): The endpoint `PUT /conversations/<conversation_id>/tracker/events` no longer
  adds session start events (to learn more about conversation sessions, please
  see [Session configuration](https://rasa.com/docs/rasa-pro/nlu-based-assistants/domain#session-configuration)) in addition to the events which were sent in the request
  payload. To achieve the old behavior send a
  `GET /conversations/<conversation_id>/tracker`
  request before appending events.

* [#5482](https://github.com/rasahq/rasa/issues/5482): Make `scale_loss` for intents behave the same way as in versions below `1.8`, but
  only scale if some of the examples in a batch has probability of the golden label more than `0.5`.
  Introduce `scale_loss` for entities in `DIETClassifier`.

### Bugfixes

* [#5205](https://github.com/rasahq/rasa/issues/5205): Fixed the bug when FormPolicy was overwriting MappingPolicy prediction (e.g. `/restart`).
  Priorities for [Mapping Policy](https://rasa.com/docs/rasa/2.x/policies#mapping-policy) and [Form Policy](https://rasa.com/docs/rasa/2.x/policies#form-policy) are no longer linear:
  `FormPolicy` priority is 5, but its prediction is ignored if `MappingPolicy` is used for prediction.

* [#5215](https://github.com/rasahq/rasa/issues/5215): Fixed issue related to storing Python `float` values as `decimal.Decimal` objects
  in DynamoDB tracker stores. All `decimal.Decimal` objects are now converted to
  `float` on tracker retrieval.

  Added a new docs section on [DynamoTrackerStore](https://rasa.com/docs/rasa-pro/production/tracker-stores#dynamotrackerstore).

* [#5356](https://github.com/rasahq/rasa/issues/5356): Fixed bug where `FallbackPolicy` would always fall back if the fallback action is
  `action_listen`.

* [#5361](https://github.com/rasahq/rasa/issues/5361): Fixed bug where starting or ending a response with `\\n\\n` led to one of the responses returned being empty.

* [#5405](https://github.com/rasahq/rasa/issues/5405): Fixes issue where model always gets retrained if multiple NLU/story files are in a
  directory, by sorting the list of files.

* [#5444](https://github.com/rasahq/rasa/issues/5444): Fixed ambiguous logging in DIETClassifier by adding the name of the calling class to the log message.

### Improved Documentation

* [#2237](https://github.com/rasahq/rasa/issues/2237): Restructure the “Evaluating models” documentation page and rename this page to [Testing Your Assistant](https://rasa.com/docs/rasa-pro/nlu-based-assistants/testing-your-assistant).

* [#5302](https://github.com/rasahq/rasa/issues/5302): Improved documentation on how to build and deploy an action server image for use on other servers such as Rasa X deployments.

### Miscellaneous internal changes

* #5340

## [1.8.3] - 2020-03-27

### Bugfixes

* [#5405](https://github.com/rasahq/rasa/issues/5405): Fixes issue where model always gets retrained if multiple NLU/story files are in a
  directory, by sorting the list of files.

* [#5444](https://github.com/rasahq/rasa/issues/5444): Fixed ambiguous logging in DIETClassifier by adding the name of the calling class to the log message.

* [#5506](https://github.com/rasahq/rasa/issues/5506): Set default value for `weight_sparsity` in `ResponseSelector` to `0`.
  This fixes a bug in the default behavior of `ResponseSelector` which was accidentally introduced in `rasa==1.8.0`.
  Users should update to this version or `rasa>=1.9.3` and re-train their models if `ResponseSelector` was used in their pipeline.

### Improved Documentation

* [#5302](https://github.com/rasahq/rasa/issues/5302): Improved documentation on how to build and deploy an action server image for use on other servers such as Rasa X deployments.

## [1.8.2] - 2020-03-19

### Bugfixes

* [#5438](https://github.com/rasahq/rasa/issues/5438): Fixed bug when installing rasa with `poetry`.

* [#5413](https://github.com/RasaHQ/rasa/issues/5413): Fixed bug with `EmbeddingIntentClassifier`, where results
  weren't the same as in 1.7.x. Fixed by setting weight sparsity to 0.

### Improved Documentation

* [#5404](https://github.com/rasahq/rasa/issues/5404): Explain how to run commands as `root` user in Rasa SDK Docker images since version
  `1.8.0`. Since version `1.8.0` the Rasa SDK Docker images does not longer run as
  `root` user by default. For commands which require `root` user usage, you have to
  switch back to the `root` user in your Docker image as described in
  [Building an Action Server Image](https://rasa.com/docs/rasa-pro/deploy/deploy-action-server#building-an-action-server-image).

* [#5402](https://github.com/RasaHQ/rasa/issues/5402): Made improvements to Building Assistants tutorial

## [1.8.1] - 2020-03-06

### Bugfixes

* [#5354](https://github.com/rasahq/rasa/issues/5354): Fixed issue with using language models like `xlnet` along with `entity_recognition` set to `True` inside
  `DIETClassifier`.

### Miscellaneous internal changes

* #5330, #5348

## [1.8.0] - 2020-02-26

### Deprecations and Removals

* [#4991](https://github.com/rasahq/rasa/issues/4991): Removed `Agent.continue_training` and the `dump_flattened_stories` parameter
  from `Agent.persist`.

* [#5266](https://github.com/rasahq/rasa/issues/5266): Properties `Component.provides` and `Component.requires` are deprecated.
  Use `Component.required_components()` instead.

### Features

* [#2674](https://github.com/rasahq/rasa/issues/2674): Add default value `__other__` to `values` of a `CategoricalSlot`.

  All values not mentioned in the list of values of a `CategoricalSlot`
  will be mapped to `__other__` for featurization.

* [#4088](https://github.com/rasahq/rasa/issues/4088): Add story structure validation functionality (e.g. rasa data validate stories –max-history 5).

* [#5065](https://github.com/rasahq/rasa/issues/5065): Add [LexicalSyntacticFeaturizer](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#lexicalsyntacticfeaturizer) to sparse featurizers.

  `LexicalSyntacticFeaturizer` does the same featurization as the `CRFEntityExtractor`. We extracted the
  featurization into a separate component so that the features can be reused and featurization is independent from the
  entity extraction.

* [#5187](https://github.com/rasahq/rasa/issues/5187): Integrate language models from HuggingFace's [Transformers](https://github.com/huggingface/transformers) Library.

  Add a new NLP component [HFTransformersNLP](https://rasa.com/docs/rasa/2.x/components#hftransformersnlp) which tokenizes and featurizes incoming messages using a specified
  pre-trained model with the Transformers library as the backend.
  Add [LanguageModelTokenizer](https://rasa.com/docs/rasa/2.x/components#languagemodeltokenizer) and [LanguageModelFeaturizer](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#languagemodelfeaturizer) which use the information from
  [HFTransformersNLP](https://rasa.com/docs/rasa/2.x/components#hftransformersnlp) and sets them correctly for message object.
  Language models currently supported: BERT, OpenAIGPT, GPT-2, XLNet, DistilBert, RoBERTa.

* [#5225](https://github.com/rasahq/rasa/issues/5225): Added a new CLI command `rasa export` to publish tracker events from a persistent
  tracker store using an event broker. See [Export Conversations to an Event Broker](https://rasa.com/docs/rasa-pro/command-line-interface#rasa-export), [Tracker Stores](https://rasa.com/docs/rasa-pro/production/tracker-stores)
  and [Event Brokers](https://rasa.com/docs/rasa-pro/production/event-brokers) for more details.

* [#5230](https://github.com/rasahq/rasa/issues/5230): Refactor how GPU and CPU environments are configured for TensorFlow 2.0.

  Please refer to the documentation on [Configuring TensorFlow](https://rasa.com/docs/rasa-pro/nlu-based-assistants/tuning-your-model#configuring-tensorflow) to understand
  which environment variables to set in what scenarios. A couple of examples are shown below as well:

  ```python
  # This specifies to use 1024 MB of memory from GPU with logical ID 0 and 2048 MB of memory from GPU with logical ID 1
  TF_GPU_MEMORY_ALLOC="0:1024, 1:2048"

  # Specifies that at most 3 CPU threads can be used to parallelize multiple non-blocking operations
  TF_INTER_OP_PARALLELISM_THREADS="3"

  # Specifies that at most 2 CPU threads can be used to parallelize a particular operation.
  TF_INTRA_OP_PARALLELISM_THREADS="2"
  ```

* [#5266](https://github.com/rasahq/rasa/issues/5266): Added a new NLU component [DIETClassifier](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#dietclassifier) and a new policy [TEDPolicy](https://rasa.com/docs/rasa-pro/nlu-based-assistants/policies#ted-policy).

  DIET (Dual Intent and Entity Transformer) is a multi-task architecture for intent classification and entity
  recognition. You can read more about this component in the [DIETClassifier](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#dietclassifier) documentation.
  The new component will replace the `EmbeddingIntentClassifier` and the
  [CRFEntityExtractor](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#crfentityextractor) in the future.
  Those two components are deprecated from now on.
  See [migration guide](https://rasa.com/docs/rasa-pro/migration-guide#rasa-17-to-rasa-18) for details on how to
  switch to the new component.

  [TEDPolicy](https://rasa.com/docs/rasa-pro/nlu-based-assistants/policies#ted-policy) is the new name for EmbeddingPolicy.
  `EmbeddingPolicy` is deprecated from now on.
  The functionality of `TEDPolicy` and `EmbeddingPolicy` is the same.
  Please update your configuration file to use the new name for the policy.

* [#663](https://github.com/rasahq/rasa/issues/663): The sentence vector of the `SpacyFeaturizer` and `MitieFeaturizer` can be calculated using max or mean pooling.

  To specify the pooling operation, set the option `pooling` for the `SpacyFeaturizer` or the `MitieFeaturizer`
  in your configuration file. The default pooling operation is `mean`. The mean pooling operation also does not take
  into account words, that do not have a word vector.

### Improvements

* [#3975](https://github.com/rasahq/rasa/issues/3975): Added command line argument `--conversation-id` to `rasa interactive`.
  If the argument is not given, `conversation_id` defaults to a random uuid.

* [#4653](https://github.com/rasahq/rasa/issues/4653): Added a new command-line argument `--init-dir` to command `rasa init` to specify
  the directory in which the project is initialised.

* [#4682](https://github.com/rasahq/rasa/issues/4682): Added support to send images with the twilio output channel.

* [#4817](https://github.com/rasahq/rasa/issues/4817): Part of Slack sanitization:
  Multiple garbled URL's in a string coming from slack will be converted into actual strings.
  `Example: health check of <http://eemdb.net|eemdb.net> and <http://eemdb1.net|eemdb1.net> to health check of
  eemdb.net and eemdb1.net`

* [#5117](https://github.com/rasahq/rasa/issues/5117): New command-line argument –conversation-id will be added and wiil give the ability to
  set specific conversation ID for each shell session, if not passed will be random.

* [#5211](https://github.com/rasahq/rasa/issues/5211): Messages sent to the [Pika Event Broker](https://rasa.com/docs/rasa-pro/production/event-brokers#pika-event-broker) are now persisted. This guarantees
  the RabbitMQ will re-send previously received messages after a crash. Note that this
  does not help for the case where messages are sent to an unavailable RabbitMQ instance.

* [#5250](https://github.com/rasahq/rasa/issues/5250): Added support for mattermost connector to use bot accounts.

* [#5266](https://github.com/rasahq/rasa/issues/5266): We updated our code to TensorFlow 2.

* [#5317](https://github.com/rasahq/rasa/issues/5317): Events exported using `rasa export` receive a message header if published through a
  `PikaEventBroker`. The header is added to the message's `BasicProperties.headers`
  under the `rasa-export-process-id` key
  (`rasa.core.constants.RASA_EXPORT_PROCESS_ID_HEADER_NAME`). The value is a
  UUID4 generated at each call of `rasa export`. The resulting header is a key-value
  pair that looks as follows:

  ```text
  'rasa-export-process-id': 'd3b3d3ffe2bd4f379ccf21214ccfb261'
  ```

* [#5292](https://github.com/rasahq/rasa/issues/5292): Added `followlinks=True` to os.walk calls, to allow the use of symlinks in training, NLU and domain data.

* [#4811](https://github.com/rasahq/rasa/issues/4811): Support invoking a `SlackBot` by direct messaging or `@<app name>` mentions.

### Bugfixes

* [#4006](https://github.com/rasahq/rasa/issues/4006): Fixed timestamp parsing warning when using DucklingHTTPExtractor

* [#4601](https://github.com/rasahq/rasa/issues/4601): Fixed issue with `action_restart` getting overridden by `action_listen` when the [Mapping Policy](https://rasa.com/docs/rasa/2.x/policies#mapping-policy) and the
  [Two-Stage Fallback Policy](https://rasa.com/docs/rasa/2.x/policies#two-stage-fallback-policy) are used together.

* [#5201](https://github.com/rasahq/rasa/issues/5201): Fixed incorrectly raised Error encountered in pipelines with a `ResponseSelector` and NLG.

  When NLU training data is split before NLU pipeline comparison,
  NLG responses were not also persisted and therefore training for a pipeline including the `ResponseSelector` would fail.

  NLG responses are now persisted along with NLU data to a `/train` directory in the `run_x/xx%_exclusion` folder.

* [#5277](https://github.com/rasahq/rasa/issues/5277): Fixed sending custom json with Twilio channel

### Improved Documentation

* [#5174](https://github.com/rasahq/rasa/issues/5174): Updated the documentation to properly suggest not to explicitly add utterance actions to the domain.

* [#5189](https://github.com/rasahq/rasa/issues/5189): Added user guide for reminders and external events, including `reminderbot` demo.

### Miscellaneous internal changes

* #3923, #4597, #4903, #5180, #5189, #5266, #699

## [1.7.4] - 2020-02-24

### Bugfixes

* [#5068](https://github.com/rasahq/rasa/issues/5068): Tracker stores supporting conversation sessions (`SQLTrackerStore` and
  `MongoTrackerStore`) do not save the tracker state to database immediately after
  starting a new conversation session. This leads to the number of events being saved
  in addition to the already-existing ones to be calculated correctly.

  This fixes `action_listen` events being saved twice at the beginning of
  conversation sessions.

## [1.7.3] - 2020-02-21

### Bugfixes

* [#5231](https://github.com/rasahq/rasa/issues/5231): Fix segmentation fault when running `rasa train` or `rasa shell`.

### Improved Documentation

* [#5286](https://github.com/rasahq/rasa/issues/5286): Fix doc links on “Deploying your Assistant” page

## [1.7.2] - 2020-02-13

### Bugfixes

* [#5197](https://github.com/rasahq/rasa/issues/5197): Fixed incompatibility of Oracle with the [SQLTrackerStore](https://rasa.com/docs/rasa-pro/production/tracker-stores#sqltrackerstore), by using a `Sequence`
  for the primary key columns. This does not change anything for SQL databases other than Oracle.
  If you are using Oracle, please create a sequence with the instructions in the [SQLTrackerStore](https://rasa.com/docs/rasa-pro/production/tracker-stores#sqltrackerstore) docs.

### Improved Documentation

* [#5197](https://github.com/rasahq/rasa/issues/5197): Added section on setting up the SQLTrackerStore with Oracle

* [#5210](https://github.com/rasahq/rasa/issues/5210): Renamed “Running the Server” page to “Configuring the HTTP API”

## [1.7.1] - 2020-02-11

### Bugfixes

* [#5106](https://github.com/rasahq/rasa/issues/5106): Fixed file loading of non proper UTF-8 story files, failing properly when checking for
  story files.

* [#5162](https://github.com/rasahq/rasa/issues/5162): Fix problem with multi-intents.
  Training with multi-intents using the `CountVectorsFeaturizer` together with `EmbeddingIntentClassifier` is
  working again.

* [#5171](https://github.com/rasahq/rasa/issues/5171): Fix bug `ValueError: Cannot concatenate sparse features as sequence dimension does not match`.

  When training a Rasa model that contains responses for just some of the intents, training was failing.
  Fixed the featurizers to return a consistent feature vector in case no response was given for a specific message.

* [#5199](https://github.com/rasahq/rasa/issues/5199): If no text features are present in `EmbeddingIntentClassifier` return the intent `None`.

* [#5216](https://github.com/rasahq/rasa/issues/5216): Resolve version conflicts: Pin version of cloudpickle to ~=1.2.0.

## [1.7.0] - 2020-01-29

### Deprecations and Removals

* [#4964](https://github.com/rasahq/rasa/issues/4964): The endpoint `/conversations/<conversation_id>/execute` is now deprecated. Instead, users should use
  the `/conversations/<conversation_id>/trigger_intent` endpoint and thus trigger intents instead of actions.

* [#4978](https://github.com/rasahq/rasa/issues/4978): Remove option `use_cls_token` from tokenizers and option `return_sequence` from featurizers.

  By default all tokenizer add a special token (`__CLS__`) to the end of the list of tokens.
  This token will be used to capture the features of the whole utterance.

  The featurizers will return a matrix of size (number-of-tokens x feature-dimension) by default.
  This allows to train sequence models.
  However, the feature vector of the `__CLS__` token can be used to train non-sequence models.
  The corresponding classifier can decide what kind of features to use.

### Features

* [#400](https://github.com/rasahq/rasa/issues/400): Rename `templates` key in domain to `responses`.

  `templates` key will still work for backwards compatibility but will raise a future warning.

* [#4902](https://github.com/rasahq/rasa/issues/4902): Added a new configuration parameter, `ranking_length` to the `EmbeddingPolicy`, `EmbeddingIntentClassifier`,
  and `ResponseSelector` classes.

* [#4964](https://github.com/rasahq/rasa/issues/4964): External events and reminders now trigger intents (and entities) instead of actions.

  Add new endpoint `/conversations/<conversation_id>/trigger_intent`, which lets the user specify an intent and a
  list of entities that is injected into the conversation in place of a user message. The bot then predicts and
  executes a response action.

* [#4978](https://github.com/rasahq/rasa/issues/4978): Add `ConveRTTokenizer`.

  The tokenizer should be used whenever the `ConveRTFeaturizer` is used.

  Every tokenizer now supports the following configuration options:
  `intent_tokenization_flag`: Flag to check whether to split intents (default `False`).
  `intent_split_symbol`: Symbol on which intent should be split (default `_`)

### Improvements

* [#1988](https://github.com/rasahq/rasa/issues/1988): Remove the need of specifying utter actions in the `actions` section explicitly if these actions are already
  listed in the `templates` section.

* [#4877](https://github.com/rasahq/rasa/issues/4877): Entity examples that have been extracted using an external extractor are excluded
  from Markdown dumping in `MarkdownWriter.dumps()`. The excluded external extractors
  are `DucklingHTTPExtractor` and `SpacyEntityExtractor`.

* [#4902](https://github.com/rasahq/rasa/issues/4902): The `EmbeddingPolicy`, `EmbeddingIntentClassifier`, and `ResponseSelector` now by default normalize confidence
  levels over the top 10 results. See [Rasa 1.6 to Rasa 1.7](https://rasa.com/docs/rasa-pro/migration-guide#rasa-16-to-rasa-17) for more details.

* [#4964](https://github.com/rasahq/rasa/issues/4964): `ReminderCancelled` can now cancel multiple reminders if no name is given. It still cancels a single
  reminder if the reminder's name is specified.

### Bugfixes

* [#4774](https://github.com/rasahq/rasa/issues/4774): Requests to `/model/train` do not longer block other requests to the Rasa server.

* [#4896](https://github.com/rasahq/rasa/issues/4896): Fixed default behavior of `rasa test core --evaluate-model-directory` when called without `--model`. Previously, the latest model file was used as `--model`. Now the default model directory is used instead.

  New behavior of `rasa test core --evaluate-model-directory` when given an existing file as argument for `--model`: Previously, this led to an error. Now a warning is displayed and the directory containing the given file is used as `--model`.

* [#5040](https://github.com/rasahq/rasa/issues/5040): Updated the dependency `networkx` from 2.3.0 to 2.4.0. The old version created incompatibilities when using pip.

  There is an imcompatibility between Rasa dependecy requests 2.22.0 and the own depedency from Rasa for networkx raising errors upon pip install. There is also a bug corrected in `requirements.txt` which used `~=` instead of `==`. All of these are fixed using networkx 2.4.0.

* [#5057](https://github.com/rasahq/rasa/issues/5057): Fixed compatibility issue with Microsoft Bot Framework Emulator if `service_url` lacked a trailing `/`.

* [#5092](https://github.com/rasahq/rasa/issues/5092): DynamoDB tracker store decimal values will now be rounded on save. Previously values exceeding 38 digits caused an unhandled error.

### Miscellaneous internal changes

* #4458, #4664, #4780, #5029

## [1.6.2] - 2020-01-28

### Improvements

* [#4994](https://github.com/rasahq/rasa/issues/4994): Switching back to a TensorFlow release which only includes CPU support to reduce the
  size of the dependencies. If you want to use the TensorFlow package with GPU support,
  please run `pip install tensorflow-gpu==1.15.0`.

### Bugfixes

* [#5111](https://github.com/rasahq/rasa/issues/5111): Fixes `Exception 'Loop' object has no attribute '_ready'` error when running
  `rasa init`.

* [#5126](https://github.com/rasahq/rasa/issues/5126): Updated the end-to-end ValueError you recieve when you have a invalid story format to point
  to the updated doc link.

## [1.6.1] - 2020-01-07

### Bugfixes

* [#4989](https://github.com/rasahq/rasa/issues/4989): Use an empty domain in case a model is loaded which has no domain
  (avoids errors when accessing `agent.doman.<some attribute>`).

* [#4995](https://github.com/rasahq/rasa/issues/4995): Replace error message with warning in tokenizers and featurizers if default parameter not set.

* [#5019](https://github.com/rasahq/rasa/issues/5019): Pin sanic patch version instead of minor version. Fixes sanic `_run_request_middleware()` error.

* [#5032](https://github.com/rasahq/rasa/issues/5032): Fix wrong calculation of additional conversation events when saving the conversation.
  This led to conversation events not being saved.

* [#5032](https://github.com/rasahq/rasa/issues/5032): Fix wrong order of conversation events when pushing events to conversations via
  `POST /conversations/<conversation_id>/tracker/events`.

## [1.6.0] - 2019-12-18

### Deprecations and Removals

* [#4935](https://github.com/rasahq/rasa/issues/4935): Removed `ner_features` as a feature name from `CRFEntityExtractor`, use `text_dense_features` instead.

  The following settings match the previous `NGramFeaturizer`:

  ```yaml-rasa
  pipeline:
  - name: 'CountVectorsFeaturizer'
    analyzer: 'char_wb'
    min_ngram: 3
    max_ngram: 17
    max_features: 10
    min_df: 5
  ```

* [#4957](https://github.com/rasahq/rasa/issues/4957): To [use custom features in the `CRFEntityExtractor`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#crfentityextractor)
  use `text_dense_features` instead of `ner_features`. If
  `text_dense_features` are present in the feature set, the `CRFEntityExtractor` will automatically make use of
  them. Just make sure to add a dense featurizer in front of the `CRFEntityExtractor` in your pipeline and set the
  flag `return_sequence` to `True` for that featurizer.

* [#4990](https://github.com/rasahq/rasa/issues/4990): Deprecated `Agent.continue_training`. Instead, a model should be retrained.

* [#684](https://github.com/rasahq/rasa/issues/684): Specifying lookup tables directly in the NLU file is now deprecated. Please specify
  them in an external file.

### Features

* [#4795](https://github.com/rasahq/rasa/issues/4795): Replaced the warnings about missing templates, intents etc. in validator.py by debug messages.

* [#4830](https://github.com/rasahq/rasa/issues/4830): Added conversation sessions to trackers.

  A conversation session represents the dialog between the assistant and a user.
  Conversation sessions can begin in three ways: 1. the user begins the conversation
  with the assistant, 2. the user sends their first message after a configurable period
  of inactivity, or 3. a manual session start is triggered with the `/session_start`
  intent message. The period of inactivity after which a new conversation session is
  triggered is defined in the domain using the `session_expiration_time` key in the
  `session_config` section. The introduction of conversation sessions comprises the
  following changes:

    * Added a new event `SessionStarted` that marks the beginning of a new conversation
      session.

    * Added a new default action `ActionSessionStart`. This action takes all
      `SlotSet` events from the previous session and applies it to the next session.

    * Added a new default intent `session_start` which triggers the start of a new
      conversation session.

    * `SQLTrackerStore` and `MongoTrackerStore` only retrieve
      events from the last session from the database.

  :::note
  The session behavior is disabled for existing projects, i.e. existing domains
  without session config section.

  :::

* [#4935](https://github.com/rasahq/rasa/issues/4935): Preparation for an upcoming change in the `EmbeddingIntentClassifier`:

  Add option `use_cls_token` to all tokenizers. If it is set to `True`, the token `__CLS__` will be added to
  the end of the list of tokens. Default is set to `False`. No need to change the default value for now.

  Add option `return_sequence` to all featurizers. By default all featurizers return a matrix of size
  (1 x feature-dimension). If the option `return_sequence` is set to `True`, the corresponding featurizer will return
  a matrix of size (token-length x feature-dimension). See [Text Featurizers](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#featurizers).
  Default value is set to `False`. However, you might want to set it to `True` if you want to use custom features
  in the `CRFEntityExtractor`.
  See [passing custom features to the `CRFEntityExtractor`](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#crfentityextractor)

  Changed some featurizers to use sparse features, which should reduce memory usage with large amounts of training data significantly.
  Read more: [Text Featurizers](https://rasa.com/docs/rasa-pro/nlu-based-assistants/components#featurizers) .

  :::caution
  These changes break model compatibility. You will need to retrain your old models!

  :::

### Improvements

* [#3549](https://github.com/rasahq/rasa/issues/3549): Added `--no-plot` option for `rasa test` command, which disables rendering of confusion matrix and histogram. By default plots will be rendered.

* [#4086](https://github.com/rasahq/rasa/issues/4086): If matplotlib couldn't set up a default backend, it will be set automatically to TkAgg/Agg one

* [#4647](https://github.com/rasahq/rasa/issues/4647): Add the option `\`random_seed\`` to the `\`rasa data split nlu\`` command to generate
  reproducible train/test splits.

* [#4734](https://github.com/rasahq/rasa/issues/4734): Changed `url` `__init__()` arguments for custom tracker stores to `host` to reflect the `__init__` arguments of
  currently supported tracker stores. Note that in `endpoints.yml`, these are still declared as `url`.

* [#4751](https://github.com/rasahq/rasa/issues/4751): The `kafka-python` dependency has become as an “extra” dependency. To use the
  `KafkaEventConsumer`, `rasa` has to be installed with the `[kafka]` option, i.e.

  ```bash
  $ pip install rasa[kafka]
  ```

* [#4801](https://github.com/rasahq/rasa/issues/4801): Allow creation of natural language interpreter and generator by classname reference
  in `endpoints.yml`.

* [#4834](https://github.com/rasahq/rasa/issues/4834): Made it explicit that interactive learning does not work with NLU-only models.

  Interactive learning no longer trains NLU-only models if no model is provided
  and no core data is provided.

* [#4899](https://github.com/rasahq/rasa/issues/4899): The `intent_report.json` created by `rasa test` now creates an extra field
  `confused_with` for each intent. This is a dictionary containing the names of
  the most common false positives when this intent should be predicted, and the
  number of such false positives.

* [#4976](https://github.com/rasahq/rasa/issues/4976): `rasa test nlu --cross-validation` now also includes an evaluation of the response selector.
  As a result, the train and test F1-score, accuracy and precision is logged for the response selector.
  A report is also generated in the `results` folder by the name `response_selection_report.json`

### Bugfixes

* [#4635](https://github.com/rasahq/rasa/issues/4635): If a `wait_time_between_pulls` is configured for the model server in `endpoints.yml`,
  this will be used instead of the default one when running Rasa X.

* [#4759](https://github.com/rasahq/rasa/issues/4759): Training Luis data with `luis_schema_version` higher than 4.x.x will show a warning instead of throwing an exception.

* [#4799](https://github.com/rasahq/rasa/issues/4799): Running `rasa interactive` with no NLU data now works, with the functionality of `rasa interactive core`.

* [#4917](https://github.com/rasahq/rasa/issues/4917): When loading models from S3, namespaces (folders within a bucket) are now respected.
  Previously, this would result in an error upon loading the model.

* [#4925](https://github.com/rasahq/rasa/issues/4925): “rasa init” will ask if user wants to train a model

* [#4942](https://github.com/rasahq/rasa/issues/4942): Pin `multidict` dependency to 4.6.1 to prevent sanic from breaking,
  see [the Sanic GitHub issue](https://github.com/huge-success/sanic/issues/1729 "Sanic Github Issue #1729 about Multidict update breaking Sanic") for more info.

* [#4985](https://github.com/rasahq/rasa/issues/4985): Fix errors during training and testing of `ResponseSelector`.

## [1.5.3] - 2019-12-11

### Improvements

* [#4933](https://github.com/rasahq/rasa/issues/4933): Improved error message that appears when an incorrect parameter is passed to a policy.

### Bugfixes

* [#4914](https://github.com/rasahq/rasa/issues/4914): Added `rasa/nlu/schemas/config.yml` to wheel package

* [#4942](https://github.com/rasahq/rasa/issues/4942): Pin `multidict` dependency to 4.6.1 to prevent sanic from breaking,
  see [the Sanic GitHub issue](https://github.com/huge-success/sanic/issues/1729 "Sanic Github Issue #1729 about Multidict update breaking Sanic")

## [1.5.2] - 2019-12-09

### Improvements

* [#3684](https://github.com/rasahq/rasa/issues/3684): `rasa interactive` will skip the story visualization of training stories in case
  there are more than 200 stories. Stories created during interactive learning will be
  visualized as before.

* [#4792](https://github.com/rasahq/rasa/issues/4792): The log level for SocketIO loggers, including `websockets.protocol`, `engineio.server`,
  and `socketio.server`, is now handled by the `LOG_LEVEL_LIBRARIES` environment variable,
  where the default log level is `ERROR`.

* [#4873](https://github.com/rasahq/rasa/issues/4873): Updated all example bots and documentation to use the updated `dispatcher.utter_message()` method from rasa-sdk==1.5.0.

### Bugfixes

* [#3684](https://github.com/rasahq/rasa/issues/3684): `rasa interactive` will not load training stories in case the visualization is
  skipped.

* [#4789](https://github.com/rasahq/rasa/issues/4789): Fixed error where spacy models where not found in the docker images.

* [#4802](https://github.com/rasahq/rasa/issues/4802): Fixed unnecessary `kwargs` unpacking in `rasa.test.test_core` call in `rasa.test.test` function.

* [#4898](https://github.com/rasahq/rasa/issues/4898): Training data files now get loaded in the same order (especially relevant to subdirectories) each time to ensure training consistency when using a random seed.

* [#4918](https://github.com/rasahq/rasa/issues/4918): Locks for tickets in `LockStore` are immediately issued without a redundant
  check for their availability.

### Improved Documentation

* [#4844](https://github.com/rasahq/rasa/issues/4844): Added `towncrier` to automatically collect changelog entries.

* [#4869](https://github.com/rasahq/rasa/issues/4869): Document the pipeline for `pretrained_embeddings_convert` in the pre-configured pipelines section.

* [#4894](https://github.com/rasahq/rasa/issues/4894): `Proactively Reaching Out to the User Using Actions` now correctly links to the
  endpoint specification.

## [1.5.1] - 2019-11-27

### Improvements

* When NLU training data is dumped as Markdown file the intents are not longer ordered
  alphabetically, but in the original order of given training data

### Bugfixes

* End to end stories now support literal payloads which specify entities, e.g.
  `greet: /greet{"name": "John"}`

* Slots will be correctly interpolated if there are lists in custom response templates.

* Fixed compatibility issues with `rasa-sdk` `1.5`

* Updated `/status` endpoint to show correct path to model archive

## [1.5.0] - 2019-11-26

### Features

* Added data validator that checks if domain object returned is empty. If so, exit early
  from the command `rasa data validate`.

* Added the KeywordIntentClassifier.

* Added documentation for `AugmentedMemoizationPolicy`.

* Fall back to `InMemoryTrackerStore` in case there is any problem with the current
  tracker store.

* Arbitrary metadata can now be attached to any `Event` subclass. The data must be
  stored under the `metadata` key when reading the event from a JSON object or
  dictionary.

* Add command line argument `rasa x --config CONFIG`, to specify path to the policy
  and NLU pipeline configuration of your bot (default: `config.yml`).

* Added a new NLU featurizer - `ConveRTFeaturizer` based on [ConveRT](https://github.com/PolyAI-LDN/polyai-models) model released by PolyAI.

* Added a new preconfigured pipeline - `pretrained_embeddings_convert`.

### Improvements

* Do not retrain the entire Core model if only the `templates` section of the domain
  is changed.

* Upgraded `jsonschema` version.

### Deprecations and Removals

* Remove duplicate messages when creating training data (issues/1446).

### Bugfixes

* `MultiProjectImporter` now imports files in the order of the import statements

* Fixed server hanging forever on leaving `rasa shell` before first message

* Fixed rasa init showing traceback error when user does Keyboard Interrupt before choosing a project path

* `CountVectorsFeaturizer` featurizes intents only if its analyzer is set to `word`

* Fixed bug where facebooks generic template was not rendered when buttons were `None`

* Fixed default intents unnecessarily raising undefined parsing error

## [1.4.6] - 2019-11-22

### Bugfixes

* Fixed Rasa X not working when any tracker store was configured for Rasa.

* Use the matplotlib backend `agg` in case the `tkinter` package is not installed.

## [1.4.5] - 2019-11-14

### Bugfixes

* NLU-only models no longer throw warnings about parsing features not defined in the domain

* Fixed bug that stopped Dockerfiles from building version 1.4.4.

* Fixed format guessing for e2e stories with intent restated as `/intent`

## [1.4.4] - 2019-11-13

### Features

* `PikaEventProducer` adds the RabbitMQ `App ID` message property to published
  messages with the value of the `RASA_ENVIRONMENT` environment variable. The
  message property will not be assigned if this environment variable isn't set.

### Improvements

* Updated Mattermost connector documentation to be more clear.

* Updated format strings to f-strings where appropriate.

* Updated tensorflow requirement to `1.15.0`

* Dump domain using UTF-8 (to avoid `\\UXXXX` sequences in the dumped files)

### Bugfixes

* Fixed exporting NLU training data in `json` format from `rasa interactive`

* Fixed numpy deprecation warnings

## [1.4.3] - 2019-10-29

### Bugfixes

* Fixed `Connection reset by peer` errors and bot response delays when using the
  RabbitMQ event broker.

## [1.4.2] - 2019-10-28

### Deprecations and Removals

* TensorFlow deprecation warnings are no longer shown when running `rasa x`

### Bugfixes

* Fixed `'Namespace' object has no attribute 'persist_nlu_data'` error during
  interactive learning

* Pinned networkx~=2.3.0 to fix visualization in rasa interactive and Rasa X

* Fixed `No model found` error when using `rasa run actions` with “actions”
  as a directory.

## [1.4.1] - 2019-10-22

Regression: changes from `1.2.12` were missing from `1.4.0`, readded them

## [1.4.0] - 2019-10-19

### Features

* add flag to CLI to persist NLU training data if needed

* log a warning if the `Interpreter` picks up an intent or an entity that does not
  exist in the domain file.

* added `DynamoTrackerStore` to support persistence of agents running on AWS

* added docstrings for `TrackerStore` classes

* added buttons and images to mattermost.

* `CRFEntityExtractor` updated to accept arbitrary token-level features like word
  vectors (issues/4214)

* `SpacyFeaturizer` updated to add `ner_features` for `CRFEntityExtractor`

* Sanitizing incoming messages from slack to remove slack formatting like `<mailto:xyz@rasa.com|xyz@rasa.com>`
  or `<http://url.com|url.com>` and substitute it with original content

* Added the ability to configure the number of Sanic worker processes in the HTTP
  server (`rasa.server`) and input channel server
  (`rasa.core.agent.handle_channels()`). The number of workers can be set using the
  environment variable `SANIC_WORKERS` (default: 1). A value of >1 is allowed only in
  combination with `RedisLockStore` as the lock store.

* Botframework channel can handle uploaded files in `UserMessage` metadata.

* Added data validator that checks there is no duplicated example data across multiples intents

### Improvements

* Unknown sections in markdown format (NLU data) are not ignored anymore, but instead an error is raised.

* It is now easier to add metadata to a `UserMessage` in existing channels.
  You can do so by overwriting the method `get_metadata`. The return value of this
  method will be passed to the `UserMessage` object.

* Tests can now be run in parallel

* Serialise `DialogueStateTracker` as json instead of pickle. **DEPRECATION warning**:
  Deserialisation of pickled trackers will be deprecated in version 2.0. For now,
  trackers are still loaded from pickle but will be dumped as json in any subsequent
  save operations.

* Event brokers are now also passed to custom tracker stores (using the `event_broker` parameter)

* Don't run the Rasa Docker image as `root`.

* Use multi-stage builds to reduce the size of the Rasa Docker image.

* Updated the `/status` api route to use the actual model file location instead of the `tmp` location.

### Deprecations and Removals

* **Removed Python 3.5 support**

### Bugfixes

* fixed missing `tkinter` dependency for running tests on Ubuntu

* fixed issue with `conversation` JSON serialization

* fixed the hanging HTTP call with `ner_duckling_http` pipeline

* fixed Interactive Learning intent payload messages saving in nlu files

* fixed DucklingHTTPExtractor dimensions by actually applying to the request

## [1.3.10] - 2019-10-18

### Features

* Can now pass a package as an argument to the `--actions` parameter of the
  `rasa run actions` command.

### Bugfixes

* Fixed visualization of stories with entities which led to a failing
  visualization in Rasa X

## [1.3.9] - 2019-10-10

### Features

* Port of 1.2.10 (support for RabbitMQ TLS authentication and `port` key in
  event broker endpoint config).

* Port of 1.2.11 (support for passing a CA file for SSL certificate verification via the
  –ssl-ca-file flag).

### Bugfixes

* Fixed the hanging HTTP call with `ner_duckling_http` pipeline.

* Fixed text processing of `intent` attribute inside `CountVectorFeaturizer`.

* Fixed `argument of type 'NoneType' is not iterable` when using `rasa shell`,
  `rasa interactive` / `rasa run`

## [1.3.8] - 2019-10-08

### Improvements

* Policies now only get imported if they are actually used. This removes
  TensorFlow warnings when starting Rasa X

### Bugfixes

* Fixed error `Object of type 'MaxHistoryTrackerFeaturizer' is not JSON serializable`
  when running `rasa train core`

* Default channel `send_` methods no longer support kwargs as they caused issues in incompatible channels

## [1.3.7] - 2019-09-27

### Bugfixes

* re-added TLS, SRV dependencies for PyMongo

* socketio can now be run without turning on the `--enable-api` flag

* MappingPolicy no longer fails when the latest action doesn't have a policy

## [1.3.6] - 2019-09-21

### Features

* Added the ability for users to specify a conversation id to send a message to when
  using the `RasaChat` input channel.

## [1.3.5] - 2019-09-20

### Bugfixes

* Fixed issue where `rasa init` would fail without spaCy being installed

## [1.3.4] - 2019-09-20

### Features

* Added the ability to set the `backlog` parameter in Sanics `run()` method using
  the `SANIC_BACKLOG` environment variable. This parameter sets the
  number of unaccepted connections the server allows before refusing new
  connections. A default value of 100 is used if the variable is not set.

* Status endpoint (`/status`) now also returns the number of training processes currently running

### Bugfixes

* Added the ability to properly deal with spaCy `Doc`-objects created on
  empty strings as discussed in
  [issue #4445](https://github.com/RasaHQ/rasa/issues/4445 "Rasa issue #4445: Handling spaCy objects on empty strings").
  Only training samples that actually bear content are sent to `self.nlp.pipe`
  for every given attribute. Non-content-bearing samples are converted to empty
  `Doc`-objects. The resulting lists are merged with their preserved order and
  properly returned.

* asyncio warnings are now only printed if the callback takes more than 100ms
  (up from 1ms).

* `agent.load_model_from_server` no longer affects logging.

### Improvements

* The endpoint `POST /model/train` no longer supports specifying an output directory
  for the trained model using the field `out`. Instead you can choose whether you
  want to save the trained model in the default model directory (`models`)
  (default behavior) or in a temporary directory by specifying the
  `save_to_default_model_directory` field in the training request.

## [1.3.3] - 2019-09-13

### Bugfixes

* Added a check to avoid training `CountVectorizer` for a particular
  attribute of a message if no text is provided for that attribute across
  the training data.

* Default one-hot representation for label featurization inside `EmbeddingIntentClassifier` if label features don't exist.

* Policy ensemble no longer incorrectly wrings “missing mapping policy” when
  mapping policy is present.

* “text” from `utter_custom_json` now correctly saved to tracker when using telegram channel

### Deprecations and Removals

* Removed computation of `intent_spacy_doc`. As a result, none of the spacy components process intents now.

## [1.3.2] - 2019-09-10

### Bugfixes

* SQL tracker events are retrieved ordered by timestamps. This fixes interactive
  learning events being shown in the wrong order.

## [1.3.1] - 2019-09-09

### Improvements

* Pin gast to == 0.2.2

## [1.3.0] - 2019-09-05

### Features

* Added option to persist nlu training data (default: False)

* option to save stories in e2e format for interactive learning

* bot messages contain the `timestamp` of the `BotUttered` event, which can be used in channels

* `FallbackPolicy` can now be configured to trigger when the difference between confidences of two predicted intents is too narrow

* experimental training data importer which supports training with data of multiple
  sub bots. Please see the
  docs for more
  information.

* throw error during training when triggers are defined in the domain without
  `MappingPolicy` being present in the policy ensemble

* The tracker is now available within the interpreter's `parse` method, giving the
  ability to create interpreter classes that use the tracker state (eg. slot values)
  during the parsing of the message. More details on motivation of this change see
  issues/3015.

* add example bot `knowledgebasebot` to showcase the usage of `ActionQueryKnowledgeBase`

* `softmax` starspace loss for both `EmbeddingPolicy` and `EmbeddingIntentClassifier`

* `balanced` batching strategy for both `EmbeddingPolicy` and `EmbeddingIntentClassifier`

* `max_history` parameter for `EmbeddingPolicy`

* Successful predictions of the NER are written to a file if `--successes` is set when running `rasa test nlu`

* Incorrect predictions of the NER are written to a file by default. You can disable it via `--no-errors`.

* New NLU component `ResponseSelector` added for the task of response selection

* Message data attribute can contain two more keys - `response_key`, `response` depending on the training data

* New action type implemented by `ActionRetrieveResponse` class and identified with `response_` prefix

* Vocabulary sharing inside `CountVectorsFeaturizer` with `use_shared_vocab` flag. If set to True, vocabulary of corpus is shared between text, intent and response attributes of message

* Added an option to share the hidden layer weights of text input and label input inside `EmbeddingIntentClassifier` using the flag `share_hidden_layers`

* New type of training data file in NLU which stores response phrases for response selection task.

* Add flag `intent_split_symbol` and `intent_tokenization_flag` to all `WhitespaceTokenizer`, `JiebaTokenizer` and `SpacyTokenizer`

* Added evaluation for response selector. Creates a report `response_selection_report.json` inside `--out` directory.

* argument `--config-endpoint` to specify the URL from which `rasa x` pulls
  the runtime configuration (endpoints and credentials)

* `LockStore` class storing instances of `TicketLock` for every `conversation_id`

* environment variables `SQL_POOL_SIZE` (default: 50) and `SQL_MAX_OVERFLOW`
  (default: 100) can be set to control the pool size and maximum pool overflow for
  `SQLTrackerStore` when used with the `postgresql` dialect

* Add a bot_challenge intent and a utter_iamabot action to all example projects and the rasa init bot.

* Allow sending attachments when using the socketio channel

* `rasa data validate` will fail with a non-zero exit code if validation fails

### Improvements

* added character-level `CountVectorsFeaturizer` with empirically found parameters
  into the `supervised_embeddings` NLU pipeline template

* NLU evaluations now also stores its output in the output directory like the core evaluation

* show warning in case a default path is used instead of a provided, invalid path

* compare mode of `rasa train core` allows the whole core config comparison,
  naming style of models trained for comparison is changed (this is a breaking change)

* pika keeps a single connection open, instead of open and closing on each incoming event

* `RasaChatInput` fetches the public key from the Rasa X API. The key is used to
  decode the bearer token containing the conversation ID. This requires
  `rasa-x>=0.20.2`.

* more specific exception message when loading custom components depending on whether component's path or
  class name is invalid or can't be found in the global namespace

* change priorities so that the `MemoizationPolicy` has higher priority than the `MappingPolicy`

* substitute LSTM with Transformer in `EmbeddingPolicy`

* `EmbeddingPolicy` can now use `MaxHistoryTrackerFeaturizer`

* non zero `evaluate_on_num_examples` in `EmbeddingPolicy`
  and `EmbeddingIntentClassifier` is the size of
  hold out validation set that is excluded from training data

* defaults parameters and architectures for both `EmbeddingPolicy` and
  `EmbeddingIntentClassifier` are changed (this is a breaking change)

* evaluation of NER does not include 'no-entity' anymore

* `--successes` for `rasa test nlu` is now boolean values. If set incorrect/successful predictions
  are saved in a file.

* `--errors` is renamed to `--no-errors` and is now a boolean value. By default incorrect predictions are saved
  in a file. If `--no-errors` is set predictions are not written to a file.

* Remove `label_tokenization_flag` and `label_split_symbol` from `EmbeddingIntentClassifier`. Instead move these parameters to `Tokenizers`.

* Process features of all attributes of a message, i.e. - text, intent and response inside the respective component itself. For e.g. - intent of a message is now tokenized inside the tokenizer itself.

* Deprecate `as_markdown` and `as_json` in favour of `nlu_as_markdown` and `nlu_as_json` respectively.

* pin python-engineio >= 3.9.3

* update python-socketio req to >= 4.3.1

### Bugfixes

* `rasa test nlu` with a folder of configuration files

* `MappingPolicy` standard featurizer is set to `None`

* Removed `text` parameter from send_attachment function in slack.py to avoid duplication of text output to slackbot

* server `/status` endpoint reports status when an NLU-only model is loaded

### Deprecations and Removals

* Removed `--report` argument from `rasa test nlu`. All output files are stored in the `--out` directory.

## [1.2.12] - 2019-10-16

### Features

* Support for transit encryption with Redis via `use_ssl: True` in the tracker store config in endpoints.yml

## [1.2.11] - 2019-10-09

### Features

* Support for passing a CA file for SSL certificate verification via the
  –ssl-ca-file flag

## [1.2.10] - 2019-10-08

### Features

* Added support for RabbitMQ TLS authentication. The following environment variables
  need to be set:
  `RABBITMQ_SSL_CLIENT_CERTIFICATE` - path to the SSL client certificate (required)
  `RABBITMQ_SSL_CLIENT_KEY` - path to the SSL client key (required)
  `RABBITMQ_SSL_CA_FILE` - path to the SSL CA file (optional, for certificate
  verification)
  `RABBITMQ_SSL_KEY_PASSWORD` - SSL private key password (optional)

* Added ability to define the RabbitMQ port using the `port` key in the
  `event_broker` endpoint config.

## [1.2.9] - 2019-09-17

### Bugfixes

* Correctly pass SSL flag values to x CLI command (backport of

## [1.2.8] - 2019-09-10

### Bugfixes

* SQL tracker events are retrieved ordered by timestamps. This fixes interactive
  learning events being shown in the wrong order. Backport of `1.3.2` patch
  (PR #4427).

## [1.2.7] - 2019-09-02

### Bugfixes

* Added `query` dictionary argument to `SQLTrackerStore` which will be appended
  to the SQL connection URL as query parameters.

## [1.2.6] - 2019-09-02

### Bugfixes

* fixed bug that occurred when sending template `elements` through a channel that doesn't support them

## [1.2.5] - 2019-08-26

### Features

* SSL support for `rasa run` command. Certificate can be specified using
  `--ssl-certificate` and `--ssl-keyfile`.

### Bugfixes

* made default augmentation value consistent across repo

* `'/restart'` will now also restart the bot if the tracker is paused

## [1.2.4] - 2019-08-23

### Bugfixes

* the `SocketIO` input channel now allows accesses from other origins
  (fixes `SocketIO` channel on Rasa X)

## [1.2.3] - 2019-08-15

### Improvements

* messages with multiple entities are now handled properly with e2e evaluation

* `data/test_evaluations/end_to_end_story.md` was re-written in the
  restaurantbot domain

## [1.2.3] - 2019-08-15

### Improvements

* messages with multiple entities are now handled properly with e2e evaluation

* `data/test_evaluations/end_to_end_story.md` was re-written in the restaurantbot domain

### Bugfixes

* Free text input was not allowed in the Rasa shell when the response template
  contained buttons, which has now been fixed.

## [1.2.2] - 2019-08-07

### Bugfixes

* `UserUttered` events always got the same timestamp

## [1.2.1] - 2019-08-06

### Features

* Docs now have an `EDIT THIS PAGE` button

### Bugfixes

* `Flood control exceeded` error in Telegram connector which happened because the
  webhook was set twice

## [1.2.0] - 2019-08-01

### Features

* add root route to server started without `--enable-api` parameter

* add `--evaluate-model-directory` to `rasa test core` to evaluate models
  from `rasa train core -c <config-1> <config-2>`

* option to send messages to the user by calling
  `POST /conversations/{conversation_id}/execute`

### Improvements

* `Agent.update_model()` and `Agent.handle_message()` now work without needing to set a domain
  or a policy ensemble

* Update pytype to `2019.7.11`

* new event broker class: `SQLProducer`. This event broker is now used when running locally with
  Rasa X

* API requests are not longer logged to `rasa_core.log` by default in order to avoid
  problems when running on OpenShift (use `--log-file rasa_core.log` to retain the
  old behavior)

* `metadata` attribute added to `UserMessage`

### Bugfixes

* `rasa test core` can handle compressed model files

* rasa can handle story files containing multi line comments

* template will retain { if escaped with {. e.g. {{“foo”: {bar}}} will result in {“foo”: “replaced value”}

## [1.1.8] - 2019-07-25

### Features

* `TrainingFileImporter` interface to support customizing the process of loading
  training data

* fill slots for custom templates

### Improvements

* `Agent.update_model()` and `Agent.handle_message()` now work without needing to set a domain
  or a policy ensemble

* update pytype to `2019.7.11`

### Bugfixes

* interactive learning bug where reverted user utterances were dumped to training data

* added timeout to terminal input channel to avoid freezing input in case of server
  errors

* fill slots for image, buttons, quick_replies and attachments in templates

* `rasa train core` in comparison mode stores the model files compressed (`tar.gz` files)

* slot setting in interactive learning with the TwoStageFallbackPolicy

## [1.1.7] - 2019-07-18

### Features

* added optional pymongo dependencies `[tls, srv]` to `requirements.txt` for better mongodb support

* `case_sensitive` option added to `WhiteSpaceTokenizer` with `true` as default.

### Bugfixes

* validation no longer throws an error during interactive learning

* fixed wrong cleaning of `use_entities` in case it was a list and not `True`

* updated the server endpoint `/model/parse` to handle also messages with the intent prefix

* fixed bug where “No model found” message appeared after successfully running the bot

* debug logs now print to `rasa_core.log` when running `rasa x -vv` or `rasa run -vv`

## [1.1.6] - 2019-07-12

### Features

* rest channel supports setting a message's input_channel through a field
  `input_channel` in the request body

### Improvements

* recommended syntax for empty `use_entities` and `ignore_entities` in the domain file
  has been updated from `False` or `None` to an empty list (`[]`)

### Bugfixes

* `rasa run` without `--enable-api` does not require a local model anymore

* using `rasa run` with `--enable-api` to run a server now prints
  “running Rasa server” instead of “running Rasa Core server”

* actions, intents, and utterances created in `rasa interactive` can no longer be empty

## [1.1.5] - 2019-07-10

### Features

* debug logging now tells you which tracker store is connected

* the response of `/model/train` now includes a response header for the trained model filename

* `Validator` class to help developing by checking if the files have any errors

* project's code is now linted using flake8

* `info` log when credentials were provided for multiple channels and channel in
  `--connector` argument was specified at the same time

* validate export paths in interactive learning

### Improvements

* deprecate `rasa.core.agent.handle_channels(...)\`. Please use \`\`rasa.run(...)`
  or `rasa.core.run.configure_app` instead.

* `Agent.load()` also accepts `tar.gz` model file

### Deprecations and Removals

* revert the stripping of trailing slashes in endpoint URLs since this can lead to
  problems in case the trailing slash is actually wanted

* starter packs were removed from Github and are therefore no longer tested by Travis script

### Bugfixes

* all temporal model files are now deleted after stopping the Rasa server

* `rasa shell nlu` now outputs unicode characters instead of `\\uxxxx` codes

* fixed PUT /model with model_server by deserializing the model_server to
  EndpointConfig.

* `x in AnySlotDict` is now `True` for any `x`, which fixes empty slot warnings in
  interactive learning

* `rasa train` now also includes NLU files in other formats than the Rasa format

* `rasa train core` no longer crashes without a `--domain` arg

* `rasa interactive` now looks for endpoints in `endpoints.yml` if no `--endpoints` arg is passed

* custom files, e.g. custom components and channels, load correctly when using
  the command line interface

* `MappingPolicy` now works correctly when used as part of a PolicyEnsemble

## [1.1.4] - 2019-06-18

### Features

* unfeaturize single entities

* added agent readiness check to the `/status` resource

### Improvements

* removed leading underscore from name of '_create_initial_project' function.

### Bugfixes

* fixed bug where facebook quick replies were not rendering

* take FB quick reply payload rather than text as input

* fixed bug where training_data path in metadata.json was an absolute path

## [1.1.3] - 2019-06-14

### Bugfixes

* fixed any inconsistent type annotations in code and some bugs revealed by
  type checker

## [1.1.2] - 2019-06-13

### Bugfixes

* fixed duplicate events appearing in tracker when using a PostgreSQL tracker store

## [1.1.1] - 2019-06-13

### Bugfixes

* fixed compatibility with Rasa SDK

* bot responses can contain `custom` messages besides other message types

## [1.1.0] - 2019-06-13

### Features

* nlu configs can now be directly compared for performance on a dataset
  in `rasa test nlu`

### Improvements

* update the tracker in interactive learning through reverting and appending events
  instead of replacing the tracker

* `POST /conversations/{conversation_id}/tracker/events` supports a list of events

### Bugfixes

* fixed creation of `RasaNLUHttpInterpreter`

* form actions are included in domain warnings

* default actions, which are overriden by custom actions and are listed in the
  domain are excluded from domain warnings

* SQL `data` column type to `Text` for compatibility with MySQL

* non-featurizer training parameters don't break SklearnPolicy anymore

## [1.0.9] - 2019-06-10

### Improvements

* revert PR #3739 (as this is a breaking change): set `PikaProducer` and
  `KafkaProducer` default queues back to `rasa_core_events`

## [1.0.8] - 2019-06-10

### Features

* support for specifying full database urls in the `SQLTrackerStore` configuration

* maximum number of predictions can be set via the environment variable
  `MAX_NUMBER_OF_PREDICTIONS` (default is 10)

### Improvements

* default `PikaProducer` and `KafkaProducer` queues to `rasa_production_events`

* exclude unfeaturized slots from domain warnings

### Bugfixes

* loading of additional training data with the `SkillSelector`

* strip trailing slashes in endpoint URLs

## [1.0.7] - 2019-06-06

### Features

* added argument `--rasa-x-port` to specify the port of Rasa X when running Rasa X locally via `rasa x`

### Bugfixes

* slack notifications from bots correctly render text

* fixed usage of `--log-file` argument for `rasa run` and `rasa shell`

* check if correct tracker store is configured in local mode

## [1.0.6] - 2019-06-03

### Bugfixes

* fixed backwards incompatible utils changes

## [1.0.5] - 2019-06-03

### Bugfixes

* fixed spacy being a required dependency (regression)

## [1.0.4] - 2019-06-03

### Features

* automatic creation of index on the `sender_id` column when using an SQL
  tracker store. If you have an existing data and you are running into performance
  issues, please make sure to add an index manually using
  `CREATE INDEX event_idx_sender_id ON events (sender_id);`.

### Improvements

* NLU evaluation in cross-validation mode now also provides intent/entity reports,
  confusion matrix, etc.

## [1.0.3] - 2019-05-30

### Bugfixes

* non-ascii characters render correctly in stories generated from interactive learning

* validate domain file before usage, e.g. print proper error messages if domain file
  is invalid instead of raising errors

## [1.0.2] - 2019-05-29

### Features

* added `domain_warnings()` method to `Domain` which returns a dict containing the
  diff between supplied {actions, intents, entities, slots} and what's contained in the
  domain

### Bugfixes

* fix lookup table files failed to load issues/3622

* buttons can now be properly selected during cmdline chat or when in interactive learning

* set slots correctly when events are added through the API

* mapping policy no longer ignores NLU threshold

* mapping policy priority is correctly persisted

## [1.0.1] - 2019-05-21

### Bugfixes

* updated installation command in docs for Rasa X

## [1.0.0] - 2019-05-21

### Features

* added arguments to set the file paths for interactive training

* added quick reply representation for command-line output

* added option to specify custom button type for Facebook buttons

* added tracker store persisting trackers into a SQL database
  (`SQLTrackerStore`)

* added rasa command line interface and API

* Rasa  HTTP training endpoint at `POST /jobs`. This endpoint
  will train a combined Rasa Core and NLU model

* `ReminderCancelled(action_name)` event to cancel given action_name reminder
  for current user

* Rasa HTTP intent evaluation endpoint at `POST /intentEvaluation`.
  This endpoints performs an intent evaluation of a Rasa model

* option to create template for new utterance action in `interactive learning`

* you can now choose actions previously created in the same session
  in `interactive learning`

* add formatter 'black'

* channel-specific utterances via the `- "channel":` key in utterance templates

* arbitrary json messages via the `- "custom":` key in utterance templates and
  via `utter_custom_json()` method in custom actions

* support to load sub skills (domain, stories, nlu data)

* support to select which sub skills to load through `import` section in
  `config.yml`

* support for spaCy 2.1

* a model for an agent can now also be loaded from a remote storage

* log level can be set via environment variable `LOG_LEVEL`

* add `--store-uncompressed` to train command to not compress Rasa model

* log level of libraries, such as tensorflow, can be set via environment variable `LOG_LEVEL_LIBRARIES`

* if no spaCy model is linked upon building a spaCy pipeline, an appropriate error message
  is now raised with instructions for linking one

### Improvements

* renamed all CLI parameters containing any `_` to use dashes `-` instead (GNU standard)

* renamed `rasa_core` package to `rasa.core`

* for interactive learning only include manually annotated and ner_crf entities in nlu export

* made `message_id` an additional argument to `interpreter.parse`

* changed removing punctuation logic in `WhitespaceTokenizer`

* `training_processes` in the Rasa NLU data router have been renamed to `worker_processes`

* created a common utils package `rasa.utils` for nlu and core, common methods like `read_yaml` moved there

* removed `--num_threads` from run command (server will be asynchronous but
  running in a single thread)

* the `_check_token()` method in `RasaChat` now authenticates against `/auth/verify` instead of `/user`

* removed `--pre_load` from run command (Rasa NLU server will just have a maximum of one model and that model will be
  loaded by default)

* changed file format of a stored trained model from the Rasa NLU server to `tar.gz`

* train command uses fallback config if an invalid config is given

* test command now compares multiple models if a list of model files is provided for the argument `--model`

* Merged rasa.core and rasa.nlu server into a single server. See swagger file in `docs/_static/spec/server.yaml` for
  available endpoints.

* `utter_custom_message()` method in rasa_core_sdk has been renamed to `utter_elements()`

* updated dependencies. as part of this, models for spacy need to be reinstalled
  for 2.1 (from 2.0)

* make sure all command line arguments for `rasa test` and `rasa interactive` are actually used, removed arguments
  that were not used at all (e.g. `--core` for `rasa test`)

### Deprecations and Removals

* removed possibility to execute `python -m rasa_core.train` etc. (e.g. scripts in `rasa.core` and `rasa.nlu`).
  Use the CLI for rasa instead, e.g. `rasa train core`.

* removed `_sklearn_numpy_warning_fix` from the `SklearnIntentClassifier`

* removed `Dispatcher` class from core

* removed projects: the Rasa NLU server now has a maximum of one model at a time loaded.

### Bugfixes

* evaluating core stories with two stage fallback gave an error, trying to handle None for a policy

* the `/evaluate` route for the Rasa NLU server now runs evaluation
  in a parallel process, which prevents the currently loaded model unloading

* added missing implementation of the `keys()` function for the Redis Tracker
  Store

* in interactive learning: only updates entity values if user changes annotation

* log options from the command line interface are applied (they overwrite the environment variable)

* all message arguments (kwargs in dispatcher.utter methods, as well as template args) are now sent through to output channels

* utterance templates defined in actions are checked for existence upon training a new agent, and a warning
  is thrown before training if one is missing