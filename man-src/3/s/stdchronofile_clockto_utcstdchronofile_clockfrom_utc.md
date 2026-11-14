---
title: "stdchronofile_clockto_utcstdchronofile_clockfrom_utc(3)"
name: "stdchronofile_clockto_utcstdchronofile_clockfrom_utc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronofile_clockto_utcstdchronofile_clockfrom_utc/"
description: "std::chrono::file_clock::to_utc,std::chrono::file_clock::from_utc – std::chrono::file_clock::to_utc,std::chrono::file_clock::from_utc"
---

<p>std::chrono::file_clock::to_utc,std::chrono::file_clock::from_utc &#8211; std::chrono::file_clock::to_utc,std::chrono::file_clock::from_utc</p>
<h2>Synopsis</h2>
<pre><code>template &lt;class Duration&gt;
(since C++ 20)

    static std::chrono::utc_time&lt;/*see below*/&gt;(1)(optional)

        to_utc(const std::chrono::file_time&lt;Duration&gt; &amp;t);

template &lt;class Duration&gt;
(since C++ 20)

    static std::chrono::file_time&lt;/*see below*/&gt;(2)(optional)

        from_utc(const std::chrono::utc_time&lt;Duration&gt; &amp;t);
1) Converts the file_time t to a utc_time representing the same point in time.

2) Converts the utc_time t to a file_time representing the same point in time.

The duration of the return type is computed from Duration in an unspecified manner.

These function templates are optional: an implementation may choose to instead provide to_sys and from_sys.
</code></pre>
<h2>Return value</h2>
<p>1) A utc_time representing the same point in time as the argument.<br />
2) A file_time representing the same point in time as the argument. </p>
<h2>Notes</h2>
<p>User code should usually use std::chrono::clock_cast, which provides a generic interface to convert time points between clocks, rather than call these functions directly. </p>
<h2>See also</h2>
<p>to_sys converts between file_time and sys_time<br />
from_sys <i>(public static member function)</i><br />
<code>[static]</code> (optional)<br />
clock_cast convert time points of one clock to another<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(C++20) </p>
