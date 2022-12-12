from flask import Flask

import Controller.SearchRoomsController as searchRooms


app = Flask(__name__, template_folder='View/Template')


@app.route('/SearchRooms', methods=['GET'])
def rooms():
    return searchRooms.rooms()


if __name__ == '__main__':
    app.run(host='85.143.222.11')