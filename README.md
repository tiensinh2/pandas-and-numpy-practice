# Pandas & NumPy Practice

A hands-on data analysis project exploring COVID-19 global time series data using **Pandas** and **NumPy**, with EDA (Exploratory Data Analysis) performed in Jupyter notebooks.

---

## 📁 Project Structure

```
pandas-and-numpy-practice/
├── Data/
│   ├── time_series_covid19_confirmed_global.csv
│   ├── time_series_covid19_deaths_global.csv
│   └── time_series_covid19_recovered_global.csv
├── notebooks/
│   └── notebook1_confirmed.ipynb   # EDA on confirmed cases
├── src/
│   └── pandas_and_numpy/
│       ├── __init__.py
│       └── covid_utils.py          # Reusable cleaning utilities
├── pyproject.toml
└── README.md
```

---

## 📊 Dataset

Data sourced from the [Johns Hopkins University CSSE COVID-19 Dataset](https://github.com/CSSEGISandData/COVID-19).

| File | Description |
|------|-------------|
| `time_series_covid19_confirmed_global.csv` | Cumulative confirmed cases by country/region |
| `time_series_covid19_deaths_global.csv` | Cumulative deaths by country/region |
| `time_series_covid19_recovered_global.csv` | Cumulative recovered cases by country/region |

- **289 rows** × **1147 columns**
- Date range: `1/22/20` → `3/9/23`
- Granularity: country-level (some countries split by province/state)

---

## 🔍 EDA Highlights

The notebook covers:

- **Data Cleaning** — missing values, duplicates, negative daily cases (data corrections)
- **Daily New Cases** — computed via `diff(axis=1)` + `clip(lower=0)`
- **Country Aggregation** — `groupby('Country/Region')` to merge province-level rows
- **Time Series Analysis** — cumulative trends and daily new case waves
- **Notable findings**:
  - 2 rows with missing `Lat`/`Long`: `Repatriated Travellers` (Canada) and `Unknown` (China ~1.5M cases)
  - 128/289 rows had at least one negative daily value due to data corrections
  - Top countries by total confirmed cases: 🇺🇸 US, 🇮🇳 India, 🇫🇷 France

---

## 🛠️ Utilities

[`src/pandas_and_numpy/covid_utils.py`](src/pandas_and_numpy/covid_utils.py) provides a reusable `clean_covid_df()` function applicable to all 3 datasets:

```python
from pandas_and_numpy.covid_utils import clean_covid_df

conf_cum, conf_daily   = clean_covid_df('Data/time_series_covid19_confirmed_global.csv')
death_cum, death_daily = clean_covid_df('Data/time_series_covid19_deaths_global.csv')
recov_cum, recov_daily = clean_covid_df('Data/time_series_covid19_recovered_global.csv')
```

Returns:
- `country_cumulative` — DataFrame with datetime columns, one row per country
- `country_daily` — Same shape, but daily new values (clipped, non-negative)

---

## ⚙️ Setup

This project uses [`uv`](https://github.com/astral-sh/uv) for dependency management.

```bash
# Install dependencies
uv sync

# Launch Jupyter
uv run jupyter lab
```

**Requirements:** Python >= 3.12, pandas, numpy, matplotlib, jupyter

---

## 📝 License

For learning and practice purposes only.
