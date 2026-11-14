---
title: "stdchronoduration_valuesmax(3)"
name: "stdchronoduration_valuesmax"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoduration_valuesmax/"
description: "std::chrono::duration_values<Rep>::max – std::chrono::duration_values<Rep>::max"
---

<p>std::chrono::duration_values&lt;Rep&gt;::max &#8211; std::chrono::duration_values&lt;Rep&gt;::max</p>
<h2>Synopsis</h2>
<pre><code>static constexpr Rep max();           (until C++20)

static constexpr Rep max() noexcept;  (since C++20)</code></pre>
<p>Returns the largest possible representation. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>returns std::numeric_limits&lt;Rep&gt;::max() </p>
<h2>See also</h2>
<p>max returns the special duration value max<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function of std::chrono::duration&lt;Rep,Period&gt;)</i><br />
<code>[static]</code><br />
zero returns a zero-length representation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code><br />
min returns the smallest possible representation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
