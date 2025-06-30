import os
import pandas as pd
import geopandas as gpd

import matplotlib.pyplot as plt

def generate_disease_maps(data_folder, shapefile_path, disease_column, county_column, output_folder):
    """
    Generates maps of disease prevalence by county.

    Args:
        data_folder (str): Path to the folder containing CSV data files.
        shapefile_path (str): Path to the county shapefile (e.g., .shp).
        disease_column (str): Name of the column with disease data.
        county_column (str): Name of the column with county identifiers.
        output_folder (str): Folder to save generated map images.
    """
    os.makedirs(output_folder, exist_ok=True)
    # Load county shapefile
    counties = gpd.read_file(shapefile_path)

    # Process each CSV file in the data folder
    for filename in os.listdir(data_folder):
        if filename.endswith('.csv'):
            data_path = os.path.join(data_folder, filename)
            df = pd.read_csv(data_path)
            # Merge data with shapefile
            merged = counties.merge(df, left_on=county_column, right_on=county_column, how='left')
            # Plot map
            fig, ax = plt.subplots(1, 1, figsize=(10, 8))
            merged.plot(column=disease_column, ax=ax, legend=True, cmap='Reds', missing_kwds={"color": "lightgrey"})
            ax.set_title(f"{disease_column} Map - {filename}")
            ax.axis('off')
            # Save map
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_{disease_column}_map.png")
            plt.savefig(output_path, bbox_inches='tight')
            plt.close(fig)