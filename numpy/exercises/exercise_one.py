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
mass   = df_exo['pl_masse'].to_numpy(dtype=float)   # planet mass (Earth masses)
radius = df_exo['pl_rade'].to_numpy(dtype=float)    # planet radius (Earth radii)
period = df_exo['pl_orbper'].to_numpy(dtype=float)  # orbital period (days)
sma    = df_exo['pl_orbsmax'].to_numpy(dtype=float) # semi-major axis (AU)
ecc    = df_exo['pl_orbeccen'].to_numpy(dtype=float)# orbital eccentricity
t_eff  = df_exo['st_teff'].to_numpy(dtype=float)    # host star temperature (K)
st_rad = df_exo['st_rad'].to_numpy(dtype=float)     # host star radius (solar radii)
st_mas = df_exo['st_mass'].to_numpy(dtype=float)    # host star mass (solar masses)
st_lum = df_exo['st_lum'].to_numpy(dtype=float)     # host star luminosity (log solar)
dist   = df_exo['sy_dist'].to_numpy(dtype=float)    # system distance (parsecs)
yr     = df_exo['disc_year'].to_numpy(dtype=float)  # discovery year

exo_array = [
    mass,
    radius,
    period,
    sma,
    ecc,
    t_eff,
    st_rad,
    st_mas,
    st_lum,
    dist,
    yr
]

confirm = 0

# 2, 3 & 4
for column in exo_array:
    print("------------------------------------------------------------------------|")
    print(f"Column: {column}")
    print(f"Dimensions: {column.ndim} Shape: {column.shape} Size: {column.size} Type: {column.dtype}")
    print(f"NaN count: {np.sum(np.isnan(column))}")
    print(f"Percentage missing: {(np.sum(np.isnan(column))) / column.size * 100}")
    
    if (len(exo_array[0]) == exo_array[0].shape[0] and len(exo_array[0]) == exo_array[0].size):
        print("Length, Shape and Size are the same.")
    else:
        print("Length, Shape and Size are NOT the same.")
        confirm = confirm + 1
        
    print("------------------------------------------------------------------------|\n\n")

print(f"Confirm: {not bool(confirm)}")

# 5

print(dist)
new_dist = dist.astype(np.int32) # you need to store it!
print(new_dist)