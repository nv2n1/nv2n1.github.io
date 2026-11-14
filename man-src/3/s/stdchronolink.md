---
title: "stdchronolink(3)"
name: "stdchronolink"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronolink/"
---

std::chrono::link - std::chrono::link

<h2>Synopsis</h2>

Defined in header &lt;chrono&gt; 
class link; <i>(since C++20)</i> 
The class link represents an alternative name for a time zone. 
Users cannot construct link objects. The library implementation creates link objects when it initializes the time zone database and provides const access to these objects. 
link is not copyable but does have a defaulted move constructor and a defaulted move assignment operator. However, as users have only const access to link objects, these functions cannot be called in user code without invoking undefined_behavior. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the name and target of this link 
name <i>(public member function)</i> 
target 

 

 
Nonmember functions 

 

 

 
operator== 
operator!= compares two link objects 
operator&lt; <i>(function)</i> 
operator&lt;= 
operator&gt; 
operator&gt;=
