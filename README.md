Author: Kshitij Mathur <br>
Email ID: mathurk29@gmail.com

# Sequences Types


Sequence: collection whose elements are indexed.

Iterable: collection whose elements can be iterated


Python's default sequence types:
- all sequence types are indexable and start with 0.
- all sequence types are iterable
- s[1] will give TypeError, cz set is not a Type that is indexable


- **All sequences are iterables** ie we can iterate over them

-  **but all iterables are not sequences** 

- Set is not a sequence as it is not subscriptible

- Set is an itearable as we can loop over it.

- iterables are more general than sequence types. i.e.

**Iterables which are indexed are sequences**

- sequence types mostly will have `in` operator.

-

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

```python
l = [Decimal(10.5)]

l2 = l * 2 # This is called repetition

id(l[0]), id(l2[0]), id(l2[1]) # All would be same

```
In repeatition, we use **same object** and **repeat** it

The above concept is a concern because if you change one object, you invariably change all the objects referencing to it.




- Tip: to empty a list, don't use ``` l = []``` cz it will create a new list. Use ``` l.clear()```

- functions doing in-place operations generally return NoneType

- list.append() just takes one arg
- for > one element, use extend


We can also extend a list using slicing.
```
For ex:

l = [1,2,3]
l[-1:0] = (4,5,6)
# l = [1,2,3,4,5,6]

```

 - reverse a string
 1. `l[::-1] # will create new list`
 2. `l.reverse() #in-place operation`

## copy function

This function does first level copy (SHALLOW COPY).
ie. it will create new object, but its contents will refer to same mem addresses.


Shallow copy refers to same object. Deepcopy iteratively creates new objects - as much as depth is there.

## deepcopy

It will create new objects recursively, except string interning.

## Disassemble

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



## Slicing

> data = 'rohan shravan ka03mt9999 aqeo4523w bangalore'
> range_name = slice(0, 5)

> data[0:5]
'rohan'

> data[slice]
'rohan'

## Few examples
```
> l = 'python'
> l[1:1], l[0:600], l[0:6:3], l[:], l[:-1], l[None:], l[None:None], l[6::-1]

('', 'python', 'ph', 'python', 'pytho', 'python', 'python', 'nohtyp')
```

# Custom Sequences

`len(my_list)` is same as ` my_list.__len__()`

`my_list[2]` is same as ` my_list.__getitem__(2)`

`my_list[::-1]` is same as  `my_list.__getitem__(slice(None, None, -1))`

If we implement above three methods, we have our own custom sequence!

Apart from it, we have to raise IndexError if accessing outside list.

```python

from functools import lru_cache

class Fib:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0 or s >=self.n:
                raise IndexError
            else:
                return Fib._fib(s)
            
    @staticmethod #Static methods are methods that are bound to a class rather than its object.
    @lru_cache(2**10) #powers of 2
    def _fib(n):
        if n < 2:
            return 1
        else:
            return Fib._fib(n-1) + Fib._fib(n-2)


```

Static methods written at module level can't be override by a subclass.