import pandas as pd
import numpy as np
 
 
def _clean_unitprice(val):
    if pd.isna(val):
        return np.nan
    s = str(val).replace(',', '').strip()
    try:
        return float(s)
    except Exception:
        return np.nan
 
 
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.strip()
 
    # Quantity -> numeric
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(0).astype(int)
 
    # UnitPrice: remove thousands separators and convert
    df['UnitPrice'] = df['UnitPrice'].apply(_clean_unitprice)
 
    # Treat non-positive prices as missing
    df.loc[df['UnitPrice'] <= 0, 'UnitPrice'] = pd.NA
 
    # Normalize names and product descriptions
    if 'ProductName' in df.columns:
        df['ProductName'] = df['ProductName'].astype(str).str.replace(',', ' ', regex=False).str.strip()
 
    # Fill missing identifiers/regions
    df['Region'] = df['Region'].fillna('Unknown')
    df['CustomerID'] = df['CustomerID'].fillna('Unknown')
 
    # Drop rows missing critical IDs
    df = df.dropna(subset=['TransactionID', 'ProductID'])
 
    # Compute TotalPrice
    df['TotalPrice'] = df['Quantity'] * pd.to_numeric(df['UnitPrice'], errors='coerce').fillna(0)
 
    return df
 
def upload_results(df, endpoint_url: str):
    """Placeholder: upload dataframe `df` to a remote endpoint.
 
    Not implemented in this scaffold.
    """
    raise NotImplementedError("API upload not configured")
 
