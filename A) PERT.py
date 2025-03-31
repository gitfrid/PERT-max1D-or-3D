# csv data from

# case incidence rate per 1M
# https://immunizationdata.who.int/global/wiise-detail-page/pertussis-reported-cases-and-incidence?GROUP=Countries&YEAR=

# vac coverage Official Numbers Pertussis-containing vaccine 3d Dose
# https://immunizationdata.who.int/global/wiise-detail-page/diphtheria-tetanus-toxoid-and-pertussis-(dtp)-vaccination-coverage?GROUP=Countries&ANTIGEN=DTPCV3&YEAR=&CODE=


import pandas as pd
import plotly.graph_objects as go

# Load the data with error handling
vac_coverage_df = pd.read_csv(r"C:\PERT-max1D-or-3D\DTP vac coverage 2025-04-03 mx 1D or 3D.csv", 
                              encoding='ISO-8859-1', 
                              on_bad_lines='skip', 
                              delimiter=';')
reported_cases_df = pd.read_csv(r"C:\PERT-max1D-or-3D\DTP reported cases and incidence 2025-04-03 15-25 RATE.csv", 
                                encoding='ISO-8859-1', 
                                on_bad_lines='skip', 
                                delimiter=';')

year_range_text = "1980-2023"

# Clean column names
vac_coverage_df.columns = vac_coverage_df.columns.str.strip()
reported_cases_df.columns = reported_cases_df.columns.str.strip()

# Set 'Country' as the index for both DataFrames
vac_coverage_df.set_index('Country', inplace=True)
reported_cases_df.set_index('Country', inplace=True)

# Clean country names by stripping extra spaces
vac_coverage_df.index = vac_coverage_df.index.str.strip()
reported_cases_df.index = reported_cases_df.index.str.strip()

# Normalize country names (strip spaces and convert to lowercase) for comparison
vac_coverage_df.index = vac_coverage_df.index.str.lower()
reported_cases_df.index = reported_cases_df.index.str.lower()

# Debugging: Print the first few country names from both DataFrames to inspect
print("First few countries in vac_coverage_df:")
print(vac_coverage_df.index[:10])  # Print the first 10 countries in the vac_coverage DataFrame

print("\nFirst few countries in reported_cases_df:")
print(reported_cases_df.index[:10])  # Print the first 10 countries in the reported_cases DataFrame

# Remove thousands dots and replace commas with periods for all values in the dataframes
vac_coverage_df = vac_coverage_df.replace({r'\.': '', ',': '.'}, regex=True)
reported_cases_df = reported_cases_df.replace({r'\.': '', ',': '.'}, regex=True)

# Convert columns (except the 'Country' index) to numeric, forcing errors to NaN
vac_coverage_df = vac_coverage_df.apply(pd.to_numeric, errors='coerce')
reported_cases_df = reported_cases_df.apply(pd.to_numeric, errors='coerce')

# Filter columns to include only years from 2000 onwards
vac_coverage_df = vac_coverage_df.loc[:, vac_coverage_df.columns.astype(int) >= 1980]
reported_cases_df = reported_cases_df.loc[:, reported_cases_df.columns.astype(int) >= 1980]

# Find countries in vac_coverage_df that are not in reported_cases_df
countries_in_vac_not_in_reported = vac_coverage_df.index.difference(reported_cases_df.index)
# Find countries in reported_cases_df that are not in vac_coverage_df
countries_in_reported_not_in_vac = reported_cases_df.index.difference(vac_coverage_df.index)

# Print differences
if not countries_in_vac_not_in_reported.empty:
    print("Countries in vac_coverage_df but not in reported_cases_df:")
    print(countries_in_vac_not_in_reported)

if not countries_in_reported_not_in_vac.empty:
    print("\nCountries in reported_cases_df but not in vac_coverage_df:")
    print(countries_in_reported_not_in_vac)

# Now compare the country names that exist in both DataFrames
common_countries = vac_coverage_df.index.intersection(reported_cases_df.index)

# Print common countries to see which countries match after normalization
print("\nCommon countries between both DataFrames:")
print(common_countries)

# Create a list of traces for each country in the common countries list
traces = []
for country in common_countries:
    # Truncate the country name for the legend if it's too long (e.g., first 20 characters)
    legend_name = f'{country[:20]}...' if len(country) > 20 else country
    
    # Plot the vaccination coverage data
    trace_vac_coverage = go.Scatter(
        x=vac_coverage_df.columns,  # Year columns
        y=vac_coverage_df.loc[country],  # Values for this country
        mode='lines',
        name=f'{legend_name} - Vac Cover',  # Use the truncated name here
        yaxis='y2'
    )
    
    # Plot the reported cases data
    trace_reported_cases = go.Scatter(
        x=reported_cases_df.columns,  # Year columns
        y=reported_cases_df.loc[country],  # Values for this country
        mode='lines',
        name=f'{legend_name} - case incidence/1M',  # Use the truncated name here
        yaxis='y1'
    )
    
    # Add traces to the list
    traces.append(trace_vac_coverage)
    traces.append(trace_reported_cases)

# Layout with two y-axes and legend visibility
layout = go.Layout(
    title='Pertussis vaccination coverage vs reported case incidence rate for different countries,DTP-containing vaccine max(1st or 3rd dose)',
    xaxis=dict(title='Year'),
    yaxis=dict(title='cases/1M', side='left'),
    yaxis2=dict(
        title='Vaccination Coverage (%)',
        side='right',
        overlaying='y1',
        tickformat=",.0f",  # Format the numbers to show without thousands separator
        tickmode='auto',  # Automatically adjust tick positions
        showgrid=True,  # Show grid lines on the right y-axis
        ticksuffix=' ',  # Optional: Adds space after tick values (for better readability)
        tickprefix='',  # Optional: Remove any prefix for the right y-axis ticks
    ),
    showlegend=True,  # Make sure legend is shown
    legend=dict(
        x=1.05,  # Move the legend a little further to the right (beyond the plot area)
        y=1,  # Align legend at the top right
        traceorder='normal',  # Ensure traces are in the correct order
        orientation='v',  # Make legend vertical
        bgcolor='rgba(255, 255, 255, 0.7)',  # Optional: Add a transparent background for readability
        bordercolor='black',  # Optional: Border color around the legend
        borderwidth=1,  # Optional: Border width around the legend
        itemwidth=30,  # Adjust the width of each legend item to fit more compactly
        itemsizing='trace',  # Ensure each legend item adjusts to its content
        tracegroupgap=5,  # Adjusts the gap between groups of traces in the legend
        font=dict(
            size=10  # Smaller font size for the legend items (adjust as needed)
        ),
    ),
    shapes=[
        # Create a transparent rectangle at the top of the plot
        dict(
            type='rect',
            x0=0,  # Start of the rectangle (0 represents the start of the x-axis)
            x1=1,  # End of the rectangle (1 represents the end of the x-axis)
            y0=1.05,  # Top of the plot (slightly above the plot area)
            y1=1.15,  # Height of the rectangle (adjust this value to your preference)
            xref='paper',  # x-axis reference to 'paper' means relative to the entire plot (from 0 to 1)
            yref='paper',  # y-axis reference to 'paper' means relative to the entire plot (from 0 to 1)
            line=dict(
                color='rgba(255, 255, 255, 0)',  # Transparent border (or you can change it to any color)
                width=0
            ),
            #fillcolor='rgba(255, 255, 255, 0.3)',  # Transparent fill (adjust the opacity here)
        ),
    ],
    annotations=[
        # Add text inside the transparent rectangle (or anywhere on the plot)
        dict(
            x=0.005,  # Position of the annotation (centered horizontally)
            y=1.05,  # Position of the annotation (vertically in the rectangle)
            xref='paper',
            yref='paper',
            # case incidence rate per 1M
            text='case incidence rate -> https://immunizationdata.who.int/global/wiise-detail-page/pertussis-reported-cases-and-incidence?GROUP=Countries&YEAR=' + 
                 '<br>vac coverage -> https://immunizationdata.who.int/global/wiise-detail-page/diphtheria-tetanus-toxoid-and-pertussis-(dtp)-vaccination-coverage?GROUP=Countries&ANTIGEN=DTPCV3&YEAR=&CODE=',  # Text content
            showarrow=False,  # No arrow for this annotation
            font=dict(size=8, color="black"),  # Text styling
            bgcolor='rgba(255, 255, 255, 0.8)',  # Background color for text, slightly transparent
            borderpad=10,  # Padding around the text
            bordercolor='black',  # Border color around the text
            borderwidth=0  # Border width for the text box
        ),
    ]
)

# Create the figure
fig = go.Figure(data=traces, layout=layout)

# Save the plot to an HTML file
fig.write_html(fr"C:\PERT-max1D-or-3D\A) PERT vaccination_vs_reported_cases {year_range_text}.html")

print("Plot has been saved to 'vaccination_vs_reported_cases.html'.")

# Show the plot (uncomment if you want t
