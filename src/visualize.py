import os
import matplotlib.pyplot as plt
import pandas as pd


def plot_forecast(df_hist: pd.DataFrame, df_forecast: pd.DataFrame, output_dir: str):
    """
    Gera gráficos de barras para demanda e linha para estoque projetado.
    """
    os.makedirs(output_dir, exist_ok=True)

    for material in df_hist["material"].unique():
        hist = df_hist[df_hist["material"] == material].sort_values("data").copy()
        prev = df_forecast[df_forecast["material"] == material].sort_values("data").copy()

        hist_plot = hist[["data", "consumo_real"]].copy()
        hist_plot["tipo"] = "Histórico"
        hist_plot["estoque_projetado"] = None
        hist_plot = hist_plot.rename(columns={"consumo_real": "consumo"})

        prev_plot = prev[["data", "consumo_previsto", "estoque_projetado"]].copy()
        prev_plot["tipo"] = "Previsão"
        prev_plot = prev_plot.rename(columns={"consumo_previsto": "consumo"})

        plot_df = pd.concat([hist_plot, prev_plot], ignore_index=True).sort_values("data")
        plot_df["periodo"] = plot_df["data"].dt.strftime("%m/%Y")

        fig, ax1 = plt.subplots(figsize=(12, 6))

        colors = ["#b0bec5" if t == "Histórico" else "#1e88e5" for t in plot_df["tipo"]]
        ax1.bar(plot_df["periodo"], plot_df["consumo"], color=colors)
        ax1.set_title(f"Demanda e Estoque Projetado - {material}", fontsize=14, fontweight="bold")
        ax1.set_xlabel("Período")
        ax1.set_ylabel("Consumo")
        ax1.tick_params(axis="x", rotation=45)

        ax2 = ax1.twinx()
        prev_only = plot_df[plot_df["tipo"] == "Previsão"]

        ax2.plot(
            prev_only["periodo"],
            prev_only["estoque_projetado"],
            color="#d32f2f",
            marker="o",
            linestyle="--",
            linewidth=2,
            label="Estoque projetado"
        )
        ax2.set_ylabel("Estoque Projetado")

        legend_hist = plt.Line2D([0], [0], color="#b0bec5", lw=8, label="Demanda histórica")
        legend_prev = plt.Line2D([0], [0], color="#1e88e5", lw=8, label="Demanda prevista")
        legend_est = plt.Line2D([0], [0], color="#d32f2f", lw=2, linestyle="--", marker="o", label="Estoque projetado")

        ax1.legend(handles=[legend_hist, legend_prev, legend_est], loc="upper right")

        plt.tight_layout()

        nome_arquivo = material.lower().replace(" ", "_")
        caminho = os.path.join(output_dir, f"{nome_arquivo}_demanda_estoque.png")
        plt.savefig(caminho, dpi=300, bbox_inches="tight")
        plt.close()

        print(f"Gráfico salvo: {caminho}")
