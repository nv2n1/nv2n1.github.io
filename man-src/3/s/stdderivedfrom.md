---
title: "stdderivedfrom(3)"
name: "stdderivedfrom"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdderivedfrom/"
---

std::DerivedFrom - std::DerivedFrom

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;concepts&gt;

    template &lt;class Derived, class Base&gt;

    concept DerivedFrom = (since C++ 20)

                              std::is_base_of_v&lt;Base, Derived&gt; &amp;&amp;

                          std::is_convertible_v&lt;const volatile Derived *, const volatile Base *&gt;;</code></pre> 
The concept DerivedFrom&lt;Derived, Base&gt; is satisfied if and only if Base is a class type that is either Derived or a public and unambiguous base of Derived, ignoring cv-qualifiers. 
Note that this behaviour is different to std::is_base_of when Base is a private or protected base of Derived. 

<h2>See also</h2>

is_base_of checks if a type is derived from the other type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
is_convertible 
is_nothrow_convertible checks if a type can be converted to the other type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
(C++20) 
