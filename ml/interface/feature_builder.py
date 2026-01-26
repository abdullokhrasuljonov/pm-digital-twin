import numpy as np
from math import cos, radians, sqrt
from .schema import PMPredictionInput

# =========================
# CONSTANTS (from training)
# =========================

EARTH_LAT_M = 111_320  # meters per degree latitude

# Min–Max values from training
SCALER = {
    "Weighted_3D_distance": (20.5426, 244.1573),
    "Weighted_Height_distance": (-10.2589, 127.5417),
    "Weighted_Lat_diff_m": (-118.4493, 174.6684),
    "Weighted_Lon_diff_m": (-190.6601, 203.9862),
    "Wind_North": (-5.45, 8.53),
    "Wind_East": (-11.21, 6.92),
    "Temperature": (4.51, 13.73),
    "Humidity": (26.08, 38.63),
    "Pressure": (1010.87, 1027.28),
}

IDW_POWER = 2.0


# =========================
# HELPERS
# =========================

def minmax_scale(x, min_val, max_val):
    return (x - min_val) / (max_val - min_val)


def latlon_to_meters(lat_diff, lon_diff, avg_lat):
    lat_m = lat_diff * EARTH_LAT_M
    lon_m = lon_diff * EARTH_LAT_M * cos(radians(avg_lat))
    return lat_m, lon_m


def idw_weighted(values, distances):
    weights = 1.0 / (np.power(distances, IDW_POWER) + 1e-6)
    return np.sum(weights * values) / np.sum(weights)


# =========================
# MAIN FEATURE BUILDER
# =========================

def build_features(data: PMPredictionInput) -> np.ndarray:
    """
    Returns feature vector in EXACT order used during training
    """

    lat_diffs = []
    lon_diffs = []
    height_diffs = []
    dist_3d = []

    avg_lat = data.latitude

    # Loop over activities
    for act in data.activities:
        dlat = data.latitude - act["latitude"]
        dlon = data.longitude - act["longitude"]
        dheight = data.altitude - act.get("altitude", 0.0)

        lat_m, lon_m = latlon_to_meters(dlat, dlon, avg_lat)

        d3d = sqrt(lat_m**2 + lon_m**2 + dheight**2)

        lat_diffs.append(lat_m)
        lon_diffs.append(lon_m)
        height_diffs.append(dheight)
        dist_3d.append(d3d)

    lat_diffs = np.array(lat_diffs)
    lon_diffs = np.array(lon_diffs)
    height_diffs = np.array(height_diffs)
    dist_3d = np.array(dist_3d)

    # IDW aggregation
    weighted_lat = idw_weighted(lat_diffs, dist_3d)
    weighted_lon = idw_weighted(lon_diffs, dist_3d)
    weighted_height = idw_weighted(height_diffs, dist_3d)
    weighted_3d = idw_weighted(dist_3d, dist_3d)

    # Select distance feature by PM type
    if data.pm_type == "pm1":
        main_distance = weighted_3d
        main_key = "Weighted_3D_distance"
    else:
        main_distance = weighted_height
        main_key = "Weighted_Height_distance"

    # =========================
    # Scaling
    # =========================

    features = [
        minmax_scale(main_distance, *SCALER[main_key]),
        minmax_scale(weighted_lat, *SCALER["Weighted_Lat_diff_m"]),
        minmax_scale(weighted_lon, *SCALER["Weighted_Lon_diff_m"]),
        minmax_scale(data.wind_north, *SCALER["Wind_North"]),
        minmax_scale(data.wind_east, *SCALER["Wind_East"]),
        minmax_scale(data.temperature, *SCALER["Temperature"]),
        minmax_scale(data.humidity, *SCALER["Humidity"]),
        minmax_scale(data.pressure, *SCALER["Pressure"]),
    ]

    return np.array([features])
