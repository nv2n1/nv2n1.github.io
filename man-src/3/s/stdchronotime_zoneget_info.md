---
title: "stdchronotime_zoneget_info(3)"
name: "stdchronotime_zoneget_info"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotime_zoneget_info/"
---

std::chrono::time_zone::get_info - std::chrono::time_zone::get_info

<h2>Synopsis</h2>

<pre><code>template &lt;class Duration&gt;
(since C++ 20)

    std::chrono::sys_info get_info(const std::chrono::sys_time&lt;Duration&gt; &amp;tp) const;

template &lt;class Duration&gt;
(since C++ 20)

    std::chrono::local_info get_info(const std::chrono::local_time&lt;Duration&gt; &amp;tp) const;</code></pre> 
Obtains information about this time zone at the time point tp. 

<h2>Return value</h2>

1) A std::chrono::sys_info structure i containing the time zone information in effect for this time zone at the time point tp. tp will be in the range [i.begin, i.end). 
2) A std::chrono::local_info structure containing information about the local time tp in this time zone. 
