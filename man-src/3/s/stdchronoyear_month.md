---
title: "stdchronoyear_month(3)"
name: "stdchronoyear_month"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month/"
---

std::chrono::year_month - std::chrono::year_month

<h2>Synopsis</h2>

Defined in header &lt;chrono&gt; 
class year_month; <i>(since C++20)</i> 
The class year_month represents a specific month of a specific year, but with an unspecified day. It is a field-based time point, with a resolution of std::chrono::months. 
year_month is a TriviallyCopyable StandardLayoutType. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a year_month 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the stored year and month 
year <i>(public member function)</i> 
month 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;modifies the year_month by some number of months or years 
operator+= <i>(public member function)</i> 
operator-= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if this year_month is valid 
ok <i>(public member function)</i> 

 

 
Nonmember functions 

 

 

 
operator== 
operator!= compares two year_month objects 
operator&lt; <i>(function)</i> 
operator&lt;= 
operator&gt; 
operator&gt;= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;performs arithmetic on year_month 
operator+ <i>(function)</i> 
operator- 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a year_month into a stream 
operator&lt;&lt; <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a year_month into a stream according to the provided format 
to_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parses a year_month from a stream according to the provided format 
from_stream <i>(function template)</i>
