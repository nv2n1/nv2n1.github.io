---
title: "stdchronoyear_month_weekday_last(3)"
name: "stdchronoyear_month_weekday_last"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_weekday_last/"
---

std::chrono::year_month_weekday_last - std::chrono::year_month_weekday_last

<h2>Synopsis</h2>

Defined in header &lt;chrono&gt; 
class year_month_weekday_last; <i>(since C++20)</i> 
The class year_month_weekday_last represents the last weekday of a specific year and month. It is a field-based time point, with a resolution of std::chrono::days, except that it is limited to pointing to the last weekday of a year and month. std::chrono::years- and std::chrono::months-oriented arithmetic are supported directly. An implicit conversion to std::chrono::sys_days allows std::chrono::days-oriented arithmetic to be performed efficiently. 
year_month_weekday_last is a TriviallyCopyable StandardLayoutType. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a year_month_weekday_last 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;modifies the time point by some number of months or years 
operator+= <i>(public member function)</i> 
operator-= 

 
year accesses the fields of this object 
month <i>(public member function)</i> 
weekday 
weekday_last 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts to a std::chrono::time_point 
operator_sys_days <i>(public member function)</i> 
operator_local_days 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether this object represents a valid date 
ok <i>(public member function)</i> 

 

 
Nonmember functions 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two year_month_weekday_last objects 
operator== <i>(function)</i> 
operator!= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;adds or subtracts a year_month_weekday_last and some number of years or months 
operator+ <i>(function)</i> 
operator- 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a year_month_weekday_last into a stream 
operator&lt;&lt; <i>(function template)</i>
