from flask import Flask,jsonify,request
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter
app = Flask(__name__)
metrics = PrometheusMetrics(app)    

REQUEST_COUNT = Counter('request_count','App Request Count')
students =[
    {
        'id':1,
        'name':'John Doe',
        'age':21
    }
]
# comment in feature branch
@app.before_request
def before_request():
    REQUEST_COUNT.inc()
@app.route('/get_students',methods=['GET'])
def get_students():
    return jsonify({'students':students})
@app.route('/add_student',methods=['POST'])
def add_student():
    new_student = request.json
    students.append(new_student)
    return jsonify({'message':'added new student'}),201
@app.route('/update_student/<int:index>',methods=['PATCH'])
def update_student(index):
    request_data = request.json
    students[index].update(request_data)
    return jsonify({'message':'student updated successfully'})
@app.route('/delete_student/<int:index>',methods=['DELETE'])
def delete_student(index):
    students.pop(index)
    return jsonify({'message':'student deleted successfully'})
if __name__ == '__main__':
    app.run(host="0.0.0.0",port =4000)
