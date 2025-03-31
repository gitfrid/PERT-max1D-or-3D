# csv data from

# case incidence rate per 1M
# https://immunizationdata.who.int/global/wiise-detail-page/pertussis-reported-cases-and-incidence?GROUP=Countries&YEAR=

# vac coverage Official Numbers Pertussis-containing vaccine 3d Dose
# https://immunizationdata.who.int/global/wiise-detail-page/diphtheria-tetanus-toxoid-and-pertussis-(dtp)-vaccination-coverage?GROUP=Countries&ANTIGEN=DTPCV3&YEAR=&CODE=


import pandas as pd
import plotly.graph_objects as go
from dowhy import CausalModel

# Load the data with error handling
vac_coverage_df = pd.read_csv(r"C:\github\PERT-max1D-or-3D\DTP vac coverage 2025-04-03 mx 1D or 3D.csv", 
                              encoding='ISO-8859-1', 
                              on_bad_lines='skip', 
                              delimiter=';')
reported_cases_df = pd.read_csv(r"C:\github\PERT-max1D-or-3D\DTP reported cases and incidence 2025-04-03 15-25 RATE.csv", 
                                encoding='ISO-8859-1', 
                                on_bad_lines='skip', 
                                delimiter=';')

filename_plot_text = "Dowhy causal estimate on mean vac coverage max(1st or 3d Dose) and cases Pertussis"
year_range_text = "1980-2023"

# Clean up column names
vac_coverage_df.columns = vac_coverage_df.columns.str.strip()
reported_cases_df.columns = reported_cases_df.columns.str.strip()

# Normalize country names (strip spaces and convert to lowercase)
vac_coverage_df.set_index('Country', inplace=True)
reported_cases_df.set_index('Country', inplace=True)

vac_coverage_df.index = vac_coverage_df.index.str.lower()
reported_cases_df.index = reported_cases_df.index.str.lower()

# Remove thousands dots and replace commas with periods for numeric conversion
vac_coverage_df = vac_coverage_df.replace({r'\.': '', ',': '.'}, regex=True)
reported_cases_df = reported_cases_df.replace({r'\.': '', ',': '.'}, regex=True)

# Convert columns (except the 'Country' index) to numeric
vac_coverage_df = vac_coverage_df.apply(pd.to_numeric, errors='coerce')
reported_cases_df = reported_cases_df.apply(pd.to_numeric, errors='coerce')

# Filter columns for years >= 1980
vac_coverage_df = vac_coverage_df.loc[:, vac_coverage_df.columns.astype(int) >= 1980]
reported_cases_df = reported_cases_df.loc[:, reported_cases_df.columns.astype(int) >= 1980]

# Find common countries between the two datasets
common_countries = vac_coverage_df.index.intersection(reported_cases_df.index)

# Lists for mean values, causal effects, and years used
mean_vac = []
mean_cases = []
causal_effects = []
valid_countries = []

# Create or open log file to write years used for causal effect
log_file_path = fr"C:\github\PERT-max1D-or-3D\C) {filename_plot_text} valid years for dowhy calc {year_range_text}.txt"

with open(log_file_path, "w") as log_file:
    # Iterate through common countries for causal analysis
    for country in common_countries:
        # Get valid years for vaccination coverage
        valid_vac_years = vac_coverage_df.columns[~vac_coverage_df.loc[country].isna() & (vac_coverage_df.loc[country] != 0)]
        valid_cases_years = reported_cases_df.columns[~reported_cases_df.loc[country].isna() & (reported_cases_df.loc[country] != 0)]

        # Find the common years
        common_years = valid_vac_years.intersection(valid_cases_years)
        if len(common_years) == 0:
            print(f"Skipping {country} due to no common valid years.")
            continue

        # Filter valid data for the common years
        valid_vac = vac_coverage_df.loc[country, common_years].dropna().values
        valid_cases = reported_cases_df.loc[country, common_years].dropna().values

        # Validate data
        if len(valid_vac) == 0 or len(valid_cases) == 0:
            print(f"Skipping {country} due to insufficient data.")
            continue

        # Calculate mean values for the country
        mean_vac_country = valid_vac.mean()
        mean_cases_country = valid_cases.mean()

        # Create the dataset for causal analysis
        data = pd.DataFrame({
            'vac': valid_vac,
            'cases': valid_cases
        })

        # Define causal graph
        causal_graph = """
        digraph {
            vac -> cases;
        }
        """

        # Initialize causal model
        model = CausalModel(
            data=data,
            treatment='vac',
            outcome='cases',
            graph=causal_graph
        )

        # Perform causal inference
        identified_estimand = model.identify_effect()

        try:
            # Estimate the causal effect using backdoor linear regression
            causal_estimate = model.estimate_effect(
                identified_estimand,
                method_name="backdoor.linear_regression",
                test_significance=True
            )
            print(f"Causal estimate for {country}: {causal_estimate.value}")

            # Append results to lists
            mean_vac.append(mean_vac_country)
            mean_cases.append(mean_cases_country)
            causal_effects.append(causal_estimate.value)
            valid_countries.append(country)  # Track countries with valid data

            # Log the years for each country
            log_file.write(f"Country: {country.capitalize()}\n")
            log_file.write(f"Years used for causal analysis: {', '.join(map(str, common_years))}\n\n")

        except Exception as e:
            print(f"Error for {country}: {e}")
            continue

# Create plot
fig = go.Figure()
fig.update_layout(
    font=dict(size=8)  # Sets font size globally
)
# Add scatter plot for mean vaccination coverage with secondary y-axis
fig.add_trace(go.Scatter(
    x=valid_countries,
    y=mean_vac,
    mode='markers',
    name='Mean Vaccination Coverage (%)', 
    marker=dict(color='blue', size=5),
    yaxis="y2"
))

# Add scatter plot for causal effect
fig.add_trace(go.Scatter(
    x=valid_countries,
    y=causal_effects,
    mode='markers',
    name='Causal Effect Vac Coverage on Cases/1M',
    marker=dict(color='green', size=5),
))

# Add scatter plot for reported cases
fig.add_trace(go.Scatter(
    x=valid_countries,
    y=mean_cases,
    mode='markers',
    name='Mean Reported Cases/1M',
    marker=dict(color='red', size=5),
    yaxis="y3"
))

# Add horizontal line at y = 0.95 on the secondary y-axis
fig.add_trace(go.Scatter(
    x=common_countries[:len(valid_countries)],  # Same x-axis range as other data
    y=[95] * len(common_countries[:len(valid_countries)]),  # Constant y-value of 0.95
    mode='lines',  # A line instead of markers
    name="Line at 95 (Vac Coverage)",
    line=dict(color='red', dash='dot', width=1),  # Red dotted line
    yaxis="y2"  # Use the secondary y-axis
))

# Layout settings with secondary y-axis for vaccination coverage
# Update y-axis font size
fig.update_layout(
    yaxis=dict(
        title="Causal Effect of Vaccination Coverage on Cases",
        side="left",
        autorange=True,
        position=0.05,
        tickfont=dict(size=8)  # Smaller font for y-axis ticks
    ),
    
    yaxis2=dict(
        title="avg vac coverage %",
        side="right",
        overlaying="y",
        autorange=True,
        tickformat=".1f",
        tickmode='auto',
        position=0.95,
        tickfont=dict(size=8)  # Smaller font for y-axis2 ticks
    ),
    
    yaxis3=dict(
        title="avg cases/1M",
        side="right",
        overlaying="y",
        autorange=True,
        tickformat=".1f",
        tickmode='auto',
        position=1,
        tickfont=dict(size=8)  # Smaller font for y-axis3 ticks
    ),
    
    xaxis=dict(
        tickmode="array",
        tickvals=valid_countries,
        ticktext=[country[:15] for country in valid_countries],
        tickfont=dict(size=6, family='Arial', color='black')  # Adjust x-axis font as needed
    ),
    
    # Title font size
    title=dict(
        text=f"{filename_plot_text} {year_range_text}",
        font=dict(size=12)  # Smaller title font
    )
)

# Save and show the plot
fig.write_html(fr"C:\github\PERT-max1D-or-3D\C) {filename_plot_text} {year_range_text}.html")
fig.show()

print(fr"C:\github\PERT-max1D-or-3D\C) {filename_plot_text} {year_range_text}.html has been saved.")
