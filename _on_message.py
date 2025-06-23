# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
  if msg.topic in mqtt_handlers:
    mqtt_handlers[msg.topic](msg)
  else:
    handle_ordinary_param(msg)

