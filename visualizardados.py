import xarray as xr

dataset_2010 = xr.open_dataset('dataset.nasa/tmax/tasmax_mon_GISS-E2-1-G_historical_r1i1p1f2_gn_2010.nc')
print(dataset_2010)
