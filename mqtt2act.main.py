
mqtt_host = ''
mqtt_port = 0
mqtt_user = ''
mqtt_passwd = ''
mqtt_subscribes = []
mqtt_handlers = {}
mqtt_translations = {}
rrd_path = ''
tlg = []
exec_user = ''
exec_group = ''

pid_file_name = 'daemon.pid'
run_folder = ''
prog_ident = os.path.basename(sys.argv[0]).rstrip('.py')
#stay_foreground = False
msg_aqua_threshold_high_not_sended = True
msg_aqua_threshold_low_not_sended = True

if __name__ == '__main__':
  parse_args(sys.argv[1:])

  if not os.path.exists(config.config):
    print(f'Config file "{config.config}" not found', file=sys.stderr)
    exit(1)

  exec(open(config.config).read())  # not good, but easy ( I understand risks )
  run_folder = rrd_path
  pid_file = os.path.join(run_folder, pid_file_name)

  if config.kill:
    daemon_stop(pid_file)
    exit(0)

  daemon = Daemonize( app=prog_ident, pid=pid_file, action=loop, foreground=config.debug, \
                      chdir=run_folder, user=exec_user, group=exec_group )
  daemon.start()
