# Guía paso a paso: de este ZIP al entregable final (Windows + VSCode)

## Paso 0 — Requisitos
- Python 3.10 o superior, Git y VSCode (con las extensiones **Python** y **Jupyter**).
- Una cuenta de GitHub.

## Paso 1 — Ubicar el proyecto
1. Descomprime `predict-future-sales.zip`, por ejemplo en `C:\Users\<tu_usuario>\Documents\predict-future-sales`.
2. Copia los 6 CSV que tienes en **Descargas\competitive-data-science-predict-future-sales** a la carpeta
   `predict-future-sales\data\raw\`. En PowerShell:

```powershell
cd $HOME\Documents\predict-future-sales
Copy-Item "$HOME\Downloads\competitive-data-science-predict-future-sales\*.csv" .\data\raw\
dir .\data\raw
```

Deben quedar: `sales_train.csv`, `items.csv`, `item_categories.csv`, `shops.csv`, `test.csv` y `sample_submission.csv`.

> **(Opcional, punto 1.a)** Si el catedrático quiere ver que **ustedes** generaron la plantilla, ejecuten
> `pip install cookiecutter-data-science` y luego `ccds` (project_name `predict-future-sales`,
> module_name `predict_future_sales`). Después copien en esa carpeta el notebook, el `.gitignore` y `reports/figures`
> de este ZIP. La estructura es la misma.

## Paso 2 — Entorno virtual e instalación

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Paso 3 — Ejecutar el notebook
1. `code .` (abre VSCode en la carpeta).
2. Abre `notebooks/01_exploratory_data_analysis.ipynb`, elige el kernel `.venv` y pulsa **Run All**.
3. Tarda 1–2 minutos. Las gráficas también se guardan en `reports/figures/`.

## Paso 4 — Repositorio local con git (puntos 1.c y 1.d)

```powershell
git init
git add .
git status        # verifica que NO aparezca ningún .csv (el .gitignore los excluye)
git commit -m "Estructura cookiecutter + EDA Predict Future Sales"
git branch -M main
```

## Paso 5 — Publicar en GitHub (punto 1.e)
1. En github.com → **New repository** → nombre `predict-future-sales`, **sin** README ni .gitignore (ya los tienen).
2. Luego:

```powershell
git remote add origin https://github.com/<tu_usuario>/predict-future-sales.git
git push -u origin main
```

3. En **Settings → Collaborators**, agrega a cada integrante del equipo.

## Paso 6 — Pull de cada integrante (punto 1.f)
Cada integrante, en su computadora:

```powershell
git clone https://github.com/<tu_usuario>/predict-future-sales.git
cd predict-future-sales
git pull origin main
```

Toma un **screenshot** de la terminal con el resultado del `git pull` y guárdalo como
`reports/figures/pull_integrante1.png`, `pull_integrante2.png`, etc. El anexo al final del notebook los muestra
automáticamente. Para agregarlos al repositorio:

```powershell
git add reports/figures/pull_*.png
git commit -m "Screenshots del pull de cada integrante"
git push
```

## Entregables
1. Enlace al repositorio de GitHub.
2. `notebooks/01_exploratory_data_analysis.ipynb` ejecutado (ya viene ejecutado; al correrlo de nuevo se regenera).
3. Screenshots del pull (`reports/figures/pull_*.png`).
