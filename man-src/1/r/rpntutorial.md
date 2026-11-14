---
title: "rpntutorial(1)"
name: "rpntutorial"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpntutorial/"
---

<h2 class="name">NAME</h2>
 

 rpntutorial - Reading RRDtool RPN Expressions by Steve Rader 

<h2>DESCRIPTION</h2>

 This tutorial should help you get to grips with RRDtool <font SIZE="-1">RPN</font> expressions as seen in <font SIZE="-1">CDEF</font> arguments of RRDtool graph.

<h2>Reading Comparison Operators</h2>

 The <font SIZE="-1">LT</font>, <font SIZE="-1">LE</font>, <font SIZE="-1">GT</font>, <font SIZE="-1">GE</font> and <font SIZE="-1">EQ</font> <font SIZE="-1">RPN</font> logic operators are not as tricky as they appear. These operators act on the two values on the stack preceding them (to the left). Read these two values on the stack from left to right inserting the operator in the middle. If the resulting statement is true, then replace the three values from the stack with ``1''. If the statement if false, replace the three values with ``0''. 

 For example, think about ``2,1,GT''. This <font SIZE="-1">RPN</font> expression could be read as ``is two greater than one?'' The answer to that question is ``true''. So the three values should be replaced with ``1''. Thus the <font SIZE="-1">RPN</font> expression 2,1,GT evaluates to 1. 

 Now consider ``2,1,LE''. This <font SIZE="-1">RPN</font> expression could be read as ``is two less than or equal to one?''. The natural response is ``no'' and thus the <font SIZE="-1">RPN</font> expression 2,1,LE evaluates to 0.

<h2>Reading the IF Operator</h2>

 The <font SIZE="-1">IF</font> <font SIZE="-1">RPN</font> logic operator can be straightforward also. The key to reading <font SIZE="-1">IF</font> operators is to understand that the condition part of the traditional ``if X than Y else Z'' notation has *already* been evaluated. So the <font SIZE="-1">IF</font> operator acts on only one value on the stack: the third value to the left of the <font SIZE="-1">IF</font> value. The second value to the left of the <font SIZE="-1">IF</font> corresponds to the true (``Y'') branch. And the first value to the left of the <font SIZE="-1">IF</font> corresponds to the false (``Z'') branch. Read the <font SIZE="-1">RPN</font> expression ``X,Y,Z,IF'' from left to right like so: ``if X then Y else Z''. 

 For example, consider ``1,10,100,IF''. It looks bizarre to me. But when I read ``if 1 then 10 else 100'' it's crystal clear: 1 is true so the answer is 10. Note that only zero is false; all other values are true. ``2,20,200,IF'' (``if 2 then 20 else 200'') evaluates to 20. And ``0,1,2,IF'' (&quot;if 0 then 1 else 2) evaluates to 2. 

 Notice that none of the above examples really simulate the whole ``if X then Y else Z'' statement. This is because computer programmers read this statement as ``if Some Condition then Y else Z''. So it's important to be able to read <font SIZE="-1">IF</font> operators along with the <font SIZE="-1">LT</font>, <font SIZE="-1">LE</font>, <font SIZE="-1">GT</font>, <font SIZE="-1">GE</font> and <font SIZE="-1">EQ</font> operators.

<h2>Some Examples</h2>

 While compound expressions can look overly complex, they can be considered elegantly simple. To quickly comprehend <font SIZE="-1">RPN</font> expressions, you must know the algorithm for evaluating <font SIZE="-1">RPN</font> expressions: iterate searches from the left to the right looking for an operator. When it's found, apply that operator by popping the operator and some number of values (and by definition, not operators) off the stack. 

 For example, the stack ``1,2,3,+,+'' gets ``2,3,+'' evaluated (as ``2+3'') during the first iteration and is replaced by 5. This results in the stack ``1,5,+''. Finally, ``1,5,+'' is evaluated resulting in the answer 6. For convenience, it's useful to write this set of operations as: 

 <pre>
 1) 1,2,3,+,+    eval is 2,3,+ = 5    result is 1,5,+
 2) 1,5,+        eval is 1,5,+ = 6    result is 6
 3) 6
</pre> 

 Let's use that notation to conveniently solve some complex <font SIZE="-1">RPN</font> expressions with multiple logic operators: 

 <pre>
 1) 20,10,GT,10,20,IF  eval is 20,10,GT = 1     result is 1,10,20,IF
</pre> 

 read the eval as pop ``20 is greater than 10'' so push 1 

 <pre>
 2) 1,10,20,IF         eval is 1,10,20,IF = 10  result is 10
</pre> 

 read pop ``if 1 then 10 else 20'' so push 10. Only 10 is left so 10 is the answer. 

 Let's read a complex <font SIZE="-1">RPN</font> expression that also has the traditional multiplication operator: 

 <pre>
 1) 128,8,*,7000,GT,7000,128,8,*,IF  eval 128,8,*       result is 1024
 2) 1024   ,7000,GT,7000,128,8,*,IF  eval 1024,7000,GT  result is 0
 3) 0,              7000,128,8,*,IF  eval 128,8,*       result is 1024
 4) 0,              7000,1024,   IF                     result is 1024
</pre> 

 Now let's go back to the first example of multiple logic operators, but replace the value 20 with the variable ``input'': 

 <pre>
 1) input,10,GT,10,input,IF  eval is input,10,GT  ( lets call this A )
</pre> 

 Read eval as ``if input &gt; 10 then true'' and replace ``input,10,GT'' with ``A'': 

 <pre>
 2) A,10,input,IF            eval is A,10,input,IF
</pre> 

 read ``if A then 10 else input''. Now replace A with it's verbose description again and---voila!--you have an easily readable description of the expression: 

 <pre>
 if input &gt; 10 then 10 else input
</pre> 

 Finally, let's go back to the first most complex example and replace the value 128 with ``input'': 

 <pre>
 1) input,8,*,7000,GT,7000,input,8,*,IF  eval input,8,*     result is A
</pre> 

 where A is ``input * 8'' 

 <pre>
 2) A,7000,GT,7000,input,8,*,IF          eval is A,7000,GT  result is B
</pre> 

 where B is ``if ((input * 8) &gt; 7000) then true'' 

 <pre>
 3) B,7000,input,8,*,IF                  eval is input,8,*  result is C
</pre> 

 where C is ``input * 8'' 

 <pre>
 4) B,7000,C,IF
</pre> 

 At last we have a readable decoding of the complex <font SIZE="-1">RPN</font> expression with a variable: 

 <pre>
 if ((input * 8) &gt; 7000) then 7000 else (input * 8)
</pre>

<h2>Exercises</h2>

 Exercise 1: 

 Compute ``3,2,*,1,+ and ''3,2,1,+,*&quot; by hand. Rewrite them in traditional notation. Explain why they have different answers. 

 Answer 1: 

 <pre>
    3*2+1 = 7 and 3*(2+1) = 9.  These expressions have
    different answers because the altering of the plus and
    times operators alter the order of their evaluation.
</pre> 

 Exercise 2: 

 One may be tempted to shorten the expression 

 <pre>
 input,8,*,56000,GT,56000,input,*,8,IF
</pre> 

 by removing the redundant use of ``input,8,*'' like so: 

 <pre>
 input,56000,GT,56000,input,IF,8,*
</pre> 

 Use traditional notation to show these expressions are not the same. Write an expression that's equivalent to the first expression, but uses the <font SIZE="-1">LE</font> and <font SIZE="-1">DIV</font> operators. 

 Answer 2: 

 <pre><code>
if (input &lt;= 56000 / 8) {
    input * 8
} else {
    56000
}
input, 56000, 8, DIV, LE, input, 8, *, 56000, IF
</code></pre> 

 Exercise 3: 

 Briefly explain why traditional mathematic notation requires the use of parentheses. Explain why <font SIZE="-1">RPN</font> notation does not require the use of parentheses. 

 Answer 3: 

 <pre>
    Traditional mathematic expressions are evaluated by
    doing multiplication and division first, then addition and
    subtraction.  Parentheses are used to force the evaluation of
    addition before multiplication (etc).  RPN does not require
    parentheses because the ordering of objects on the stack
    can force the evaluation of addition before multiplication.
</pre> 

 Exercise 4: 

 Explain why it was desirable for the RRDtool developers to implement <font SIZE="-1">RPN</font> notation instead of traditional mathematical notation. 

 Answer 4: 

 <pre>
    The algorithm that implements traditional mathematical
    notation is more complex then algorithm used for RPN.
    So implementing RPN allowed Tobias Oetiker to write less
    code!  (The code is also less complex and therefore less
    likely to have bugs.)
</pre>

<h2>AUTHOR</h2>

 Steve Rader &lt;rader [at] wiscnet.net&gt; 

<h2>Index</h2>


