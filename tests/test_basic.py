def test_root():
    # lightweight smoke test
    from fastapi.testclient import TestClient
    from sentinel_net.main import app

    client = TestClient(app)
    r = client.get("/")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"
