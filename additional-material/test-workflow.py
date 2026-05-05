import os
import joblib
import pandas as pd

# Check if feature importances exist
if hasattr(fitted_workflow, "feature_importances_"):
    importances = fitted_workflow.feature_importances_
    # Optionally, create a sorted table
    feature_importances = pd.DataFrame({
        "feature": fitted_workflow.feature_names_in_,
        "importance": importances
    }).sort_values(by="importance", ascending=False)

    print(feature_importances)
script_dir = "/Users/gabrielbaker/Desktop/AEF2026/AEF-2026-course-homepage/additional-material"
os.chdir(script_dir)



fitted_workflow = joblib.load("fitted_workflow_1987.joblib")

type(fitted_workflow)
print(fitted_workflow)

…
# Check if feature importances exist
if hasattr(fitted_workflow, "feature_importances_"):
    importances = fitted_workflow.feature_importances_
    # Optionally, create a sorted table
    feature_importances = pd.DataFrame({
        "feature": fitted_workflow.feature_names_in_,
        "importance": importances
    }).sort_values(by="importance", ascending=False)

    print(feature_importances)

