# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc, properties=None):
  log.info(f'Connected with result code "{rc}"')

  # Subscribing in on_connect() means that if we lose the connection and
  # reconnect then subscriptions will be renewed.
  for s in mqtt_subscribes:
    log.debug(f'Subscribing to {s}')
    client.subscribe(s)
  log.info('All subscribed')

