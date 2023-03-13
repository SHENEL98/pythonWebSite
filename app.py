from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data',
    'type':'perment',
    'salary':'Rs.20000'
  },
  {
    'id':2,
    'title':'Data-2',
    'type':'perment',
    'salary':'Rs.20000'
  },
  {
    'id':3,
    'title':'Data-3',
    'type':'perment',
    'salary':'Rs.20000'
  }
]

@app.route("/")
def helloworld():
  return render_template('home.html',jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  # print("indise the if now")
  app.run(host='0.0.0.0',debug=True)