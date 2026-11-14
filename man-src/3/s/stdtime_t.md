---
title: "stdtime_t(3)"
name: "stdtime_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtime_t/"
---

std::time_t - std::time_t

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ctime&gt;

typedef /* unspecified */ time_t;</code></pre> 
Arithmetic type capable of representing times. 
Although not defined, this is almost always an integral value holding the number of seconds (not counting leap seconds) since 00:00, Jan 1 1970 UTC, corresponding to POSIX_time. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the current time of the system as time since epoch 
time <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts time since epoch to calendar time expressed as local time 
localtime <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts time since epoch to calendar time expressed as Universal Coordinated Time 
gmtime <i>(function)</i> 
