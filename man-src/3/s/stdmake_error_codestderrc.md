---
title: "stdmake_error_codestderrc(3)"
name: "stdmake_error_codestderrc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_error_codestderrc/"
---

std::make_error_code(std::errc) - std::make_error_code(std::errc)

<h2>Synopsis</h2>

Defined in header &lt;system_error&gt; 
std::error_code make_error_code( std::errc e ) noexcept; <i>(since C++11)</i> 
Creates error code value for errc enum e. 
Equivalent to std::error_code(static_cast&lt;int&gt;(e), std::generic_category()) 

<h2>Parameters</h2>

e - error code enum to create error code for

<h2>Return value</h2>

Error code corresponding to e. 
