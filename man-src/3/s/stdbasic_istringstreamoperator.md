---
title: "stdbasic_istringstreamoperator(3)"
name: "stdbasic_istringstreamoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbasic_istringstreamoperator/"
---

std::basic_istringstream::operator= - std::basic_istringstream::operator=

<h2>Synopsis</h2>

<pre><code>basic_istringstream&amp; operator=( basic_istringstream&amp;&amp; other );  (since C++11)</code></pre> 
Move assigns the string stream other to *this, effectively move-assigning both the std::basic_istream base class and the associated std::basic_stringbuf. 
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
operator= move-assigns from another basic_istream
(protected member function)

(C++11)




</code></pre>
