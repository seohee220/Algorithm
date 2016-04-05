class DoublyLinkedList:
    
    class Handle: # Item(==Node)
        __slots__=['e','prev','nxt']
        def __init__(self, e=None, prev=None, next=None):
            self.e=e
            self.prev=prev
            self.next=next
    
    def __init__(self):
        pass
    
    def createList(self):
        dummy = self.Handle(e="dummy")
        dummy.next = dummy
        dummy.prev = dummy
        return dummy
    
    def isEmpty(self,h):
        return h.next==h #true: 더미만 존재 
    
    def first(self,h):
        if not self.isEmpty(h):
            return h.next
        else:
            print "리스트가 비어있습니다."
            return None
    
    def last(self,h):
        if not self.isEmpty(h):
            return h.prev
        else:
            print "리스트가 비어있습니다."
    
    #free list에 노드 있는지 체크 / 없으면 생성
    def checkFreeList(self):
        global F
        if self.isEmpty(F):
            freeList=[self.Handle() for i in range(10)]
            freeList[0] = F
            
            freeList[0].prev = freeList[9]
            freeList[0].next = freeList[1]
            freeList[9].prev = freeList[8]
            freeList[9].next = freeList[0]
            for i in range(1,9):
                freeList[i].prev = freeList[i-1]
                freeList[i].next = freeList[i+1]
        return self.first(F)
    
    # a~b까지 노드들을 떼어내, t노드 다음에 끼워넣기
    def splice(self, a, b, t):
        aPrime = a.prev
        bPrime = b.next
        tPrime = t.next
        #a' b' 연결
        aPrime.next = bPrime
        bPrime.prev = aPrime
        #insert between t and t'
        a.prev = t
        t.next = a
        b.next = tPrime
        tPrime.prev = b
    
    #노드b를 a다음으로 이동
    def moveAfter(self,b,a):
        self.splice(b,b,a)
    
    #노드b 제거 (노드b를 F로 이동)
    def remove(self,b):
        self.moveAfter(b,F)
        return b.e
    
    #pop first node
    def popFront(self,h):
        if self.first(h):
            return self.remove(self.first(h))
        else:
            return "This is empty list"
    
    #pop last node
    def popBack(self, h):
        if self.last(h):
            return self.remove(self.last(h))
        else:
            return "This is empty list"
    
    #x라는 element를 갖는 새로운 노드를 하나 만들어서(=F에서 받아와서) a라는 노드 뒤에 넣기
    def insertAfter(self, x, a):
        b = self.checkFreeList() #F에서 빈 노드(첫번째) 불러오기
        b.e = x
        return self.moveAfter(b, a) #노드a 뒤에 b삽입
    
    def insertBefore(self, x, a):
        return self.insertAfter(x, a.prev)
    
    # 맨 앞에 insert
    def pushFront(self, x, h):
        return self.insertBefore(x, h.next)

    # 맨 뒤에 insert
    def pushBack(self, x, h):
        return self.insertAfter(x, h.prev)
    
    # 두개의 list 결합 (h리스트 뒤에 h' 리스트를 연결) ####### 합친다: concatenation
    def concate(self, h_prime, h):
        return self.splice(self.first(h_prime), self.last(h_prime), self.last(h)) #h에 합쳐짐 h_prime은 더미만 남음
    
    # 하나의 리스트를 a에서 끊어서 리스트 두개로 쪼개기
    def split(self, a, h):
        h_prime = self.createList()
        self.splice(a,self.last(h), h_prime)
        return h_prime
    
    #19 리스트에 노드들 다 지우기 
    def makeEmpty(self, h):
        self.concate(h,F) #freelist로 다 보내버리기
    
    # 리스트 h의 from 노드부터 끝까지 x가 저장된 첫 노드를 찾아 리턴함. 
    def findNext(self,x, fromHandle, h):
        if fromHandle is None:
            print "fromHandle is None"
            return h #더미
        h.e = x #더미에 넣고 시작
        while fromHandle.e != x:
            fromHandle=fromHandle.next
        h.e="dummy"
        return fromHandle # 중간에 x가 없었다면, 더미가 return됨. //// 있다면 while문 중간에 끝나고 찾은 그 노드가 리턴됨.
    
    # 처음부터 끝까지 출력
    def printList(self, h):
        pl = str(h.e)
        nxt = h.next
        while (nxt.e != "dummy"):
            pl += " --> "
            pl += str(nxt.e)
            nxt = nxt.next
        print pl


def __main__():
    global F
    dll = DoublyLinkedList()
    F=dll.createList()
    h=dll.createList()
    
    #make h_prime for test function concate()
    h_prime = dll.createList()
    for i in range(100, 105):
        dll.pushBack(i, h_prime)
    
    while(1):
        cmd = raw_input("\nCommand : ")
        if cmd=="insA":
            print "노드a의 오른쪽에 새로운 노드b를 삽입한다."
            print "a.e의 값과 b.e의 값을 차례로 입력하시오:"
            ea = int( raw_input("a.e의 값 :") )
            eb = int( raw_input("b.e의 값 :") )
            a = dll.findNext(ea, dll.first(h), h)
            if a!=h:
                dll.insertAfter(eb,a)
                print "insert 되었습니다."
            else:
                print "노드a가 존재하지 않습니다."
        
        if cmd=="insB":
            print "노드a의 왼쪽에 새로운 노드b를 삽입한다."
            ea = int( raw_input("a.e의 값 :") )
            eb = int( raw_input("b.e의 값 :") )
            a = dll.findNext(ea, dll.first(h), h)
            if a!=h:
                dll.insertBefore(eb,a)
            else:
                print "노드a가 존재하지 않습니다."
        
        elif cmd=="find":
            e = int( raw_input("e 값 :") )
            a = dll.findNext(e, dll.first(h), h)
            if a!=h:
                print a.e,"is founded"
            else:
                print "Not Found"
        
        elif cmd=="remove":
            print "제거할 노드의 element 값을 입력하시오."
            e = int( raw_input("e 값 :") )
            a = dll.findNext(e, dll.first(h), h)
            if a!=h:
                dll.remove(a)
                "제거되었습니다."
            else:
                print "노드a가 존재하지 않습니다."
                
        
        elif cmd=="pushFront":
            print "h의 first 값으로 e를 삽입한다."
            e = int( raw_input("e 값 :") )
            dll.pushFront(e, h)
        
        elif cmd=="pushBack":
            print "h의 last 값으로 e를 삽입한다."
            e = int( raw_input("e 값 :") )
            dll.pushBack(e, h)
            
        elif cmd=="popFront":
            print "h의 first 값 pop."
            print dll.popFront(h)
            
        elif cmd=="popBack":
            print "h의 last 값 pop."
            print dll.popBack(h)
            
        elif cmd=="moveA":
            print "노드b를 노드a 오른쪽으로 이동."
            ea = int( raw_input("a.e의 값 :") )
            eb = int( raw_input("b.e의 값 :") )
            a = dll.findNext(ea, dll.first(h), h)
            b = dll.findNext(eb, dll.first(h), h)
            if a!=h and b!=h:
                dll.moveAfter(b,a)
            else:
                print "노드a 혹은 노드b가 존재하지 않습니다."
                
        
        elif cmd=="splice":
            print "a~b까지 노드들을 떼어내, t노드 다음에 끼워넣기"
            ea = int( raw_input("a.e의 값 :") )
            eb = int( raw_input("b.e의 값 :") )
            et = int( raw_input("t.e의 값 :") )
            a = dll.findNext(ea, dll.first(h), h)
            b = dll.findNext(eb, dll.first(h), h)
            t = dll.findNext(et, dll.first(h), h)
            if a!=h and b!=h:
                dll.splice(a,b,t)
            else:
                print "노드a or 노드b or 노드t가 존재하지 않습니다."
        
        elif cmd=="concate":
            print "(현재 다루는 h와 미리 만들어 놓은 h') 두개의 list 결합 "
            dll.concate(h_prime, h)
            print "두 개의 리스트가 h에 합쳐졌습니다."
            
        elif cmd=="split":
            print "하나의 리스트를 a에서 끊어서 리스트 두개로 쪼개기"
            ea = int( raw_input("a.e의 값 :") )
            a = dll.findNext(ea, dll.first(h), h)
            if a!=h:
                h_prime = dll.split(a, h)
                print "h_prime 결과 : "
                dll.printList(h_prime)
            else:
                print "노드a가 존재하지 않습니다."
        
        elif cmd=="makeEmpty":
            if not dll.isEmpty(h):
                dll.concate(h,F)
                print "리스트에 있던 노드들이 모두 지워졌습니다."
            else:
                print "현재 리스트에 노드가 없습니다."
            
        elif cmd=="print":
            dll.printList(h)
        
        elif cmd=="exit":
            break;

__main__()