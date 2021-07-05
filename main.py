from flask import Flask, render_template, request, jsonify
import rospy

from std_msgs.msg import String


app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def hello_world():
    return render_template("joystick.html")

@app.route("/user/<string:name>/<int:id>")
def user(name, id):
    return "user" + name + " " + str(id)

@app.route('/post', methods = ['POST'])
def update_text():
    request_data = request.get_json()
    x = request_data['x']
    y = request_data['y']
    return jsonify({'status' : 'OK'})

if __name__ == "__main__":
    app.run(debug=True)


# class Joystick(Node):
#     def __init__(self):
#         super().__init__('joystick_server')
#         self._action_server = ActionServer(
#             self,
#             ______,
#             'joystick',
#             self.execute_callback)
#

pub = rospy.Publisher('hello', String, queue_size=10)
rospy.init_node('hello_topic_publisher')
rospy.loginfo("Hello from PUB node")
r = rospy.Rate(10) # 10hz

while not rospy.is_shutdown():
    pub.publish("Hello World")
    r.sleep()