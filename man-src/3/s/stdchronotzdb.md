---
title: "stdchronotzdb(3)"
name: "stdchronotzdb"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotzdb/"
---

std::chrono::tzdb - std::chrono::tzdb

<h2>Synopsis</h2>

Defined in header &lt;chrono&gt; 
struct tzdb; <i>(since C++20)</i> 
The class tzdb represents a copy of the IANA_time_zone_database. Users cannot construct a tzdb and can only obtain read-only access to one via the free functions std::chrono::get_tzdb_list and std::chrono::get_tzdb. 

<h2>Member objects</h2>

Member object Description 
version A std::string that contains the version of the database 
zones A sorted std::vector&lt;std::chrono::time_zone&gt; containing description of time zones 
links A sorted std::vector&lt;std::chrono::link&gt; containing description of alternative names of time zones (links) 
leaps A sorted std::vector&lt;std::chrono::leaps&gt; containing description of leap seconds

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;locate a time zone with the given name 
locate_zone <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return the local time zone 
current_zone <i>(public member function)</i>
