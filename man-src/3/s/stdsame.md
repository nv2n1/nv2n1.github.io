---
title: "stdsame(3)"
name: "stdsame"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsame/"
---

std::Same - std::Same

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;concepts&gt;

template &lt; class T, class U &gt;    (since C++20)

concept Same = /* see below */;</code></pre> 
The concept Same&lt;T, U&gt; is satisfied if and only if T and U denote the same type. 
std::Same&lt;T, U&gt; subsumes std::Same&lt;U, T&gt; and vice versa. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;namespace detail { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt; class T, class U &gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;concept SameHelper = std::is_same_v&lt;T, U&gt;; 
&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;template&lt; class T, class U &gt; 
&nbsp;<wbr>&nbsp;concept Same = detail::SameHelper&lt;T, U&gt; &amp;&amp; detail::SameHelper&lt;U, T&gt;;

<h2>See also</h2>

is_same checks if two types are the same 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
