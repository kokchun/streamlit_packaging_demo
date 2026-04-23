import streamlit as st
from salaries.utils.helpers import get_salaries_df, read_textfile
from salaries.utils.constants import MARKDOWN_PATH
from salaries.components.kpis import avg_salary_usd_kpi


def dashboard_layout():
    st.markdown("# Salaries dashboard")
    st.markdown(read_textfile(MARKDOWN_PATH / "salaries_dashboard_description.md"))
    st.dataframe(get_salaries_df())

    # KPIs
    roles = [
        "Data Scientist",
        "Data Analyst",
        "Data Engineer",
        "Machine Learning Engineer",
        "AI Engineer",
    ]

    cols = st.columns(len(roles))

    for column, role in zip(cols, roles):
        with column:
            avg_salary_usd_kpi(role, role)



    # data scientist
    # machine learning engineer
    # data engineer


if __name__ == "__main__":
    dashboard_layout()
