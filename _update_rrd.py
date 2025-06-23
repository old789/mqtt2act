# Update rrd file with a given value
# The default timestamp, N, means 'now'
def update_rrd(filename, value, timestamp='N'):
  global path_rrd
  if config.dry_run:
    return
  filename = os.path.join(path_rrd, filename + '.rrd')
  if os.path.exists(filename):
    rrdtool.update(filename, timestamp+':'+str(float(value)))
  else:
    log.error(f'File {filename} does not esists')

