import pandas as pd
import ETL_process

df_customers =pd.read_json("customers.json")

categorize_columns = {"personal_info": ["id","name","birth_date", "address","phone_number"],
                      "financial_status": ["id","income_level","occupation","employer", "assets","liabilities"]}

new_table_names = ["personal_info",
                    "financial_status",
                    "credit_applications",
                    "credit_card_usage",
                    "credit_score",
                    "bank_transactions",
                    "demographics",
                    "risk_factors",
                    "loan_application_forms"]

column_to_table = ["credit_score"]
id_column_name = "id"


ETL_process = ETL_process.ETL_process(df_customers, categorize_columns, new_table_names, column_to_table, id_column_name)
ETL_process.data_import("customers", "luminadb")