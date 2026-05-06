import requests

BASE_URL = "http://127.0.0.1:8000"


def create_user():
    response = requests.post(
        f"{BASE_URL}/users",
        json={
            "name": "Ishan",
            "email": "ishan@example.com",
            "phone": "+919876543210",
            "privilege_level": "admin"
        }
    )

    print("\nCREATE USER")
    print(response.status_code)
    print(response.json())

    return response.json()["_id"]


def get_users():
    response = requests.get(
        f"{BASE_URL}/users"
    )

    print("\nGET USERS")
    print(response.status_code)
    print(response.json())


def create_card(user_id):
    response = requests.post(
        f"{BASE_URL}/cards",
        json={
            "uid": "a1b2c3d4",
            "assigned_user_id": user_id,
            "is_active": True
        }
    )

    print("\nCREATE CARD")
    print(response.status_code)
    print(response.json())


def get_cards():
    response = requests.get(
        f"{BASE_URL}/cards"
    )

    print("\nGET CARDS")
    print(response.status_code)
    print(response.json())


def revoke_card():
    response = requests.patch(
        f"{BASE_URL}/cards/A1B2C3D4/revoke"
    )

    print("\nREVOKE CARD")
    print(response.status_code)
    print(response.json())


def activate_card():
    response = requests.patch(
        f"{BASE_URL}/cards/A1B2C3D4/activate"
    )

    print("\nACTIVATE CARD")
    print(response.status_code)
    print(response.json())


if __name__ == "__main__":

    user_id = create_user()

    get_users()

    create_card(user_id)

    get_cards()

    revoke_card()

    get_cards()

    activate_card()

    get_cards()