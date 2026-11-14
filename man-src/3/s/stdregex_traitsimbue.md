---
title: "stdregex_traitsimbue(3)"
name: "stdregex_traitsimbue"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_traitsimbue/"
---

std::regex_traits&lt;CharT&gt;::imbue - std::regex_traits&lt;CharT&gt;::imbue

<h2>Synopsis</h2>

locale_type imbue( locale_type loc ); <i>(since C++11)</i> 
Replaces the current locale with a copy of loc. If loc is different than the current locale, then all cached data is invalidated. 
After the call getloc() == loc. 

<h2>Parameters</h2>

loc - the locale to imbue

<h2>Return value</h2>

The current locale of the traits object. 
If imbue() has been never called for this object, then the global locale at the time of the call is returned. Otherwise, the locale passed to the last call to imbue() is returned. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets the locale 
getloc <i>(public member function)</i> 
