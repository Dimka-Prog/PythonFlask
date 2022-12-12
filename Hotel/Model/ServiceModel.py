import pandas


def getTypesService(connectDB):
    return pandas.read_sql('''
                            SELECT 
                                ServiceID AS 'ID Услуги', 
                                TypeService AS 'Услуга'
                            FROM TypeService
                            ORDER BY ServiceID
                            ''', connectDB)


def getDailyAccounting(connectDB):
    return pandas.read_sql('''
                            SELECT 
                                RoomNum AS 'Номер комнаты',
                                StartServiceDate AS 'Начало обслуживания', 
                                FIO AS 'ФИО',
                                Post AS 'Должность',
                                TypeService AS 'Услуга',
                                EndServiceDate AS 'Завершение обслуживания',
                                InspectionResult AS 'Результат осмотра(руб.)'
                            FROM DailyAccounting
                                JOIN HotelStaff USING (StaffID)
                                JOIN Post USING (PostID)
                                JOIN TypeService USING (ServiceID)
                            ORDER BY RoomNum
                            ''', connectDB)

# print('\n2. ТАБЛИЦА ВЫВОДЯЩАЯ ВСЕ ПЛАНОВЫЕ ОСМОТРЫ ЗА ВСЕ ВРЕМЯ')
# dataFrame = pandas.read_sql('''
#                             SELECT
#                                 FIO AS 'ФИО',
#                                 TypeService AS "Тип сервиса",
#                                 EndServiceDate AS "Завершение обслуживания"
#                             FROM DailyAccounting
#                                 JOIN HotelStaff USING (StaffID)
#                                 JOIN TypeService USING (ServiceID)
#                             WHERE TypeService = 'Плановый осмотр'
#                             ORDER BY EndServiceDate DESC
#                             ''', database)


# print('\n2. ТАБЛИЦА ВЫВОДЯЩАЯ РЕЗУЛЬТАТЫ ОСМОТРА, КОТОРЫЕ БОЛЬШЕ СРЕДНЕГО ЗНАЧЕНИЯ ЗА ВСЕ ВРЕМЯ')
# dataFrame = pandas.read_sql('''
#                             SELECT
#                                 TypeService AS 'Тип сервиса',
#                                 EndServiceDate AS 'Завершение обслуживания',
#                                 InspectionResult AS 'Результат осмотра(руб.)'
#                             FROM DailyAccounting
#                                 JOIN TypeService USING (ServiceID)
#                             WHERE TypeService = "Плановый осмотр"
#                                 and InspectionResult > (SELECT AVG(InspectionResult) FROM DailyAccounting)
#                             ''', database)
