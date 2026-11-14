---
title: "stdva_list(3)"
name: "stdva_list"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdva_list/"
---

std::va_list - std::va_list

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;cstdarg&gt;

typedef /* unspecified */ va_list;</code></pre> 
va_list is a complete object type suitable for holding the information needed by the macros va_start, va_copy, va_arg, and va_end. 
If a va_list instance is created, passed to another function, and used via va_arg in that function, then any subsequent use in the calling function should be preceded by a call to va_end. 
It is legal to pass a pointer to a va_list object to another function and then use that object after the function returns. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;enables access to variadic function arguments 
va_start <i>(function macro)</i> 
va_copy makes a copy of the variadic function arguments 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function macro)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the next variadic function argument 
va_arg <i>(function macro)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ends traversal of the variadic function arguments 
va_end <i>(function macro)</i> 
