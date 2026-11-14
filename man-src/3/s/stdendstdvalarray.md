---
title: "stdendstdvalarray(3)"
name: "stdendstdvalarray"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdendstdvalarray/"
---

std::end(std::valarray) - std::end(std::valarray)

<h2>Synopsis</h2>

<pre><code>template &lt;class T&gt;
(1)(since C++ 11)

    /*unspecified1*/ end(valarray&lt;T&gt; &amp;v);

template &lt;class T&gt;
(2)(since C++ 11)

    /*unspecified2*/ end(const valarray&lt;T&gt; &amp;v);</code></pre> 
The overload of std::end for valarray returns an iterator of unspecified type referring to the one past the last element in the numeric array. 
1) The return type meets the requirements of mutable LegacyRandomAccessIterator. 
2) The return type meets the requirements of constant LegacyRandomAccessIterator. 
The iterator obtained from this function template is invalidated when the member function resize() is called on the array v or when the lifetime of v ends, whichever comes first. 

<h2>Parameters</h2>

v - a numeric array

<h2>Return value</h2>

Iterator to one past the last value in the numeric array. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Notes</h2>

Unlike other functions that take std::valarray arguments, end() cannot accept the replacement types (such as the types produced by expression templates) that may be returned from expressions involving valarrays: std::end(v1 + v2) is not portable, std::end(std::valarray&lt;T&gt;(v1 + v2)) has to be used instead. 
The intent of this function is to allow range_for_loops to work with valarrays, not to provide container semantics. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

std::begin(std::valarray) specializes std::begin 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
