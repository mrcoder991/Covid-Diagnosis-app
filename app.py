from flask import Flask, request, render_template


app = Flask(__name__)

def fun(userAns, question):
    if question == "this is first question":
    
        if userAns == "True":
            return "Have you taken the vaccination?", "Yes", "No", None
   
    elif question == "Have you taken the vaccination?":
        if userAns == "True":
            return "Which vaccine you have been given?", "Covishield", "Covaxin", None
        elif userAns=="False":
            return "Do you currently have any of the following: Cough, Fever, Sore throat, Chest congestion or runny nose, Body ache, difficulty in breathing, Loss in sense of smell or taste, hearing impairment, Pink eyes?", "I have only one Symptom", "I have more than one symptom", "I Don't have any of these symptoms"

    elif question == "Which vaccine you have been given?":
        if userAns == "True" or "False":
           return "How many doses have you taken?", "First dose only!", "Both doses are done", None

    elif question == "How many doses have you taken?":
        if userAns == "True" or "False":
            return "Did you had covid related symptoms in past 3 months or after taking the shot?", "Yes", "No", None
    
    elif question == "Did you had covid related symptoms in past 3 months or after taking the shot?":
        if userAns == "True":
            return "Do you currently have any of the following: Cough, Fever, Sore throat, Chest congestion or runny nose, Body ache, difficulty in breathing, Loss in sense of smell or taste, hearing impairment, Pink eyes?", "I have only one Symptom", "I have more than one symptom", "I Don't have any of these symptoms"
        elif userAns == "False":
            return "Your infection risk is low. We recommend that you stay at home to avoid any chance of exposure to the Novel Coronavirus.Retake the Self-Assessment Test if you develop symptoms or come in contact with a COVID-19 confirmed patient.", None, None, None
    
    elif question == "Do you currently have any of the following: Cough, Fever, Sore throat, Chest congestion or runny nose, Body ache, difficulty in breathing, Loss in sense of smell or taste, hearing impairment, Pink eyes?":
        if userAns == "True":
            return "Do you have any of the following pre existing conditions: Diabetes, Hypertension, Lung disease, Kidney disorder, Asthama, Heart disease" , "Yes, I have only one of above condition", "I have more than one of above condition", "None of the above"
        elif userAns == "False":
            return "Oh! so you have more than one major Covid-19 related symptoms, Do you have any of the following pre existing conditions: Diabetes, Hypertension, Lung disease, Kidney disorder, Asthama, Heart disease", "Yes, I have only one of above condition", "I have more than one of above condition", "None of the above"
        else:
            return "Do you have any of the following pre existing conditions: Diabetes, Hypertension, Lung disease, Kidney disorder, Asthama, Heart disease" , "Yes, I have only one of above condition", "I have more than one of above condition", "None of the above"
    
    elif question == "Oh! so you have more than one major Covid-19 related symptoms, Do you have any of the following pre existing conditions: Diabetes, Hypertension, Lung disease, Kidney disorder, Asthama, Heart disease":
        if userAns == "True":
            return "You have High risk of infection!", "What to do now?", None, None
        elif userAns == "False":
            return "You have High risk of infection!", "What to do now?", None, None
        elif userAns == "else":
            return "You have High risk of infection!", "What to do now?", None, None

    elif question == "You have High risk of infection!":
        if userAns == "True":
            return "Things to do next : 1.Isolate yourself 2.Log temperature every two hours 3.Get yourself tested immediately", "How do I Isolate myself?", None, None

    elif question == "Do you have any of the following pre existing conditions: Diabetes, Hypertension, Lung disease, Kidney disorder, Asthama, Heart disease":
        if userAns == "True":
            return "Which of the following apply to you?", "I have recently interacted or lived with someone who has tested positive for COVID-19", "I am a healthcare worker and I examined a COVID-19 confirmed case without protective gear", "None of the above"
        elif userAns == "False":
            return "Which of the following apply to you?", "I have recently interacted or lived with someone who has tested positive for COVID-19", "I am a healthcare worker and I examined a COVID-19 confirmed case without protective gear", "None of the above"
        elif userAns == "else":
            return "Which of the following apply to you?", "I have recently interacted or lived with someone who has tested positive for COVID-19", "I am a healthcare worker and I examined a COVID-19 confirmed case without protective gear", "None of the above"
        
    elif question == "Which of the following apply to you?":
        if userAns == "True":
            return "When did this interaction take place?", "Less than 5 days ago", "Greater than 5 days ago", "Greater than 14 days ago"
        elif userAns == "False":
            return "When did this interaction take place?", "Less than 5 days ago", "Greater than 5 days ago", "Greater than 14 days ago"
        elif userAns == "else":
            return "Your infection risk is low. We recommend that you stay at home to avoid any chance of exposure to the Novel Coronavirus.Retake the Self-Assessment Test if you develop symptoms or come in contact with a COVID-19 confirmed patient.", "Ok", "Thank you" , "sure"
    
    elif question == "When did this interaction take place?":
        if userAns == "True":
            return "Moderate risk of infection", "What to do next?", None, None
        elif userAns == "False":
            return "High risk of infection", "What to do next?", None, None
        elif userAns== "else":
            return "Medium risk of infection", "What to do next?", None, None
        
    elif question == "Moderate risk of infection":
        if userAns == "True":
            return "Things to do next : 1.Home quarantine immediately. 2.If you show symptoms call helpline 1075" , "how do I home Quarantine?", None, None
    
    elif question == "High risk of infection":
        if userAns == "True":
            return "Things to do next : 1.Isolate yourself 2.Log temperature every two hours 3.Get yourself tested immediately", "How do I Isolate myself?", None, None

    elif question == "Medium risk of infection":
        if userAns == "True":
            return "Things to do next: 1. Be cautious 2. Stay at home 3. Retake take self assessment test if you develop symptoms.", None, None, None

    elif question == "Things to do next : 1.Home quarantine immediately. 2.If you show symptoms call helpline 1075":
        if userAns == "True":
            return "1.Wash hands 2. Maintain social distance of 6 feets 3. Do not share towel and utensils 4. Do not have visitors at home 5. Stay in a separate room", None, None, None

    elif question == "Things to do next : 1.Isolate yourself 2.Log temperature every two hours 3.Get yourself tested immediately":
        if userAns == "True":
            return "1. Wear a face mask  2. Do not share towel and utencils  3. Limit contact with others 4. Stay in separate room", None, None, None








@app.route("/", methods=["POST", "GET"])
def hello():
    a=0
    while a < 1:
        question = "this is first question"
        userAns = 'True'
        returnValue = fun(userAns, question)
        a += 1
        
    if request.method == "POST":
        userAns = request.form["answer"]
        print(userAns)
        returnValue = fun(userAns, question)
        question=returnValue[0]
    return render_template("index.html",question=returnValue[0], option1= returnValue[1],option2=returnValue[2],option3=returnValue[3])

if __name__ == "__main__":
    app.run(debug=True)
