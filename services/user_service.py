from repositories.user_repository import get_all_users, create_user, get_user_by_id, update_user, delete_user, patch_user

def fetch_users(db):
    return get_all_users(db)

def create_new_user(db, user_data):
    return create_user(db, user_data.name, user_data.age)

def fetch_user_by_id(db, user_id: int):
    return get_user_by_id(db, user_id)

def update_existing_user(db, user_id: int, user_data):
    return update_user(db, user_id, user_data.name, user_data.age)

def patch_existing_user(db, user_id: int, user_data):
    return patch_user(db, user_id, user_data.name, user_data.age)

def delete_existing_user(db, user_id: int):
    return delete_user(db, user_id)