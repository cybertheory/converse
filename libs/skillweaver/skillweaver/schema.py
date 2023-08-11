from skillweaver.schema import Web, Skill, Spindle

class Schema():

    Schema: Web

    def __init__(self) -> None:
        pass

    def load_web(self) -> Web:
        return Web()

    def create_web(self) -> Web:
        return Web()
    
    def load_skills(self, skills) -> Skill:
        return Skill()
    
    def create_skill(self) -> Skill:
        return Skill()
    
    def