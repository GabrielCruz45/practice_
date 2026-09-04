# Filter arrays by condition without loops — the NumPy skill you'll use most when cleaning librosa output or 
# selecting frames above an energy threshold.

# np.where executes a vectorized operation on your array-like; vectorized -> apply a single operation to an entire dataset (an array or "vector")

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

# stack 2 stats for use
mass_and_radius = np.column_stack((mass, radius))


# Instructions
# 16 Find all planets with mass less than 2 Earth masses using a boolean mask. Print how many there are and their average radius.

# long way
boolean_mask_m_long = mass < 2
mass_less_than_indices = np.where(boolean_mask_m_long)
# print(mass_and_radius[mass_less_than_indices])

# short way
# print(mass_and_radius[np.where(mass < 2)].size)
# print(np.count_nonzero(mass_and_radius[np.where(mass < 2)]))
# print(len(mass_and_radius[np.where(mass < 2)]))

radii = mass_and_radius[mass_less_than_indices, 1]
exos_with_less = np.count_nonzero(boolean_mask_m_long)

print(f"There are {exos_with_less} exoplanets with mass less than 2 times the Earth's.")
print(f"Average radius for these exoplanets: {((np.sum(radii)) / exos_with_less):.2f}")



# 17 Find planets where both mass AND radius are less than 2 (super-Earths). Use the & operator to combine two conditions.
boolean_mask_mr = (mass_and_radius[:, 0] < 2) & (mass_and_radius[:, 1] < 2)
mr_indices = np.where(boolean_mask_mr)

print(type(mass_and_radius[mr_indices]))
mr_indices_arr = np.array(mr_indices[0])

print(len(mr_indices_arr), len(mass_and_radius[mr_indices]))

print(f"""
        Planets where both mass and radius are less than 2; has three columns: [index, mass, radius]:\n
        {np.column_stack((mr_indices_arr, mass_and_radius[mr_indices]))}
""")
     


# 18 Remove all NaN values from the mass array using mass[np.isfinite(mass)]. Compare the length before and after.
print(mass[np.isfinite(mass)])
print(mass.size)
print(mass[np.isfinite(mass)].size)

# 19 Use np.where() to classify planets: return 'small' where radius < 1.6 and 'large' otherwise. Print the first 10 labels.
print(f"""
        \t\t\tIf planet 1.6 < radius of Earth = small, large otherwise; first 100 planets:\n
        {np.where(radius < 1.6, "small", "large")[0:100:1]}
""")


# 20 Find the indices of all planets with orbital period shorter than 1 day (ultra-short period planets) using np.argwhere(). 
# Print how many exist and print the mass array values at those indices.
twenty_indices = np.argwhere(period < 1)
print(f"""
        \t\t\t----Planets with an ultra-short orbital period----\n
        Indices:\n{twenty_indices}\n
        Ultra-short orbital period planet count: {twenty_indices.size}
""")

print(f"List of the mass of these planets:\n{mass[twenty_indices]}")



# --- Build + apply via np.where (mask stays full shape, non-matches get replaced) ---

# 21 Stack `period` and `ecc` into a 2-column array called `period_and_ecc`. Build a mask
# for "eccentric, short-period" planets: eccentricity greater than 0.3 AND orbital period
# less than 100 days. Apply it with np.where(mask[:, None], period_and_ecc, 0).
# Print the match count with mask.sum(), then print result.shape.

period_ecc_stack = np.column_stack((period, ecc))
period_ecc_mask = (period_ecc_stack[:, 0] < 100) & (period_ecc_stack[:, 1] < 0.3)
print(period_ecc_mask.size, period_ecc_mask.sum())
print(period_ecc_mask.shape)

# 22 Build a mask for "Sun-like" host stars: t_eff between 5000 and 6000 K. Both bounds
# are on the SAME column this time, not two different columns — combine them with &.
# Stack `t_eff` and `st_rad` into a 2-column array called `t_eff_and_st_rad`, apply the
# mask with np.where, but replace non-matches with np.nan instead of 0.
# Print how many rows are NOT nan using ~np.isnan(result).any(axis=1).sum()
sun_like_mask = (t_eff > 5000 ) & (t_eff < 6000)
t_eff_and_st_rad = np.stack((t_eff, st_rad))

print(t_eff_and_st_rad.shape)

sun_like_rows, sun_like_columns = t_eff_and_st_rad[np.where(sun_like_mask, t_eff_and_st_rad, np.nan)]
# print(np.isnan(sun_like_result).any(axis=1).sum())



# 23 Build a mask for "unusual, nearby" planets: mass greater than 500 Earth masses OR
# radius greater than 15 Earth radii, AND system distance less than 500 parsecs.
# This needs both `&` and `|` in one expression — get the parentheses right.
# Apply it to `mass_and_radius` with np.where, zero-filling non-matches.


# --- Same masks, applied via boolean indexing (array shrinks to just the matches) ---

# 24 Reuse the exact mask from Exercise 21. Instead of np.where, use boolean indexing:
# period_and_ecc[mask]. Print its shape and compare it directly to Exercise 21's
# result.shape.

# 25 Reuse the exact mask from Exercise 22 (Sun-like host stars). Apply it to a
# DIFFERENT array this time: pull names = df_exo['pl_name'].to_numpy(), then print
# names[mask][:10]. The mask was built from t_eff and st_rad but works on any
# array of the same length — that's the part to notice.