---
title: "stdchronofile_clockto_sysstdchronofile_clockfrom_sys(3)"
name: "stdchronofile_clockto_sysstdchronofile_clockfrom_sys"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronofile_clockto_sysstdchronofile_clockfrom_sys/"
description: "std::chrono::file_clock::to_sys,std::chrono::file_clock::from_sys – std::chrono::file_clock::to_sys,std::chrono::file_clock::from_sys"
---

<p>std::chrono::file_clock::to_sys,std::chrono::file_clock::from_sys &#8211; std::chrono::file_clock::to_sys,std::chrono::file_clock::from_sys</p>
<h2>Synopsis</h2>
<pre><code>template &lt;class Duration&gt;
(since C++ 20)

    static std::chrono::sys_time&lt;/*see below*/&gt;(1)(optional)

        to_sys(const std::chrono::file_time&lt;Duration&gt; &amp;t);

template &lt;class Duration&gt;
(since C++ 20)

    static std::chrono::file_time&lt;/*see below*/&gt;(2)(optional)

        from_sys(const std::chrono::sys_time&lt;Duration&gt; &amp;t);
1) Converts the file_time t to a sys_time representing the same point in time.

2) Converts the sys_time t to a file_time representing the same point in time.

The duration of the return type is computed from Duration in an unspecified manner.

These function templates are optional: an implementation may choose to instead provide to_utc and from_utc.
</code></pre>
<h2>Return value</h2>
<p>1) A sys_time representing the same point in time as the argument.<br />
2) A file_time representing the same point in time as the argument. </p>
<h2>Notes</h2>
<p>User code should usually use std::chrono::clock_cast, which provides a generic interface to convert time points between clocks, rather than call these functions directly. </p>
<h2>See also</h2>
<p>to_utc converts between file_time and utc_time<br />
from_utc <i>(public static member function)</i><br />
<code>[static]</code> (optional)<br />
clock_cast convert time points of one clock to another<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20) </p>
