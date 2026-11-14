---
title: "stdmovable(3)"
name: "stdmovable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmovable/"
---

std::Movable - std::Movable

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;concepts&gt;

template &lt; class T &gt;

concept Movable =

std::is_object_v&lt;T&gt; &amp;&amp;        (since C++20)

std::MoveConstructible&lt;T&gt; &amp;&amp;

std::Assignable&lt;T&amp;, T&gt; &amp;&amp;

std::Swappable&lt;T&gt;;</code></pre> 
The concept Movable&lt;T&gt; specifies that T is an object type that can moved (that is, it can be move constructed, move assigned, and lvalues of type T can be swapped). 

<h2>See also</h2>

Copyable specifies that an object of a type can be copied, moved, and swapped 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(concept) 
(C++20) 
