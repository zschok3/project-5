"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control open time.
       This will be in the same time zone as the brevet start time.
   """
   time = 0
   distances = [1000, 800, 600, 400, 200, 0]
   speeds = [26, 28, 28, 30, 32, 34]

   for i in range(len(distances)):
      if control_dist_km > distances[i]: 
         distance = max(control_dist_km - distances[i], 0)
         time += distance / speeds[i]
         control_dist_km = distances[i]
   return brevet_start_time.shift(hours=time)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An arrow object
    Returns:
       An arrow object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    time = 0
    distances = [1000, 800, 600, 400, 200, 0]
    speeds = [13.333, 11.428, 11.428, 15, 15, 15]

    for i in range(len(distances)):
      if control_dist_km > distances[i]: 
         distance = max(control_dist_km - distances[i], 0)
         time += distance / speeds[i]
         control_dist_km = distances[i]
    return brevet_start_time.shift(hours=time)




