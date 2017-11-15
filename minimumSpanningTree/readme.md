##### sorted的lambda用法：

    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
    ]
    sorted(student_tuples,key=lambda s:s[1])
    >>output:  [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
    
sorted的第三部分的意思是：以student_tuples的第2位，即'A','B'来sort。然后排出一个结果。那个s:s可以换成任何名字。
