import firebase_admin
from firebase_admin import credentials, firestore
import uuid
import random

# Initialize Firebase Admin SDK
cred = credentials.Certificate("kolz108-firebase-adminsdk-daceu-ed6793dc61.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Sample Users Data
def create_users(n=1):
    users_ref = db.collection("users")
    for _ in range(n):
        user_data = {
            "refreshToken": str(uuid.uuid4()),
            "email": f"user{_}@example.com",
            "displayName": f"User {_}",
            "phoneNumber": f"+12345678{_}",
            "photoURL": "https://loremflickr.com/200/200?random=1",
            "providerId": "firebase",
            "uid": str(uuid.uuid4()),
        }
        users_ref.add(user_data)
    print(f"Added {n} users to Firestore")

# Sample Items Data
def create_items(n=20):
    items_ref = db.collection("items")
    categories = ["curry", "rice", "fruits", "vegetables", "snaks", "icecreams", "fish", "drinks", "others"]
    for _ in range(n):
        item_data = {
            "databaseId": str(uuid.uuid4()),
            "calories": str(random.randint(100, 500)),
            "category": random.choice(categories),
            "description": random.choice(categories),
            "id": str(uuid.uuid4()),
            "imageUrl": "https://loremflickr.com/200/200?random=1",
            "price": str(random.randint(5, 50)),
            "title": f"Item {_}",
        }
        items_ref.add(item_data)
    print(f"Added {n} items to Firestore")

# Sample Cart Data
# Sample Cart Data
def create_cart_data(n=1):
    cart_ref = db.collection("cart")
    items = [doc.to_dict() for doc in db.collection("items").stream()]
    
    for _ in range(n):
        cart_items = [{**item, "qty": str(random.randint(1, 3))} for item in random.sample(items, min(len(items), random.randint(1, 5)))]
        cart_data = {
            "isCartOpen": False,
            "cartItems": cart_items,
            "cartTotal": sum(int(item["price"]) * int(item["qty"]) for item in cart_items),
            "numOfCartItems": len(cart_items),
        }
        cart_ref.add(cart_data)
    print(f"Added {n} carts to Firestore")


# Run Data Population
create_users(10)
create_items(20)
create_cart_data(5)
