# Netflix-Azure-Data-Pipeline
Real-time Netflix data processing on Azure using Data Factory, Databricks Auto Loader, and Delta Lake architecture

This project demonstrates a full-scale real-time data engineering pipeline for processing Netflix datasets using Azure services.

### 📚 Project Architecture
**Data Ingestion (ADF):**

- Use Azure Data Factory to copy Netflix CSV files from GitHub to the Bronze layer of Azure Data Lake Gen2.
- Validation check ensures critical files exist before ingestion using the Validation Activity.
- Parameterized Copy Activity looping over a file array using ForEach.

**Data Storage:**

- Raw and structured data stored in Azure Data Lake Storage Gen2 containers: raw, bronze, silver.
- Streaming Data Processing (Databricks + Auto Loader):
    - Databricks Auto Loader to incrementally read new files from raw container.
    - Handle schema evolution automatically.
    - Write streaming data into Delta Lake tables in the Bronze layer.

**Data Transformation (Databricks):**

- Parameterized notebooks using dbutils widgets.
- Read Bronze data, clean/transform it, and write structured Delta tables into the Silver layer.
- Workflows automate the notebook execution dynamically based on lookup configurations.

**Data Governance (Unity Catalog):**

- Secure external storage access via Managed Identity and external locations.
- Unity Catalog enabled for better access control and schema organization.

**Data Quality:**

- Applied basic Delta Live Tables Expectations (where applicable) to enforce:
    - show_id IS NOT NULL
    - newflag IS NOT NULL

- Ensured clean, reliable data for downstream analytics.

### 🔧 Tech Stack
* Azure Data Factory
* Azure Databricks (Auto Loader, PySpark basics)
* Azure Data Lake Storage Gen2
* Delta Lake Format
* Unity Catalog (Metastore & External Locations)


### 📈 Outcomes

- Automated and scalable real-time ingestion pipeline.
- Streamlined ETL process ready for BI and reporting teams.
- Secure and compliant data access using Unity Catalog.