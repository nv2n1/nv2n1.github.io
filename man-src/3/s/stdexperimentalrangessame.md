---
title: "stdexperimentalrangessame(3)"
name: "stdexperimentalrangessame"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangessame/"
---

std::experimental::ranges::Same - std::experimental::ranges::Same

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/concepts&gt;

template &lt; class T, class U &gt;                                (ranges TS)

concept bool Same = std::is_same&lt;T, U&gt;::value; // see below</code></pre> 
The concept Same&lt;T, U&gt; is satisfied if and only if T and U denote the same type. 
Despite being specified using it, there need not be any subsumption relationship between Same&lt;T, U&gt; and std::is_same&lt;T, U&gt;::value. 
For the purposes of constraint checking, Same&lt;T, U&gt; implies Same&lt;U, T&gt;. 

<h2>Notes</h2>

The additional requirement on constraint checking differentiates Same from std::is_same. 

<h2>See also</h2>

is_same checks if two types are the same 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
