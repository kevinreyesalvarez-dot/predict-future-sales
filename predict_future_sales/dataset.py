"""Carga de los archivos crudos de Kaggle (Predict Future Sales)."""
import pandas as pd

from predict_future_sales.config import RAW_DATA_DIR


def load_raw():
    """Devuelve (sales, items, categories, shops, test) desde data/raw/."""
    sales = pd.read_csv(RAW_DATA_DIR / "sales_train.csv")
    sales["date"] = pd.to_datetime(sales["date"], format="%d.%m.%Y")
    items = pd.read_csv(RAW_DATA_DIR / "items.csv")
    categories = pd.read_csv(RAW_DATA_DIR / "item_categories.csv")
    shops = pd.read_csv(RAW_DATA_DIR / "shops.csv")
    test = pd.read_csv(RAW_DATA_DIR / "test.csv")
    return sales, items, categories, shops, test
