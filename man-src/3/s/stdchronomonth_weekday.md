---
title: "stdchronomonth_weekday(3)"
name: "stdchronomonth_weekday"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronomonth_weekday/"
---

std::chrono::month_weekday - std::chrono::month_weekday

<h2>Synopsis</h2>

Defined in header &lt;chrono&gt; 
class month_weekday; <i>(since C++20)</i> 
The class month_weekday represents the n-th weekday of a specific month, of some yet to be specified year. 
month_weekday is a TriviallyCopyable StandardLayoutType. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a month_weekday 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;retrieves the stored month and weekday_indexed values 
month <i>(public member function)</i> 
weekday_indexed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the contained month and weekday_indexed are valid 
ok <i>(public member function)</i> 

 

 
Nonmember functions 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two month_weekday objects 
operator== <i>(function)</i> 
operator!= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a month_weekday into a stream 
operator&lt;&lt; <i>(function template)</i>
