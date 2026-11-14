---
title: "stdctypeclassic_table(3)"
name: "stdctypeclassic_table"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdctypeclassic_table/"
---

std::ctype&lt;char&gt;::classic_table - std::ctype&lt;char&gt;::classic_table

<h2>Synopsis</h2>

Defined in header &lt;locale&gt; 
static const mask* classic_table() throw(); <i>(until C++11)</i> 
static const mask* classic_table() noexcept; <i>(since C++11)</i> 
Returns the classification table that matches the classification used by the minimal &quot;C&quot; locale. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A pointer to the first element in the classification table (which an array of size std::ctype&lt;char&gt;::table_size) 

<h2>Notes</h2>

Default-constructed std::ctype&lt;char&gt; facets use this table for classification. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
