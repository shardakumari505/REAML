from flask import Flask
from flask import jsonify
from data_analysis import generate_plot

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/get_plot_data', methods=['GET'])
def get_plot_data():
    plot_data = generate_plot()
    return jsonify(plot_data)

if __name__ == '__main__':
    app.run(debug=True)
