# Predict Future Sales — Proyecto #1: EDA

Análisis exploratorio de datos (EDA) sobre el dataset **Predict Future Sales** de Kaggle
(ventas diarias de la cadena rusa 1C Company, enero 2013 – octubre 2015).
El objetivo final de la competencia es predecir las ventas mensuales de cada par
tienda‑producto para noviembre de 2015; este EDA prepara esa etapa de forecasting.

## Cómo reproducir

```bash
git clone https://github.com/<usuario>/predict-future-sales.git
cd predict-future-sales
python -m venv .venv
# Windows: .venv\Scripts\activate    |  Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

1. Descargar los datos desde
   <https://www.kaggle.com/competitions/competitive-data-science-predict-future-sales/data>.
2. Copiar los 6 CSV a `data/raw/` (no se suben al repositorio, ver `.gitignore`).
3. Abrir `notebooks/01_exploratory_data_analysis.ipynb` en VSCode y ejecutar todo.

## Organización del proyecto (cookiecutter-data-science)

```
├── LICENSE
├── Makefile               <- Comandos útiles (make requirements, make clean)
├── README.md              <- Este archivo
├── data
│   ├── external           <- Datos de terceros
│   ├── interim            <- Datos intermedios transformados
│   ├── processed          <- Datos finales para modelar
│   └── raw                <- Datos originales de Kaggle (inmutables, NO versionados)
├── docs                   <- Documentación
├── models                 <- Modelos entrenados
├── notebooks              <- Notebooks (01_exploratory_data_analysis.ipynb)
├── pyproject.toml         <- Metadatos del proyecto
├── references             <- Diccionarios de datos, enunciados, material explicativo
├── reports
│   └── figures            <- Gráficas generadas por el EDA
├── requirements.txt       <- Dependencias
└── predict_future_sales   <- Código fuente del proyecto
    ├── __init__.py
    ├── config.py          <- Rutas y variables de configuración
    ├── dataset.py         <- Carga de datos
    ├── features.py        <- Ingeniería de variables
    ├── plots.py           <- Visualizaciones
    └── modeling
        ├── __init__.py
        ├── predict.py
        └── train.py
```
