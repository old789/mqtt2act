# Update rrd file with a given value
# The default timestamp, N, means 'now'
def update_rrd(filename, value, timestamp='N'):
  global rrd_path
  filename = os.path.join(rrd_path, filename + '.rrd')
  if not os.path.exists(filename):
    log.error(f'File {filename} does not exists')
    return
  if config.dry_run:
    return
  upd = timestamp+':'+str(float(value))
  log.debug(f'Updating RRD {filename} with data {upd}')
  try:
    rrdtool.update(filename, upd)
  except ProgrammingError as err:
    log.error(f'Can\'t update RRD {filename} because programming error "{err}"')
  except OperationalError as err:
    log.error(f'Can\'t update RRD {filename} because operational error "{err}"')

