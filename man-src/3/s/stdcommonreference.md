---
title: "stdcommonreference(3)"
name: "stdcommonreference"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcommonreference/"
---

std::CommonReference - std::CommonReference

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;concepts&gt;

template &lt; class T, class U &gt;

concept CommonReference =

std::Same&lt;std::common_reference_t&lt;T, U&gt;, std::common_reference_t&lt;U, T&gt;&gt; &amp;&amp;  (since C++20)

std::ConvertibleTo&lt;T, std::common_reference_t&lt;T, U&gt;&gt; &amp;&amp;

std::ConvertibleTo&lt;U, std::common_reference_t&lt;T, U&gt;&gt;;</code></pre> 
The concept CommonReference&lt;T, U&gt; specifies that two types T and U share a common reference type (as computed by std::common_reference_t) to which both can be converted. 
T and U model CommonReference&lt;T, U&gt; only if, given equality-preserving expressions t1, t2, u1 and u2 such that decltype((t1)) and decltype((t2)) are both T and decltype((u1)) and decltype((u2)) are both U, 
* std::common_reference_t&lt;T, U&gt;(t1) equals std::common_reference_t&lt;T, U&gt;(t2) if and only if t1 equals t2; and 
* std::common_reference_t&lt;T, U&gt;(u1) equals std::common_reference_t&lt;T, U&gt;(u2) if and only if u1 equals u2. 
In other words, the conversion to the common reference type must preserve equality. 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 

<h2>See also</h2>

common_reference determines the common reference type of a group of types 
basic_common_reference <i>(class template)</i> 
(C++20) 
Common specifies that two types share a common type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(concept) 
(C++20) 
common_type determines the common type of a group of types 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
