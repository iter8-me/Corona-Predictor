from flask import Flask, render_template, request

app = Flask(__name__)

#state, age, q2, q3, q4, q5, q6 = ""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/checkup")
def quiz():
    return render_template("quiz2.html")
#global state, age, q2, q3, q4, q5, q6
#state=state, age=age, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6
# <!-- {% if ((state) and (age) and (q2) and (q3) and (q4) and (q5) and(q6)) %} -->


@app.route("/ans", methods=["GET", "POST"])
def ans():
    count = 0
    danger = ["Maharastra", "Tamil", "Delhi",
              "Gujarat", "Rajasthan", "Madhya", "UP"]
    medium = ["WB", "Andhra", "Bihar", "Jammu", "Haryana", "Kerela",
              "Assam", "Uttarakhand", "Jharkhand", "Chattisgarh"]
    green = ["Himachal", "Tripura", "Ladakh", "Goa", "Manipur", "Puducherry", "Andaman",
             "Meghalaya", "Nagaland", "Arunachal", "DadarNagar", "Sikkim", "Mizoram", "Lakshadweep", "DD"]
    if request.method == "POST":
        # state
        state = request.form.get("state")
        if state in danger:
            count += 3
        if state in medium:
            count += 2
        if state in green:
            count += 1
        # age
        age = request.form.get("q1")
        if age:
            count += int(age)
        # ques2
        q2 = request.form.get("q2")
        if q2:
            count += int(q2)
        # ques3
        q3 = request.form.get("q3")
        if q3:
            count += int(q3)
        # ques4
        q4 = request.form.get("q4")
        if q4:
            count += int(q4)
        # ques5
        q5 = request.form.get("q5")
        if q5:
            count += int(q5)
        # ques6
        q6 = request.form.get("q6")
        if q6:
            count += int(q6)
        q7 = request.form.get("q7")
        if q7:
            count += int(q7)
        q8 = request.form.get("q8")
        if q8:
            count += int(q8)
     #calculation       
    probab = ((count/(33))*100)
    answer = round(probab, 2)

    suggest = ""
    col = ""
    if answer <= 30:
        suggest += "You are safe. No need to worry about anything. But make sure to keep yourself up to date with recent WHO guidelines."
        col += "green"

    elif answer < 70 and answer > 30:
        suggest += "you need to be more cautious about your daily habits. Please follow these official guidelines on covid-19."
        col += "yellow"
    elif answer >= 70:
        suggest += "The chance of getting infected with corona virus is very high. Please follow these official guidelines on covid-19."
        col += "red"

    rotate_css = answer/200
    rotation = "rotate("+str(rotate_css)+"turn)"

    return render_template("ans.html", answer=answer, rotant=rotation, suggest=suggest,state=state, age=age, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, col = col)


@app.route("/misc")
def misc():
    return render_template("test.html")


@app.route("/failed")
def failed():
    return render_template("failed.html")

@app.route("/thanks")
def thanks():
    return render_template("thanks.html")

if __name__ == "__main__":
    app.run()
