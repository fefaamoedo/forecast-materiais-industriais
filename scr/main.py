import os
from preprocess import load_and_prepare_data
from forecast import generate_forecast
from visualize import plot_forecast
from heatmap import gerar_heatmap_risco


def main():
    print("Iniciando projeto...")

    input_file = "../data/consumo_materiais.csv"
    output_dir = "../outputs"

    os.makedirs(output_dir, exist_ok=True)

    df = load_and_prepare_data(input_file)
    df_forecast = generate_forecast(df, forecast_periods=3)

    output_csv = os.path.join(output_dir, "forecast_resultado.csv")
    df_forecast.to_csv(output_csv, index=False, encoding="utf-8-sig")

    plot_forecast(df, df_forecast, output_dir)
    gerar_heatmap_risco(df_forecast, output_dir)

    print("Projeto executado com sucesso.")
    print(f"Arquivo salvo em: {output_csv}")


if __name__ == "__main__":
    main()
