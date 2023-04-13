# Setup Kafka broker with SASL_PLAIN and TLS bound to localhost

This directory contains `docker-compose.yml` along with pre-generated certificates for TLS bound to IP `localhost`.

## Description of files in this directory
* `docker-compose.yml` - docker compose file with Kafka and Zookeeper containers
* `server.keystore.jks` - keystore with server certificates and CA certificate
* `ca-cert` - CA (Certificate Authority) certificate (used to sign the server certificate), it must be imported into the keystore as a trusted certificate. 
Client should also import this certificate to verify the identity of the Kafka broker.
* `ca-key` - CA private key (used to generate CA certificate `ca-cert`)
* `cert-request` - certificate request for the broker, it must be signed by the CA before it can be used
* `signed-server-cert` - signed certificate for the broker, it must be imported into the keystore
* `ssl_keystore_password` - file containing the password for the keystore
* `ssk_key_password` - file containing the password for the CA private key, used to unlock the CA certificate
* `broker_jaas.conf` - JAAS configuration file for the broker, contains usernames and passwords a client can use to authenticate

## How to generate certificates for TLS bound to DNS localhost
First we need to produce certificates for the Kafka brokers and store them in the server's keystore.
We create a certificate authority (CA), also known as root certificate, 
and use it to sign the certificate request for the Kafka broker.
Kafka broker will send its signed certificate to the client. 
Client will use the CA certificate to verify the identity of the Kafka broker.

You can create the certificates and store them in the keystore using the following commands:
```shell
# Create private and public key (public key is usually reffered to as Certificate Authority's certificate or CA certificate)
openssl req -x509 -newkey rsa:4096 -keyout ca-key -out ca-cert -days 365 -nodes -subj '/CN=localhost/OU=Atom/O=Rasa/L=Berlin/ST=Germany/C=GE' -passin pass:123456 -passout pass:123456

# Create server keystore protected with storepass and keypass
keytool -dname "CN=localhost,OU=Atom,O=Rasa,L=Berlin,S=Germany,C=GE" -keystore server.keystore.jks -alias localhost -validity 365 -genkey -keyalg RSA -storetype pkcs12 -ext SAN=IP:localhost -storepass 123456 -keypass 123456

# Create a certificate request
keytool -keystore server.keystore.jks -alias localhost -certreq -file cert-request -storepass 123456 -keypass 123456 -ext "SAN=IP:localhost"

# Sign the certificate request
openssl x509 -req -CA ca-cert -CAkey ca-key -in cert-request -out signed-server-cert -days 365 -CAcreateserial -passin pass:123456

# Import CA certificate into keystore
# It will be used to decrypt (unseal) the signed certificate sent by the Kafka broker
keytool -keystore server.keystore.jks -alias CARoot -import -file ca-cert -storepass 123456 -keypass 123456
# Import signed certificate into keystore
keytool -noprompt -keystore server.keystore.jks -alias localhost -import -file signed-server-cert -storepass 123456 -keypass 123456 -ext "SAN=DNS:localhost"
```