---
title: "stderror_categoryoperator(3)"
name: "stderror_categoryoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderror_categoryoperator/"
description: "std::error_category::operator==,!=,< – std::error_category::operator==,!=,<"
---

<p>std::error_category::operator==,!=,&lt; &#8211; std::error_category::operator==,!=,&lt;</p>
<h2>Synopsis</h2>
<p>bool operator==( const error_category&amp; rhs ) const noexcept; <code>(1)</code> <i>(since C++11)</i><br />
bool operator!=( const error_category&amp; rhs ) const noexcept; <code>(2)</code> <i>(since C++11)</i><br />
bool operator&lt;( const error_category&amp; rhs ) const noexcept; <code>(3)</code> <i>(since C++11)</i><br />
Compares to another error category.<br />
1) Checks whether *this and rhs refer to the same object.<br />
2) Checks whether *this and rhs do not refer to the same object.<br />
3) Orders *this and rhs by the order of this and &amp;rhs. Equivalent to std::less&lt;const error_category*&gt;()(this, &amp;rhs). </p>
<h2>Parameters</h2>
<p>code &#8211; specifies the error code to compare<br />
condition &#8211; specifies the error condition to compare</p>
<h2>Return value</h2>
<p>1) true if *this and rhs refer to the same object, false otherwise.<br />
2) true if *this and rhs do not refer to the same object, false otherwise.<br />
3) true if *this is less than rhs as defined by the order of this and &amp;rhs. </p>
