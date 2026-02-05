# Food Recommendation Engine
# This program uses user input to navigate a decision tree

print("--- The Ultimate Dinner Decider ---")

# Question 1: Dietary preference/style
style = input("Do you want something 'healthy' or 'comfort' food? ").lower()

# Question 2 & 3: Nested logic based on the first answer
if style == "healthy":
    # Logic for the healthy path
    temp = input("Do you prefer 'hot' or 'cold' food? ").lower()
    
    if temp == "cold":
        print("Recommendation: A fresh Greek Salad with grilled chicken!")
    elif temp == "hot":
        protein = input("Do you like 'fish' or 'tofu'? ").lower()
        if protein == "fish":
            print("Recommendation: Baked Salmon with asparagus.")
        else:
            print("Recommendation: A spicy Tofu stir-fry with brown rice.")
    else:
        print("Recommendation: A colorful Buddha Bowl with lemon tahini dressing.")

elif style == "comfort":
    # Logic for the comfort food path
    flavor = input("Are you craving 'cheesy' or 'spicy' flavors? ").lower()
    
    if flavor == "cheesy":
        print("Recommendation: Classic Four-Cheese Macaroni or a Margherita Pizza.")
    elif flavor == "spicy":
        cuisine = input("Do you prefer 'Mexican' or 'Indian' food? ").lower()
        if cuisine == "mexican":
            print("Recommendation: Sizzling Beef Fajitas with extra jalapeños.")
        else:
            print("Recommendation: Chicken Tikka Masala with garlic naan.")
    else:
        print("Recommendation: A big bowl of Ramen.")

else:
    # Catch-all for unexpected inputs
    print("I'm not sure about that choice, but you can never go wrong with a classic Grilled Cheese sandwich!")

print("--- Enjoy your meal! ---")