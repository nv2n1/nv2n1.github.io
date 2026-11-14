---
title: "stdexperimentalmake_optional(3)"
name: "stdexperimentalmake_optional"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalmake_optional/"
---

std::experimental::make_optional - std::experimental::make_optional

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/optional&gt;

template&lt; class T &gt;

constexpr optional&lt;typename std::decay&lt;T&gt;::type&gt;   (library fundamentals TS)

make_optional( T&amp;&amp; value );</code></pre> 
Creates an optional object from value. Effectively calls optional&lt;typename std::decay&lt;T&gt;::type&gt;(std::forward&lt;T&gt;(value)) 

<h2>Parameters</h2>

value - the value to construct optional object with

<h2>Return value</h2>

An optional object with value as the contained value. 

<h2>Exceptions</h2>

Throws any exception thrown by the constructor of T.

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the optional object 
constructor <i>(public member function)</i> 
