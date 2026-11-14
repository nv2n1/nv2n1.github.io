---
title: "stdctypetable(3)"
name: "stdctypetable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdctypetable/"
---

std::ctype&lt;char&gt;::table - std::ctype&lt;char&gt;::table

<h2>Synopsis</h2>

Defined in header &lt;locale&gt; 
const mask* table() const throw(); <i>(until C++11)</i> 
const mask* table() const noexcept; <i>(since C++11)</i> 
Returns the classification table that was provided in the constructor of this instance of std::ctype&lt;char&gt;, or returns a copy of classic_table() if none was provided. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A pointer to the first element in the classification table (which an array of size std::ctype&lt;char&gt;::table_size). 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
