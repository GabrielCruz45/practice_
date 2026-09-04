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


# Reuse boilerplate from Exercise 01
# The yr array (discovery years) is key here:

# Year axis for the histogram you'll build
year_range = np.arange(1995, 2025)              # shape (30,)
counts     = np.zeros(len(year_range))          # shape (30,), all 0.0




# 6 Create a 1D array of 50 evenly-spaced values between 0 and 1 using np.linspace(). Print the first and last three values.

special_array = np.array(np.linspace(0, 1))
print(special_array)
print(special_array[0:3])
print(special_array[-1:-4:-1])
print(np.shape(special_array))
print(np.ndim(special_array))

# 7 Create an integer array from 1 to 500 in steps of 5 using np.arange(). Print its shape and last value.
integer_array = np.array(np.arange(1, 500, 5, dtype=int))
print(integer_array)
print(integer_array[0])
print(integer_array[-1])

# 8 Create a zero-filled array with the same shape as mass using np.zeros_like(). Confirm shape and dtype match.
zero_shape = np.zeros_like(mass)
print(zero_shape)

# 9 Use np.full() to create an array of 100 elements all set to np.nan. This is the pattern for pre-allocating a result buffer.
full_arr = np.full((3,4), np.nan)
print(full_arr)


# 10 Simulate a 'number of exoplanets discovered per year' array: use np.arange(1995, 2025) as year labels and np.zeros(30) as a count buffer. 
# Then fill counts by iterating over the yr array from the boilerplate.

exoplanets_discovered_by_year = np.array(counts, dtype=int)

for year in yr:
    if int(year) in year_range:
        exoplanets_discovered_by_year[int(year) - 1995] = exoplanets_discovered_by_year[int(year) - 1995] + 1       
        
print(exoplanets_discovered_by_year)



        