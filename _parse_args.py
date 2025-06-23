# Parse command line args ###and load config file
def parse_args(args):
  global config
  parser = argparse.ArgumentParser()
  parser.add_argument("-v", "--verbose", help="Verbose", \
                        default=False, action='store_true')
  parser.add_argument("-n", "--dry-run", help="dry run, do not update .rrd files", \
                        default=False, action='store_true')
  parser.add_argument("-i", "--id", help="MQTT Client ID", \
                        default='mqtt2act', type=str)
  parser.add_argument("-c", "--config", help="Config file", \
                        default='mqtt2act.conf', type=str)
  config = parser.parse_args(args)

