# Forecast de Materiais Industriais

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## Sobre o Projeto

Sistema desenvolvido em Python para previsão de consumo de materiais industriais, com foco em apoiar áreas de:

- Planejamento de Produção  
- Supply Chain  
- Compras  
- Gestão de Estoque  
- Prevenção de Rupturas  

A aplicação utiliza dados históricos para projetar consumo futuro, estimar estoque e classificar automaticamente materiais com risco de falta.

---

## Problema de Negócio Resolvido

Em ambientes industriais, decisões de compra tardias podem gerar:

- Paradas de produção  
- Custos emergenciais  
- Compras urgentes  
- Ruptura de estoque  
- Falta de visibilidade futura  

Este projeto antecipa esses cenários por meio de previsões simples e indicadores visuais.

---

## Funcionalidades

- Leitura de base CSV histórica  
- Tratamento e validação dos dados  
- Forecast de consumo por material  
- Projeção de estoque futuro  
- Classificação de risco de ruptura  
- Heatmap executivo de criticidade  
- Gráficos automáticos por material  
- Exportação CSV com resultados

---

## Materiais Simulados

- PEAD  
- PEBD  
- PEBDL  
- ADITIVOS  

---

## Resultados Visuais

### Heatmap de Risco

![Heatmap](outputs/heatmap_risco.png)

### Forecast de Demanda

![Forecast PEBD](outputs/pebd_demanda_estoque.png)

### Forecast Material Crítico

![Forecast Aditivos](outputs/aditivos_demanda_estoque.png)

---

## Lógica de Classificação de Risco

| Situação | Status |
|--------|--------|
| Estoque saudável | BAIXO |
| Estoque menor que 1 período de consumo | MÉDIO |
| Estoque zerado ou negativo | ALTO |

---

## Estrutura do Projeto

```bash
forecast-materiais-industriais/
│
├── data/
│   └── consumo_materiais.csv
│
├── outputs/
│   ├── forecast_resultado.csv
│   ├── heatmap_risco.png
│   └── gráficos gerados
│
├── src/
│   ├── preprocess.py
│   ├── forecast.py
│   ├── visualize.py
│   ├── heatmap.py
│   └── main.py
│
├── requirements.txt
└── README.md
