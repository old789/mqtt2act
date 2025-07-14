def handle_aqua_water(msg):
  global msg_aqua_threshold_high_sended, msg_aqua_threshold_low_sended
  threshold_high = 28
  threshold_low = 25
  tlg_channel = 0
  topic_name = 'aquarium_water_t'
  t = float(msg.payload)
  txt = 'Temperature of water in an aquarium'
  info_msg = ''

  update_rrd(topic_name, t)
  log.debug(f'{txt} {t}{chr(0xB0)}')

  if ( t >= threshold_high ):
    if not msg_aqua_threshold_high_sended:
      info_msg = f'\U0001F4C8\U0001F321 {txt} is too high ({t}{chr(0xB0)})!'
      msg_aqua_threshold_high_sended = True
  else:
    if msg_aqua_threshold_high_sended:
      info_msg = f'\U00002705\U0001F321 {txt} back to normal ({t}{chr(0xB0)})!'
      msg_aqua_threshold_high_sended = False

  if ( threshold_low >= t ):
    if not msg_aqua_threshold_low_sended:
      info_msg = f'\U0001F4C9\U0001F321 {txt} is too low ({t}{chr(0xB0)})!'
      msg_aqua_threshold_low_sended = True
  else:
    if msg_aqua_threshold_low_sended:
      info_msg = f'\U00002705\U0001F321 {txt} back to normal ({t}{chr(0xB0)})!'
      msg_aqua_threshold_low_sended = False

  if len(info_msg) > 0:
      log.info(info_msg)
      send_notification(tlg[tlg_channel]['token'], tlg[tlg_channel]['chat'], info_msg)

  return

