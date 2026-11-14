---
title: "stdchar_traitseof(3)"
name: "stdchar_traitseof"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchar_traitseof/"
description: "std::char_traits<CharT>::eof – std::char_traits<CharT>::eof"
---

<p>std::char_traits&lt;CharT&gt;::eof &#8211; std::char_traits&lt;CharT&gt;::eof</p>
<h2>Synopsis</h2>
<pre><code>static int_type eof();                     (until C++11)

static constexpr int_type eof() noexcept;  (since C++11)</code></pre>
<p>Returns a value not equivalent to any valid value of type char_type.<br />
Formally, returns a value e such that X::eq_int_type(e, X::to_int_type(c)) is false for all values c. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>A value not equivalent to any valid value of type char_type. </p>
<h2>Complexity</h2>
<p>Constant.</p>
<h2>See also</h2>
<p>not_eof checks whether a character is eof value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
