import streamlit as st
from salaries.utils.helpers import get_salaries_df
import duckdb

df = get_salaries_df()

df_top_avg_salaries = duckdb.sql("""--sql
        SELECT 
            job_title,
            ROUND(AVG(salary_in_usd),-3)::INT AS avg_salary_usd
        FROM df
        GROUP BY job_title
        ORDER BY avg_salary_usd DESC
    """).df()


print(df_top_avg_salaries)
