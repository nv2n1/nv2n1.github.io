---
title: "stdchronoweekday(3)"
name: "stdchronoweekday"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoweekday/"
---

std::chrono::weekday - std::chrono::weekday

<h2>Synopsis</h2>

Defined in header &lt;chrono&gt; 
class weekday; <i>(since C++20)</i> 
inline constexpr std::chrono::weekday Sunday{0}; <i>(since C++20)</i> 
inline constexpr std::chrono::weekday Monday{1}; <i>(since C++20)</i> 
inline constexpr std::chrono::weekday Tuesday{2}; <i>(since C++20)</i> 
inline constexpr std::chrono::weekday Wednesday{3}; <i>(since C++20)</i> 
inline constexpr std::chrono::weekday Thursday{4}; <i>(since C++20)</i> 
inline constexpr std::chrono::weekday Friday{5}; <i>(since C++20)</i> 
inline constexpr std::chrono::weekday Saturday{6}; <i>(since C++20)</i> 
The class weekday represent a day of the week in the Gregorian calendar. Its normal range is [0, 6], for Sunday through Saturday, but it can hold any value in the range [0, 255]. Seven named constants are predefined in the std::chrono namespace for the seven days of the week. 
weekday is a TriviallyCopyable StandardLayoutType. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a weekday 
constructor <i>(public member function)</i> 

 
operator++ increments or decrements the weekday 
operator++(int) <i>(public member function)</i> 
operator-- 
operator--(int) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;adds or subtracts a number of days 
operator+= <i>(public member function)</i> 
operator-= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;retrieves the stored weekday value 
operator_unsigned <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the stored weekday value is valid 
ok <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;convenience syntax for constructing a weekday_indexed or weekday_last from this weekday 
operator[] <i>(public member function)</i> 

 

 
Nonmember functions 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two weekday objects 
operator== <i>(function)</i> 
operator!= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;performs arithmetic on weekdays 
operator+ <i>(function)</i> 
operator- 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a weekday into a stream 
operator&lt;&lt; <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a weekday into a stream according to the provided format 
to_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parses a weekday from a stream according to the provided format 
from_stream <i>(function template)</i>
