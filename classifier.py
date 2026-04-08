data = [
    {"Post_Type": "Reel", "Time": "Night", "Hashtags": 8, "Caption_Length": 120, "Engagement": "High"},
    {"Post_Type": "Reel", "Time": "Night", "Hashtags": 6, "Caption_Length": 100, "Engagement": "High"},
    {"Post_Type": "Image", "Time": "Day", "Hashtags": 3, "Caption_Length": 50, "Engagement": "Low"},
    {"Post_Type": "Carousel", "Time": "Evening", "Hashtags": 5, "Caption_Length": 80, "Engagement": "High"},
    {"Post_Type": "Reel", "Time": "Day", "Hashtags": 2, "Caption_Length": 40, "Engagement": "Low"},
    {"Post_Type": "Image", "Time": "Night", "Hashtags": 7, "Caption_Length": 110, "Engagement": "High"},
    {"Post_Type": "Carousel", "Time": "Day", "Hashtags": 2, "Caption_Length": 60, "Engagement": "Low"},
    {"Post_Type": "Reel", "Time": "Evening", "Hashtags": 6, "Caption_Length": 90, "Engagement": "High"},
    {"Post_Type": "Image", "Time": "Evening", "Hashtags": 4, "Caption_Length": 70, "Engagement": "Low"},
    {"Post_Type": "Reel", "Time": "Night", "Hashtags": 10, "Caption_Length": 150, "Engagement": "High"}
]

# Rule-based classifier
def predict_engagement(post_type, time, hashtags, caption_length):
    if post_type == "Reel" and time == "Night" and hashtags >= 5:
        return "High"
    elif time == "Evening" and hashtags >= 5:
        return "High"
    elif caption_length > 100 and hashtags >= 6:
        return "High"
    else:
        return "Low"

# Apply prediction to dataset
print("Dataset Predictions:\n")
for row in data:
    prediction = predict_engagement(
        row["Post_Type"],
        row["Time"],
        row["Hashtags"],
        row["Caption_Length"]
    )
    print(row, "→ Predicted:", prediction)

# BONUS: User input
print("\n--- Test Your Own Post ---")
ptype = input("Enter Post Type (Reel/Image/Carousel): ")
time = input("Enter Time (Day/Evening/Night): ")
hashtags = int(input("Enter number of hashtags: "))
caption = int(input("Enter caption length: "))

result = predict_engagement(ptype, time, hashtags, caption)
print("Predicted Engagement:", result)