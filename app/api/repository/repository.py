class Repo:
    def __init__(self,db):
        self.db = db    
    
    def create(self,data):
        self.db.append(data)
    
    def read(self,id):
        pass
    
    def update(self,id,data):
        pass
    
    def delete(self,id):
        pass