---
title: "stdoperator(3)"
name: "stdoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdoperator/"
description: "std::operator==,!=,<(std::error_code) – std::operator==,!=,<(std::error_code)"
---

<p>std::operator==,!=,&lt;(std::error_code) &#8211; std::operator==,!=,&lt;(std::error_code)</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;system_error&gt;<br />
bool operator==( const error_code&amp; lhs, const error_code&amp; rhs ) noexcept; <code>(1)</code> <i>(since C++11)</i><br />
bool operator!=( const error_code&amp; lhs, const error_code&amp; rhs ) noexcept; <code>(1)</code> <i>(since C++11)</i><br />
bool operator&lt;( const error_code&amp; lhs, const error_code&amp; rhs ) noexcept; <code>(1)</code> <i>(since C++11)</i><br />
Compares two error code objects.<br />
1) Compares lhs and rhs for equality.<br />
2) Compares lhs and rhs for equality.<br />
3) Checks whether lhs is less than rhs. </p>
<h2>Parameters</h2>
<p>lhs, rhs &#8211; error codes to compare</p>
<h2>Return value</h2>
<p>1) true if the error category and error value compare equal.<br />
2) true if the error category or error value compare are not equal.<br />
3) true if lhs.category() &lt; rhs.category(). Otherwise, true if lhs.category() == rhs.category() &amp;&amp; lhs.value() &lt; rhs.value(). Otherwise, false </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the error_category for this error_code<br />
category <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the value of the error_code<br />
value <i>(public member function)</i><br />
operator== compares error_conditions and error_codes<br />
operator!= <i>(function)</i><br />
operator&lt; </p>
