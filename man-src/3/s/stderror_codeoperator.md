---
title: "stderror_codeoperator(3)"
name: "stderror_codeoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderror_codeoperator/"
---

std::error_code::operator= - std::error_code::operator=

<h2>Synopsis</h2>

<pre><code>template&lt; class ErrorCodeEnum &gt;                     (since C++11)

error_code&amp; operator=( ErrorCodeEnum e ) noexcept;</code></pre> 
Replaces the error code and corresponding category with those representing error code enum e. 
Equivalent to *this = std::make_error_code(e). The overload participates in overload resolutions only if std::is_error_code_enum&lt;ErrorCodeEnum&gt;::value == true. 

<h2>Parameters</h2>

e - error code enum to construct

<h2>Return value</h2>

*this 

<h2>Notes</h2>

Copy-assignment operator is defined implicitly. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;assigns another error code 
assign <i>(public member function)</i> 
