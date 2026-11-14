---
title: "stdbasic_ifstream(3)"
name: "stdbasic_ifstream"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbasic_ifstream/"
---

std::basic_ifstream&lt;CharT,Traits&gt;::swap - std::basic_ifstream&lt;CharT,Traits&gt;::swap

<h2>Synopsis</h2>

<pre><code>void swap(basic_ifstream &amp;other);
(since C++ 11)</code></pre> 
Exchanges the state of the stream with those of other. 
This is done by calling basic_istream&lt;CharT, Traits&gt;::swap(other) and rdbuf()-&gt;swap(other.rdbuf()). 

<h2>Parameters</h2>

other - stream to exchange the state with

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

<pre><code>operator= moves the file stream
(public member function)

(C++11)</code></pre> 
swap swaps two basic_filebuf objects 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function of std::basic_filebuf&lt;CharT,Traits&gt;)</i> 
<i>(C++11)</i> 
