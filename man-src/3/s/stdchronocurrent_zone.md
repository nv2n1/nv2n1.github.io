---
title: "stdchronocurrent_zone(3)"
name: "stdchronocurrent_zone"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronocurrent_zone/"
---

std::chrono::current_zone - std::chrono::current_zone

<h2>Synopsis</h2>

Defined in header &lt;chrono&gt; 
const std::chrono::time_zone* current_zone(); <i>(since C++20)</i> 
Convenience function for obtaining local time zone from the time zone database. Equivalent to std::chrono::get_tzdb().current_zone(). 

<h2>Exceptions</h2>

std::runtime_error if this is the first reference to the time zone database and the time zone database cannot be initialized.

<h2>Notes</h2>

A call to this function that is the first reference to the time zone database will cause it to be initialized. 

<h2>See also</h2>

<pre><code>return the local time zone

current_zone   (public member function of std::chrono::tzdb)</code></pre> 
get_tzdb 
get_tzdb_list accesses and controls the global time zone database information 
reload_tzdb <i>(function)</i> 
remote_version 
(C++20) 
