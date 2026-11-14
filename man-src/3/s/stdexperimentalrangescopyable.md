---
title: "stdexperimentalrangescopyable(3)"
name: "stdexperimentalrangescopyable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangescopyable/"
---

std::experimental::ranges::Copyable - std::experimental::ranges::Copyable

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / concepts&gt;

    template &lt;class T&gt;

    concept bool Copyable =

        CopyConstructible&lt;T&gt; &amp;&amp; (ranges TS)

                                    Movable&lt;T&gt; &amp;&amp;

        Assignable&lt;T &amp;, const T &amp;&gt;;</code></pre> 
The concept Copyable&lt;T&gt; specifies that T is an Movable object type that can also copied (that is, it supports copy construction and copy assignment). 

<h2>Notes</h2>

It is intended that Copyable&lt;T&gt; also requires Assignable&lt;T&amp;, const T&gt; (assignment from const rvalue) and Assignable&lt;T&amp;, T&amp;&gt; (assignment from non-const lvalue) to be satisfied. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specifies that an object of a type can be moved and swapped 
Movable (concept) 
