
mqtt_host = ''
mqtt_port = 0
mqtt_user = ''
mqtt_passwd = ''
mqtt_subscribes = []
mqtt_handlers = {}
mqtt_translations = {}
rrd_path = ''
tlg = []
user = ''
group = ''

pid_file_name = 'daemon.pid'
run_folder = ''
prog_ident = os.path.basename(sys.argv[0]).rstrip('.py')
stay_foreground = False
msg_aqua_threshold_high_not_sended = True
msg_aqua_threshold_low_not_sended = True

if __name__ == '__main__':
  parse_args(sys.argv[1:])

  if os.path.exists(config.config):
    exec(open(config.config).read())
  else:
    print(f'Config file "{config.config}" not found', file=sys.stderr)
    exit(1)
  run_folder = rrd_path

  if config.kill:
    daemon_stop(pid_file)
    exit(0)

  init()
  connect()

  daemon = Daemonize(app=prog_ident, pid=pid_file, action=loop, foreground=stay_foreground, chdir=run_folder, user=user, group=group)
  daemon.start()
