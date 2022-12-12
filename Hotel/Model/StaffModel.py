import pandas


def getStaff(connectDB):
    return pandas.read_sql('''
                            SELECT
                                StaffID AS 'ID Сотрудника', 
                                FIO AS 'ФИО', 
                                Post AS 'Должность', 
                                Salary AS 'Зар-ная плата'
                            FROM HotelStaff
                                JOIN Post USING (PostID)
                            ORDER BY StaffID
                            ''', connectDB)


def getPosts(connectDB):
    return pandas.read_sql('''
                            SELECT 
                                PostID AS 'ID Должности', 
                                Post AS 'Должность', 
                                Salary AS 'Зар. плата'
                            FROM Post
                            ORDER BY PostID
                            ''', connectDB)


# print(f'1. ТАБЛИЦА СОТРУДНИКОВ С ЗАРПЛАТОЙ ВЫШЕ {salary} РУБЛЕЙ')
# dataFrame = pandas.read_sql(f'''
#                             SELECT
#                                 FIO, Salary
#                             FROM HotelStaff
#                                 JOIN Post USING (PostID)
#                             WHERE Salary > {salary}
#                             ORDER BY Salary
#                             ''', database)


# print('1. ТАБЛИЦА ОТОБРАЖАЮЩАЯ КОЛИЧЕСТВО СПЕЦИАЛИСТОВ ОПРЕДЕЛЕННОЙ ДОЛЖНОСТИ')
# dataFrame = pandas.read_sql('''
#                             SELECT
#                                 Post,
#                                 COUNT(Post) AS "Количество специалистов"
#                             FROM HotelStaff
#                                 JOIN Post USING (PostID)
#                             GROUP BY Post
#                             ''', database)


# print(f'1. ТАБЛИЦА СОДЕРЖАЩАЯ ИНФОРМАЦИЮ О СОТРУДНИКАХ С ДОЛЖНОСТЬЮ "{post}"')
# dataFrame = pandas.read_sql(f'''
#                             SELECT
#                                 StaffID,
#                                 FIO,
#                                 (SELECT Post FROM Post WHERE PostID = HotelStaff.PostID and Post = "{post}") AS Должность
#                             FROM HotelStaff
#                             WHERE Должность not null
#                             ''', database)


# print(f'1. ДОБАВЛЕНИЕ СОТРУДНИКА "{FIO}" В ТАБЛИЦУ "СОТРУДНИКИ"')
# cursor.execute(f'''
#                 INSERT INTO HotelStaff (StaffID, FIO, PostID)
#                 VALUES ({staffID}, '{FIO}', {postID})
#                 ''')
# database.commit()


# print(f'\n2. УДАЛЕНИЕ СОТРУДНИКА "{FIO}" ИЗ ТАБЛИЦЫ "СОТРУДНИКИ"')
# cursor.execute(f'''DELETE FROM HotelStaff WHERE StaffID = {staffID}''')
# database.commit()