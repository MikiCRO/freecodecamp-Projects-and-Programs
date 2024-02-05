import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.color = kwargs
        contents = [key for key, value in self.color.items() for _ in range(value)]
        izbacene_kuglice = []
        self.contents = contents
        self.izbacene_kuglice = izbacene_kuglice
        
    def draw(self,drawn = 0):
        self.drawn = drawn
        
        while self.drawn >= 1:
            if self.contents:
                self.drawn -= 1
                izbaceno = self.contents.pop(random.randrange(len(self.contents)))
                print(self.contents)
                self.izbacene_kuglice.append(izbaceno) 
            else:
                self.contents += self.izbacene_kuglice
                break
        return self.izbacene_kuglice
            
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    m = 0
    pokusaji = 0
    expected_balls = [key for key, value in expected_balls.items() for _ in range(value)]
    
    while num_experiments >= 1:
        hat2 = copy.deepcopy(hat)
        hat2.draw(num_balls_drawn)
        num_experiments -= 1
        pokusaji += 1
        
        
        i = iter(sorted(hat2.izbacene_kuglice))
        if hat2.izbacene_kuglice and all(j in i for j in sorted(expected_balls)):
            m += 1
        if not hat2.izbacene_kuglice:
            pokusaji -= 1
            num_experiments += 1
        
    return m/pokusaji
            

hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)

print(probability)
                
               
                
    
        
    
    
    
                             
                
                 
        