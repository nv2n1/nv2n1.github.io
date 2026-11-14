---
title: "stditer_value_tstditer_reference_tstditer_difference_t(3)"
name: "stditer_value_tstditer_reference_tstditer_difference_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stditer_value_tstditer_reference_tstditer_difference_t/"
---

std::iter_value_t,std::iter_reference_t,std::iter_difference_t, - std::iter_value_t,std::iter_reference_t,std::iter_difference_t,

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;iterator&gt;

template&lt; class T &gt;

concept /*dereferenceable*/ = /* see below */; // exposition only

template&lt; class T &gt;                                                      (1) (since

using iter_value_t = /* see below */;                                        C++20)

template&lt; /*dereferenceable*/ T &gt;                                        (2) (since

using iter_reference_t = decltype(*std::declval&lt;T&amp;&gt;());                      C++20)

template&lt; class T &gt;                                                      (3) (since

using iter_difference_t = /* see below */;                                   C++20)

template&lt; /*dereferenceable*/ T&gt;
requires /* see below */                                                 (4) (since
C++20)

using iter_rvalue_reference_t =

decltype(ranges::iter_move(std::declval&lt;T&amp;&gt;()));

template&lt; Readable T &gt;
using iter_common_reference_t =                                          (5) (since

std::common_reference_t&lt;std::iter_reference_t&lt;T&gt;,                            C++20)
std::iter_value_t&lt;T&gt;&amp;&gt;;</code></pre> 
Compute the associated types of an iterator. The exposition-only concept 
dereferenceable is satisfied if and only if the expression&nbsp;<wbr>*std::declval&lt;T&amp;&gt;()&nbsp;<wbr>is 
valid and has a referenceable type&nbsp;<wbr>(in particular, not void). 
1)&nbsp;<wbr>Computes the value type of T. If std::iterator_traits&lt;T&gt;&nbsp;<wbr>is not specialized, then 
std::iter_value_t&lt;T&gt;&nbsp;<wbr>is std::readable_traits&lt;T&gt;::value_type. Otherwise, it is 
std::iterator_traits&lt;T&gt;::value_type. 
2)&nbsp;<wbr>Computes the reference type of T. 
3)&nbsp;<wbr>Computes the difference type of T. If std::iterator_traits&lt;T&gt;&nbsp;<wbr>is not specialized, 
then std::iter_difference_t&lt;T&gt;&nbsp;<wbr>is std::incrementable_traits&lt;T&gt;::difference_type. 
Otherwise, it is std::iterator_traits&lt;T&gt;::difference_type. 
4)&nbsp;<wbr>Computes the rvalue reference type of T. The&nbsp;<wbr>&quot;see below&quot;&nbsp;<wbr>portion of the 
constraint on this alias template is satisfied if and only if the expression 
ranges::iter_move(std::declval&lt;T&amp;&gt;())&nbsp;<wbr>is valid and has a referenceable type&nbsp;<wbr>(in 
particular, not void). 
5)&nbsp;<wbr>Computes the common reference type of T. This is the common reference type 
between its reference type and an lvalue reference to its value type. 

<h2>See also</h2>

Readable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specifies that a type is readable by applying operator&nbsp;<wbr>* 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(concept) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specifies that a Semiregular type can be incremented with pre- 
WeaklyIncrementable&nbsp;<wbr>&nbsp;<wbr>and post-increment operators 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(concept) 
readable_traits&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>computes the value type of a Readable type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i> 
incrementable_traits computes the difference type of a WeaklyIncrementable type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i> 
iterator_traits&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>provides uniform interface to the properties of an iterator 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>(class template)</i> 
