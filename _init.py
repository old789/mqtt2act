# Initialize subsystems according to configs that were loaded
def init():
  global log
  if config.verbose:
    logging.basicConfig(format='%(asctime)s %(levelname)-8.8s %(name)s: %(message)s',
                      datefmt='%H:%M:%S',
                      level=logging.ERROR)

  log = logging.getLogger('mqtt2act')

  if config.verbose:
    log.setLevel(logging.DEBUG)
  else:
    handl = logging.handlers.SysLogHandler(address='/var/run/log')
    log.addHandler(handl)
    log.setLevel(logging.INFO)

