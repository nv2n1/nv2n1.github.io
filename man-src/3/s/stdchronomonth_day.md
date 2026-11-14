---
title: "stdchronomonth_day(3)"
name: "stdchronomonth_day"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronomonth_day/"
---

std::chrono::month_day - std::chrono::month_day

<h2>Synopsis</h2>

Defined in header &lt;chrono&gt; 
class month_day; <i>(since C++20)</i> 
The class month_day represents a specific day of a specific month, of some yet to be specified year. 
month_day is a TriviallyCopyable StandardLayoutType. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a month_day 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;retrieve the stored month and day values 
month <i>(public member function)</i> 
day 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the month_day is valid 
ok <i>(public member function)</i> 

 

 
Nonmember functions 

 

 

 
operator== 
operator!= compares two month_day objects 
operator&lt; <i>(function)</i> 
operator&lt;= 
operator&gt; 
operator&gt;= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a month_day into a stream 
operator&lt;&lt; <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a month_day into a stream according to the provided format 
to_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parses a month_day from a stream according to the provided format 
from_stream <i>(function template)</i>
