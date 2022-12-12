import pandas


def getGuests(connectDB):
    return pandas.read_sql('''
                            SELECT 
                                PassportNum AS 'Номер паспорта', 
                                FIO AS 'ФИО', 
                                Citizenship AS 'Гражданство', 
                                TypeGuest AS 'Статус', 
                                Discount AS 'Скидка'
                            FROM Guests
                            ORDER BY PassportNum
                            ''', connectDB)


def getPlacement(connectDB):
    return pandas.read_sql('''
                            SELECT 
                                FIO AS 'ФИО', 
                                RoomNum AS 'Номер комнаты', 
                                SetDate AS 'Дата заезда', 
                                DepartureDate AS 'Дата выезда' 
                            FROM Placement
                                JOIN Guests USING (PassportNum)
                            ORDER BY RoomNum
                            ''', connectDB)

# print('\n2. ТАБЛИЦА ОТОБРАЖАЮЩАЯ КОЛИЧЕСТВО ГОСТЕЙ ОПРЕДЕЛЕННОГО ТИПА')
# dataFrame = pandas.read_sql('''
#                             SELECT
#                                 TypeGuest,
#                                 COUNT(TypeGuest) AS "Количество гостей"
#                             FROM Guests
#                             GROUP BY TypeGuest
#                             HAVING "Количество гостей" > 1
#                             ''', database)
