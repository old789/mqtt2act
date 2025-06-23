def send_notification(token, chat, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    params = {'chat_id': chat, 'text': text, 'parse_mode': 'HTML'}
    if config.dry_run:
      return
    response = requests.post(url, data=params)
    if not response.ok:
      log.error(f'Telegram server return HTTP response code {response.status_code} ("{response.reason}")')
    return

