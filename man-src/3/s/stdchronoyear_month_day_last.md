---
title: "stdchronoyear_month_day_last(3)"
name: "stdchronoyear_month_day_last"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_day_last/"
---

std::chrono::year_month_day_last - std::chrono::year_month_day_last

<h2>Synopsis</h2>

Defined in header &lt;chrono&gt; 
class year_month_day_last; <i>(since C++20)</i> 
The class year_month_day_last represents the last day of a specific year and month. It is a field-based time point, with a resolution of std::chrono::days, subject to the limit that it can only represent the last day of a month. 
std::chrono::years- and std::chrono::months-oriented arithmetic are supported directly. An implicit conversion to std::chrono::sys_days allows std::chrono::days-oriented arithmetic to be performed efficiently. 
year_month_day_last is a TriviallyCopyable StandardLayoutType. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a year_month_day_last object 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;modifies the time point by some number of months or years 
operator+= <i>(public member function)</i> 
operator-= 

 
year accesses the fields of this object 
month <i>(public member function)</i> 
day 
month_day_last 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts to a std::chrono::time_point 
operator_sys_days <i>(public member function)</i> 
operator_local_days 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether this object represents a valid date 
ok <i>(public member function)</i> 

 

 
Nonmember functions 

 

 

 
operator== 
operator!= compares two year_month_day_last objects 
operator&lt; <i>(function)</i> 
operator&lt;= 
operator&gt; 
operator&gt;= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;adds or subtracts a year_month_day_last and some number of years or months 
operator+ <i>(public member function)</i> 
operator- 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a year_month_day_last into a stream 
operator&lt;&lt; <i>(function template)</i>
