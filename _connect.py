def connect():
  global client
  client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=config.id, clean_session=True)
  client.on_connect = on_connect
  client.on_message = on_message
  client.on_subscribe = on_subscribe
  client.username_pw_set(mqtt_user, mqtt_passwd)
  client.connect(mqtt_host, mqtt_port, 60)

