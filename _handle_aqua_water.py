def handle_aqua_water(msg):
  global msg_aqua_threshold_high_not_sended, msg_aqua_threshold_low_not_sended
  threshold_high = 28
  threshold_low = 25
  tlg_channel = 1
  topic_name = 'aquarium_water_t'
  t = float(msg.payload)

  if not config.dry_run:
    update_rrd(topic_name, msg.payload)
  log.debug(f'Temperature of water in an aquarium {t}{chr(0xB0)}')

  if ( t >= threshold_high ):
    if msg_aqua_threshold_high_not_sended:
      send_notification(tlg[tlg_channel]['token'], tlg[tlg_channel]['chat'], f'Temperature of water in an aquarium is too high ({t}{chr(0xB0)})!')
      msg_aqua_threshold_high_not_sended = False
  else:
    if not msg_aqua_threshold_high_not_sended:
      send_notification(tlg[tlg_channel]['token'], tlg[tlg_channel]['chat'], f'Temperature of water in an aquarium back to normal ({t}{chr(0xB0)})!')
      msg_aqua_threshold_high_not_sended = True

  if ( threshold_low >= t ):
    if msg_aqua_threshold_low_not_sended:
      send_notification(tlg[tlg_channel]['token'], tlg[tlg_channel]['chat'], f'Temperature of water in an aquarium is too low ({t}{chr(0xB0)})!')
      msg_aqua_threshold_low_not_sended = False
  else:
    if not msg_aqua_threshold_low_not_sended:
      send_notification(tlg[tlg_channel]['token'], tlg[tlg_channel]['chat'], f'Temperature of water in an aquarium back to normal ({t}{chr(0xB0)})!')
      msg_aqua_threshold_low_not_sended = True
  return

