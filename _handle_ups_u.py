def handle_ups_u(msg):
  global topic_state

  tlg_channel = 0
  log.debug(f'Enter topic "{msg.topic}"')
  mode_battery = msg.topic.find('battery/status') > -1
  if msg.topic not in topic_state:
    topic_state[msg.topic] = msg.payload
    log.debug(f'New message in empty topic "{msg.topic}"')
    state_is_ok = 'batteryOk' if mode_battery else 'powerOk'
    if msg.payload.decode('UTF-8') == state_is_ok :
      return
  elif topic_state[msg.topic] == msg.payload:
    log.debug(f'Existing message in topic "{msg.topic}"')
    return

  ups_name = extract_ups_name(msg.topic)
  msg_str = msg.payload.decode('UTF-8')
  txt = f'{ups_name.upper()} battery ' if mode_battery else f'{ups_name.upper()} external power'
  log.debug(f'Processing a message "{msg_str}" from a device "{ups_name}" in a topic "{msg.topic}"')

  info_msg = ''
  if msg_str == 'nopower':
    info_msg = f'\U0000274C\U000026A1 {txt} failed!'
  elif msg_str == 'powerOk':
    info_msg = f'\U00002705\U000026A1 {txt} restored!'
  elif msg_str == 'batteryDischarged':
    info_msg = f'\U0000274C\U0001FAAB {txt} discharged'
  elif msg_str == 'noBattery':
    info_msg = f'\U0000274C\U0001F50B {txt} disconnected'
  elif msg_str == 'batteryLow':
    info_msg = f'\U00002757\U0001FAAB {txt} is low'
  elif msg_str == 'batteryOk':
    info_msg = f'\U00002705\U0001F50B {txt} is good'
  else:
    log.error(f'Unknown message "{msg_str}" in a topic "{msg.topic}"')
    return

  topic_state[msg.topic] = msg.payload
  if len(info_msg) > 0:
    log.info(info_msg)
    send_notification(tlg[tlg_channel]['token'], tlg[tlg_channel]['chat'], info_msg)
  return


