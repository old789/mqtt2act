def on_subscribe(client, userdata, mid, rc, properties=None):
  log.info(f'Subscribed with result code "{rc}"')

