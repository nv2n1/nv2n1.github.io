---
title: "stdisunordered(3)"
name: "stdisunordered"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdisunordered/"
description: "std::isunordered – std::isunordered"
---

<p>std::isunordered &#8211; std::isunordered</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
bool isunordered( float x, float y ); <code>(1)</code> <i>(since C++11)</i><br />
bool isunordered( double x, double y ); <code>(2)</code> <i>(since C++11)</i><br />
bool isunordered( long double x, long double y ); <code>(3)</code> <i>(since C++11)</i><br />
bool isunordered( Arithmetic x, Arithmetic y ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Determines if the floating point numbers x and y are unordered, that is, one or both are NaN and thus cannot be meaningfully compared with each other.<br />
4) A set of overloads or a function template for all combinations of arguments of arithmetic type not covered by (1-3). If any argument has integral_type, it is cast to double. </p>
<h2>Parameters</h2>
<p>x &#8211; floating point value<br />
y &#8211; floating point value</p>
<h2>Return value</h2>
<p>true if either x or y is NaN, false otherwise </p>
<h2>See also</h2>
<p>fpclassify categorizes the given floating point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isnan checks if the given number is NaN<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i> </p>
