---
title: "stdchronoleap(3)"
name: "stdchronoleap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoleap/"
---

std::chrono::leap - std::chrono::leap

<h2>Synopsis</h2>

Defined in header &lt;chrono&gt; 
class leap; <i>(since C++20)</i> 
The class leap represents the date and time of a leap second insertion. 
Users cannot construct leap objects except by copying from existing leap objects. The library implementation creates leap objects when it initializes the time zone database and provides const access to these objects. 
leap has a defaulted copy constructor and a defaulted copy assignment operator. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the time of leap second insertion 
date <i>(public member function)</i> 

 

 
Nonmember functions 

 

 

 
operator== 
operator!= compares two leap objects or a leap object and a sys_time 
operator&lt; <i>(function template)</i> 
operator&lt;= 
operator&gt; 
operator&gt;=
