---
title: "stdcopyable(3)"
name: "stdcopyable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcopyable/"
---

std::Copyable - std::Copyable

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;concepts&gt;

    template &lt;class T&gt;

    concept Copyable =

        std::CopyConstructible&lt;T&gt; &amp;&amp;(since C++ 20)

            std::Movable&lt;T&gt; &amp;&amp;

        std::Assignable&lt;T &amp;, const T &amp;&gt;;</code></pre> 
The concept Copyable&lt;T&gt; specifies that T is an Movable object type that can also copied (that is, it supports copy construction and copy assignment). 

<h2>Notes</h2>

It is intended that Copyable&lt;T&gt; also requires std::Assignable&lt;T&amp;, const T&gt; (assignment from const rvalue) and std::Assignable&lt;T&amp;, T&amp;&gt; (assignment from non-const lvalue) to be satisfied. 

<h2>See also</h2>

Movable specifies that an object of a type can be moved and swapped 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(concept) 
(C++20) 
