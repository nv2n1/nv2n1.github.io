---
title: "stdexperimentalrangesderivedfrom(3)"
name: "stdexperimentalrangesderivedfrom"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesderivedfrom/"
---

std::experimental::ranges::DerivedFrom - std::experimental::ranges::DerivedFrom

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/concepts&gt;

template &lt; class T, class U &gt;

concept bool DerivedFrom =                                               (ranges TS)

std::is_base_of&lt;U, T&gt;::value &amp;&amp;

std::is_convertible&lt;std::remove_cv_t&lt;T&gt;*, std::remove_cv_t&lt;U&gt;*&gt;::value;</code></pre> 
The concept DerivedFrom&lt;T, U&gt; is satisfied if and only if U is a class type that is either T or a public and unambiguous base of T. 
Despite the use of std::is_base_of and std::is_convertible in its description above, DerivedFrom is not required to use it in its implementation. Thus, there need not be any subsumption relationship between DerivedFrom&lt;T, U&gt; and std::is_base_of&lt;U,T&gt;::value or std::is_convertible&lt;std::remove_cv_t&lt;T&gt;*, std::remove_cv_t&lt;U&gt;*&gt;::value. 

<h2>See also</h2>

is_base_of checks if a type is derived from the other type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
is_convertible 
is_nothrow_convertible checks if a type can be converted to the other type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
(C++20) 
