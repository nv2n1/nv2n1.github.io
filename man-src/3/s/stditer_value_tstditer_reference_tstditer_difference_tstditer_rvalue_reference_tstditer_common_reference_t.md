---
title: "stditer_value_tstditer_reference_tstditer_difference_tstditer_rvalue_reference_tstditer_common_reference_t(3)"
name: "stditer_value_tstditer_reference_tstditer_difference_tstditer_rvalue_reference_tstditer_common_reference_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stditer_value_tstditer_reference_tstditer_difference_tstditer_rvalue_reference_tstditer_common_reference_t/"
---

std::iter_value_t,std::iter_reference_t,std::iter_difference_t,std::iter_rvalue_reference_t,std::iter_common_reference_t - std::iter_value_t,std::iter_reference_t,std::iter_difference_t,std::iter_rvalue_reference_t,std::iter_common_reference_t

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;iterator&gt;

template&lt; class T &gt;

concept /*dereferenceable*/ = /* see below */; // exposition only

template&lt; class T &gt;                                                               (1) (since C++20)

using iter_value_t = /* see below */;

template&lt; /*dereferenceable*/ T &gt;                                                 (2) (since C++20)

using iter_reference_t = decltype(*std::declval&lt;T&amp;&gt;());

template&lt; class T &gt;                                                               (3) (since C++20)

using iter_difference_t = /* see below */;

template&lt; /*dereferenceable*/ T&gt;

requires /* see below */                                                          (4) (since C++20)

using iter_rvalue_reference_t = decltype(ranges::iter_move(std::declval&lt;T&amp;&gt;()));

template&lt; Readable T &gt;

using iter_common_reference_t = std::common_reference_t&lt;std::iter_reference_t&lt;T&gt;, (5) (since C++20)

std::iter_value_t&lt;T&gt;&amp;&gt;;</code></pre> 
Compute the associated types of an iterator. The exposition-only concept dereferenceable is satisfied if and only if the expression *std::declval&lt;T&amp;&gt;() is valid and has a referenceable type (in particular, not void). 
1) Computes the value type of T. If std::iterator_traits&lt;T&gt; is not specialized, then std::iter_value_t&lt;T&gt; is std::readable_traits&lt;T&gt;::value_type. Otherwise, it is std::iterator_traits&lt;T&gt;::value_type. 
2) Computes the reference type of T. 
3) Computes the difference type of T. If std::iterator_traits&lt;T&gt; is not specialized, then std::iter_difference_t&lt;T&gt; is std::incrementable_traits&lt;T&gt;::difference_type. Otherwise, it is std::iterator_traits&lt;T&gt;::difference_type. 
4) Computes the rvalue reference type of T. The &quot;see below&quot; portion of the constraint on this alias template is satisfied if and only if the expression ranges::iter_move(std::declval&lt;T&amp;&gt;()) is valid and has a referenceable type (in particular, not void). 
5) Computes the common reference type of T. This is the common reference type between its reference type and an lvalue reference to its value type. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specifies that a type is readable by applying operator * 
Readable (concept) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specifies that a Semiregular type can be incremented with pre- and post-increment operators 
WeaklyIncrementable (concept) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes the value type of a Readable type 
readable_traits <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes the difference type of a WeaklyIncrementable type 
incrementable_traits <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;provides uniform interface to the properties of an iterator 
iterator_traits <i>(class template)</i> 
