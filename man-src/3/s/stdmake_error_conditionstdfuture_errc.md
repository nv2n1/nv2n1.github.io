---
title: "stdmake_error_conditionstdfuture_errc(3)"
name: "stdmake_error_conditionstdfuture_errc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_error_conditionstdfuture_errc/"
---

std::make_error_condition(std::future_errc) - std::make_error_condition(std::future_errc)

<h2>Synopsis</h2>

Defined in header &lt;future&gt; 
std::error_condition make_error_condition( std::future_errc e ); <i>(since C++11)</i> 
Constructs an std::error_condition object from a value of type std::future_errc as if by: 
std::error_condition(static_cast&lt;int&gt;(e), std::future_category()). 

<h2>Parameters</h2>

e - error code number

<h2>Return value</h2>

A value of type std::error_condition that holds the error code number from e associated with the error category &quot;future&quot;. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

error_condition holds a portable error code 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
future_errc identifies the future error codes 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i> 
<i>(C++11)</i> 
