---
title: "stdallocatorconstruct(3)"
name: "stdallocatorconstruct"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdallocatorconstruct/"
description: "std::allocator<T>::construct – std::allocator<T>::construct"
---

<p>std::allocator&lt;T&gt;::construct &#8211; std::allocator&lt;T&gt;::construct</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;memory&gt;<br />
void construct( pointer p, const_reference val ); <code>(1)</code> <i>(until C++11)</i><br />
template&lt; class U, class&#8230; Args &gt; <i>(since C++11)</i><br />
void construct( U* p, Args&amp;&amp;&#8230; args ); <code>(2)</code> (deprecated in C++17)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(removed in C++20)<br />
Constructs an object of type T in allocated uninitialized storage pointed to by p, using placement-new<br />
1) Calls new((void *)p) T(val)<br />
2) Calls ::new((void *)p) U(std::forward&lt;Args&gt;(args)&#8230;) </p>
<h2>Parameters</h2>
<p>p &#8211; pointer to allocated uninitialized storage<br />
val &#8211; the value to use as the copy constructor argument<br />
args&#8230; &#8211; the constructor arguments to use</p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>See also</h2>
<p>construct constructs an object in the allocated storage<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<code>[static]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocation functions<br />
operator_new <i>(function)</i><br />
operator_new[] </p>
