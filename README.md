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

