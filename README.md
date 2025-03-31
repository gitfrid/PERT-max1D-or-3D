### PERT-py 
<br>
<br>

Case incidence rate per 1M
[Download Link immunizationdata.who.int](https://immunizationdata.who.int/global/wiise-detail-page/pertussis-reported-cases-and-incidence?GROUP=Countries&YEAR=)
<br>Vac coverage official Numbers Pertussis-containing vaccine 2d Dose
[Download Link immunizationdata.who.int](https://immunizationdata.who.int/global/wiise-detail-page/diphtheria-tetanus-toxoid-and-pertussis-(dtp)-vaccination-coverage?GROUP=Countries&ANTIGEN=DTPCV3&YEAR=&CODE=)
<br>[The recommended case definitions](https://www.who.int/publications/m/item/vaccine-preventable-diseases-surveillance-standards-pertussis)
### Disclaimer:
**The results have not been checked for errors. Neither methodological nor technical checks or data cleansing have been performed.**
_________________________________________

### Dowhy causal impact estimation vax coverage on case incidence rate for differnt counties, <br>DTP-containing vac 3rd Dose

<br>
<p>DoWhy is a Python library for causal inference that allows modeling and testing of causal assumptions, based on a unified language for causal inference.
<strong>See the book <em>Models, Reasoning, and Inference</em> by Judea Pearl for deeper insights, that goes far beyond my horizon.</strong></p>
<br>

Phyton script [C) PERT.py](https://github.com/gitfrid/PERT-py/blob/main/C%29%20PERT.py) for visualizing the downloaded CSV data
<br>DoWhy Library see: https://github.com/py-why/dowhy

<br>
<img src=https://github.com/gitfrid/PERT-py/blob/main/C%29%20Dowhy%20causal%20estimate%20on%20mean%20vac%20coverage%20and%20cases%20pertussis%202000-2023.png width="1280" height="auto">
<br>
To select or deselect all, double-click on the legend. To select a single legend, click on it once
<br>

<br>[Download interactive html](https://github.com/gitfrid/PERT-py/blob/main/C%29%20Dowhy%20causal%20estimate%20on%20mean%20vac%20coverage%20and%20cases%20pertussis%202000-2023.html) 2000-2023
<br>[Years for each country the dowhy estimation is based on](https://github.com/gitfrid/PERT-py/blob/main/C%29%20Dowhy%20causal%20estimate%20on%20mean%20vac%20coverage%20and%20cases%20pertussis%20valid%20years%20for%20dowhy%20calc%202000-2023.txt)
<br>
<br>

Interpretation of Causal Effect Estimation:

The causal effect estimation gives a numerical value indicating how much the outcome (reported cases per million) changes when the treatment (coverage in percentage) changes by one unit.

    Positive causal effect (e.g. 0.5): For each 1% increase in coverage, reported cases expected to increase by 0.5 cases per million.
    Negative causal effect (e.g. -0.5): For each 1% increase in vaccination coverage, reported cases are expected to decrease by 0.5 cases per million.
    Warning: the results were not checked for confounding factors or lack of causality neither methodological errors

_________________________________________
<br>

### Vax coverage vs case incidence rate for differnt counties, DTP-containing vac 3rd Dose

Phyton script [A) PERT.py](https://github.com/gitfrid/PERT-py/blob/main/A%29%20PERT.py) for visualizing the downloaded CSV data


To select or deselect all countries, double-click on the legend. To select a single country, click on it once
<br>
<img src=https://github.com/gitfrid/PERT-py/blob/main/A%29%20PERT%20vaccination_vs_reported_cases%202000-2023.png width="1280" height="auto">
<br>
<br>
[Download interactive html](https://github.com/gitfrid/PERT-py/blob/main/A%29%20PERT%20vaccination_vs_reported_cases%202000-2023.html) 2000-2023
<br>
_________________________________________

<br>
<img src=https://github.com/gitfrid/PERT-py/blob/main/A%29%20PERT%20vaccination_vs_reported_cases%201980-2023.png width="1280" height="auto">
<br>

[Download interactive html](https://github.com/gitfrid/PERT-py/blob/main/A%29%20PERT%20vaccination_vs_reported_cases%201980-2023.html) 1980-2023
<br>
<br>
_________________________________________
<br>

### Vax coverage vs case incidence rate for differnt counties including trend line categories ,DTP-containing vac 3rd Dose 2000-2023:
    Rising Coverage and Rising Cases:
    Falling Coverage and Falling Cases:
    Rising Coverage and Falling Cases:
    Falling Coverage and Rising Cases:

<br>

Phyton script [B) PERT.py](https://github.com/gitfrid/PERT-py/blob/main/B%29%20PERT.py) for visualizing the downloaded CSV data with trend lines 
<br>


**Rising Coverage and Rising Cases:**
<br>
<img src=https://github.com/gitfrid/PERT-py/blob/main/B%29%20PERT%20rising%20vac%20coverage%20and%20rising%20cases%20trend%202000-2023.png width="1280" height="auto">
<br>

[Download interactive html](https://github.com/gitfrid/PERT-py/blob/main/B%29%20PERT%20rising%20vac%20coverage%20and%20rising%20cases%20trend%202000-2023.html) 2000-2023
<br>
_________________________________________

**Falling Coverage and Falling Cases:**
<br>
<img src=https://github.com/gitfrid/PERT-py/blob/main/B%29%20PERT%20falling%20vac%20coverage%20and%20falling%20trend%202000-2023.png width="1280" height="auto">
<br>

[Download interactive html](https://github.com/gitfrid/PERT-py/blob/main/B%29%20PERT%20falling%20vac%20coverage%20and%20falling%20trend%202000-2023.html) 2000-2023
<br>

_________________________________________

**Rising Coverage and Falling Cases:**
<br>
<img src=https://github.com/gitfrid/PERT-py/blob/main/B%29%20PERT%20rising%20vac%20coverage%20and%20falling%20cases%20trend%202000-2023.png width="1280" height="auto">
<br>

[Download interactive html](https://github.com/gitfrid/PERT-py/blob/main/B%29%20PERT%20rising%20vac%20coverage%20and%20falling%20cases%20trend%202000-2023.html) 2000-2023
<br>

_________________________________________

**Falling Coverage and Rising Cases:**
<br>
<img src=https://github.com/gitfrid/PERT-py/blob/main/B%29%20PERT%20falling%20vac%20coverage%20and%20rising%20cases%20trend%202000-2023.png width="1280" height="auto">
<br>

[Download interactive html](https://github.com/gitfrid/PERT-py/blob/main/B%29%20PERT%20falling%20vac%20coverage%20and%20rising%20cases%20trend%202000-2023.html) 2000-2023
<br>
_________________________________________
<br>

### Vax coverage vs case incidence rate for differnt counties including trend line categories , <br>DTP-containing vac 3rd Dose for years 1980-2023:

Warning: In order to compare the trends, M-containing vac 1st Dose from 1980 onwards would also have to be taken into account, which are not included here!
<br>
<br>Includes Dropdown menu for easy selection: 
<br>
<img src=https://github.com/gitfrid/PERT-py/blob/main/D%29%20PERT%20vaccination_vs_reported_cases_dropdown_1980_2023.png width="1280" height="auto">
<br>
[Download interactive html](https://github.com/gitfrid/PERT-py/blob/main/D%29%20PERT%20vaccination_vs_reported_cases_dropdown_1980-2023.html) 1980-2023
[Download interactive html](https://github.com/gitfrid/PERT-py/blob/main/D%29%20PERT%20vaccination_vs_reported_cases_dropdown_2000-2023.html) 2000-2023
<br>Download Trends 1980-2023 as interactive HTML-Files from [root directory](https://github.com/gitfrid/PERT-py/tree/main) for visualizing the downloaded CSV data with trend lines 
<br>
_________________________________________


