import pandas as pd
from pathlib import Path
from typing import Optional
 
 
def load_data(path: str, sep: Optional[str] = '|', dtype: Optional[dict] = None, **kwargs):
    """Load a delimited file into a DataFrame.
 
    - If `sep` is None, the function will try to sniff a delimiter from the header line.
    - `dtype` can be used to pass a dict of column dtypes; by default reads all as `str`.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Data file not found: {path}")
 
    if sep is None:
        # Simple delimiter sniffing from the first line
        encoding = kwargs.get('encoding', 'utf-8')
        with p.open('r', encoding=encoding, errors='ignore') as f:
            header = f.readline()
        if '|' in header:
            sep = '|'
        elif ',' in header:
            sep = ','
        elif '\t' in header:
            sep = '\t'
        else:
            sep = ','
 
    return pd.read_csv(p, sep=sep, dtype=dtype or str, **kwargs)
 
 
def save_data(df: pd.DataFrame, path: str, format: str = 'csv', index: bool = False, **kwargs):
    """Save DataFrame to `path` in `csv` or `parquet` format.
 
    - Ensures parent directories exist before writing.
    - For Parquet export, requires `pyarrow` or `fastparquet` installed.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
 
    fmt = format.lower()
    if fmt == 'csv':
        df.to_csv(p, index=index, **kwargs)
    elif fmt in ('parquet', 'pq'):
        try:
            df.to_parquet(p, index=index, **kwargs)
        except Exception as e:
            raise RuntimeError("Parquet write failed; install 'pyarrow' or 'fastparquet'.") from e
    else:
        raise ValueError(f"Unsupported format: {format}")
