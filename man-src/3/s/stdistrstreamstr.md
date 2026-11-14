---
title: "stdistrstreamstr(3)"
name: "stdistrstreamstr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdistrstreamstr/"
---

std::istrstream::str - std::istrstream::str

<h2>Synopsis</h2>

<pre><code>char *str();</code></pre> 
Returns the pointer to the beginning of the buffer, after freezing it. Effectively calls rdbuf()-&gt;str() 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

Pointer to the beginning of the buffer in the associated std::strsteambuf or NULL if no buffer is available. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
