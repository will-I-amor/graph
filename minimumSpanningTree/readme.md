##### sorted的lambda用法：

    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
    ]
    sorted(student_tuples,key=lambda s:s[1])
    >>output:  [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    
sorted的第三部分的意思是：以student_tuples的第2位，即'A','B'来sort。然后排出一个结果。那个s:s可以换成任何名字。



    
    parent是list，parent = [0,1,2,3]

    [0,1,2,2]  ->  [2,1,2,2]可以在kruskal那个function里print出parent和rank的值。
    graph的值print时需要加self.graph
    rank一开始是[0,0,0,0]后来变成[0,0,1,0]
    graph = [[2, 3, 4], [0, 3, 5], [0, 2, 6], [0, 1, 10], [1, 3, 15]]
