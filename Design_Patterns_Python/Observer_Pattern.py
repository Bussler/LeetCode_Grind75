

class Subscriber():
    
    def __init__(self) -> None:
        pass
    
    def update(self, context):
        raise NotImplementedError()
    
class Concrete_Subscriber(Subscriber):
    
    def update(self, context):
        print("Event Recorded!")
        print(context.text)
    
    
class Publisher():
    def __init__(self) -> None:
        self.subscribers = []
        self.text = ""
        
    def subscribe(self, sub: Subscriber):
        self.subscribers.append(sub)
        
    def unsubscribe(self, sub: Subscriber):
        del self.subscribers[sub]
        
    def notify_subscribers(self):
        for s in self.subscribers:
            s.update(self)
            
    def change_data(self, text):
        self.text = text
        self.notify_subscribers()
        
pub = Publisher()
calling_subs = Concrete_Subscriber()
pub.subscribe(calling_subs)
pub.change_data("HEHE")