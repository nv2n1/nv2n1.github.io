---
title: "stdislessgreater(3)"
name: "stdislessgreater"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdislessgreater/"
description: "std::islessgreater – std::islessgreater"
---

<p>std::islessgreater &#8211; std::islessgreater</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
bool islessgreater( float x, float y ); <code>(1)</code> <i>(since C++11)</i><br />
bool islessgreater( double x, double y ); <code>(2)</code> <i>(since C++11)</i><br />
bool islessgreater( long double x, long double y ); <code>(3)</code> <i>(since C++11)</i><br />
bool islessgreater( Arithmetic x, Arithmetic y ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Determines if the floating point number x is less than or greater than the floating-point number y, without setting floating-point exceptions.<br />
4) A set of overloads or a function template for all combinations of arguments of arithmetic type not covered by (1-3). If any argument has integral_type, it is cast to double. </p>
<h2>Parameters</h2>
<p>x &#8211; floating point value<br />
y &#8211; floating point value</p>
<h2>Return value</h2>
<p>true if x &lt; y || x &gt; y, false otherwise </p>
<h2>Notes</h2>
<p>The built-in operator&lt; and operator&gt; for floating-point numbers may raise FE_INVALID if one or both of the arguments is NaN. This function is a &quot;quiet&quot; version of the expression x &lt; y || x &gt; y. </p>
<h2>See also</h2>
<p>isless checks if the first floating-point argument is less than the second<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isgreater checks if the first floating-point argument is greater than the second<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i> </p>
