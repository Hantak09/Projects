from matplotlib import pyplot as plt
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/", methods=["POST", "GET"])
def output():
    if request.method == "GET":
        return render_template("index.html")
    data = None
    id_value = None
    if request.method == "POST":
        data = request.form.get("ID")
        id_value = request.form.get("id_value")
    if id_value is None or data is None:
        return render_template("error.html"),200
    else:
        if data == "student_id":
            marks = []
            total = 0
            with open("data.csv", "r") as infile:
                for line in infile:
                    content = line.rstrip().split(",")
                    if content[0] == id_value:
                        marks.append(content)
                        total += int(content[2])
            if marks == []:
                return render_template("error.html")
            return render_template("student_data_page.html", marks=marks, total=total), 200
        elif data == "course_id":
            marks = []
            with open("data.csv", "r") as infile:
                for line in infile:
                    content = line.rstrip().split(",")
                    if content[1].lstrip() == id_value:
                        marks.append(int(content[2]))
            if marks == []:
                return render_template("error.html"),200
            else:
                fig, ax = plt.subplots()
                ax.hist(marks)
                ax.set_xlabel('Marks')
                ax.set_ylabel('Frequency')
                fig.savefig("./static/hist.png")

                return render_template("course_details_page.html", average=(sum(marks))/len(marks), max=max(marks), image="./static/hist.png"), 200


# @app.route("/", methods=["GET"])
# def index():
#     if request.method == "GET":
#         return render_template("index.html") ,200

if __name__ == '__main__':
    app.run()