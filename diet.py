def bmi_calculator(weight,height):
    bmi=weight/((height/100)**2)
    return round(bmi,2)

def bmr_calculator(gender,age,weight,height):
    if gender=="Male" :
        bmr=(10*weight)+(6.25*height)-(5*age)+5
        return round(bmr,2)
    elif gender=="Female":
        bmr=(10*weight)+(6.25*height)-(5*age)-161
        return round(bmr,2)

def tdee_calculator(bmr,activity):
    activity_factor={"sadentary":1.20,
                     "lightly active":1.375,
                     "moderately active":1.55,
                     "very active":1.725,
                     "extra active":1.90
                     }
    tdee=bmr*activity_factor[activity]
    return round(tdee,2)

def calorie_target(tdee,aim):
    if aim=="weight maintain":
        calorie=tdee
    elif aim=="weight loss":
        calorie=tdee-400
    elif aim=="weight gain":
        calorie=tdee+300
    return round(calorie,2)
    
# bmi=bmi_calculator(50,150)
# bmr=bmr_calculator("Male",25,50,150)
# tdee=tdee_calculator(bmr,"very active")
# print(calorie_target(tdee,"weight loss"))