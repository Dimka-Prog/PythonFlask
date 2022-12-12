import pandas


def getTypesRooms(connectDB):
    return pandas.read_sql('''
                            SELECT
                                TypeID AS 'ID Типа', 
                                RoomType AS 'Тип комнаты', 
                                Price AS 'Цена'
                             FROM RoomType
                            ORDER BY TypeID
                             ''', connectDB)


def getRooms(connectDB):
    return pandas.read_sql('''
                            SELECT 
                                RoomType AS 'Тип комнаты',
                                RoomNum AS 'Номер',
                                Places AS 'Места',
                                RoomFeatures AS 'Особенности', 
                                Floor AS 'Этаж', 
                                RoomStatus AS 'Статус'
                            FROM Rooms
                                JOIN RoomType USING (TypeID)
                            ORDER BY RoomNum
                            ''', connectDB)
