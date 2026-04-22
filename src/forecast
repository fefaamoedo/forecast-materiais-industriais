import pandas as pd


def classificar_risco(estoque: float, consumo: float) -> str:
    """
    Classifica o risco de ruptura com base no estoque projetado
    em relação ao consumo previsto do período.
    """
    if estoque <= 0:
        return "ALTO"
    elif estoque < consumo:
        return "MÉDIO"
    else:
        return "BAIXO"


def generate_forecast(df: pd.DataFrame, forecast_periods: int = 3) -> pd.DataFrame:
    """
    Gera previsão simples por material usando tendência média histórica
    e classifica o risco de ruptura.
    """
    forecast_rows = []

    for material, group in df.groupby("material"):
        group = group.sort_values("data").copy()

        categoria = group["categoria"].iloc[-1]
        estoque_atual = float(group["estoque"].iloc[-1])
        entrada_prevista = float(group["entrada_prevista"].iloc[-1])
        ultimo_consumo = float(group["consumo_real"].iloc[-1])
        ultima_data = group["data"].iloc[-1]

        variacoes = group["consumo_real"].diff().dropna()
        tendencia_media = variacoes.mean() if not variacoes.empty else 0

        estoque_proj = estoque_atual

        for step in range(1, forecast_periods + 1):
            consumo_previsto = max(
                0,
                round(ultimo_consumo + (tendencia_media * step), 2)
            )

            data_futura = ultima_data + pd.DateOffset(months=step)

            estoque_proj = round(
                estoque_proj + entrada_prevista - consumo_previsto,
                2
            )

            status = classificar_risco(estoque_proj, consumo_previsto)

            forecast_rows.append(
                {
                    "data": data_futura,
                    "material": material,
                    "categoria": categoria,
                    "consumo_previsto": consumo_previsto,
                    "estoque_projetado": estoque_proj,
                    "entrada_prevista": entrada_prevista,
                    "status_risco": status,
                }
            )

    return pd.DataFrame(forecast_rows)
