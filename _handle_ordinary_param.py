def handle_ordinary_param(msg):
  if msg.topic in mqtt_translations:
    update_rrd(mqtt_translations[msg.topic], msg.payload)
    log.debug(f'A topic "{msg.topic}" with name "{mqtt_translations[msg.topic]}" received a message "{autoconvert(msg.payload)}"')
  else:
    log.error(f'An untranslated topic "{msg.topic}" received a message "{autoconvert(msg.payload)}"')
  return

