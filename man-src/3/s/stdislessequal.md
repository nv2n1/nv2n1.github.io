---
title: "stdislessequal(3)"
name: "stdislessequal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdislessequal/"
description: "std::islessequal – std::islessequal"
---

<p>std::islessequal &#8211; std::islessequal</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
bool islessequal( float x, float y ); <code>(1)</code> <i>(since C++11)</i><br />
bool islessequal( double x, double y ); <code>(2)</code> <i>(since C++11)</i><br />
bool islessequal( long double x, long double y ); <code>(3)</code> <i>(since C++11)</i><br />
bool islessequal( Arithmetic x, Arithmetic y ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Determines if the floating point number x is less than or equal to the floating-point number y, without setting floating-point exceptions.<br />
4) A set of overloads or a function template for all combinations of arguments of arithmetic type not covered by (1-3). If any argument has integral_type, it is cast to double. </p>
<h2>Parameters</h2>
<p>x &#8211; floating point value<br />
y &#8211; floating point value</p>
<h2>Return value</h2>
<p>true if x &lt;= y, false otherwise </p>
<h2>Notes</h2>
<p>The built-in operator&lt;= for floating-point numbers may raise FE_INVALID if one or both of the arguments is NaN. This function is a &quot;quiet&quot; version of operator&lt;=. </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object implementing x &lt;= y<br />
less_equal <i>(class template)</i><br />
isgreaterequal checks if the first floating-point argument is greater or equal than the second<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i> </p>
