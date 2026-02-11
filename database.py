from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('sandbox.db')

class BaseModel(Model):
    class Meta:
        database = db

class RoomBlockCode(BaseModel):
    block_id = CharField()
    access_code_id = CharField()
    access_code = CharField()
    room_id = CharField()


db.connect()
db.create_tables([RoomBlockCode])