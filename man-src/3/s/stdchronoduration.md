---
title: "stdchronoduration(3)"
name: "stdchronoduration"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoduration/"
description: "std::chrono::duration<Rep,Period>::zero – std::chrono::duration<Rep,Period>::zero"
---

<p>std::chrono::duration&lt;Rep,Period&gt;::zero &#8211; std::chrono::duration&lt;Rep,Period&gt;::zero</p>
<h2>Synopsis</h2>
<pre><code>static constexpr duration zero();           (until C++20)

static constexpr duration zero() noexcept;  (since C++20)</code></pre>
<p>Returns a zero-length duration.<br />
If the representation rep of the duration requires some other implementation to return a zero-length duration, std::chrono::duration_values can be specialized to return the desired value. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>returns duration(std::chrono::duration_values&lt;rep&gt;::zero()) </p>
<h2>See also</h2>
<p>min returns the special duration value min<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
max returns the special duration value max<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
