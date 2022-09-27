from Shared.Node import Node

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        
        itr = self.head
        llist = ''

        while itr:
            llist+= str(itr.data) + '-->'
            itr = itr.next
        print(llist)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_values):
        self.head = None
        for value in data_values:
            self.insert_at_end(value)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
            
        return count

    def remove_at(self, index):
        if index<0 or index>= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1

    def insert_at(self, index, value):
        if index<0 or index>= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_beginning(value)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(value, itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1

    def insert_after_value(self, existing_value, new_value):
        itr = self.head
        exists = False
        while itr:
            if itr.data == existing_value:
                exists = True
                node = Node(new_value, itr.next)
                itr.next = node
                break
            itr = itr.next
        
        if not exists:
            raise Exception("No such value exists!")

    def remove_by_value(self, value):
        if self.head == None:
            return
        
        itr = self.head
        if itr.data == value:
            if itr.next == None:
                self.head = None
            else:
                self.head = itr.next
            return

        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                return
            itr = itr.next
        
        print(f"{value} not present in LL")

        


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()