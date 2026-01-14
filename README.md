# Prix — Gas Price Analysis & Forecasting

**Short description**
A Spark-based project to clean, visualize and model gas prices in France (2022–2024). Includes notebooks to prepare data, visualize weekly and departmental averages, and a simple time-series model for SP98.

---

## Project structure
- `main.ipynb` — primary notebook (project pipeline & analysis)  
- `Notebook/`  
  - `main.ipynb` — auxiliary notebook (additional analysis)  
  - `script_download.py` — data download helper  
- `Data/1-raw/` — raw input CSV files (`Prix*.csv.gz`)  
- `requirements.txt` — Python dependencies  
- `LICENSE` — license file  
- generated outputs: `gas_price_map_<gas_type>.html` (choropleth maps)

---

## Requirements
- Linux / macOS or Windows (WSL)  
- Python 3.8+  
- Apache Spark (local mode OK for small runs)  
- Java (for Spark)
- Recommended: create and activate the virtualenv and run the provided requirements.txt file(e.g., `.env`)

---

## Quick setup & run

Run the downloader before if the data files are not loaded:
- `python Notebook/script_download.py`

1. Activate environment:
   - `source .env/bin/activate`
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Launch Jupyter:
   - `jupyter lab` (or `jupyter notebook`)
4. Open `main.ipynb` and run cells top-to-bottom



---

## Notes / Tips
The notebooks create a SparkSession with increased driver memory settings if you run into resource issues. Ensure Java + Spark are available on your PATH.

- Choropleth maps are saved as `gas_price_map_<gas_type>.html`. You can open it via the terminal. 
- The pipeline aggregates prices by department to avoid high-cardinality station features.
- Visualizations use weekly aggregation and include price index plots for each gas type.

---

## Usage examples
- Explore weekly trends: run the visualization cells in `main.ipynb`.  
- Train & evaluate model: run the model pipeline cells to reproduce RMSE and forecasts.  
- Generate department maps: run the mapping cells (requires internet to fetch GeoJSON).

---

## Contributing & Contact
- Open an issue or PR with improvements or bugfixes.  
- For questions, use the repository issues.

---

## License
See `LICENSE`.

---
