---
title: "stdexperimentalrangescopyconstructible(3)"
name: "stdexperimentalrangescopyconstructible"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangescopyconstructible/"
---

std::experimental::ranges::CopyConstructible - std::experimental::ranges::CopyConstructible

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / concepts&gt;

    template &lt;class T&gt;

    concept bool CopyConstructible =

        MoveConstructible&lt;T&gt; &amp;&amp; (ranges TS)

                                    Constructible&lt;T, T &amp;&gt; &amp;&amp;
        ConvertibleTo&lt;T &amp;, T&gt; &amp;&amp;

        Constructible&lt;T, const T &amp;&gt; &amp;&amp; ConvertibleTo&lt;const T &amp;, T&gt; &amp;&amp;

        Constructible&lt;T, const T&gt; &amp;&amp; ConvertibleTo&lt;const T, T&gt;;</code></pre> 
The concept CopyConstructible is satisfied if T is an lvalue reference type, or if it is a MoveConstructible object type where an object of that type can constructed from a (possibly const) lvalue or const rvalue of that type in both direct- and copy-initialization contexts with the usual semantics (a copy is constructed with the source unchanged). 
More precisely, if T is an object type, then CopyConstructible&lt;T&gt; is satisfied only if given 
* v, a lvalue of type (possibly const) T or an rvalue of type const T, 
the following are true: <pre><code>* After the definition T u = v;, u is equal to v;

* T{v} is equal to v.

</code></pre>

<h2>See also</h2>

is_copy_constructible 
is_trivially_copy_constructible 
is_nothrow_copy_constructible checks if a type has a copy constructor 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
