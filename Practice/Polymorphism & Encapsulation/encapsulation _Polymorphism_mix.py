class ProjectMember:
    def get_role(self, role):
        self.__role = role

class Developer(ProjectMember):
    def get_role(self, role):
        return super().get_role(role)

class Tester(ProjectMember):
    def get_role(self, role):
        return super().get_role(role)

p = ProjectMember()
d = Developer()
t = Tester()

p.get_role("Role")
d.get_role("Developer role")
t.get_role("Tester role")