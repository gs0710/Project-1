import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(16, 12), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Title & Subtitle
ax.text(50, 97, "EMPLOYEE ATTRITION PROJECT WORKFLOW & ARCHITECTURE", 
        ha='center', va='center', fontsize=18, fontweight='bold', color='#1e3d59')
ax.text(50, 94.5, "Phase 1: Problem Definition & Planning (Current)  vs.  Phase 2: Predictive Modeling (Future)", 
        ha='center', va='center', fontsize=12, style='italic', color='#555555')

# Draw Phase 1 Container Box
p1_box = patches.FancyBboxPatch((4, 28), 92, 63, boxstyle="round,pad=1.5", 
                               edgecolor='#1e3d59', facecolor='#f4f7f9', linewidth=2.5, linestyle='-')
ax.add_patch(p1_box)
ax.text(7, 88.5, "PHASE 1: Problem Definition, Diagnostic EDA, and Governance (Current Assignment Scope)", 
        fontsize=12, fontweight='bold', color='#1e3d59')

# Define Phase 1 steps (3 columns x 4 rows)
steps_p1 = [
    # Column 1
    (8, 77, "1. Business Understanding", "HR Analytics maturity, business case,\nvoluntary vs involuntary attrition"),
    (8, 62, "2. Stakeholder Analysis", "Governance matrix, RBAC tiers,\nretention strategy mapping"),
    (8, 47, "3. Dataset Acquisition", "Verified IBM HR benchmark,\nlicense audit & documentation"),
    (8, 32, "4. Dataset Validation", "Completeness check (0 nulls),\nconstant & ID feature isolation"),

    # Column 2
    (38, 77, "5. Feature Dictionary", "35 attributes cataloged, scales,\nethical tags & modeling roles"),
    (38, 62, "6. Target Definition", "Attrition (Yes/No), 16.12% rate,\n5.2:1 class imbalance analysis"),
    (38, 47, "7. Business KPI Definition", "Standard formulas, denominators,\nsnapshot vs annual nuances"),
    (38, 32, "8. Basic Exploratory Data Analysis", "Overtime, tenure, compensation,\ndepartment & role cross-tabs"),

    # Column 3
    (68, 77, "9. Ethics & Privacy Review", "Protected demographics (Age, Gender),\nprohibition of punitive action"),
    (68, 62, "10. Problem Formulation", "Research questions, assumptions,\nconstraints & success criteria"),
    (68, 47, "11. Project Roadmap", "Gantt timeline, milestones,\ndependencies & deliverables"),
    (68, 32, "12. GitHub Repository Prep", "Academic docs, tests, notebooks,\nreports & clean repository")
]

# Draw Phase 1 Step Cards
card_w = 24
card_h = 10.5

for x, y, title, desc in steps_p1:
    card = patches.FancyBboxPatch((x, y), card_w, card_h, boxstyle="round,pad=0.6",
                                 edgecolor='#1e3d59', facecolor='#ffffff', linewidth=1.5)
    ax.add_patch(card)
    ax.text(x + 1.2, y + 8, title, fontsize=10.5, fontweight='bold', color='#1e3d59')
    ax.text(x + 1.2, y + 4.2, desc, fontsize=8.5, color='#333333', va='center')

# Arrows connecting Phase 1 steps
# Col 1 downward
for y in [77, 62, 47]:
    ax.annotate('', xy=(20, y - 0.5), xytext=(20, y + 1.5),
                arrowprops=dict(facecolor='#1e3d59', edgecolor='#1e3d59', width=1.5, headwidth=6))
# Across col 1 to col 2
ax.annotate('', xy=(38, 37.25), xytext=(32, 37.25),
            arrowprops=dict(facecolor='#1e3d59', edgecolor='#1e3d59', width=1.5, headwidth=6))
# Col 2 upward
for y in [32, 47, 62]:
    ax.annotate('', xy=(50, y + card_h + 1.5), xytext=(50, y + card_h - 0.5),
                arrowprops=dict(facecolor='#1e3d59', edgecolor='#1e3d59', width=1.5, headwidth=6))
# Across col 2 to col 3
ax.annotate('', xy=(68, 82.25), xytext=(62, 82.25),
            arrowprops=dict(facecolor='#1e3d59', edgecolor='#1e3d59', width=1.5, headwidth=6))
# Col 3 downward
for y in [77, 62, 47]:
    ax.annotate('', xy=(80, y - 0.5), xytext=(80, y + 1.5),
                arrowprops=dict(facecolor='#1e3d59', edgecolor='#1e3d59', width=1.5, headwidth=6))

# Transition Arrow from Phase 1 to Phase 2
ax.annotate('', xy=(50, 23.5), xytext=(80, 32),
            arrowprops=dict(facecolor='#d95f02', edgecolor='#d95f02', width=2.5, headwidth=8))
ax.text(68, 25.5, "Handoff to Phase 2", fontsize=9.5, fontweight='bold', color='#d95f02')

# Draw Phase 2 Container Box (Dashed)
p2_box = patches.FancyBboxPatch((4, 3), 92, 19, boxstyle="round,pad=1.5", 
                               edgecolor='#6c757d', facecolor='#fbfbfb', linewidth=2.0, linestyle='--')
ax.add_patch(p2_box)
ax.text(7, 19.5, "PHASE 2: Advanced Machine Learning & Retention Optimization (Future Project Scope)", 
        fontsize=11.5, fontweight='bold', color='#6c757d', style='italic')

# Phase 2 steps
steps_p2 = [
    (6, 6, "13. Preprocessing", "One-hot encoding,\nscaling, SMOTE"),
    (24.5, 6, "14. Model Benchmarks", "Logistic, Trees,\nRandom Forest"),
    (43, 6, "15. Ensembles & Tuning", "XGBoost, LightGBM,\nBayesian Opt"),
    (61.5, 6, "16. Explainability", "SHAP attribution,\nfeature importance"),
    (80, 6, "17. Retention Support", "Ethical intervention,\nsupportive programs")
]

for x, y, title, desc in steps_p2:
    card = patches.FancyBboxPatch((x, y), 16, 11, boxstyle="round,pad=0.5",
                                 edgecolor='#6c757d', facecolor='#ffffff', linewidth=1.2, linestyle='--')
    ax.add_patch(card)
    ax.text(x + 0.8, y + 8, title, fontsize=9.5, fontweight='bold', color='#495057')
    ax.text(x + 0.8, y + 4.5, desc, fontsize=8, color='#666666', va='center')

# Connect Phase 2 steps
for x in [22, 40.5, 59, 77.5]:
    ax.annotate('', xy=(x + 2.5, 11.5), xytext=(x, 11.5),
                arrowprops=dict(facecolor='#6c757d', edgecolor='#6c757d', width=1.2, headwidth=5))

plt.tight_layout()
plt.savefig('diagrams/project_workflow.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved diagrams/project_workflow.png")
