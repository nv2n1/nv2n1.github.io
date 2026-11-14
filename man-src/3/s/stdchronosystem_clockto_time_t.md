---
title: "stdchronosystem_clockto_time_t(3)"
name: "stdchronosystem_clockto_time_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronosystem_clockto_time_t/"
description: "std::chrono::system_clock::to_time_t – std::chrono::system_clock::to_time_t"
---

<p>std::chrono::system_clock::to_time_t &#8211; std::chrono::system_clock::to_time_t</p>
<h2>Synopsis</h2>
<pre><code>static std::time_t to_time_t(const time_point &amp;t) noexcept;
(since C++ 11)</code></pre>
<p>Converts t to a std::time_t type.<br />
If std::time_t has lower precision, it is implementation-defined whether the value is rounded or truncated. </p>
<h2>Parameters</h2>
<p>t &#8211; system clock time point to convert</p>
<h2>Return value</h2>
<p>A std::time_t value representing t. </p>
<h2>See also</h2>
<p>from_time_t converts std::time_t to a system clock time point<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
