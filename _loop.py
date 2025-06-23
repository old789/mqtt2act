def loop():
  # Blocking call that processes network traffic, dispatches callbacks and
  # handles reconnecting.
  # Other loop*() functions are available that give a threaded interface and a
  # manual interface.
  client.loop_forever()

