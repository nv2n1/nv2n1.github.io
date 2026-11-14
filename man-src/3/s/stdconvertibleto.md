---
title: "stdconvertibleto(3)"
name: "stdconvertibleto"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdconvertibleto/"
---

std::ConvertibleTo - std::ConvertibleTo

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;concepts&gt;

template &lt;class From, class To&gt;

concept ConvertibleTo =

std::is_convertible_v&lt;From, To&gt; &amp;&amp;  (since C++20)

requires(From (&amp;f)()) {

    static_cast&lt;To&gt;(f());

};</code></pre> 
The concept ConvertibleTo&lt;From, To&gt; specifies that an expression of the type and value category specified by From can be implicitly and explicitly converted to the type To, and the two forms of conversion are equivalent. 
Specifically, ConvertibleTo&lt;From, To&gt; is satisfied only if, given a function fun of type From () such that the expression fun() is equality-preserving (see below), 
* Either <pre><code>o To is neither an object type nor a reference - to - object type, or

                                                                       o static_cast&lt;To&gt;(fun()) is equal to[]()-&gt;To
{
    return fun();
}
(), and
</code></pre> 
* One of the following is true: 
&nbsp;<wbr>&nbsp;o From is not a reference-to-object type, or 
&nbsp;<wbr>&nbsp;o From is an rvalue reference to a non-const-qualified type, and the resulting state of the object referenced by fun() is valid but unspecified after either expression above; or 
&nbsp;<wbr>&nbsp;o the object referred to by fun() is not modified by either expression above. 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 
Unless noted otherwise, every expression used in a requires-expression is required to be equality preserving and stable, and the evaluation of the expression may only modify its non-constant operands. Operands that are constant must not be modified. 

<h2>See also</h2>

is_convertible 
is_nothrow_convertible checks if a type can be converted to the other type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
(C++20) 
