# Update rrd file with a given value
# The default timestamp, N, means 'now'
def update_rrd(filename, value, timestamp='N'):
  global rrd_path
  filename = os.path.join(rrd_path, filename + '.rrd')
  if os.path.exists(filename):
    if config.dry_run:
      return
    rrdtool.update(filename, timestamp+':'+str(float(value)))
  else:
    log.error(f'File {filename} does not exists')

