class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def __str__(self):
        return "Nome: " + self.data

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if current != None:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    def imprime(self):
        itr=self.head
        list_str=" "
        while itr:
            list_str+=str(itr.data)+ "-->"
            itr=itr.next
        return list_str



def teste():
    lista_l=LinkedList()
    n=[1,2,4,5,6,7,20]
    for num in n:
        lista_l.add(num)
    print(lista_l.imprime())
teste()