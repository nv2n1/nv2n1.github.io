---
title: "stdexperimentalrangescommonreference(3)"
name: "stdexperimentalrangescommonreference"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangescommonreference/"
---

std::experimental::ranges::CommonReference - std::experimental::ranges::CommonReference

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/concepts&gt;

template &lt; class T, class U &gt;

concept bool CommonReference =

Same&lt;ranges::common_reference_t&lt;T, U&gt;, ranges::common_reference_t&lt;U, T&gt;&gt; &amp;&amp;  (ranges TS)

ConvertibleTo&lt;T, ranges::common_reference_t&lt;T, U&gt;&gt; &amp;&amp;

ConvertibleTo&lt;U, ranges::common_reference_t&lt;T, U&gt;&gt;;</code></pre> 
The concept CommonReference&lt;T, U&gt; specifies that two types T and U share a common reference type (as computed by ranges::common_reference_t) to which both can be converted. 
CommonReference&lt;T, U&gt; is satisfied only if, given expressions t and u such that decltype((t)) is T and decltype((u)) is U, 
* ranges::common_reference_t&lt;T, U&gt;(t) is equal to ranges::common_reference_t&lt;T, U&gt;(t) if and only if t is an equality-preserving expression; and 
* ranges::common_reference_t&lt;T, U&gt;(u) is equal to ranges::common_reference_t&lt;T, U&gt;(u) if and only if u is an equality-preserving expression. 
In other words, the conversion to the common reference type must not alter the equality-preservation property of the original expression. 
Equality preservation 
An expression is equality preserving if it results in equal outputs given equal inputs. 
* The inputs to an expression consist of its operands. 
* The outputs of an expression consist of its result and all operands modified by the expression (if any). 
Every expression required to be equality preserving is further required to be stable: two evaluations of such an expression with the same input objects must have equal outputs absent any explicit intervening modification of those input objects. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determine the common reference type of a set of types 
common_reference <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specifies that two types share a common type 
Common (concept) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determine the common type of a set of types 
common_type <i>(class template)</i> 
