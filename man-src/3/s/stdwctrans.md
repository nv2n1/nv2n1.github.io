---
title: "stdwctrans(3)"
name: "stdwctrans"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwctrans/"
---

std::wctrans - std::wctrans

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwctype&gt;

    std::wctrans_t wctrans(const char *str);</code></pre> 
Constructs a value of type std::wctrans_t that describes a LC_CTYPE category of wide character mapping. It may be one of the standard mappings, or a locale-specific mapping, such as &quot;tojhira&quot; or &quot;tojkana&quot;. 

<h2>Parameters</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;C string holding the name of the desired mapping. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The following values of str are supported in all C locales: 

 
str - Value of str Effect 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;toupper&quot; identifies the mapping used by towupper 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;tolower&quot; identifies the mapping used by towlower

<h2>Return value</h2>

std::wctrans_t object suitable for use with std::towctrans to map wide characters according to the named mapping of the current C locale or zero if str does not name a mapping supported by the current C locale. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;performs character mapping according to the specified LC_CTYPE mapping category 
towctrans <i>(function)</i> 
