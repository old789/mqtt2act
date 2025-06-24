def init_logging():
  global log

  logging.logProcesses = True
  logging.logThreads = False
  logging.logMultiProcessing = False
  logging._srcFile = None

  log = logging.getLogger(prog_ident)

  if config.debug:
    log.setLevel(logging.DEBUG)
    h = logging.StreamHandler(stream=sys.stderr)
    f = logging.Formatter('%(asctime)s %(levelname)-8.8s %(name)s: %(message)s', '%H:%M:%S')
  else:
    log.setLevel(logging.INFO if not config.verbose else logging.DEBUG)
    h = logging.handlers.SysLogHandler(address='/var/run/log')
    f = logging.Formatter('%(name)s[%(process)d]: %(message)s')

  h.setFormatter(f)
  log.addHandler(h)

