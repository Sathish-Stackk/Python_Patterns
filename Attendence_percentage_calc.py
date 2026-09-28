total_days = 120
present_days = 105

percentage = (present_days / total_days) * 100

print("Attendance:", round(percentage, 2), "%")
print("Eligible:", percentage >= 75)
