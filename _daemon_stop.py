# based on https://gist.github.com/josephernest/77fdb0012b72ebdf4c9d19d6256a1119.js
def daemon_stop(pid_file):
  # Get the pid from the pidfile
  try:
    pf = open(pid_file,'r')
    pid = int(pf.read().strip())
    pf.close()
  except IOError:
    pid = None

  if not pid:
    log.error(f'pidfile {pid_file} does not exist. Daemon not running?')
    exit(1)

  # Try killing the daemon process
  try:
    for i in range(100):
      os.kill(pid, signal.SIGTERM)
      time.sleep(0.1)
  except OSError as err:
    err = str(err)
    if err.find('No such process') > 0:
      if os.path.exists(pid_file):
        os.remove(pid_file)
      exit(0)
    else:
      log.error(f'Error while killing process : {str(err)}')
      exit(1)
  log.error('Error killing process : timeout')
  exit(1)

