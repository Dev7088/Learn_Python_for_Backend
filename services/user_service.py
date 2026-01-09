from repositories.user_repository import get_all_users, create_user

def fetch_users(db):
    return get_all_users(db)

def create_new_user(db, user_data):
    return create_user(db, user_data.name, user_data.age)