from flask import Flask, render_template,jsonify

app = Flask(__name__)

roles = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru',
    'salary': 'Rs. 10,00,000',
}, {
    'id': 2,
    'title': 'Data Science',
    'location': 'Bengaluru',
    'salary': 'Rs. 12,00,000',
}, {
    'id': 3,
    'title': 'Devops Enginner',
    'location': 'Bengaluru',
    'salary': 'Rs. 15,00,000',
}, {
    'id': 4,
    'title': 'AWS Enginner',
    'location': 'Bengaluru',
    'salary': 'Rs. 20,00,000',
}]


@app.route('/')
def hello_world():
  return render_template('index.html', jobs=roles,
                        company_name='Jovian')

@app.route('/jobs')
def list_jobs():
  return jsonify(roles)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
