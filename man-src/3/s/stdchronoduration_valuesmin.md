---
title: "stdchronoduration_valuesmin(3)"
name: "stdchronoduration_valuesmin"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoduration_valuesmin/"
description: "std::chrono::duration_values<Rep>::min – std::chrono::duration_values<Rep>::min"
---

<p>std::chrono::duration_values&lt;Rep&gt;::min &#8211; std::chrono::duration_values&lt;Rep&gt;::min</p>
<h2>Synopsis</h2>
<pre><code>static constexpr Rep min();           (until C++20)

static constexpr Rep min() noexcept;  (since C++20)</code></pre>
<p>Returns the lowest possible representation. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>returns std::numeric_limits&lt;Rep&gt;::lowest() </p>
<h2>See also</h2>
<p>min returns the special duration value min<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::chrono::duration&lt;Rep,Period&gt;)</i><br />
<code>[static]</code><br />
zero returns a zero-length representation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
max returns the largest possible representation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
