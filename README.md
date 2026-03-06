# XmR Chart App

An interactive web application for building and exploring XmR charts (process behavior charts). Built as part of [The Broken Quality Initiative](https://www.brokenquality.com/).

---

## Overview

Try the live app at [xmr-chart.streamlit.app](https://xmr-chart.streamlit.app).

The XmR chart is the most useful type of process behavior chart. When a dataset is composed of logically comparable individual values that retain their time-ordered sequence, the XmR chart is the most effective tool for making sense of that data. It characterizes process behavior as either predictable or unpredictable by comparing individual values and moving ranges against calculated process limits.

This app allows users to:
- Explore nine sample datasets spanning manufacturing, economics, and science
- Upload their own CSV files
- Visualize data as an XmR chart with calculated process limits
- Analyze multi-stage processes
- Test their understanding with interactive questions

---

## Features

- **Sample datasets** — nine preloaded datasets with default column configurations and descriptions
- **CSV upload** — upload your own data with selectable data, label, and stage columns
- **XmR chart** — interactive Plotly chart with Upper Process Limit (UPL), Lower Process Limit (LPL), and Upper Range Limit (URL)
- **Stage view** — divide data into stages for direct visual comparison of process behavior across periods
- **Display controls** — adjust tick interval, decimal places, tick angle, and toggle process limits, annotations, and connecting lines
- **Interactive questions** — multiple choice questions with instant feedback for each sample dataset
- **Bound LPL/UPL** — options to prevent limits from going below zero or above 100%

---

## Installation

### Requirements

```
streamlit
pandas
plotly
Pillow
```

Install dependencies:

```bash
pip install streamlit pandas plotly Pillow
```

### Running the App

```bash
streamlit run xmr_chart_app.py
```

---

## File Structure

```
├── xmr_chart_app.py          # Main application file
├── requirements.txt          # Python dependencies
├── data/                     # Sample CSV datasets
│   ├── automated_manufacturing_part_lengths.csv
│   ├── manufacturing_PMI.csv
│   ├── millikans_electron_charge_observations.csv
│   ├── monthly_united_states_trade_deficits_2024.csv
│   ├── OP200_weekly_first_pass_yield.csv
│   ├── quarterly_sales_by_region.csv
│   ├── shewharts_resistance_measurements.csv
│   ├── vienna_general_death_to_birth_rates.csv
│   └── wafer_assembly_part_placement.csv
└── figures/                  # Images used in the app
    ├── Broken_quality_logo.png
    ├── Fig_xmr_chart_example.png
    ├── Fig_is_all_the_data_within_limits.png
    ├── EQ_process_limits.png
    └── virus_of_variation_book_cover_cropped.png
```

---

## How to Use

### Selecting a Sample Dataset
Use the **Select a sample dataset** dropdown to choose from nine preloaded datasets. Each dataset includes a description, default column selections, and a set of interactive questions.

### Uploading Your Own Data
Use the **Or upload a CSV file** file uploader to upload a CSV. You will be prompted to select:
- **Data column** — the column containing the values to be plotted
- **Label column** — the column used for x-axis labels (or use the default 1 to n)
- **Stage column** — optional column used to divide the data into stages

### XmR Chart Display Controls
Expand the **XmR Chart Display Controls** section to adjust:
- Tick interval and label angle
- Number of decimal places displayed
- Show/hide process limits, annotations, and connecting lines
- Bound UPL at 100% or LPL at 0%

### Stage View
If a stage column is selected, expand the **Stage View & Customization** section to enable stage-based process limits. Each stage is calculated independently, allowing direct comparison of process behavior across different periods or conditions.

---

## Process Limit Formulas

The XmR chart process limits are calculated as follows:

```
UPL = X̄ + 2.660 × mR̄
LPL = X̄ - 2.660 × mR̄
URL = 3.268 × mR̄
```

Where X̄ is the mean of the data and mR̄ is the average moving range. The scaling factors 2.660 (E2) and 3.268 (D4) correspond to a subgroup size of n = 2.

---

## Sample Datasets

| Dataset | Description |
|---|---|
| Automated Manufacturing Part Lengths | 60 part length measurements from an automated manufacturing line |
| Manufacturing PMI | Monthly Purchase Manager's Index values from Feb 2025 to Jan 2026 |
| Millikan's Electron Charge Observations | 58 electron charge measurements by Millikan |
| Monthly United States Trade Deficits 2024 | Monthly US trade deficits for 2024 |
| OP200 Weekly First Pass Yield | 24 weeks of first-pass yield data for operation 200 |
| Quarterly Sales by Region | Quarterly sales for 6 regions over 20 consecutive quarters |
| Shewhart's Resistance Measurements | Electrical resistance measurements before and after process improvements |
| Vienna General Death-to-Birth Rates | Death-to-birth rates at Vienna General Hospital, 1841–1849 |
| Wafer Assembly Part Placement | X-coordinate placement measurements from a pick-and-place line |

---

## About

This app is part of [The Broken Quality Initiative](https://www.brokenquality.com/), a body of work that teaches engineers how to reduce costs and improve quality by understanding variation.

To learn more, visit [BrokenQuality.com](https://www.brokenquality.com/) or read [The Virus of Variation: Making Sense of Death and Data using Process Behavior Charts](https://www.brokenquality.com/book).

**Author:** [Jim Lehner](https://www.linkedin.com/in/jim-lehner/)
**Contact:** James.Lehner@gmail.com | QualityIsBroken@gmail.com
