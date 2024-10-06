import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Função para plotar os dados de temperatura, permitindo escolher o mês
def plot_map(dataset, title, time_index, month):
    data = dataset.tasmax.isel(time=time_index)  
    fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
    ax.coastlines()
    ax.set_extent([-35, -34.5, -9.5, -8.0], crs=ccrs.PlateCarree())  # Foco na região de Recife
    data.plot(ax=ax, transform=ccrs.PlateCarree(), cmap='YlOrRd', add_colorbar=True)
    plt.title(f'Temperatura Máxima - {title} ({month}) [°C]\nFonte: NASA GISS Climate Model')
    plt.show()

# Função para calcular a média anual de temperatura máxima
def calcular_media_anual(dataset):
    # Calcula a média ao longo do tempo (média anual), ignorando valores NaN
    media_anual = dataset.tasmax.mean(dim='time', skipna=True)
    return media_anual

# Dados obtidos de: NASA GISS Climate Model, GISS-E2-1-G
datasets = {
    "2010": xr.open_dataset('dataset.nasa/histor/tmax/tasmax_mon_GISS-E2-1-G_historical_r1i1p1f2_gn_2010.nc'),
    "2020": xr.open_dataset('dataset.nasa/ssp/tmax/tasmax_mon_GISS-E2-1-G_ssp126_r1i1p1f2_gn_2020.nc'),
    "2024": xr.open_dataset('dataset.nasa/ssp/tmax/tasmax_mon_GISS-E2-1-G_ssp126_r1i1p1f2_gn_2024.nc'),
    "2030 com práticas mitigantes": xr.open_dataset('dataset.nasa/ssp/tmax/tasmax_mon_GISS-E2-1-G_ssp126_r1i1p1f2_gn_2030.nc'),
    "2030 sem práticas mitigantes": xr.open_dataset('dataset.nasa/ssp/tmax/tasmax_mon_GISS-E2-1-G_ssp370_r1i1p1f2_gn_2030.nc'),
}

# SSP1-2.6: Cenário de mitigação com baixas emissões
# SSP3-7.0: Cenário de altas emissões, sem práticas mitigantes


# Meses representativos (Janeiro, Julho, e Dezembro)
meses_representativos = ['Janeiro', 'Julho', 'Dezembro']
indices_meses = [0, 6, 11]  # Índices correspondentes aos meses representativos

# Iterar sobre os datasets e meses representativos
for year, dataset in datasets.items():
    print(f"\nAno: {year}")
    
    # Calcula e exibe a média anual de temperatura máxima
    media_anual = calcular_media_anual(dataset)
    
    # Verifica se a média contém valores válidos e imprime
    if not media_anual.isnull().all():  
        print(f"Média Anual de Temperatura Máxima (°C): {media_anual.values.mean()}")
    else:
        print("Os dados estão ausentes ou não estão disponíveis para este ano.")
    
    # Plotar mapas para os meses representativos
    for i, month in zip(indices_meses, meses_representativos):  
        plot_map(dataset, year, i, month)  
