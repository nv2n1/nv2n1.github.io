---
title: "stdmoveconstructible(3)"
name: "stdmoveconstructible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmoveconstructible/"
---

std::MoveConstructible - std::MoveConstructible

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;concepts&gt;

template&lt; class T &gt;                                                                (since C++20)

concept MoveConstructible = std::Constructible&lt;T, T&gt; &amp;&amp; std::ConvertibleTo&lt;T, T&gt;;</code></pre> 
The concept MoveConstructible is satisfied if T is a reference type, or if it is an object type where an object of that type can constructed from an rvalue of that type in both direct- and copy-initialization contexts, with the usual semantics. 
More precisely, if T is an object type, then MoveConstructible&lt;T&gt; is satisfied only if given 
* rv, an rvalue of type T, and 
* u2, a distinct object of type T equal to rv, 
the following are true: <pre><code>*After the definition T u = rv;
, u is equal to u2;

*T(rv)
is equal to u2;
and

    *If T is not const -
    qualified,
    then rv's resulting state (after the definition/expression is evaluated in either bullets above) is valid but unspecified; otherwise, it is unchanged.
</code></pre>

<h2>See also</h2>

is_move_constructible 
is_trivially_move_constructible 
is_nothrow_move_constructible checks if a type can be constructed from an rvalue reference 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
