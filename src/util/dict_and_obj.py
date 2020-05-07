# dict转orm对象
def dict_to_orm(obj_db, data):
    for key in obj_db.__class__.__dict__.keys():
        if key in list(data.keys()):
            setattr(obj_db, key, data[key])


# orm对象转dict
def orm_to_dict(obj):
    return {c.name: getattr(obj, c.name, None) for c in obj.__table__.columns}
