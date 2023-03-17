---
sidebar_label: rasa.core.brokers.kafka
title: rasa.core.brokers.kafka
---
## KafkaEventBroker Objects

```python
class KafkaEventBroker(EventBroker)
```

Kafka event broker.

#### \_\_init\_\_

```python
def __init__(url: Union[Text, List[Text], None],
             topic: Text = "rasa_core_events",
             client_id: Optional[Text] = None,
             partition_by_sender: bool = False,
             sasl_username: Optional[Text] = None,
             sasl_password: Optional[Text] = None,
             sasl_mechanism: Optional[Text] = "PLAIN",
             ssl_cafile: Optional[Text] = None,
             ssl_certfile: Optional[Text] = None,
             ssl_keyfile: Optional[Text] = None,
             ssl_check_hostname: bool = False,
             security_protocol: Text = "SASL_PLAINTEXT",
             **kwargs: Any) -> None
```

Kafka event broker.

**Arguments**:

- `url` - &#x27;url[:port]&#x27; string (or list of &#x27;url[:port]&#x27;
  strings) that the producer should contact to bootstrap initial
  cluster metadata. This does not have to be the full node list.
  It just needs to have at least one broker that will respond to a
  Metadata API Request.
- `topic` - Topics to subscribe to.
- `client_id` - A name for this client. This string is passed in each request
  to servers and can be used to identify specific server-side log entries
  that correspond to this client. Also submitted to `GroupCoordinator` for
  logging with respect to producer group administration.
- `partition_by_sender` - Flag to configure whether messages are partitioned by
  sender_id or not
- `sasl_username` - Username for plain authentication.
- `sasl_password` - Password for plain authentication.
- `sasl_mechanism` - Authentication mechanism when security_protocol is
  configured for SASL_PLAINTEXT or SASL_SSL.
  Valid values are: PLAIN, GSSAPI, OAUTHBEARER, SCRAM-SHA-256,
  SCRAM-SHA-512. Default: `PLAIN`
- `ssl_cafile` - Optional filename of ca file to use in certificate
  verification.
- `ssl_certfile` - Optional filename of file in pem format containing
  the client certificate, as well as any ca certificates needed to
  establish the certificate&#x27;s authenticity.
- `ssl_keyfile` - Optional filename containing the client private key.
- `ssl_check_hostname` - Flag to configure whether ssl handshake
  should verify that the certificate matches the broker&#x27;s hostname.
- `security_protocol` - Protocol used to communicate with brokers.
  Valid values are: PLAINTEXT, SSL, SASL_PLAINTEXT, SASL_SSL.

#### from\_endpoint\_config

```python
@classmethod
async def from_endpoint_config(
    cls,
    broker_config: EndpointConfig,
    event_loop: Optional[AbstractEventLoop] = None
) -> Optional["KafkaEventBroker"]
```

Creates broker. See the parent class for more information.

#### publish

```python
def publish(event: Dict[Text, Any],
            retries: int = 60,
            retry_delay_in_seconds: float = 5) -> None
```

Publishes events.

#### rasa\_environment

```python
@rasa.shared.utils.common.lazy_property
def rasa_environment() -> Optional[Text]
```

Get value of the `RASA_ENVIRONMENT` environment variable.

#### kafka\_error\_callback

```python
def kafka_error_callback(err: "KafkaError") -> None
```

Callback for Kafka errors.

Any exception raised from this callback will be re-raised from the
triggering flush() call.

#### delivery\_report

```python
def delivery_report(err: Exception, msg: "Message") -> None
```

Reports the failure or success of a message delivery.

**Arguments**:

- `err` _KafkaError_ - The error that occurred on None on success.
- `msg` _Message_ - The message that was produced or failed.
