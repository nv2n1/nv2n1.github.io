---
title: "stdchronotzdblocate_zone(3)"
name: "stdchronotzdblocate_zone"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotzdblocate_zone/"
---

std::chrono::tzdb::locate_zone - std::chrono::tzdb::locate_zone

<h2>Synopsis</h2>

<pre><code>const std::chrono::time_zone *locate_zone(std::string_view tz_name) const;
(since C++ 20)</code></pre> 
Obtains a pointer to a std::chrono::time_zone in this database that represents the time zone designated by tz_name. If p is the returned pointer, then either p-&gt;name() == tz_name or that there is a std::chrono::link l in this database such that p-&gt;name() == l.target() and l.name() == tz_name. 

<h2>Return value</h2>

A pointer to the std::chrono::time_zone in this database that represents the time zone designated by tz_name. 

<h2>Exceptions</h2>

Throws std::runtime_error if no such time_zone can be found.
