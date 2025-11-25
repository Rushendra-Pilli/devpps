from app import app

def test_get_students():
    client = app.test_client()
    response = client .get('/get_students')
    assert response.status_code ==200

def test_patch_student():
    client = app.test_client()

    # first add a student
    response1 = client.post('/add_student', json={"id":2,"name": "Alice", "age": 21})

    update_data = {"age": 22}

    response = client.patch('/update_student/0', json=update_data)
    print(response)
    assert (response.status_code == 200 )& (response1.status_code == 201)