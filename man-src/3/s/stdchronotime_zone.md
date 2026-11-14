---
title: "stdchronotime_zone(3)"
name: "stdchronotime_zone"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotime_zone/"
---

std::chrono::time_zone - std::chrono::time_zone

<h2>Synopsis</h2>

Defined in header &lt;chrono&gt; 
class time_zone; <i>(since C++20)</i> 
The class time_zone represents all time zone transitions for a specific geographic area. 
Users cannot construct time_zone objects. The library implementation creates time_zone objects when it initializes the time zone database and provides const access to these objects. 
time_zone is not copyable but does have a defaulted move constructor and a defaulted move assignment operator. However, as users have only const access to time_zone objects, these functions cannot be called in user code without invoking undefined_behavior. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the name of this time_zone 
name <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtain information associated with a sys_time or local_time 
get_info <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a local_time in this time zone to a sys_time 
to_sys <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a sys_time to a local_time in this time zone 
to_local <i>(public member function)</i> 

 

 
Nonmember functions 

 

 

 
operator== 
operator!= compares two time_zone objects 
operator&lt; <i>(function)</i> 
operator&lt;= 
operator&gt; 
operator&gt;=
