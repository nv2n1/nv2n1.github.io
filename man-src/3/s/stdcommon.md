---
title: "stdcommon(3)"
name: "stdcommon"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcommon/"
---

std::Common - std::Common

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;concepts&gt;

    template &lt;class T, class U&gt;

    concept Common =

        std::Same&lt;std::common_type_t&lt;T, U&gt;, std::common_type_t&lt;U, T&gt;&gt; &amp;&amp;

    requires
{

    static_cast&lt;std::common_type_t&lt;T, U&gt;&gt;(std::declval&lt;T&gt;());

    static_cast&lt;std::common_type_t&lt;T, U&gt;&gt;(std::declval&lt;U&gt;());

} &amp;&amp;

    std::CommonReference&lt;(since C++ 20)

                             std::add_lvalue_reference_t&lt;const T&gt;,

                         std::add_lvalue_reference_t&lt;const U&gt;&gt; &amp;&amp;

    std::CommonReference&lt;

        std::add_lvalue_reference_t&lt;std::common_type_t&lt;T, U&gt;&gt;,

        std::common_reference_t&lt;

            std::add_lvalue_reference_t&lt;const T&gt;,

            std::add_lvalue_reference_t&lt;const U&gt;&gt;&gt;;</code></pre> 
The concept Common&lt;T, U&gt; specifies that two types T and U share a common type (as computed by std::common_type_t) to which both can be converted. 
T and U model Common&lt;T, U&gt; only if, given equality-preserving expressions t1, t2, u1 and u2 such that decltype((t1)) and decltype((t2)) are both T and decltype((u1)) and decltype((u2)) are both U, 
* std::common_type_t&lt;T, U&gt;(t1) equals std::common_type_t&lt;T, U&gt;(t2) if and only if t1 equals t2; and 
* std::common_type_t&lt;T, U&gt;(u1) equals std::common_type_t&lt;T, U&gt;(u2) if and only if u1 equals u2. 
In other words, the conversion to the common type must preserve equality. 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 

<h2>See also</h2>

common_type determines the common type of a group of types 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
common_reference determines the common reference type of a group of types 
basic_common_reference <i>(class template)</i> 
(C++20) 
CommonReference specifies that two types share a common reference type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(concept) 
(C++20) 
