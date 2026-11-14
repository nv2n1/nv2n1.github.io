---
title: "stdfuture_category(3)"
name: "stdfuture_category"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfuture_category/"
---

std::future_category - std::future_category

<h2>Synopsis</h2>

Defined in header &lt;future&gt; 
const std::error_category&amp; future_category() noexcept; <i>(since C++11)</i> <pre><code>Obtains a reference to the static error category object for the errors related to futures and promises. The object is required to override the virtual function error_category::name() to return a pointer to the string &quot;future&quot;. It is used to identify error codes provided in the exceptions of type std::future_error.
</code></pre>

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A reference to the static object of unspecified runtime type, derived from std::error_category. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

future_errc identifies the future error codes 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i> 
<i>(C++11)</i> 
future_error reports an error related to futures or promises 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
error_category base class for error categories 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
