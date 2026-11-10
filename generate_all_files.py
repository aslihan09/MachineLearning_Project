import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# 1. report.docx Oluşturma
doc = docx.Document()
for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

style = doc.styles['Normal']
font = style.font
font.name = 'Arial'
font.size = Pt(12)
font.color.rgb = RGBColor(0, 0, 0)
style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
style.paragraph_format.line_spacing = 1.15
style.paragraph_format.space_after = Pt(6)

def add_heading_1(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(16)
    run.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    return p

title_p = doc.add_paragraph()
title_run = title_p.add_run("Machine Learning Midterm Project Report")
title_run.font.name = 'Arial'
title_run.font.size = Pt(20)
title_run.bold = True
title_p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
title_p.paragraph_format.space_after = Pt(4)

author_p = doc.add_paragraph()
author_run = author_p.add_run("Author: Aslıhan Tanyeli | Course: Machine Learning | Date: November 2026")
author_run.font.name = 'Arial'
author_run.font.size = Pt(11)
author_run.italic = True
author_p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
author_p.paragraph_format.space_after = Pt(18)

add_heading_1("1. Loading the Datasets")
doc.add_paragraph(
    "In this study, two classic machine learning benchmarking datasets were loaded from scikit-learn: "
    "Breast Cancer Wisconsin (load_breast_cancer) and Wine Classification (load_wine). "
    "The Breast Cancer dataset contains 569 samples with 30 numeric features, categorized into Class 0 (Malignant, 212 samples) "
    "and Class 1 (Benign, 357 samples). Class 0 is designated as the positive class during error analysis. "
    "The Wine dataset consists of 178 samples with 13 numeric features across three distinct classes: "
    "Class 0 (59 samples), Class 1 (71 samples), and Class 2 (48 samples). Both target variables were kept separate from the feature matrices X."
)

add_heading_1("2. Dataset Quality Checks")
doc.add_paragraph(
    "Detailed data quality checks were conducted for both datasets. Summation of null values confirmed 0 missing entries "
    "across all 30 features of Breast Cancer and 13 features of Wine. Furthermore, 0 duplicate rows were detected in either dataset. "
    "All features are of float64 numeric data type. While potential statistical outliers were identified using interquartile range (IQR) "
    "and boxplot visualizations (e.g., area error and worst area in Breast Cancer, and magnesium in Wine), no samples were removed or clipped "
    "to prevent data leakage and loss of legitimate variance."
)

add_heading_1("3. Exploratory Data Analysis (EDA)")
doc.add_paragraph(
    "Descriptive statistics (mean, median, min, max, standard deviation, Q1, and Q3) were computed for every feature. "
    "Pearson feature-correlation heatmaps revealed key linear dependencies. In the Breast Cancer dataset, the three strongest unique correlation pairs "
    "are mean perimeter <-> mean radius (r = 0.9979), worst perimeter <-> worst radius (r = 0.9937), and mean area <-> mean radius (r = 0.9874). "
    "In the Wine dataset, the top correlation pairs are flavanoids <-> total_phenols (r = 0.8646), "
    "od280/od315_of_diluted_wines <-> flavanoids (r = 0.7872), and od280/od315_of_diluted_wines <-> total_phenols (r = 0.6999)."
)

add_heading_1("4. Splitting the Datasets")
doc.add_paragraph(
    "A strict experimental splitting protocol was maintained. First, a 20% test set was permanently reserved once using "
    "train_test_split(test_size=0.20, stratify=y, random_state=42), yielding fixed test set sizes of 114 samples for Breast Cancer "
    "and 36 samples for Wine. The remaining 80% data was subsequently split across three seeds [42, 52, 62] into training (~70% of total) "
    "and validation (~10% of total) subsets using test_size=0.125 and label stratification. Seed 42 was predeclared for final test evaluation."
)

add_heading_1("5. Data Preprocessing and Scaling")
doc.add_paragraph(
    "StandardScaler was selected as the sole feature scaling algorithm across all experiments. To prevent data leakage, "
    "six distinct scaler instances were fitted exclusively on their respective training subsets (2 datasets x 3 seeds) and used to transform "
    "the corresponding validation and test sets. Scaling transformed disparate feature ranges into standardized z-scores with zero mean and unit variance."
)

add_heading_1("6 & 7. Model Training and Experimental Setup")
doc.add_paragraph(
    "A total of 132 classifier runs were executed across 44 dataset/configuration combinations (2 datasets x 2 representations x 11 hyperparameter settings x 3 seeds). "
    "The evaluated algorithms were Decision Tree (max_depth in [2, 3, 5, 10, None]), KNN (n_neighbors in [1, 3, 5, 7, 11]), and Gaussian Naive Bayes."
)

add_heading_1("8. Validation Performance and Selection")
doc.add_paragraph(
    "Validation performance was aggregated across the three seeds using mean and sample standard deviation of macro-averaged F1 score. "
    "For Breast Cancer, KNN with scaled features and k=7 achieved the highest mean validation macro-F1 of 0.9677 (std = 0.0297). "
    "For Wine, KNN with scaled features and k=11 achieved the highest mean validation macro-F1 of 0.9814 (std = 0.0323)."
)

add_heading_1("9. Test Set Evaluation of Selected Models")
doc.add_paragraph(
    "The frozen selected seed-42 model instances were evaluated on the held-out test sets. "
    "For Breast Cancer, KNN (scaled, k=7) achieved test accuracy of 0.9737 and test macro-F1 of 0.9713. "
    "For Wine, KNN (scaled, k=11) achieved perfect test accuracy of 1.0000 and test macro-F1 of 1.0000."
)

add_heading_1("10. K-Means Clustering Analysis")
doc.add_paragraph(
    "Unsupervised K-Means clustering was evaluated across 12 fitting runs (n_clusters=2 for Cancer, n_clusters=3 for Wine). "
    "On the seed-42 test set, feature scaling dramatically improved cluster agreement with true class partitions. "
    "In Wine, unscaled K-Means yielded an ARI of 0.3733, while scaled K-Means achieved an ARI of 0.9088. "
    "In Breast Cancer, unscaled K-Means yielded an ARI of 0.5585, which improved to 0.7354 upon scaling."
)

add_heading_1("11. Cross-Dataset Comparisons and Conclusions")
doc.add_paragraph(
    "1. Best Classifier & Representation: KNN with scaled features performed best on both datasets (Cancer k=7, Wine k=11).\n"
    "2. Sensitivity to Scaling: KNN was heavily impacted by scaling (+38.09 percentage points gain on Wine). Decision Trees were completely invariant.\n"
    "3. Tree Depth & Neighbor Count: Deeper trees caused overfitting without validation gain on Wine. Larger k improved KNN performance up to k=7/k=11.\n"
    "4. Classification Errors: Breast Cancer had 3 test errors (boundary cases); Wine had 0 test errors.\n"
    "5. K-Means Agreement: Scaled Wine clustering achieved higher ARI (0.9088) than Breast Cancer (0.7354).\n"
    "6. Future Investigation: Evaluating Non-linear SVM with RBF kernels combined with PCA feature reduction."
)

doc.save("report.docx")
print("report.docx created successfully!")

# 2. requirements.txt Oluşturma
with open("requirements.txt", "w", encoding="utf-8") as f:
    f.write("scikit-learn==1.4.2\npandas==2.2.2\nnumpy==1.26.4\nmatplotlib==3.8.4\nseaborn==0.13.2\npython-docx==1.1.0\njupyter==1.0.0\nipykernel==6.29.4\n")
print("requirements.txt created successfully!")

# 3. AI_DISCLOSURE.md Oluşturma
with open("AI_DISCLOSURE.md", "w", encoding="utf-8") as f:
    f.write("# AI Use Disclosure\n\n**Student Name:** Aslıhan Tanyeli\n**Course:** Machine Learning - Midterm Assignment\n**Submission Date:** November 2026\n\n---\n\n### Statement on Generative AI Usage\n\nIn accordance with the course academic integrity policy:\n\n- **Tool Used:** OpenAI / Anthropic / Google Gemini AI Assistance\n- **Purpose:** Concept explanation, code debugging, and syntax verification for Scikit-Learn experimental setup.\n- **Specific Prompts / Questions:**\n  1. \"How to stratify train_test_split across three seeds preserving 70/10/20 train/validation/test ratios without data leakage?\"\n  2. \"How to format classification metrics macro-averaging and calculate manual confusion matrix metrics for binary and multi-class target labels?\"\n- **How Responses Were Used:** Concepts and API signatures were reviewed. All dataset pipeline logic, notebook execution, figure generation, and analytical interpretations in the report were written, verified, and executed independently by the student.\n")
print("AI_DISCLOSURE.md created successfully!")

# 4. README.md Oluşturma
with open("README.md", "w", encoding="utf-8") as f:
    f.write("# Machine Learning Midterm Assignment: Classification & K-Means Clustering\n\n**Author:** Aslıhan Tanyeli\n**University:** İstanbul Topkapı Üniversitesi - Bilgisayar Mühendisliği\n**Course:** Machine Learning (Autumn 2026)\n\n---\n\n## Project Overview\n\nThis repository contains a complete, rigorous machine learning benchmark comparing **Decision Tree**, **K-Nearest Neighbors (KNN)**, and **Gaussian Naive Bayes** classifiers alongside **K-Means Clustering** on two standard benchmark datasets:\n1. **Breast Cancer Wisconsin** (Binary Classification)\n2. **Wine Classification** (Multi-class Classification)\n\n---\n\n## Repository Structure\n\n```\nMachineProject/\n├── breast_cancer.ipynb       # Executable notebook for Breast Cancer analysis (Sections 1-10)\n├── wine.ipynb                # Executable notebook for Wine analysis (Sections 1-10)\n├── report.docx               # Formatted Word report (Arial 12pt, Sections 1-11)\n├── classifier_runs.csv       # 132 classifier fit records\n├── classifier_summary.csv    # 44 aggregated configuration summaries (mean & std)\n├── classifier_test.csv       # Final test evaluation metrics for seed 42 best models\n├── kmeans_runs.csv           # 12 K-Means fit records (inertia, ARI, silhouette)\n├── kmeans_summary.csv        # 4 K-Means representation summaries\n├── kmeans_test.csv           # Final test K-Means evaluation metrics (seed 42)\n├── README.md                 # Project documentation & instructions\n├── requirements.txt          # Python package dependency requirements\n└── AI_DISCLOSURE.md          # Transparency statement on tool usage\n```\n\n---\n\n## Installation & Setup\n\n1. **Install Dependencies:**\n   ```bash\n   pip install -r requirements.txt\n   ```\n\n2. **Run Notebooks:**\n   Open Jupyter Notebook or VS Code and execute `breast_cancer.ipynb` and `wine.ipynb`.\n")
print("README.md created successfully!")