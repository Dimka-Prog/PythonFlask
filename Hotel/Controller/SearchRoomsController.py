import os
import sqlite3
import Model.RoomsModel as rooms

from flask import render_template, request

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
pathDB = os.path.join(SITE_ROOT.replace('Controller', ''), "hotel.db.sqlite")
connectDB = sqlite3.connect(pathDB)

entityRooms = rooms.getRooms(connectDB)


def rooms():
    typeRooms = list(request.args.getlist('Тип комнаты'))
    places = list(map(int, request.args.getlist('Места')))
    floors = list(map(int, request.args.getlist('Этаж')))
    roomStatus = list(request.args.getlist('Статус'))

    dictValuesColumns = {'Тип комнаты': typeRooms, 'Места': places, 'Этаж': floors, 'Статус': roomStatus}

    dataFrame = entityRooms
    for key in dictValuesColumns:
        if dictValuesColumns[key]:
            dataFrame = dataFrame[dataFrame[key].isin(dictValuesColumns[key])].reset_index(drop=True)

    return render_template(
        'SearchRoomsTemplate.html',
        tableName='Комнаты',
        entity=entityRooms,
        dataframe=dataFrame,
        dictionary=dictValuesColumns,
        clickSearch=request.args.get('searchButton'),
        len=len
    )


connectDB.close()
