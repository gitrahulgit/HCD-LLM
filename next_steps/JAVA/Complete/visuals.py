# import json
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load the JSON data
# file_path = r"D:\llm_exam\next_steps\JAVA\Partial\java_students_scores_partial.json" # Replace with the correct file path
# with open(file_path, 'r') as file:
#     data = json.load(file)

# # Process the data into a structured DataFrame
# rows = []
# for iteration in data:
#     iteration_number = iteration["iterationNumber"]
#     if iteration_number > 5:  # Restrict to iterations 1 to 5
#         continue
#     for student in iteration["students"]:
#         student_id = int(student["Student ID"])  # Ensure Student ID is numeric for sorting
#         overall_marks = student["Overall Marks"]
#         modules = student["modules"]
#         for module_name, details in modules.items():
#             rows.append({
#                 "Iteration": iteration_number,
#                 "Student ID": student_id,
#                 "Module": module_name,
#                 "Score": details.get("total", 0),
#                 "Overall Marks": overall_marks
#             })

# df = pd.DataFrame(rows)

# # Sort the DataFrame by Student ID and Iteration
# df = df.sort_values(by=["Student ID", "Iteration"])

# # Overall Marks Comparison
# overall_marks_df = df.groupby(["Iteration", "Student ID"])["Overall Marks"].first().unstack()
# overall_marks_df = overall_marks_df.sort_index(axis=1)  # Ensure Student IDs are sorted
# plt.figure(figsize=(12, 6))
# overall_marks_df.T.plot(marker='o', figsize=(12, 6))
# plt.title("Overall Marks Comparison Across Iterations")
# plt.xlabel("Student ID")
# plt.ylabel("Overall Marks")
# plt.legend(title="Iteration")
# plt.grid(True)
# plt.show()

# # Module-wise Marks Comparison
# module_scores_df = df.pivot_table(index=["Student ID", "Iteration"], columns="Module", values="Score").fillna(0)
# module_scores_df = module_scores_df.sort_index(level="Student ID")  # Sort Student IDs
# for module in module_scores_df.columns:
#     module_trends = module_scores_df[module].unstack()
#     module_trends = module_trends.sort_index(axis=1)  # Ensure Student IDs are sorted
#     module_trends.plot(kind="bar", figsize=(12, 6))
#     plt.title(f"Marks for {module} Across Iterations")
#     plt.xlabel("Student ID")
#     plt.ylabel("Scores")
#     plt.legend(title="Iteration")
#     plt.tight_layout()
#     plt.show()

# # Deviation from Average Marks
# average_scores = df.groupby(["Iteration", "Module"])["Score"].mean().reset_index()
# df_with_avg = pd.merge(df, average_scores, on=["Iteration", "Module"], suffixes=("", "_Avg"))
# df_with_avg["Deviation"] = df_with_avg["Score"] - df_with_avg["Score_Avg"]
# heatmap_data = df_with_avg.pivot_table(index="Student ID", columns="Module", values="Deviation")
# heatmap_data = heatmap_data.sort_index()  # Ensure Student IDs are sorted
# plt.figure(figsize=(14, 8))
# sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, fmt=".2f")
# plt.title("Deviation from Module-Wise Average Across Iterations")
# plt.xlabel("Modules")
# plt.ylabel("Student ID")
# plt.tight_layout()
# plt.show()

# # Module-wise Average and Student-wise Deviation
# module_avg = df.groupby(["Module", "Iteration"])["Score"].mean().unstack()
# module_avg = module_avg.sort_index(axis=1)  # Ensure Iterations are sorted
# plt.figure(figsize=(14, 6))
# module_avg.T.plot(marker='o', figsize=(14, 6))
# plt.title("Module-wise Averages Across Iterations")
# plt.xlabel("Iteration")
# plt.ylabel("Average Scores")
# plt.legend(title="Modules")
# plt.grid(True)
# plt.show()

# # Display module-wise deviation table
# module_deviation_table = df_with_avg.pivot_table(index=["Student ID"], columns=["Module", "Iteration"], values="Deviation")
# module_deviation_table = module_deviation_table.sort_index()  # Ensure Student IDs are sorted

import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure output directory exists
output_dir = r"D:\llm_exam\next_steps\JAVA\Complete\graphs"
os.makedirs(output_dir, exist_ok=True)

# Load the JSON data
file_path = r"D:\llm_exam\next_steps\JAVA\Complete\java_students_scores.json"
with open(file_path, 'r') as file:
    data = json.load(file)

# Process the data into a structured DataFrame
rows = []
# Get unique student IDs across all iterations
all_student_ids = set()
for iteration in data:
    for student in iteration["students"]:
        all_student_ids.add(int(student["Student ID"]))

# Preprocess to ensure all 5 iterations exist for each student
for iteration_number in range(1, 6):
    for student_id in sorted(all_student_ids):
        # Find the data for this student in this iteration
        student_iteration_data = None
        for iteration in data:
            if iteration["iterationNumber"] == iteration_number:
                for student in iteration["students"]:
                    if int(student["Student ID"]) == student_id:
                        student_iteration_data = student
                        break
                if student_iteration_data:
                    break
        
        # If no data found, create a default entry
        if not student_iteration_data:
            student_iteration_data = {
                "Student ID": student_id,
                "Overall Marks": 0,
                "modules": {module: {"total": 0} for module in set(
                    module 
                    for iteration in data 
                    for student in iteration["students"] 
                    for module in student.get("modules", {}).keys()
                )}
            }
        
        # Process student data
        overall_marks = student_iteration_data["Overall Marks"]
        modules = student_iteration_data["modules"]
        for module_name, details in modules.items():
            rows.append({
                "Iteration": iteration_number,
                "Student ID": student_id,
                "Module": module_name,
                "Score": details.get("total", 0),
                "Overall Marks": overall_marks
            })

# Create DataFrame
df = pd.DataFrame(rows)

# Sort the DataFrame by Student ID and Iteration
df = df.sort_values(by=["Student ID", "Iteration"])

# Overall Marks Comparison
plt.figure(figsize=(16, 8))
overall_marks_df = df.groupby(["Iteration", "Student ID"])["Overall Marks"].first().unstack()
overall_marks_df = overall_marks_df.sort_index(axis=1)  # Ensure Student IDs are sorted
overall_marks_df.T.plot(marker='o', figsize=(16, 8))
plt.title("Overall Marks Comparison Across Iterations")
plt.xlabel("Student ID")
plt.ylabel("Overall Marks")
plt.legend(title="Iteration", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "overall_marks_comparison.png"))
plt.close()

# Module-wise Marks Comparison
# Prepare the module scores DataFrame
module_scores_df = df.pivot_table(
    index=["Student ID", "Iteration"], 
    columns="Module", 
    values="Score"
).fillna(0)
module_scores_df = module_scores_df.sort_index(level="Student ID")

# Plot for each module
for module in module_scores_df.columns:
    plt.figure(figsize=(16, 8))
    module_trends = module_scores_df[module].unstack()
    module_trends = module_trends.sort_index(axis=1)  # Ensure Student IDs are sorted
    module_trends.T.plot(kind="bar", figsize=(16, 8))
    plt.title(f"Marks for {module} Across Iterations")
    plt.xlabel("Iteration")
    plt.ylabel("Scores")
    plt.legend(title="Student ID", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"{module}_marks_comparison.png"))
    plt.close()

# Deviation from Average Marks
average_scores = df.groupby(["Iteration", "Module"])["Score"].mean().reset_index()
df_with_avg = pd.merge(df, average_scores, on=["Iteration", "Module"], suffixes=("", "_Avg"))
df_with_avg["Deviation"] = df_with_avg["Score"] - df_with_avg["Score_Avg"]

# Heatmap of Deviation
plt.figure(figsize=(20, 12))
heatmap_data = df_with_avg.pivot_table(
    index="Student ID", 
    columns="Module", 
    values="Deviation"
)
heatmap_data = heatmap_data.sort_index()  # Ensure Student IDs are sorted
sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, fmt=".2f", cbar_kws={'label': 'Deviation from Average'})
plt.title("Deviation from Module-Wise Average Across Iterations")
plt.xlabel("Modules")
plt.ylabel("Student ID")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "module_deviation_heatmap.png"))
plt.close()

# Module-wise Average Across Iterations
plt.figure(figsize=(16, 8))
module_avg = df.groupby(["Module", "Iteration"])["Score"].mean().unstack()
module_avg = module_avg.sort_index(axis=1)  # Ensure Iterations are sorted
module_avg.T.plot(marker='o', figsize=(16, 8))
plt.title("Module-wise Averages Across Iterations")
plt.xlabel("Iteration")
plt.ylabel("Average Scores")
plt.legend(title="Modules", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "module_averages.png"))
plt.close()

# Save module deviation table to CSV
module_deviation_table = df_with_avg.pivot_table(
    index=["Student ID"], 
    columns=["Module", "Iteration"], 
    values="Deviation"
)
module_deviation_table = module_deviation_table.sort_index()  # Ensure Student IDs are sorted
module_deviation_table.to_csv(os.path.join(output_dir, "module_deviation_table.csv"))

print("Analysis complete. Graphs and data saved in:", output_dir)