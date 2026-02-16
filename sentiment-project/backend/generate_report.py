from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from datetime import date
import os

def create_report():
    doc = Document()
    
    # Define styles
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)

    # Title Page
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title_p.add_run('\n\n\n\nAcademic Project Report')
    run.font.size = Pt(16)
    
    project_title = doc.add_paragraph()
    run = project_title.add_run('\nDepression Sentiment Analysis Using Support Vector Machine')
    run.bold = True
    run.font.size = Pt(24)
    project_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # User Details
    details_p = doc.add_paragraph()
    details_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = details_p.add_run(f'\n\n\nPresented by: Tejeshwar\nDate: {date.today().strftime("%B %d, %Y")}')
    run.font.size = Pt(14)
    
    doc.add_page_break()

    # 1. Abstract
    doc.add_heading('1. Abstract', level=1)
    doc.add_paragraph(
        "Mental health assessment through digital footprints has become a critical area of research. "
        "This project presents an automated sentiment analysis system designed to classify text-based messages into depressive and non-depressive categories. "
        "Utilizing a dataset of over 10,000 labeled instances, the methodology employs NLP techniques for data preprocessing, "
        "TF-IDF vectorization for feature extraction, and a Support Vector Machine (SVM) classifier. "
        "The model achieved an accuracy of approximately 99%. The implementation includes a Flask-based REST API and a modern web frontend."
    )

    # 2. Introduction
    doc.add_heading('2. Introduction', level=1)
    doc.add_paragraph(
        "Artificial Intelligence (AI) and Machine Learning (ML) have revolutionized behavioral analysis. "
        "One of the most profound applications is in early depression detection. Depression is characterized by persistent sadness and lack of interest. "
        "Sentiment analysis provides tools to programmatically interpret psychological states through linguistic patterns. "
        "This project leverages SVM to build a high-accuracy classification system."
    )

    # 3. Problem Statement
    doc.add_heading('3. Problem Statement', level=1)
    doc.add_paragraph(
        "The primary challenge is the binary classification of textual data into depressive or non-depressive categories. "
        "Distinguishing between temporary sadness and persistent depressive sentiment is nuanced. "
        "Data imbalance (3.5 to 1 ratio) further complicates reliable detection."
    )

    # 4. Literature Review
    doc.add_heading('4. Literature Review', level=1)
    doc.add_paragraph(
        "Early approaches used lexicon-based methods (predefined dictionaries). Modern ML brought Naive Bayes, Logistic Regression, and SVMs. "
        "SVMs are particularly effective for high-dimensional sparse text data represented via TF-IDF."
    )

    # 5. Dataset Description
    doc.add_heading('5. Dataset Description', level=1)
    doc.add_paragraph(
        "The dataset utilized in this study consists of 10,314 textual records. The class distribution is:\n"
        "• Non-Depressive (0): 8,000 samples\n"
        "• Depressive (1): 2,314 samples\n"
        "This indicates a significant class imbalance that required addressing during training."
    )

    # 6. Methodology
    doc.add_heading('6. Methodology', level=1)
    
    doc.add_heading('6.1 Data Loading and Inspection', level=2)
    doc.add_paragraph("Data was imported from CSV. Initial inspection revealed the text content and corresponding binary labels.")
    
    doc.add_heading('6.2 Data Cleaning', level=2)
    doc.add_paragraph(
        "Raw text data underwent: Lowercasing, Punctuation Removal, and Digit Removal to focus on sentiment-bearing content."
    )
    
    doc.add_heading('6.3 Feature Engineering (TF-IDF)', level=2)
    doc.add_paragraph(
        "TF-IDF was selected for numeric conversion, with max_features set to 5,000 and stop word removal."
    )
    
    doc.add_heading('6.4 Train-Test Split', level=2)
    doc.add_paragraph("80% training / 20% testing split with stratification to maintain class distribution.")
    
    doc.add_heading('6.5 Model Training (SVM)', level=2)
    doc.add_paragraph(
        "LinearSVC with 'class_weight=balanced' was utilized to combat imbalance by adjusting weights inversely to class frequencies."
    )

    # 7. Exploratory Data Analysis (EDA)
    doc.add_heading('7. Exploratory Data Analysis', level=1)
    doc.add_paragraph("Analysis confirmed high-weight keywords in depressive texts (e.g., 'lonely', 'hopeless').")
    
    # Adding Word Cloud if exists
    img_path = 'c:/Users/Administrator/Desktop/sentimental analysis based on tweets/word_cloud.png'
    if os.path.exists(img_path):
        doc.add_paragraph("Visual representation of sentiment vocabulary (Word Cloud):")
        doc.add_picture(img_path, width=Inches(5))
        last_p = doc.paragraphs[-1]
        last_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # 8. Model Evaluation and Results
    doc.add_heading('8. Model Evaluation and Results', level=1)
    doc.add_paragraph(
        "The model achieved 99% accuracy. Below are the performance visualizations for both classes."
    )
    
    # Adding results images
    res_img1 = 'c:/Users/Administrator/Desktop/sentimental analysis based on tweets/depressive_sentiment.png'
    res_img2 = 'c:/Users/Administrator/Desktop/sentimental analysis based on tweets/non_depressive_sentiment.png'
    
    if os.path.exists(res_img1):
        doc.add_paragraph("Binary classification metrics for Depressive class:")
        doc.add_picture(res_img1, width=Inches(4.5))
        last_p = doc.paragraphs[-1]
        last_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
    if os.path.exists(res_img2):
        doc.add_paragraph("Binary classification metrics for Non-Depressive class:")
        doc.add_picture(res_img2, width=Inches(4.5))
        last_p = doc.paragraphs[-1]
        last_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # 9. System Architecture
    doc.add_heading('9. System Architecture', level=1)
    doc.add_paragraph(
        "Full-stack application using Flask (REST API) and a modern web interface (HTML5, CSS3, Vanilla JS). "
        "Models are loaded via joblib for persistent inference."
    )

    # 10. Limitations
    doc.add_heading('10. Limitations', level=1)
    doc.add_paragraph(
        "• Dataset Bias: Dependent on training corpus.\n"
        "• Overfitting: High accuracy may require more out-of-domain testing.\n"
        "• Ethics: Not a replacement for professional human diagnosis.\n"
        "• Semantics: Lacks Transformer-level contextual depth."
    )

    # 11. Future Scope
    doc.add_heading('11. Future Scope', level=1)
    doc.add_paragraph(
        "Future move toward LSTM/BERT, Cloud deployment (AWS/Azure), and multi-class emotion detection."
    )

    # 12. Conclusion
    doc.add_heading('12. Conclusion', level=1)
    doc.add_paragraph(
        "The project successfully implemented a reliable depression sentiment analysis system. "
        "It serves as an accessible first line of detection for AI-driven mental health support tools."
    )

    # Save the document
    doc_path = 'c:/Users/Administrator/Desktop/sentimental analysis based on tweets/Academic_Project_Report_Final.docx'
    doc.save(doc_path)
    return doc_path

path = create_report()
print(f"Report generated at: {path}")
