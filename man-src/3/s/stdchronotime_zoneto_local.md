---
title: "stdchronotime_zoneto_local(3)"
name: "stdchronotime_zoneto_local"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotime_zoneto_local/"
---

std::chrono::time_zone::to_local - std::chrono::time_zone::to_local

<h2>Synopsis</h2>

<pre><code>template &lt;class Duration&gt;

auto to_local(const std::chrono::sys_time&lt;Duration&gt; &amp;tp) const(since C++ 20)

    -&gt; std::chrono::local_time&lt;std::common_type_t&lt;Duration, std::chrono::seconds&gt;&gt;;</code></pre> 
Converts the sys_time tp to the corresponding local_time in this time zone. 

<h2>Return value</h2>

The local_time associated with tp and this time zone. 

<h2>Notes</h2>

The precision of the result is at least std::chrono::seconds, and will be finer if the argument has finer precision. 
