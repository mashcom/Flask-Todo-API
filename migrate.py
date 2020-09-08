from database import init_db

print("Creating database")
if init_db() is None:
    print("Migration Completed. You can go ahead and use the Todo API")
else:
    print("Migration Failed")
