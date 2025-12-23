class node:
   data = None
   childs = []
  
   def __init__(self, d=None, c=[]):
       self.data = d
       self. childs = c
       pass

   def __str__(self):
       if self.isEmpty():
           return ""
          
       if self.childs == []:
           return str(self.data)
      
       s = "\n"
       for x in self.childs:
           s += x.__str__() + " "
       return str(self.data) + s
      
   def isEmpty(self):
       return self.data == None and self.childs == []


e=node()
print(e.isEmpty())
print(e)                                                                                       
a = node("a")
print(a)

b = node("b")
c = node("c")
a.childs = [b,c]

print(a)
