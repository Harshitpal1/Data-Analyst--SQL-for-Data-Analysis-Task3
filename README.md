# Data Analyst Internship - Task 4: Dashboard Design

[cite_start]This repository contains the deliverables for Task 4 of the Elevate Labs Data Analyst Internship program[cite: 2]. [cite_start]The primary objective of this task was to design an interactive dashboard for business stakeholders using a sales and financial dataset[cite: 4].

## Project Objective

[cite_start]The goal of this project is to create a dashboard that informs business decisions[cite: 16]. [cite_start]This involves selecting appropriate Key Performance Indicators (KPIs), creating insightful visualizations, and ensuring the dashboard is interactive and user-friendly[cite: 4, 8, 9].

## Dataset

[cite_start]As per the task guidelines, a sales dataset was used for this analysis[cite: 15]. The specific dataset used here is a pharmaceutical sales dataset, containing daily sales figures for various product categories.

* `salesdaily.csv`
* `saleshourly.csv`
* `salesmonthly.csv`
* `salesweekly.csv`

## Tools Used

* [cite_start]**Dashboarding Tools:** The project could be implemented in **Power BI** or **Tableau**[cite: 5].
* **Data Analysis & Visualization:** **Python** (with pandas and matplotlib libraries) was used for data processing and generating the visual insights for this prototype.

## Dashboard Analysis & Visualizations

The dashboard design focuses on clarity and insight, presenting key data points to help stakeholders understand business performance at a glance.

### Key Performance Indicator (KPI): Total Sales

* **Total Sales:** 127,595.50 units
* [cite_start]This primary KPI gives an immediate summary of the overall business performance[cite: 8, 11].

### Visualizations

#### 1. Total Daily Sales Trend
[cite_start]This line chart provides a time-series analysis of sales, which is crucial for identifying patterns and seasonality[cite: 10].
![Daily Sales Trend](daily_sales_trend.png)

#### 2. Total Sales by Weekday
This bar chart shows the sales distribution across different days of the week, helping to inform operational decisions like staffing and inventory management.
![Weekday Sales](weekday_sales.png)

#### 3. Total Sales by Product Category
This visualization helps identify the best-performing product categories and those that may require additional marketing efforts.
![Product Sales](product_sales.png)

#### 4. Total Monthly Sales
This chart provides a month-over-month view of sales, essential for tracking performance against monthly targets and observing broader trends.
![Monthly Sales](monthly_sales.png)

## Interview Questions & Answers

Here are the answers to the interview questions listed in the task description:

**1. [cite_start]What are the key elements of a dashboard?** [cite: 19]
   * [cite_start]**Clear and Relevant KPIs:** High-level metrics that reflect business objectives[cite: 8, 11].
   * **Data Visualizations:** Charts and graphs for easy data interpretation.
   * [cite_start]**Interactivity:** Features like slicers and filters allowing users to explore data[cite: 9].
   * [cite_start]**Time-Series Analysis:** Visuals showing trends over time[cite: 10].
   * [cite_start]**Logical Layout:** An intuitive and consistently designed user interface[cite: 12].

**2. [cite_start]What is a KPI?** [cite: 20]
   A Key Performance Indicator (KPI) is a measurable value that demonstrates how effectively a company is achieving its key business objectives. [cite_start]For a sales dashboard, KPIs could include Total Sales, Profit Margin, and Sales Growth[cite: 8].

**3. [cite_start]What are slicers in Power BI?** [cite: 21]
   Slicers in Power BI are on-canvas visual filters that provide a user-friendly way to filter data in a report. [cite_start]They allow users to click buttons or select from a list to dynamically segment the data, updating all visuals on the report page accordingly[cite: 9].

**4. [cite_start]Difference between Power BI and Tableau?** [cite: 22]
   | Feature | Power BI | Tableau |
   | :--- | :--- | :--- |
   | **User Interface** | Considered more intuitive for beginners, especially those familiar with Excel. | Offers a more flexible and complex interface, often favored by data analysts. |
   | **Data Connectivity** | Strong integration with Microsoft products (e.g., Excel, Azure). | Known for extensive connectivity to a very wide range of data sources. |
   | **Cost** | Generally more cost-effective with a free desktop version. | Tends to have a higher price point. |

**5. [cite_start]How do you make a dashboard interactive?** [cite: 23]
   You can make a dashboard interactive by:
   * [cite_start]Adding slicers and filters for data segmentation[cite: 9].
   * Enabling drill-down capabilities to view detailed data.
   * Using cross-filtering, where selections in one visual affect others.

**6. [cite_start]How do you deal with large datasets in dashboards?** [cite: 24]
   * **Data Aggregation:** Pre-summarize data to a higher level.
   * **Data Extracts:** Work with smaller, extracted subsets of the data instead of a live connection.
   * **Source Filtering:** Use queries to import only the necessary columns and rows.
   * **Optimized Data Models:** Build efficient data models and relationships.

**7. [cite_start]What chart types do you use for trend analysis?** [cite: 25]
   * [cite_start]**Line Charts:** The most common choice for showing trends over a continuous period[cite: 10].
   * **Area Charts:** Similar to line charts but emphasize the volume of change over time.
   * **Bar/Column Charts:** Effective for comparing discrete time intervals like months or years.
