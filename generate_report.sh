#!/bin/bash

# Step 1: Clear old Allure results
echo "Cleaning old Allure results..."
rm -rf reports/allure-results
rm -rf reports/allure-report

# Step 2: Run Behave tests with Allure formatter
echo "Running Behave tests..."
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results

# Step 3: Generate Allure HTML report
echo "Generating Allure report..."
allure generate reports/allure-results -o reports/allure-report --clean

# Step 4: Notify user
echo "Allure report generated. Open it with: allure open reports/allure-report"