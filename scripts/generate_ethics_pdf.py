import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        if self._pageNumber == 1:
            return  # Skip cover page
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#555555"))
        
        # Header
        self.drawString(54, 11 * 72 - 36, "Ethical Considerations in Employee Attrition Analytics")
        self.setStrokeColor(colors.HexColor("#cccccc"))
        self.setLineWidth(0.5)
        self.line(54, 11 * 72 - 42, 8.5 * 72 - 54, 11 * 72 - 42)
        
        # Footer
        self.line(54, 48, 8.5 * 72 - 54, 48)
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * 72 - 54, 34, page_str)
        self.drawString(54, 34, "CONFIDENTIAL - WORKFORCE GOVERNANCE & ETHICS BASELINE")
        self.restoreState()

def build_ethics_pdf():
    os.makedirs('reports', exist_ok=True)
    pdf_path = 'reports/ethics_report.pdf'
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=30,
        textColor=colors.HexColor('#1e3d59'),
        alignment=0,
        spaceAfter=12
    )
    
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#555555'),
        spaceAfter=24
    )
    
    meta_style = ParagraphStyle(
        'CoverMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=15,
        textColor=colors.HexColor('#333333')
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=colors.HexColor('#1e3d59'),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#2b5c8f'),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#222222'),
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=body_style,
        leftIndent=15,
        bulletIndent=5,
        spaceAfter=4
    )

    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#8c2d19')
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#222222')
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    story = []

    # --- COVER PAGE ---
    story.append(Spacer(1, 40))
    story.append(Paragraph("ACADEMIC & PROFESSIONAL GOVERNANCE REPORT", ParagraphStyle('PreTitle', fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor('#d95f02'), spaceAfter=8)))
    story.append(Paragraph("Ethical Considerations in Employee Attrition Analytics", title_style))
    story.append(HRFlowable(width="100%", thickness=3, color=colors.HexColor('#1e3d59'), spaceAfter=15))
    story.append(Paragraph("Privacy Safeguards, Algorithmic Fairness Audits, and Responsible Use Protocols for Workforce Predictive Modeling", subtitle_style))
    
    story.append(Spacer(1, 120))
    
    meta_text = """
    <b>Project Title:</b> Employee Attrition Problem Definition and Planning<br/>
    <b>Domain:</b> People Analytics, Algorithmic Ethics & HR Governance<br/>
    <b>Benchmark Dataset:</b> IBM HR Analytics Employee Attrition (1,470 Records, 35 Attributes)<br/>
    <b>Author / Role:</b> Senior HR Data Analyst & Lead People Analytics Specialist<br/>
    <b>Version:</b> 1.0 (Final Formal Submission)<br/>
    <b>Publication Date:</b> Academic Term 2026
    """
    story.append(Paragraph(meta_text, meta_style))
    story.append(PageBreak())

    # --- PAGE 2: EXECUTIVE SUMMARY & PRIVACY ---
    story.append(Paragraph("1. Executive Summary & Foundational Principles", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2b5c8f'), spaceAfter=8))
    story.append(Paragraph(
        "Workforce analytics operates directly at the intersection of enterprise business strategy and individual human dignity. "
        "Unlike abstract physical or financial systems, people analytics deals with personal livelihood, career opportunities, and psychological safety. "
        "Deploying analytical models on employee data without explicit ethical constraints introduces catastrophic risks: algorithmic discrimination, "
        "surveillance anxiety, self-fulfilling negative prophecies, and legal liability under civil rights and privacy statutes.",
        body_style
    ))
    story.append(Paragraph(
        "This report formalizes the ethical, legal, and operational governance framework governing the Employee Attrition Analytics project. "
        "It defines strict data minimization rules, evaluates fairness across protected demographics (Age, Gender, Marital Status), "
        "codifies an absolute prohibition on punitive employment actions, and establishes a practical pre-deployment ethics checklist.",
        body_style
    ))

    story.append(Spacer(1, 6))
    story.append(Paragraph("2. Privacy, Confidentiality, and Data Minimization", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2b5c8f'), spaceAfter=8))
    story.append(Paragraph(
        "In accordance with modern privacy standards (GDPR, CCPA/CPRA, and standard enterprise governance), workforce analytics must honor three foundational privacy principles:",
        body_style
    ))
    story.append(Paragraph("<b>1. Data Minimization:</b> Only features strictly necessary to understand organizational retention drivers are admitted into analytical pipelines. Administrative features with zero predictive value (e.g. <code>EmployeeCount</code>, <code>StandardHours</code>) are purged.", bullet_style))
    story.append(Paragraph("<b>2. Purpose Limitation:</b> Employee records gathered for payroll, administration, or pulse surveys are processed strictly for supportive retention planning. Secondary repurposing (e.g. covert productivity tracking) is expressly banned.", bullet_style))
    story.append(Paragraph("<b>3. Pseudonymization & Severance of Direct Identifiers:</b> Direct identifiers (such as <code>EmployeeNumber</code>, employee names, and contact details) are completely stripped from analytical sandboxes. A cryptographic pseudonymization key is held in an isolated security vault by IT systems administrators.", bullet_style))
    story.append(Paragraph("<b>4. Safe Aggregate Reporting (k-Anonymity):</b> In small organizational cohorts (e.g. Human Resources with 63 employees, or specialized job roles), individual identities can be inferred from demographic intersections. Strict cell suppression (minimum cohort size k &ge; 5) is enforced across all reporting.", bullet_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("3. Fairness, Bias, and Protected Demographics", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2b5c8f'), spaceAfter=8))
    story.append(Paragraph(
        "Historical HR data inevitably reflects past organizational decisions, societal dynamics, and managerial habits. "
        "If historic promotions or workload allocations were uneven, an uncritical algorithm will internalize and perpetuate those patterns under the guise of statistical objectivity.",
        body_style
    ))
    story.append(Paragraph(
        "The benchmark dataset was audited across three legally protected demographic dimensions:",
        body_style
    ))

    # Audit table
    audit_data = [
        [Paragraph("Demographic Attribute", table_header), Paragraph("Observed Categories", table_header), Paragraph("Attrition Rate (%)", table_header), Paragraph("Legal & Ethical Guardrail", table_header)],
        [Paragraph("<b>Age</b><br/>(18 to 60 years)", table_cell), Paragraph("Retained Mean: 37.6 yrs<br/>Departed Mean: 33.6 yrs", table_cell), Paragraph("Higher turnover among early-career staff (&le;30 yrs)", table_cell), Paragraph("Protected under ADEA (40+ yrs). Retention initiatives must not exclusively favor younger workers.", table_cell)],
        [Paragraph("<b>Gender</b><br/>(Binary in dataset)", table_cell), Paragraph("Male (n=882, 60%)<br/>Female (n=588, 40%)", table_cell), Paragraph("Male: 17.01%<br/>Female: 14.80%", table_cell), Paragraph("Protected under Title VII & Equal Pay Act. Gender must NEVER be used to score risk or alter pay.", table_cell)],
        [Paragraph("<b>Marital Status</b>", table_cell), Paragraph("Single (n=470)<br/>Married (n=673)<br/>Divorced (n=327)", table_cell), Paragraph("Single: 25.53%<br/>Married: 12.48%<br/>Divorced: 10.09%", table_cell), Paragraph("Personal demographic. Single employees must not face bias regarding travel or overtime expectations.", table_cell)]
    ]
    t = Table(audit_data, colWidths=[100, 110, 120, 174])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3d59')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dddddd')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#1e3d59')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t)

    story.append(PageBreak())

    # --- PAGE 3: PROHIBITION ON PUNITIVE ACTION & CHECKLIST ---
    story.append(Paragraph("4. Strict Prohibition on Punitive Employment Actions", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2b5c8f'), spaceAfter=8))
    
    # Red Callout Box
    ban_box_data = [[
        Paragraph(
            "<b>MANDATORY GOVERNANCE CLAUSE: STRICT PROHIBITION ON PUNITIVE USE</b><br/><br/>"
            "Exploratory attrition findings, risk classifications, or future predictive flight-risk scores "
            "<b>MUST NEVER BE USED</b> as the sole basis, or as a contributing factor, for any adverse employment action, including:<br/>"
            "• Termination, layoff, or involuntary separation.<br/>"
            "• Disciplinary reprimands or performance improvement plans (PIPs).<br/>"
            "• Denial of promotions, salary hikes, equity awards, or lateral transfers.<br/>"
            "• Preemptive assignment of undesirable shifts, projects, or travel obligations.<br/><br/>"
            "<b>Permitted Use:</b> Analytics must be channeled exclusively into supportive, systemic enhancements: workload balancing, "
            "management coaching academies, compensation benchmarking, and early-career mentorship programs.",
            callout_style
        )
    ]]
    ban_table = Table(ban_box_data, colWidths=[504])
    ban_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#fdf2f0')),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#d95f02')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(ban_table)

    story.append(Spacer(1, 10))
    story.append(Paragraph("5. Practical Pre-Deployment Ethics Checklist", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2b5c8f'), spaceAfter=8))
    story.append(Paragraph("Before any analytical model or retention intervention is transitioned into organizational practice, the People Analytics Governance Board must certify completion of this 10-point checklist:", body_style))

    checklist_data = [
        [Paragraph("Checkpoint Category", table_header), Paragraph("Evaluation Requirement", table_header), Paragraph("Responsible Role", table_header), Paragraph("Status", table_header)],
        [Paragraph("1. Data Authorization", table_cell), Paragraph("Legal review completed confirming lawful basis for processing.", table_cell), Paragraph("Legal & Privacy", table_cell), Paragraph("Verified [x]", table_cell)],
        [Paragraph("2. Purpose Limitation", table_cell), Paragraph("Scope restricted strictly to voluntary retention planning.", table_cell), Paragraph("People Analytics", table_cell), Paragraph("Verified [x]", table_cell)],
        [Paragraph("3. Data Hygiene", table_cell), Paragraph("100% missing-value audit; constants and IDs isolated.", table_cell), Paragraph("Data Science", table_cell), Paragraph("Verified [x]", table_cell)],
        [Paragraph("4. Identifier Severance", table_cell), Paragraph("EmployeeNumber stripped from analytical modeling sandboxes.", table_cell), Paragraph("Data Engineering", table_cell), Paragraph("Verified [x]", table_cell)],
        [Paragraph("5. Cell Suppression", table_cell), Paragraph("Minimum cohort threshold (k &ge; 5) applied to all reporting.", table_cell), Paragraph("Analytics Lead", table_cell), Paragraph("Verified [x]", table_cell)],
        [Paragraph("6. Demographic Parity", table_cell), Paragraph("Audits completed across Age, Gender, and Marital Status.", table_cell), Paragraph("Ethics Board", table_cell), Paragraph("Verified [x]", table_cell)],
        [Paragraph("7. Non-Punitive Clause", table_cell), Paragraph("Executive sign-off prohibiting adverse personnel actions.", table_cell), Paragraph("CHRO & Legal", table_cell), Paragraph("Verified [x]", table_cell)],
        [Paragraph("8. Role-Based Access", table_cell), Paragraph("Access tiers enforced; frontline managers denied raw risk scores.", table_cell), Paragraph("IT Security", table_cell), Paragraph("Verified [x]", table_cell)],
        [Paragraph("9. Explainability", table_cell), Paragraph("Feature attribution (SHAP) required; black-box models barred.", table_cell), Paragraph("Lead Data Scientist", table_cell), Paragraph("Verified [x]", table_cell)],
        [Paragraph("10. Employee Notice", table_cell), Paragraph("Workforce policy published explaining retention objectives.", table_cell), Paragraph("Internal Comms", table_cell), Paragraph("Verified [x]", table_cell)],
    ]
    chk_table = Table(checklist_data, colWidths=[105, 204, 115, 80])
    chk_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3d59')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e0e0e0')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#1e3d59')),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(chk_table)

    story.append(Spacer(1, 10))
    story.append(Paragraph("6. Conclusion & Governance Sign-Off", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#2b5c8f'), spaceAfter=6))
    story.append(Paragraph(
        "Ethical workforce analytics is not a bureaucratic obstacle; it is the essential bedrock of trust. "
        "By enforcing data minimization, auditing protected demographics, and guaranteeing supportive-only interventions, "
        "the organization establishes a credible, legally sound, and humane retention intelligence program.",
        body_style
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("Successfully built reports/ethics_report.pdf")

if __name__ == '__main__':
    build_ethics_pdf()
