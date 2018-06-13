from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    #def on_start(self):
    #    """ on_start is called when a Locust start before any task is scheduled """
    #    self.login()

    #def on_stop(self):
    #   """ on_stop is called when the TaskSet is stopping """
    #   self.logout()

    #def login(self):
    #    self.client.post("/login/", {"email":"widl@gmail.com", "senha":"opaopa"})

    @task(5)
    def sobreGet(self):
        self.client.get("/sobre/")

    @task(4)
    def contateGet(self):
        self.client.get("/contate-nos/")

    @task(3)
    def loginGet(self):
        self.client.get("/login/")

    @task(2)
    def indexGet(self):
        self.client.get("/")

    @task(1)
    def cadastroGet(self):
        self.client.get("/cadastro/")

class WebsiteUser(HttpLocust):
    host = "http://127.0.0.1:8089"
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000