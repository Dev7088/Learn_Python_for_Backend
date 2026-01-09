from database import SessionLocal
from models.user import User

db = SessionLocal()

# Insert
# new_user = User(name="Venom", age=40)
# print(f"new_user : {new_user}")

# db.add(new_user)   # This is the line waiting area not yet add in the database it only way to tell the database i want to save this but not yet.
# db.commit() # This line is do the real changes in the databse so it Make changes permanent


# Select query 
# users = db.query(User).all()
# users = db.query(User).filter(User.id == 1).first()


# print("users : ",users)
# for user in users:
#     print(user.id, user.name, user.age)

db.close()