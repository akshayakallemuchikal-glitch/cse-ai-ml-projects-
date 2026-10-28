def ai_predict_performance():
    print("=== AI Student Performance Predictor ===")
    print("This AI predicts Pass/Fail using marks\n")
    
    name = input("Enter student name: ")
    attendance = int(input("Enter attendance % (0-100): "))
    assignment = int(input("Enter assignment marks (0-100): "))
    internal = int(input("Enter internal exam marks (0-100): "))
    
    # AI Logic - weighted calculation like ML model
    # Weights: attendance 20%, assignment 30%, internal 50%
    score = (attendance * 0.2) + (assignment * 0.3) + (internal * 0.5)
    
    print(f"\n--- AI Analysis for {name} ---")
    print(f"AI Score: {score:.2f}/100")
    
    # AI Decision Boundary
    if score >= 75:
        result = "Excellent - Distinction (AI Prediction: Top Performer)"
        suggestion = "Keep it up! You can be a topper."
    elif score >= 60:
        result = "Good - First Class (AI Prediction: Will PASS)"
        suggestion = "Good job! Focus a bit more."
    elif score >= 40:
        result = "Average - Second Class (AI Prediction: PASS but risk)"
        suggestion = "AI suggests: Need more study time."
    else:
        result = "Fail Risk (AI Prediction: Needs Improvement)"
        suggestion = "AI Alert: Low attendance & marks - Improve fast!"
    
    print(f"Result: {result}")
    print(f"AI Suggestion: {suggestion}")
    
    # AI Feature Importance
    print("\n--- AI Insights ---")
    if attendance < 75:
        print("⚠️ Low attendance affecting score!")
    if assignment < 50:
        print("⚠️ Assignments need improvement!")
    if internal < 50:
        print("⚠️ Internal marks are low!")

ai_predict_performance()
