---
title: "stdexperimentalrangesconvertibleto(3)"
name: "stdexperimentalrangesconvertibleto"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesconvertibleto/"
---

std::experimental::ranges::ConvertibleTo - std::experimental::ranges::ConvertibleTo

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/concepts&gt;

template &lt;class From, class To&gt;

concept bool ConvertibleTo =

std::is_convertible&lt;From, To&gt;::value &amp;&amp;           (ranges TS)

requires(From (&amp;f)()) {

    static_cast&lt;To&gt;(f());

};</code></pre> 
The concept ConvertibleTo&lt;From, To&gt; specifies that an expression of the type and value category specified by From can be implicitly and explicitly converted to the type To, and the two forms of conversion are equivalent. 
Specifically, ConvertibleTo&lt;From, To&gt; is satisfied only if, given the invented function To test(From (&amp;f)()) { return f(); } and a function f of type From () such that the expression f() is equality-preserving (see below), 
* Either 
&nbsp;<wbr>&nbsp;o To is neither an object type nor a reference-to-object type, or 
&nbsp;<wbr>&nbsp;o static_cast&lt;To&gt;(f()) is equal to test(f), and 
* One of the following is true: 
&nbsp;<wbr>&nbsp;o From is not a reference-to-object type, or 
&nbsp;<wbr>&nbsp;o From is an rvalue reference to a non-const-qualified type, and the resulting state of the object referenced by f() is valid but unspecified after either expression above; or 
&nbsp;<wbr>&nbsp;o the object referred to by f() is not modified by either expression above. 
There need not be any subsumption relationship between ConvertibleTo&lt;From, To&gt; and std::is_convertible&lt;From, To&gt;::value. 
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
