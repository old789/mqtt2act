def autoconvert(val):
  try:
    return(int(val))
  except ValueError:
    pass

  try:
    return(float(val))
  except ValueError:
    return(str(val))

