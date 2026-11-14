---
title: "stdbeginstdvalarray(3)"
name: "stdbeginstdvalarray"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbeginstdvalarray/"
---

std::begin(std::valarray) - std::begin(std::valarray)

<h2>Synopsis</h2>

<pre><code>template &lt;class T&gt;
(1)(since C++ 11)

    /*unspecified1*/ begin(valarray&lt;T&gt; &amp;v);

template &lt;class T&gt;
(2)(since C++ 11)

    /*unspecified2*/ begin(const valarray&lt;T&gt; &amp;v);</code></pre> 
The overload of std::begin for valarray returns an iterator of unspecified type referring to the first element in the numeric array. 
1) The return type meets the requirements of mutable LegacyRandomAccessIterator. 
2) The return type meets the requirements of constant LegacyRandomAccessIterator. 
The iterator obtained from this function is invalidated when the member function resize() is called on the array v or when the lifetime of v ends, whichever comes first. 

<h2>Parameters</h2>

v - a numeric array

<h2>Return value</h2>

Iterator to the first value in the numeric array. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Notes</h2>

Unlike other functions that take std::valarray arguments, begin() cannot accept the replacement types (such as the types produced by expression templates) that may be returned from expressions involving valarrays: std::begin(v1 + v2) is not portable, std::begin(std::valarray&lt;T&gt;(v1 + v2)) has to be used instead. 
The intent of this function is to allow range_for_loops to work with valarrays, not to provide container semantics. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

std::end(std::valarray) specializes std::end 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
