import math

def latlon_to_xyz(lat, lon, alt, lat0, lon0, alt0):
    """
    Convert latitude/longitude/altitude to local Cartesian coordinates (meters)
    relative to a reference origin (lat0, lon0, alt0).

    X → East
    Y → Up
    Z → North
    """
    meters_per_deg = 111_320.0
    lat0_rad = math.radians(lat0)

    x = (lon - lon0) * meters_per_deg * math.cos(lat0_rad)
    z = (lat - lat0) * meters_per_deg
    y = alt - alt0

    return x, y, z
