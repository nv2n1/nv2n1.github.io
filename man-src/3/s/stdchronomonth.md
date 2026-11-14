---
title: "stdchronomonth(3)"
name: "stdchronomonth"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronomonth/"
---

std::chrono::month - std::chrono::month

<h2>Synopsis</h2>

Defined in header &lt;chrono&gt; 
class month; <i>(since C++20)</i> 
inline constexpr std::chrono::month January{1}; <i>(since C++20)</i> 
inline constexpr std::chrono::month February{2}; <i>(since C++20)</i> 
inline constexpr std::chrono::month March{3}; <i>(since C++20)</i> 
inline constexpr std::chrono::month April{4}; <i>(since C++20)</i> 
inline constexpr std::chrono::month May{5}; <i>(since C++20)</i> 
inline constexpr std::chrono::month June{6}; <i>(since C++20)</i> 
inline constexpr std::chrono::month July{7}; <i>(since C++20)</i> 
inline constexpr std::chrono::month August{8}; <i>(since C++20)</i> 
inline constexpr std::chrono::month September{9}; <i>(since C++20)</i> 
inline constexpr std::chrono::month October{10}; <i>(since C++20)</i> 
inline constexpr std::chrono::month November{11}; <i>(since C++20)</i> 
inline constexpr std::chrono::month December{12}; <i>(since C++20)</i> 
The class month represents a month in a year. Its normal range is [1, 12], but it may hold any number in [0, 255]. Twelve named constants are predefined in the std::chrono namespace for the twelve months of the year. 
month is a TriviallyCopyable StandardLayoutType. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a month 
constructor <i>(public member function)</i> 

 
operator++ increments or decrements the month 
operator++(int) <i>(public member function)</i> 
operator-- 
operator--(int) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;adds or subtracts a number of months 
operator+= <i>(public member function)</i> 
operator-= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;retrieves the stored month value 
operator_unsigned <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if the stored month value is in the normal range 
ok <i>(public member function)</i> 

 

 
Nonmember functions 

 

 

 
operator== 
operator!= compares two month objects 
operator&lt; <i>(function)</i> 
operator&lt;= 
operator&gt; 
operator&gt;= 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;performs arithmetic on months 
operator+ <i>(function)</i> 
operator- 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a month into a stream 
operator&lt;&lt; <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a month into a stream according to the provided format 
to_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parses a month from a stream according to the provided format 
from_stream <i>(function template)</i>
