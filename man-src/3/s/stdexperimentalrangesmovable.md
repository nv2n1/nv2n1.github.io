---
title: "stdexperimentalrangesmovable(3)"
name: "stdexperimentalrangesmovable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesmovable/"
---

std::experimental::ranges::Movable - std::experimental::ranges::Movable

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/concepts&gt;

template &lt; class T &gt;

concept bool Movable =

std::is_object&lt;T&gt;::value &amp;&amp;                       (ranges TS)

MoveConstructible&lt;T&gt; &amp;&amp;

Assignable&lt;T&amp;, T&gt; &amp;&amp;

Swappable&lt;T&gt;;</code></pre> 
The concept Movable&lt;T&gt; specifies that T is an object type that can moved (that is, it can be move constructed, move assigned, and lvalues of type T can be swapped). 
There need not be any subsumption relationship between Movable&lt;T&gt; and std::is_object&lt;T&gt;::value. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specifies that an object of a type can be copied, moved, and swapped 
Copyable (concept) 
