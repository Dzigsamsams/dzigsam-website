from flask import Flask, render_template

app = Flask(__name__)

COURCES = [
  {
    'id': 1,
    'title': 'Practical Python Programming',
    'Cost for 6months': '8,000',
    'Cost for 1yr': '14,000'
  },
  {
    'id': 2,
    'title': 'Practical Java Programming',
    'Cost for 6months': '6,000',
    'Cost for 1yr': '11,000'
  },
  {
  'id': 3,
  'title': 'Practical C# Programming',
  'Cost for 6months': '7,000',
  'Cost for 1yr': '12,000'
  },
  {
  'id': 4,
  'title': 'Practical C++ Programming',
  'Cost for 6months': '9,000',
  'Cost for 1yr': '15,000'
  }
]

@app.route("/")
def hell0_world():
  return render_template('home.html', 
                         cources=COURCES)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)