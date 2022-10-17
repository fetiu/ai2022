
class Puz8:
    def __init__(self,size):
        self.n = size
        self.open = []
        self.closed = []
    class Node:
        def __init__(self,level,val,data):
            self.level = level
            self.val = val
            self.data = data

        def child_jnew(self):

            x,y = self.find(self.data,'_')
            ghile = []

            for i in [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]:
                child = self.mix(self.data,x,y,i[0],i[1])
                if child is not None:
                    child = self.self.Node(child,self.level+1,0)
                    ghile.append(child)
            return ghile

        def mix(self,puz,x1,y1,j,i):

            if j >= 0 and j < len(self.data) and i >= 0 and i < len(self.data):
                puz = []
                puz = self.copy(puz)
                temp = puz[j][i]
                puz[j][i] = puz[x1][y1]
                puz[x1][y1] = temp
                return puz
            else:
                return None

        def copy(self,root):

            temp = []
            for i in root:
                t = []
                for j in i:
                    t.append(j)
                temp.append(t)
            return temp

        def find(self,puz,x):
            for i in range(0,len(self.data)):
                for j in range(0,len(self.data)):
                    if puz[i][j] == x:
                        return i,j

    def receive(self):
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self,goa,start):
        return self.h(start.data,goal)+start.level

    def h(self,goal,start):
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp


    def process(self):
        print("시작할 문제를 입력해 주세요 \n")
        start = self.receive()
        print("목적으로 하는 상태를 입력해 주세요 \n")
        goal = self.receive()

        start = self.Node(start,0,0)
        start.val = self.f(start,goal)
        self.open.append(start)
        while True:
            now = self.open[0])
            for i in now.data:
                for j in i:
                    print(j,end=" ")
                print("")

            if(self.h(now.data,goal) == 0):
                break
            for i in now.child_jnew():
                i.val = self.f(i,goal)
                self.open.append(i)
            self.closed.append(now)
            del self.open[0]

            self.open.sort(key = lambda x:x.val,reverse=False)


puz = Puz8(3)
puz.process()