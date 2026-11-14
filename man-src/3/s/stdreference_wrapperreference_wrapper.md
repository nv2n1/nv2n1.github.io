---
title: "stdreference_wrapperreference_wrapper(3)"
name: "stdreference_wrapperreference_wrapper"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdreference_wrapperreference_wrapper/"
description: "std::reference_wrapper<T>::reference_wrapper – std::reference_wrapper<T>::reference_wrapper"
---

<p>std::reference_wrapper&lt;T&gt;::reference_wrapper &#8211; std::reference_wrapper&lt;T&gt;::reference_wrapper</p>
<h2>Synopsis</h2>
<p>template&lt; class U &gt; <code>(1)</code><br />
reference_wrapper( U&amp;&amp; x ) noexcept(/*see below*/) ;<br />
reference_wrapper( const reference_wrapper&amp; other ) noexcept; <code>(2)</code> </p>
<pre><code>Constructs a new reference wrapper.

1) Converts x to T&amp; as if by T&amp; t = std::forward&lt;U&gt;(x);
, then stores a reference to t.This overload only participates in overload resolution if typename std::decay&lt;U&gt;::type is not the same type as reference_wrapper and the expression FUN(std::declval&lt;U&gt;()) is well - formed, where FUN names the set of imaginary functions void FUN(T &amp;) noexcept;

void FUN(T &amp;&amp;) = delete;</code></pre>
<p>2) Copy constructor. Stores a reference to other.get(). </p>
<h2>Parameters</h2>
<p>x &#8211; an object to wrap<br />
other &#8211; another reference wrapper</p>
<h2>Exceptions</h2>
<p>1)<br />
noexcept specification:<br />
noexcept(noexcept(FUN(std::declval&lt;U&gt;())))<br />
where FUN is the set of imaginary functions described in the description above. </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
LWG_2993 C++11 deleted reference_wrapper(T&amp;&amp;) constructor interferes with overload resolution in some cases replaced with a constructor template</p>
