import requests


URL_BASE = "http://localhost:8080"
API_VERSION = "v1.0"
def test_get_questions_bad():
	resp = requests.get(URL_BASE + "/api/"+API_VERSION+"/questions",
            headers = {"Content-Type": "application/json"},
            data = "some wierd data that doesn't inlude count")
	assert resp.status_code == 400, "%d: %s" % (resp.status_code, resp.text)