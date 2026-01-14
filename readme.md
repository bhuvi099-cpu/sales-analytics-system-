sales-analytics-system
 
Small analytics scaffold to load, clean, analyze and export sales data.
 
Quick start
 
- Create a virtualenv and install minimal dependencies:
 
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
 
- Run the cleaning pipeline (reads `data/sales_data.txt` and writes a cleaned CSV):
 
```bash
python main.py
```
 
Additional utilities
 
- Analysis: compute summaries and detect duplicates:
 
```bash
python -c "from utils.analyze import run; run()"
```
 
- Exports: generate `by_customer.csv`, `by_product.csv` and (optionally) Parquet:
 
```bash
python -c "from utils.export import run; run()"
```
 
Files and outputs
 
- `main.py`: pipeline runner (read -> clean -> write `output/cleaned.csv`)
- `utils/file_handler.py`: robust read/save helpers (CSV/Parquet support)
- `utils/data_processor.py`: cleaning logic (parse numeric fields, normalize names, compute `TotalPrice`)
- `utils/analyze.py`: generates `output/report.txt` and `output/duplicates.csv`
- `utils/export.py`: writes `output/by_customer.csv` and `output/by_product.csv` (and Parquet when engine available)
- `utils/api_handler.py`: placeholder for remote upload
- `data/sales_data.txt`: input (pipe-delimited)
- `output/`: contains `cleaned.csv`, `report.txt`, `by_customer.csv`, `by_product.csv`, `duplicates.csv`
 
Optional packages
 
- To enable Parquet export install one of:
 
```
pip install pyarrow
```
 
or
 
```
pip install fastparquet
```
 
- To generate plots (not included by default) install:
 
```
pip install matplotlib seaborn
```
 
Notes
 
- The code currently reads the example file `data/sales_data.txt` and writes outputs to `output/`.
- If you want CLI-style flags (input/output paths, enable/disable Parquet or plots), I can add an argument parser to `main.py` — tell me how you'd like the CLI to behave.
 
Troubleshooting
 
- If Parquet export fails, install `pyarrow` or `fastparquet` as shown above.
- If a file is missing, ensure the path is correct or run from the project root.

 
