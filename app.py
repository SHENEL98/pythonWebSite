from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
  return "hellow world"

if __name__ == "__main__":
  # print("indise the if now")
  app.run(host='0.0.0.0',debug=True)