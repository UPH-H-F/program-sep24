from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get input values from the form
        absences = int(request.form.get('absences'))
        prelim_grade = float(request.form.get('prelim_grade'))
        quizzes_grade = float(request.form.get('quizzes_grade'))
        requirements_grade = float(request.form.get('requirements_grade'))
        recitation_grade = float(request.form.get('recitation_grade'))

        # Pass input values to the template, let JavaScript handle the calculations
        return render_template('index.html', 
                                absences=absences, 
                                prelim_grade=prelim_grade, 
                                quizzes_grade=quizzes_grade, 
                                requirements_grade=requirements_grade, 
                                recitation_grade=recitation_grade)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)