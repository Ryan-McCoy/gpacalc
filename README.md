# GPA Calculator

This is a simple GPA calculator

## Usage guide

Place all grades in .csv files in the grades folder. See grades.csv.example for an example format
All classes that start with AP will recieve an AP weight, and all classes that start with Honors will recieve an Honors weight. Capitalization doesn't matter.
GPAs will be calculated using Brophy College Preparatory's standards. Changes can be made by changing mostly the `getgp(gr)` function.
Append `-u` to the command to calculate the unweighted GPA. By default, the weighted GPA is calculated.
