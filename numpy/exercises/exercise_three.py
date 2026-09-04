import numpy as np
import pandas as pd

# NASA Exoplanet Archive — TAP API, no login required
# Returns confirmed exoplanet composite parameters as CSV
TAP = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync'
QUERY = (
    '?query=select+pl_name,pl_masse,pl_rade,pl_orbper,'
    'pl_orbsmax,pl_orbeccen,st_teff,st_rad,st_mass,'
    'st_lum,sy_dist,disc_year'
    '+from+pscomppars'
    '+where+pl_masse+is+not+null'
    '+and+pl_rade+is+not+null'
    '&format=csv'
)
df_exo = pd.read_csv(TAP + QUERY)

# Strip any comment rows NASA prepends (start with '#')
df_exo = df_exo[~df_exo.iloc[:, 0].astype(str).str.startswith('#')]
df_exo = df_exo.reset_index(drop=True)

# Convert key columns to NumPy arrays — NaNs preserved as np.nan
mass   = df_exo['pl_masse'].to_numpy(dtype=float)       # planet mass (Earth masses)
radius = df_exo['pl_rade'].to_numpy(dtype=float)        # planet radius (Earth radii)
period = df_exo['pl_orbper'].to_numpy(dtype=float)      # orbital period (days)
sma    = df_exo['pl_orbsmax'].to_numpy(dtype=float)     # semi-major axis (AU)
ecc    = df_exo['pl_orbeccen'].to_numpy(dtype=float)    # orbital eccentricity
t_eff  = df_exo['st_teff'].to_numpy(dtype=float)        # host star temperature (K)
st_rad = df_exo['st_rad'].to_numpy(dtype=float)         # host star radius (solar radii)
st_mas = df_exo['st_mass'].to_numpy(dtype=float)        # host star mass (solar masses)
st_lum = df_exo['st_lum'].to_numpy(dtype=float)         # host star luminosity (log solar)
dist   = df_exo['sy_dist'].to_numpy(dtype=float)        # system distance (parsecs)
yr     = df_exo['disc_year'].to_numpy(dtype=float)      # discovery year


# 11 From the mass array, extract: the first 10 values, the last 10 values, and every 100th value. Print each slice's shape.
print(mass)
print(mass[0:10])
print(mass[-1:-11:-1])
print(mass[::100])

# 12 Stack mass, radius, and period into a 2D array with shape (N, 3) using np.column_stack(). Call it features.
features = np.column_stack((mass, radius, period))

# 13 From features, extract: the entire first row (one planet), the entire second column (all radii), and the sub-matrix rows 50 to 100.
print(features[0])
print([float(row[1]) for row in features])
print(features[50:101:1])


# 14 Use the [:, col] pattern to pull column 0 (masses) back out of features and confirm it equals the original mass array 
# using np.array_equal() on the non-NaN subset.

print(np.array_equal(features[:, 0], mass))


# 15 Simulate a librosa-style operation: treat features as a (3, N) matrix by transposing it with .T. Then extract 'frame 200' as 
# features.T[:, 200] and print its shape — it should be (3,), like slicing one time frame from an MFCC matrix.

features = features.T
print(np.shape(features))

print(np.shape(features[:, 200]))
