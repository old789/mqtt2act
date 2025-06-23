
mqtt_host = ''
mqtt_port = 0
mqtt_user = ''
mqtt_passwd = ''
mqtt_subscribes = []
mqtt_handlers = {}
mqtt_translations = {}
rrd_path = ''
tlg = []

msg_aqua_threshold_high_not_sended = True
msg_aqua_threshold_low_not_sended = True

if __name__ == '__main__':
  parse_args(sys.argv[1:])

  if os.path.exists(config.config):
    exec(open(config.config).read())
  else:
    print(f'Config file "{config.config}" not found', file=sys.stderr)
    exit(1)

  init()
  connect()

  # Blocking call that processes network traffic, dispatches callbacks and
  # handles reconnecting.
  # Other loop*() functions are available that give a threaded interface and a
  # manual interface.
  client.loop_forever()

