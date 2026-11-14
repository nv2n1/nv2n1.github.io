---
title: "stdios_baseimbue(3)"
name: "stdios_baseimbue"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_baseimbue/"
---

std::ios_base::imbue - std::ios_base::imbue

<h2>Synopsis</h2>

<pre><code>std::locale imbue(const std::locale &amp;loc);</code></pre> 
Sets the associated locale of the stream to the given one. Before returning, each function, registered by register_callback() is called with imbue_event as a parameter. 

<h2>Parameters</h2>

loc - new locale to associate the stream to

<h2>Return value</h2>

The locale object, associated with the stream before the operation 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns current locale 
getloc <i>(public member function)</i> 
