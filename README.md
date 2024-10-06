# ECO(Gee) - Technical Documentation

## 1. Project Overview

**ECO(Gee)** is a gamified app that encourages sustainable actions in Recife, Brazil. Using satellite data from NASA, the app maps zones of greenhouse gas emissions and absorption (CO2), offering rewards to users for practices like tree planting and conscious consumption. ECO(Gee) aims to raise awareness and engage the population in the fight against climate change in a collaborative and enjoyable way.

The project addresses the challenge of creating tools that promote sustainability and environmental actions by providing an interactive interface that encourages people to act in their communities.

## 2. Data Source

### 2.1. Data Source

The data used in the project is extracted from NASA sources, specifically:
- **NEX-DCP30-CMIP6** (NASA Earth Exchange Downscaled Climate Projections): Climate projections that include greenhouse gas (GHG) emissions.
- We use the **GISS-E2-1-G** model to represent future and historical climate change scenarios.
- The dataset: CMS (Carbon Monitoring System), which would be more suitable for focusing on carbon fluxes and monitoring CO₂ emissions and absorption, was unavailable for download during the development of the solution.

#### Scenarios Used:
- **Historical (2010, 2020, 2024)**: Real data to analyze past and current trends.
- **SSP1-2.6 (2030)**: Optimistic scenario with mitigation practices applied, including those available in our app’s gamification system.
- **SSP3-7.0 (2030)**: Pessimistic scenario, without mitigation practices. The year 2030 was chosen due to the global commitment to the UN's 2030 Agenda.

The data is in NetCDF (.nc) format, widely used in scientific data.

### 2.2. Data Preprocessing

The tools used to manipulate and visualize the data include:
- **Xarray** for processing large NetCDF datasets.
- **Cartopy** for geospatial visualization.
- **Matplotlib** for graphical visualization of the results.

## 3. Processing Algorithm

### 3.1. Algorithm Workflow

1. **Data Loading**: We use Xarray to load maximum and minimum temperature data for different years and scenarios.
   ```
   import xarray as xr
   dataset = xr.open_dataset('dataset.nasa/histor/tmax/tasmax_mon_GISS-E2-1-G_historical_r1i1p1f2_gn_2010.nc')
   data = dataset.tasmax.isel(time=0)  # Selects the first month of the year
   ```

2. **Geographical Clipping**: We filter the climate data for the Recife area using specific coordinates.
   ```
   lat_min, lat_max = -9.0, -7.0
   lon_min, lon_max = -36.0, -34.0
   data_recife = data.sel(lat=slice(lat_min, lat_max), lon=slice(lon_min, lon_max))
   ```

3. **Map Visualization**: We use Cartopy and Matplotlib to plot maps, showing temperature variations over the years and scenarios.
   ```
   import matplotlib.pyplot as plt
   import cartopy.crs as ccrs

   plt.figure(figsize=(10, 6))
   ax = plt.axes(projection=ccrs.PlateCarree())
   data_recife.plot(ax=ax, cmap='RdYlBu_r', cbar_kwargs={'label': 'Maximum Temperature [°C]'})
   ax.set_title('Maximum Temperature - 2030 - SSP1-2.6 (Recife)')
   ax.coastlines()
   plt.show()
   ```

### 3.2. App Integration

The system loads and processes the data in the background, displaying visualizations of emission and absorption areas on the app’s map. Users can click on the icons to view more details and participate in sustainable missions.

Depending on the selected scenario (with or without mitigation), the app shows different predictions for 2030, engaging users to adopt more sustainable practices.

## 4. Tools and Libraries Used

- **Xarray (v2024.1.0)**: For NetCDF data processing.
- **Cartopy (v0.20.0)**: For geospatial visualization.
- **Matplotlib (v3.7.1)**: For graph visualization.
- **Python 3.10**: Development environment.
- **NetCDF4 (v1.5.8)**: Interface for NetCDF data manipulation.

## 5. Project Description

**ECO(Gee)** offers an interactive interface that maps CO2 emissions and absorption in Recife, highlighting critical zones and encouraging tree planting and sustainable practices. Gamification is one of the central elements to engage users.

### Functionality:
- **Interactive Map**: Users see a map with emission (red) and absorption (green) icons. By clicking, they can see more details about the area and recommended actions.
- **Gamified Missions**: The app encourages users to complete sustainable missions, like tree planting, with associated rewards.

### Benefits:
- **Awareness**: Increases knowledge about climate change, local impact, and how CO2 emission and absorption zones can interact to bring greater climate balance, integrating it into users' daily lives.
- **Sustainable Actions**: Encourages practices that help mitigate the effects of climate change.
- **Collaborative Impact**: Engages citizens in community actions that have a direct impact on CO2 reduction.

### Tools:
- **Python** for backend and data processing.
- **Leaflet** for frontend and interactive map visualization.

## 6. NASA and Space Agency Partner Data

The data used in the project comes from NASA, specifically the **NEX-DCP30-CMIP6**, with long-term climate projection data and temperature trends.

## 7. References

- **NASA Earth Exchange Downscaled Climate Projections (NEX-DCP30)**.
- **The United Nations in Brazil (https://brasil.un.org/en/sdgs)**.
- **Recife’s Greenhouse Gas Emissions Reduction Plan (https://www2.recife.pe.gov.br/sites/default/files/plano_de_baixo_co2_recife.pdf)**.
- **Xarray**, **Cartopy**, and **Matplotlib** for data processing and visualization.

## 8. User Journey

1. **Registration**: The user registers in the app and sees nearby emission/absorption areas.
2. **Exploration**: They navigate the map and click on icons to view more details of critical zones.
3. **Missions**: The user participates in missions, like tree planting or conscious consumption, earning points.
4. **Rewards**: Accumulated points can be exchanged for discounts at partner companies, ranked in the app based on their commitment to reducing greenhouse gas emissions, or for local tax reductions in partnerships with sustainable companies.

## 9. Scalability

For the future, we plan:
- **Expansion to other cities**: Add more regions to increase the app’s impact.
- **Integration with other climate data sources**: Incorporate data from more satellites and space agencies.
- **Business partnerships**: Establish more partnerships with companies that promote sustainable practices, expanding the rewards system.

## 10. Useful Links

- **Slide Presentation**: [https://drive.google.com/file/d/1fqItzpVACpS99uHzkjwty1puAtyI_gwk/view?usp=drive_link]
- **Figma Screens**: [https://www.figma.com/proto/czuezU1JV0l0ELtQXSwUsP/CO%C2%B2--app-Final?node-id=0-1&t=CRupKxIf7dXRZShR-1]
  
