class Node(object):
    def __init__(self, elem, next=None):
        self.elem = elem  # 表示对应的元素值
        self.next = next  # 表示下一个链接的链点

class Queue(object):
    def __init__(self):
        """队列
        
        Keyword arguments:
        self.head -- 队列头部
        self.rear -- 队列尾部
        self.length -- 队列当前长度
        Return: None
        """
        
        self.head = None  # 头部链点为 None
        self.rear = None  # 尾部链点为 None
        self.length = 0
    
    # 判断当前队列是否为空
    def isEmpty(self):
        """判断当前队列是否为空
        
        Keyword arguments:
        Return: Bool
        """
        
        return self.head is None
    
    # 往队列添加元素
    def enqueue(self, elem:object):
        """创建节点
        
        Keyword arguments:
        elem -- 要加入队列的元素
        Return: return_description
        """

        obj = Node(elem)
        self.limitLength()
        if self.isEmpty():
            self.head = obj
            self.rear = obj
        else:
            self.rear.next = obj
            self.rear = obj
        
        self.length += 1

    # 删除队列头部元素
    def pop(self):
        """删除队列头部元素
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if self.isEmpty():
            raise "队列为空"
        else:
            tmep = self.head.elem
            self.head = self.head.next
            return tmep
    
    # 限制队列长度为20
    def limitLength(self):
        """限制队列长度为20
        Return: None
        """
        if self.length == 20: # 限制队列长度为20
            self.pop()
            self.length -= 1

    # 取出队列头
    def getHead(self):
        """取出队列头
        Return: 取出队列头
        """
        return self.head.elem

    # 取出队列尾
    def getRail(self):
        """取出队列尾
        Return: 取出队列尾
        """
        return self.rear.elem