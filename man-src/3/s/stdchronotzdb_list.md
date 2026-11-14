---
title: "stdchronotzdb_list(3)"
name: "stdchronotzdb_list"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotzdb_list/"
---

std::chrono::tzdb_list - std::chrono::tzdb_list

<h2>Synopsis</h2>

Defined in header &lt;chrono&gt; 
class tzdb_list; <i>(since C++20)</i> 
tzdb_list is a singleton list of std::chrono::tzdbs, each of which represents a copy of the IANA time zone database. Users cannot construct a tzdb_list and can only obtain access to one via the std::chrono::get_tzdb_list free function. 

<h2>Member types</h2>

Member type Definition 
const_iterator constant LegacyForwardIterator whose value type is std::chrono::tzdb

<h2>Member functions</h2>

constructor copy constructor is defined as deleted 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
(deleted) 

 
operator= copy assignment operator is defined as deleted 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
(deleted) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;access the first element 
front <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;erases an element after an element 
erase_after <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns an iterator to the beginning of the list 
begin <i>(public member function)</i> 
cbegin 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns an iterator past the end of the list 
end <i>(public member function)</i> 
cend
