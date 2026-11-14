---
title: "stdregex_traitsgetloc(3)"
name: "stdregex_traitsgetloc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_traitsgetloc/"
---

std::regex_traits&lt;CharT&gt;::getloc - std::regex_traits&lt;CharT&gt;::getloc

<h2>Synopsis</h2>

locale_type getloc() const; <i>(since C++11)</i> 
Returns the current locale of the traits object. 
If imbue() has been never called for this object, then the global locale at the time of the call is returned. Otherwise, the locale passed to the last call to imbue() is returned. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The current locale of the traits object. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the locale 
imbue <i>(public member function)</i> 
