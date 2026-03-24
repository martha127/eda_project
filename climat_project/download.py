import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'format': 'grib',
        'variable': [
            '2m_temperature',
        '2m_dewpoint_temperature',
        '10m_u_component_of_wind',
        '10m_v_component_of_wind',
        'Surface_solar_radiation_downwards',
        'Evaporation',
        'Total_precipitation',
        'Snowfall',
        'Volumetric_soil_water_layer_1',
        'Volumetric_soil_water_layer_2',
        'Volumetric_soil_water_layer_3',
        'Volumetric_soil_water_layer_4',
        'Convective_available_potential_energy',
        ],
        'year': ['2009'],
        'month': [f"{m:02d}" for m in range(1, 13)],
        'day': [f'{i:02d}' for i in range(1, 32)],
        'time': ['00:00','06:00','12:00','18:00'],
        'area': [41.4, -7.75, 39.65, -7.0],
        'grid': [0.25, 0.25],
    },
    'single_levels_portugal_9.grib'
)
