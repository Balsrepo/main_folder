-------
Rings
-------

Ring – Let addition (+) and Multiplication (.) be two binary operations defined on a non empty set R. Then R is said to form a ring w.r.t addition (+) and multiplication (.) if the following conditions are satisfied:

(R, +) is an abelian group ( i.e commutative group)  
(R, .) is a semigroup

For any three elements a, b, c epsilon R the left distributive law a.(b+c) = a.b + a.c and the right distributive property
  (b + c).a = b.a + c.a  ; Therefore a non- empty set R is a ring w.r.t to binary operations + and . if the following conditions are satisfied.  
  
  
Defintion source:  
https://www.geeksforgeeks.org/mathematics-rings-integral-domains-and-fields/

-----------
How to Run:
-----------

Input: An integer 'x'  
Output: A matrix showing (Zx,+) and (Zx,*).

>python math.py

  
Enter the number: 4  
(Z4 ,+)  
    +(0, 1, 2, 3)  
0 [0, 1, 2, 3]  
1 [1, 2, 3, 0]  
2 [2, 3, 0, 1]  
3 [3, 0, 1, 2]

(Z4 ,*)  
    *(0, 1, 2, 3)  
0 [0, 0, 0, 0]  
1 [0, 1, 2, 3]  
2 [0, 2, 0, 2]  
3 [0, 3, 2, 1]  


-------
Note: 
-------
This code is made for fun to understand the concepts of Ring and groups.
Sometimes small example can make us understand things clearly.

-----
Tags:
-----
#Rings #Groups #Mathematics #Mathematics #Ring 
