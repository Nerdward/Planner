import httpx
import pytest


# informs pytest to treat this as an async test
@pytest.mark.asyncio
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:
    payload = {
        "email": "testuser@packt.com",
        "password": "testpassword",
    }

    # Request header
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
        }
    
    test_response = {
        "message": "User successfully registered"
        }

    response = await default_client.post("/user/signup", json=payload,
                                         headers=headers)
    assert response.status_code == 200
    assert response.json() == test_response

async def test_sign_user_in(default_client: httpx.AsyncClient) -> None:
    payload = {
        "username": "testuser@packt.com",
        "password": "testpassword",
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
        }
    
    response = await default_client.post("/user/signin", data=payload,
                                         headers=headers)
    assert response.status_code == 200
    assert response.json()["token_type"] == "Bearer"
