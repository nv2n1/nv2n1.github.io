---
title: "stdchronotzdbcurrent_zone(3)"
name: "stdchronotzdbcurrent_zone"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotzdbcurrent_zone/"
---

std::chrono::tzdb::current_zone - std::chrono::tzdb::current_zone

<h2>Synopsis</h2>

<pre><code>const std::chrono::time_zone *current_zone() const;
(since C++ 20)</code></pre> 
Obtains a pointer to a std::chrono::time_zone in this database that represents the local time zone of the computer. 

<h2>Return value</h2>

A pointer to the std::chrono::time_zone in this database that represents the local time zone of the computer. 
