from locust import HttpUser, task, between

class AccessUser(HttpUser):

    wait_time = between(1, 5)

    @task
    def index(self):
        self.client.get("/")

