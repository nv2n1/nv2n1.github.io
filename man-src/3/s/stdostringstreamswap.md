---
title: "stdostringstreamswap(3)"
name: "stdostringstreamswap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdostringstreamswap/"
---

std::basic_ostringstream::swap - std::basic_ostringstream::swap

<h2>Synopsis</h2>

<pre><code>void swap(basic_ostringstream &amp;other);
(since C++ 11)</code></pre> 
Exchanges the state of the stream with those of other. 
This is done by callingbasic_ostream&lt;CharT, Traits&gt;::swap(other) and rdbuf()-&gt;swap(*other.rdbuf()). 

<h2>Parameters</h2>

other - stream to exchange the state with

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

<pre><code>operator= moves the string stream
(public member function)

(C++11)</code></pre> 
swap swaps two basic_stringbuf objects 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function of std::basic_stringbuf&lt;CharT,Traits,Allocator&gt;)</i> 
<i>(C++11)</i> 
