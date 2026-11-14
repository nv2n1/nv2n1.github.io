---
title: "stdtimespec(3)"
name: "stdtimespec"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtimespec/"
---

std::timespec - std::timespec

<h2>Synopsis</h2>

Defined in header &lt;ctime&gt; 
struct timespec; <i>(since C++17)</i> 
Structure holding an interval broken down into seconds and nanoseconds. 

<h2>Member objects</h2>

std::time_t tv_sec whole seconds – &gt;= 0 
long tv_nsec nanoseconds – [0, 999999999]

<h2>See also</h2>

timespec_get returns the calendar time based on a given time base 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(since C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;calendar time type 
tm <i>(class)</i> 
