from fastapi import status
import pytest


class TestCableModemAPI:
    """Test cases for the CableModem API."""

    @pytest.mark.asyncio
    async def test_create_cable_modem(self, client):
        response = await client.post("/api/cableModems", json={
            "model": "CM 100 MB",
            "description": "Configuracion para 100 MB.",
            "status": "active",
            "valid_since": "2023-11-14T12:00:00.000Z",
            "tags": [
                "internet",
                "voip"
            ]
        })
        assert response.status_code == status.HTTP_201_CREATED
        _id = response.json().get("id")
        assert _id is not None

        response = await client.get("/api/cableModems")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 1
        assert response.json()[0]["id"] == _id

    @pytest.mark.asyncio
    async def test_list_cable_modems(self, client):
        for n in range(1,4):
            await client.post("/api/cableModems", json={
                "model": f"CM {n*100} MB",
                "description": "Configuracion para {n*100} MB.",
                "status": "active",
                "valid_since": "2023-11-14T12:00:00.000Z",
                "tags": [
                    "internet",
                    "voip"
                ]
            })

        response = await client.get("/api/cableModems")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 3

    @pytest.mark.asyncio
    async def test_get_cable_modem(self, client):
        response = await client.post("/api/cableModems", json={
            "model": "CM 500 MB",
            "description": "Configuracion para 500 MB.",
            "status": "provision",
            "valid_since": "2023-11-14T12:00:00.000Z",
            "tags": [
            ]
        })
        assert response.status_code == status.HTTP_201_CREATED
        _id = response.json()["id"]
        assert _id is not None

        response = await client.get(f"/api/cableModems/{_id}")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["id"] == _id
