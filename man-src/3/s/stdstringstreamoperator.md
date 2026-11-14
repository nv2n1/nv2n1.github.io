---
title: "stdstringstreamoperator(3)"
name: "stdstringstreamoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstringstreamoperator/"
---

std::basic_stringstream::operator= - std::basic_stringstream::operator=

<h2>Synopsis</h2>

<pre><code>basic_stringstream&amp; operator=( basic_stringstream&amp;&amp; other );  (since C++11)</code></pre> 
Move assigns the string stream other to *this, effectively move-assigning both the std::basic_iostream base class and the associated std::basic_stringbuf. 
Note that the base class move assignment swaps all stream state variables (except for rdbuf) between *this and other. 

<h2>Parameters</h2>

other - string stream to move from

<h2>Return value</h2>

*this 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

swap swaps two string streams 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
<i>(C++11)</i> <pre><code>operator= assigns a basic_stringbuf object
(public member function of std::basic_stringbuf&lt;CharT,Traits,Allocator&gt;)

(C++11)
operator= move-assigns another basic_iostream
(protected member function)

(C++11)




</code></pre>
