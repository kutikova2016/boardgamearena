import peewee as _PW

connection = _PW.SqliteDatabase('ivaners_test.db')

cursor = connection.cursor()

cursor.execute("""
    select * from user
    where age > 21
    """)

res = cursor.fetchall()

print(res)

connection.close()


class Person(_PW.Model):
    name = _PW.CharField()
    birthday = _PW.DateField()
    is_relative = _PW.BooleanField()

    class Meta:
        database = connection


class Pet(_PW.Model):
    owner = _PW.ForeignKeyField(Person, related_name='pets')
    name = _PW.CharField()
    animal_type = _PW.CharField()

    class Meta:
        database = connection


#Person.create_table()
#Pet.create_table()

import datetime
u1 = Person(name='bob', birthday=datetime.date(1960, 1, 15), is_relative=True)
u1.save()

for e in Person.select():
    print(e.name)




