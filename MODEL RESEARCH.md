MODEL RESEARCH
AI-Based Threat Detection & Anomaly Analysis Engine
AI-Assisted Threat Detection Dashboard
Prepared By: Neelam Jyothi
Internship: Infosys Springboard Internship
Project: AI-Assisted Threat Detection Dashboard

1. Introduction
Cybersecurity has become one of the most critical challenges in today's digital world. Organizations generate massive amounts of security data from firewalls, intrusion detection systems, authentication logs, antivirus software, cloud services, and network devices. Analyzing this data manually is difficult due to its volume and complexity.
Traditional security systems mainly depend on signature-based or rule-based detection methods, which are effective only for known threats. However, modern cyberattacks such as zero-day exploits, insider threats, ransomware, phishing attacks, and Advanced Persistent Threats (APTs) continuously evolve, making traditional approaches insufficient.
Artificial Intelligence (AI) and Machine Learning (ML) provide intelligent solutions by learning patterns from historical security data and identifying suspicious activities automatically. AI-based threat detection systems can detect abnormal behavior, classify security incidents, estimate risk levels, and assist security analysts in making faster and more accurate decisions.
This report focuses on researching different machine learning models suitable for cyber threat detection and compares their strengths, limitations, and applications to determine the most effective models for an AI-Assisted Threat Detection Dashboard.

2. Research Objectives
The primary objective of this research is to study and compare various Artificial Intelligence and Machine Learning models that can be used for cybersecurity threat detection.
The specific objectives are:
•	Study different supervised and unsupervised machine learning algorithms. 
•	Understand how each model detects cyber threats. 
•	Compare models based on accuracy, speed, scalability, and interpretability. 
•	Analyze the advantages and limitations of each model. 
•	Recommend suitable models for anomaly detection, threat classification, and risk prioritization. 
•	Support the development of an AI-Assisted Threat Detection Dashboard with appropriate AI techniques.
3. Why AI is Needed in Cybersecurity
Modern organizations face thousands of cyber threats every day. Manual monitoring of security logs is time-consuming and often leads to delayed responses. AI helps overcome these challenges by continuously analyzing large volumes of security events and identifying malicious activities in real time.
AI provides several benefits in cybersecurity:
•	Detects unknown and zero-day attacks. 
•	Reduces false-positive alerts. 
•	Improves incident response time. 
•	Automates threat classification. 
•	Learns continuously from new attack patterns. 
•	Supports cybersecurity analysts with intelligent recommendations. 
As cyber threats become increasingly sophisticated, AI-powered monitoring systems are becoming an essential component of modern Security Operations Centers (SOCs).
4. Threat Detection Workflow
The AI-Assisted Threat Detection Dashboard follows a structured workflow for identifying suspicious activities.
Security Logs
        ↓
Data Collection
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Machine Learning Models
        ↓
Threat Detection
        ↓
Risk Scoring
        ↓
Dashboard Visualization
The workflow begins with collecting security logs from various sources. The data is then cleaned, normalized, and transformed into meaningful features before being processed by machine learning models. The detected threats are assigned risk scores and displayed on an interactive dashboard for security analysts.
5. Machine Learning Models Considered
The following machine learning models were selected for research based on their widespread use in cybersecurity applications.
1.	Logistic Regression 
2.	Decision Tree 
3.	Random Forest 
4.	Support Vector Machine (SVM) 
5.	XGBoost 
6.	Isolation Forest 
7.	Autoencoder 
8.	Long Short-Term Memory (LSTM) 
Each model has unique characteristics and is suitable for different cybersecurity tasks such as anomaly detection, threat classification, and risk prediction.
6. Logistic Regression
6.1 Overview
Logistic Regression is a supervised machine learning algorithm used for binary classification. In cybersecurity, it classifies security events as normal or malicious based on probability.
6.2 Working Principle
The model uses a sigmoid function to calculate the probability of an event being a threat. If the probability is above a threshold, it is classified as malicious; otherwise, it is considered normal.
6.3 Advantages
•	Simple and fast 
•	Easy to understand 
•	Good for binary classification 
6.4 Limitations
•	Less effective for complex attacks 
•	Assumes linear relationships 
6.5 Applications
•	Phishing detection 
•	Malware classification 
•	Login analysis 
Diagram
Input Features
      │
      ▼
Logistic Regression
      │
      ▼
Probability Score
      │
 ┌────┴────┐
 ▼         ▼
Normal   Threat
7. Decision Tree
7.1 Overview
Decision Tree is a supervised learning algorithm that classifies data using a tree-like structure of decisions. It is easy to understand and widely used in cybersecurity.
7.2 Working Principle
The model splits the data based on important features until it reaches a final decision of normal or malicious activity.
7.3 Advantages
•	Easy to interpret 
•	Fast prediction 
•	Minimal preprocessing 
7.4 Limitations
•	Can overfit 
•	Less accurate than ensemble models 
7.5 Applications
•	Intrusion detection 
•	Malware detection 
•	Network traffic classification 
Diagram
Security Event
      │
      ▼
Failed Login?
   /      \
 Yes      No
 │         │
Threat   Normal
8. Random Forest
8.1 Overview
Random Forest is a supervised learning algorithm that combines multiple Decision Trees to improve prediction accuracy. It is one of the most widely used models in cybersecurity.
8.2 Working Principle
The model creates several Decision Trees using different subsets of data. Each tree predicts the result, and the final prediction is based on majority voting.
8.3 Advantages
•	High accuracy 
•	Reduces overfitting 
•	Handles large datasets 
8.4 Limitations
•	Requires more memory 
•	Slightly slower training 
8.5 Applications
•	Threat detection 
•	Malware detection 
•	Intrusion detection 
Diagram
Security Data
      │
      ▼
Tree 1   Tree 2   Tree 3
   │        │        │
   └────┬───┴───┬────┘
        ▼
 Majority Vote
        │
        ▼
 Threat / Normal
9. Support Vector Machine (SVM)
9.1 Overview
Support Vector Machine (SVM) is a supervised learning algorithm used for binary classification. It separates normal and malicious activities using an optimal decision boundary.
9.2 Working Principle
SVM identifies the best hyperplane that separates different classes. New security events are classified based on which side of the boundary they fall.
9.3 Advantages
•	High accuracy 
•	Works well with high-dimensional data 
•	Effective for intrusion detection 
9.4 Limitations
•	Slow for large datasets 
•	Requires parameter tuning 
9.5 Applications
•	Intrusion detection 
•	Phishing detection 
•	Malware classification 
Diagram
Security Data
      │
      ▼
     SVM
(Hyperplane)
      │
 ┌────┴────┐
 ▼         ▼
Normal   Threat
10. XGBoost
10.1 Overview
XGBoost is an advanced supervised learning algorithm that builds multiple decision trees sequentially to improve prediction accuracy. It is widely used for threat classification and risk scoring.
10.2 Working Principle
The model creates a series of trees where each new tree corrects the errors of the previous one, resulting in better overall predictions.
10.3 Advantages
•	Very high accuracy 
•	Fast performance 
•	Handles complex datasets 
10.4 Limitations
•	Needs parameter tuning 
•	More computationally intensive 
10.5 Applications
•	Threat classification 
•	Risk scoring 
•	Malware detection 
Diagram
Security Data
      │
      ▼
Tree 1
  │
  ▼
Tree 2
  │
  ▼
Tree 3
  │
  ▼
Final Prediction
11. Isolation Forest
11.1 Overview
Isolation Forest is an unsupervised learning algorithm used for anomaly detection. It identifies unusual activities by isolating them from normal data.
11.2 Working Principle
The model creates multiple random trees. Activities that are isolated quickly are considered anomalies and flagged as potential threats.
11.3 Advantages
•	Detects unknown attacks 
•	No labeled data required 
•	Fast for large datasets 
11.4 Limitations
•	Does not classify attack types 
•	Sensitive to parameter settings 
11.5 Applications
•	Insider threat detection 
•	Network anomaly detection 
•	Fraud detection 
Diagram
Security Data
      │
      ▼
Isolation Trees
      │
      ▼
Anomaly Score
      │
 ┌────┴────┐
 ▼         ▼
Normal   Threat

12. Autoencoder
12.1 Overview
An Autoencoder is an unsupervised deep learning model used for anomaly detection. It learns normal patterns in security data and identifies unusual activities by measuring reconstruction error.
12.2 Working Principle
The model compresses input data using an Encoder and reconstructs it using a Decoder. If the reconstruction error is high, the activity is considered suspicious.
12.3 Advantages
•	Detects unknown attacks. 
•	Works well with large datasets. 
•	Does not require labeled attack data. 
12.4 Limitations
•	Requires high computational power. 
•	Longer training time. 
12.5 Applications
•	Network anomaly detection 
•	Insider threat detection 
•	Fraud detection 
12.6 Diagram
Input Data
     │
     ▼
  Encoder
     │
     ▼
Compressed Data
     │
     ▼
  Decoder
     │
     ▼
Reconstructed Data
     │
     ▼
High Error → Threat
Low Error → Normal
13. Long Short-Term Memory (LSTM)
13.1 Overview
LSTM is a deep learning model designed to analyze sequential data. It is useful for detecting cyberattacks that occur over a series of events.
13.2 Working Principle
LSTM stores previous information using memory cells and analyzes sequences of security events to identify suspicious patterns.
13.3 Advantages
•	Learns long-term patterns. 
•	Effective for network traffic analysis. 
•	High accuracy on sequential data. 
13.4 Limitations
•	Requires large datasets. 
•	Slow training process. 
13.5 Applications
•	Intrusion detection 
•	User behavior analysis 
•	DDoS detection 
•	Attack sequence detection 
13.6 Diagram
Security Event 1
       │
       ▼
    LSTM Cell
       │
       ▼
Security Event 2
       │
       ▼
    LSTM Cell
       │
       ▼
Threat Prediction






14. Comparison of AI Models
Model	Type	Main Use	Advantages	Limitations
Logistic Regression	Supervised	Binary Classification	Simple and Fast	Less effective for complex attacks
Decision Tree	Supervised	Threat Classification	Easy to understand	Can overfit
Random Forest	Supervised	Threat Detection	High Accuracy	More memory required
SVM	Supervised	Intrusion Detection	Works well with high-dimensional data	Slow on large datasets
XGBoost	Supervised	Risk Prediction	Excellent Performance	Needs parameter tuning
Isolation Forest	Unsupervised	Anomaly Detection	Detects unknown attacks	Doesn't classify attack types
Autoencoder	Deep Learning	Anomaly Detection	Learns complex patterns	High computational cost
LSTM	Deep Learning	Sequential Attack Detection	Good for time-series data	Requires large datasets
15. Selected Models for the Project
Based on the research, the following models are selected for the AI-Assisted Threat Detection Dashboard:
•	Isolation Forest – Detects abnormal and unknown security activities. 
•	Random Forest – Classifies security events as normal or malicious. 
•	XGBoost – Calculates threat confidence and risk scores. 
•	LSTM – Detects attack patterns occurring over time. 
Using multiple models improves the accuracy and reliability of the threat detection system.


16. Conclusion
This model research compared various machine learning and deep learning algorithms used in cybersecurity. Each model has its own strengths and limitations. Random Forest provides accurate threat classification, Isolation Forest is effective for anomaly detection, XGBoost performs well in risk scoring, and LSTM is suitable for sequential attack analysis.
A combination of these models is recommended for developing an AI-Assisted Threat Detection Dashboard because it can improve detection accuracy, reduce false alarms, and support faster cybersecurity decision-making.
17. References
1.	Ian Goodfellow, Yoshua Bengio, Aaron Courville. Deep Learning. MIT Press. 
2.	Aurélien Géron. Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow. 
3.	CIC-IDS2017 Dataset Documentation. 
4.	UNSW-NB15 Dataset Documentation. 
5.	MITRE ATT&CK Framework Documentation. 
6.	Common Vulnerabilities and Exposures (CVE) Database. 
7.	Scikit-learn Documentation. 
8.	XGBoost Official Documentation.






