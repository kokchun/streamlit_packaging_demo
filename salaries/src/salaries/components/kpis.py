#%%
from salaries.utils.helpers import get_salaries_df
import duckdb

df = get_salaries_df()

def avg_salary_usd_kpi(role):
    avg_salary = duckdb.sql(f"""--sql
        SELECT 
            AVG(salary_in_usd) AS avg_salary_usd
        FROM df
        WHERE job_title ILIKE '{role}'
    """).df()

    return avg_salary

avg_salary_usd_kpi("data scientist")
# %%
