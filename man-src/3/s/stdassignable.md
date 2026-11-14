---
title: "stdassignable(3)"
name: "stdassignable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdassignable/"
---

std::Assignable - std::Assignable

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;concepts&gt;

    template &lt;class LHS, class RHS&gt;

    concept Assignable =

        std::is_lvalue_reference_v&lt;LHS&gt; &amp;&amp;

        std::CommonReference &lt;

        const std::remove_reference_t&lt;LHS&gt;
&amp;, (since C++ 20)

           const std::remove_reference_t&lt;RHS&gt; &amp; &gt; &amp;&amp;

                                                  requires(LHS lhs, RHS &amp;&amp;rhs)
{

    lhs = std::forward&lt;RHS&gt;(rhs);

    requires std::Same&lt;decltype(lhs = std::forward&lt;RHS&gt;(rhs)), LHS&gt;;
};</code></pre> 
The concept Assignable&lt;LHS, RHS&gt; specifies that an expression of the type and value category specified by RHS can be assigned to an lvalue expression whose type is specified by LHS. 
Given 
* lhs, an lvalue that refers to an object lcopy such that decltype((lhs)) is LHS, 
* rhs, an expression such that decltype((rhs)) is RHS, 
* rcopy, a distinct object that is equal to rhs, 
Assignable&lt;LHS, RHS&gt; is satisfied only if * std::addressof(lhs = rhs) == std::addressof(lcopy) (i.e., the assignment expression yields an lvalue referring to the left operand);

* After evaluating lhs = rhs: 
&nbsp;<wbr>&nbsp;o lhs is equal to rcopy, unless rhs is a non-const xvalue that refers to lcopy (i.e., the assignment is a self-move-assignment), 
&nbsp;<wbr>&nbsp;o if rhs is a glvalue: #If it is a non - const xvalue, the object to which it refers is in a valid but unspecified state;
#Otherwise, the object it refers to is not modified;
 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 
Unless noted otherwise, every expression used in a requires-expression is required to be equality preserving and stable, and the evaluation of the expression may only modify its non-constant operands. Operands that are constant must not be modified. 

<h2>Notes</h2>

<pre><code>Assignment need not be a total function. In particular, if assigning to some object x can cause some other object y to be modified, then x = y is likely not in the domain of =. This typically happens if the right operand is owned directly or indirectly by the left operand (e.g., with smart pointers to nodes in an node-based data structure, or with something like std::vector&lt;std::any&gt;).
</code></pre>

<h2>See also</h2>

is_assignable 
is_trivially_assignable 
is_nothrow_assignable checks if a type has a assignment operator for a specific argument 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
