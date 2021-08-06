Author: Kshitij Mathur <br>
Email ID: mathurk29@gmail.com

# Sequences Types



All sequences are iterables, but all iterables are not sequences i.e. unordered collections For ex: Set



## Concatenation
Concatenation takes 2 **sequences** of same **type** and concatenate them together

- We can use + operator, * operator or use join function to concatenate strings.

```
"".join(['a', 'b', 'c'])
abc

"".join(list('abc') + ['a', 'b', 'c'])
abcabc


(1, 2, 3)* 4
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)


```


# Slicing

```
s = 'python'
s[4:1000]
'on'

#but 

l[1000]
IndexError: list index out of range

l1 = [1, 2, 3]
l2 = l1[:]
id(l1), id(l2), l1 is l2
(140319651080768, 140319653828480, False)



s = "python"
s[0:5:2], s[::-1], s[-1::-1], s[-3::-1]
('pto', 'nohtyp', 'nohtyp', 'htyp')



l




l = [Decimal('10.5')]
l2 = l * 2
id(l[0]), id(l2[0]), id(l2[1])
(140319647999456, 140319647999456, 140319647999456)

# In repetition, we will take the same object and just repeat it

# So when we deal with immutable objects, it's fine, but if is is mutable, we have a problem as chaning one would change all.


```

- Slicing returns new list
- list append/extend/pop/insert/reverse/ returns None and adds in the same list

# Copy vs deepcoypy

Shallow copy refers to same object. Deepcopy iteratively creates new objects - as much as depth is there.


## dis

```
from dis import dis


> dis(compile('(1, 2, 3, 4, 5, 6, "a")', 'sting', 'eval'))


  1           0 LOAD_CONST               0 ((1, 2, 3, 4, 5, 6, 'a'))
              2 RETURN_VALUE



> dis(compile('[1, 2, 3, 4, 5, 6, "a"]', 'sting', 'eval'))

1           0 LOAD_CONST               0 (1)
              2 LOAD_CONST               1 (2)
              4 LOAD_CONST               2 (3)
              6 LOAD_CONST               3 (4)
              8 LOAD_CONST               4 (5)
             10 LOAD_CONST               5 (6)
             12 LOAD_CONST               6 ('a')
             14 BUILD_LIST               7
             16 RETURN_VALUE

```


List has less Storage efficiency as it keeps some room for more elements.



# Slicing