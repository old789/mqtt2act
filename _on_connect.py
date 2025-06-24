def on_connect(client, userdata, flags, rc, properties=None):
  log.info(f'Connected with result code "{rc}"')
  for s in mqtt_subscribes:
    log.debug(f'Subscribing to {s}')
    client.subscribe(s)

