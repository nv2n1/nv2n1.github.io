---
title: "stdchronolocate_zone(3)"
name: "stdchronolocate_zone"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronolocate_zone/"
---

std::chrono::locate_zone - std::chrono::locate_zone

<h2>Synopsis</h2>

Defined in header &lt;chrono&gt; 
const std::chrono::time_zone* locate_zone(std::string_view tz_name); <i>(since C++20)</i> 
Convenience function for locating a time zone in the time zone database. Equivalent to std::chrono::get_tzdb().locate_zone(tz_name). 

<h2>Exceptions</h2>

std::runtime_error if the specified time zone cannot be found, or if this is the first reference to the time zone database and the time zone database cannot be initialized.

<h2>Notes</h2>

A call to this function that is the first reference to the time zone database will cause it to be initialized. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locate a time zone with the given name 
locate_zone <i>(public member function of std::chrono::tzdb)</i> 
get_tzdb 
get_tzdb_list accesses and controls the global time zone database information 
reload_tzdb <i>(function)</i> 
remote_version 
(C++20) 
