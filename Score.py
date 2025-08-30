#Challenge - Food supplier 

input_score = int(input("Enter the score for the food supplier: "))
# Function to determine the score category  
def determine_score_category(score):
    if score < 50:
        return print("Fail")
    else:
        return print("Pass")
    
while input_score >=0:
    determine_score_category(input_score)
    input_score = int(input("Enter the score for the food supplier: "))