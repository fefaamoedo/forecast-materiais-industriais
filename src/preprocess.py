import pandas as pd


def load_and_prepare_data(file_path: str) -> pd.DataFrame:
    """
    Carrega a base CSV, valida colunas e cria um índice temporal por material.
    """
    df = pd.read_csv(file_path)

    required_columns = [
        "data",
        "material",
        "categoria",
        "consumo_real",
        "estoque",
        "entrada_prevista",
    ]

    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Colunas ausentes no CSV: {missing}")

    df["data"] = pd.to_datetime(df["data"])
    df = df.sort_values(["material", "data"]).reset_index(drop=True)
    df["periodo_idx"] = df.groupby("material").cumcount() + 1

    return df
