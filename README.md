# 🧪 DLT ETL Project: Exchange Rate Pipeline

This project demonstrates how to build a simple but powerful **ETL pipeline** using the [DLT library](https://github.com/dlt-hub/dlt) to extract foreign exchange rates from an API and load them into a **local PostgreSQL** database.

---

## 📌 Features

- 🔁 Extracts exchange rate data from the [ExchangeRate-API](https://www.exchangerate-api.com/)
- 🧹 Transforms and normalizes JSON data using `pandas`
- 🗃️ Loads cleaned data into a **PostgreSQL** destination using **DLT**
- ♻️ Incremental pipeline execution with deduplication using `primary_key` and `merge` mode

---

## 🛠️ Technologies Used

- `Python`
- `pandas`
- [`dlt`](https://dlthub.com/)
- `PostgreSQL`
- `requests`

---

## 📁 Project Structure

```
dlt_project/
│
├── .dlt/                          # DLT pipeline metadata
├── .venv/                         # Virtual environment (ignored)
├── assets/                        # Images and visual documentation
│   ├── etl_dbt.jpg
│   └── data_loaded_successfully.png
├── etl.py                         # Main ETL script
├── requirements.txt               # Python dependencies
├── .gitignore                     # Ignored files
└── README.md                      # Documentation

```

---

## 📸 Architecture Overview

![ETL Architecture](https://github.com/ChahiriAbderrahmane/dlt_project/blob/master/assets/etl_dbt.jpg)

---

## ✅ Data Loaded Successfully

After the pipeline runs, data is successfully inserted into a local **PostgreSQL** database:

![Data Loaded](https://github.com/ChahiriAbderrahmane/dlt_project/blob/master/assets/data_loaded_successfully.png)

---

## 🚀 How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone git@github.com:ChahiriAbderrahmane/dlt_project.git
   cd dlt_project


