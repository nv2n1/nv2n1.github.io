---
title: "stdchronosystem_clockfrom_time_t(3)"
name: "stdchronosystem_clockfrom_time_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronosystem_clockfrom_time_t/"
description: "std::chrono::system_clock::from_time_t – std::chrono::system_clock::from_time_t"
---

<p>std::chrono::system_clock::from_time_t &#8211; std::chrono::system_clock::from_time_t</p>
<h2>Synopsis</h2>
<pre><code>static std::chrono::system_clock::time_point from_time_t( std::time_t t ) noexcept;  (since C++11)</code></pre>
<p>Converts t to a time point type, using the coarser precision of the two types.<br />
If time_point has lower precision, it is implementation defined whether the value is rounded or truncated. </p>
<h2>Parameters</h2>
<p>t &#8211; std::time_t value to convert</p>
<h2>Return value</h2>
<p>A value of type std::chrono::system_clock::time_point representing t. </p>
<h2>See also</h2>
<p>to_time_t converts a system clock time point to std::time_t<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
