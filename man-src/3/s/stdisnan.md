---
title: "stdisnan(3)"
name: "stdisnan"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdisnan/"
description: "std::isnan – std::isnan"
---

<p>std::isnan &#8211; std::isnan</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
bool isnan( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
bool isnan( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
bool isnan( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
bool isnan( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Determines if the given floating point number arg is a not-a-number (NaN) value.<br />
4) A set of overloads or a function template accepting the arg argument of any integral_type. Equivalent to <code>(2)</code> (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; floating point value</p>
<h2>Return value</h2>
<p>true if arg is a NaN, false otherwise </p>
<h2>Notes</h2>
<p>There are many different NaN values with different sign bits and payloads, see std::nan and std::numeric_limits::quiet_NaN.<br />
NaN values never compare equal to themselves or to other NaN values. Copying a NaN is not required, by IEEE-754, to preserve its bit representation (sign and payload), though most implementation do.<br />
Another way to test if a floating-point value is NaN is to compare it with itself: bool is_nan(double x) { return x != x; } </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cfloat&gt;
int main()

{
    std::cout &lt;&lt; std::boolalpha
              &lt;&lt; &quot;isnan(NaN) = &quot; &lt;&lt; std::isnan(NAN) &lt;&lt; '
'
              &lt;&lt; &quot;isnan(Inf) = &quot; &lt;&lt; std::isnan(INFINITY) &lt;&lt; '
'
              &lt;&lt; &quot;isnan(0.0) = &quot; &lt;&lt; std::isnan(0.0) &lt;&lt; '
'
              &lt;&lt; &quot;isnan(DBL_MIN/2.0) = &quot; &lt;&lt; std::isnan(DBL_MIN / 2.0) &lt;&lt; '
'
              &lt;&lt; &quot;isnan(0.0 / 0.0)   = &quot; &lt;&lt; std::isnan(0.0 / 0.0) &lt;&lt; '
'
              &lt;&lt; &quot;isnan(Inf - Inf)   = &quot; &lt;&lt; std::isnan(INFINITY - INFINITY) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;isnan(NaN) = true<br />
&nbsp;<wbr>&nbsp;isnan(Inf) = false<br />
&nbsp;<wbr>&nbsp;isnan(0.0) = false<br />
&nbsp;<wbr>&nbsp;isnan(DBL_MIN/2.0) = false<br />
&nbsp;<wbr>&nbsp;isnan(0.0 / 0.0) = true<br />
&nbsp;<wbr>&nbsp;isnan(Inf &#8211; Inf) = true</p>
<h2>See also</h2>
<p>nan<br />
nanf<br />
nanl not-a-number (NaN)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
fpclassify categorizes the given floating point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isfinite checks if the given number has finite value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isinf checks if the given number is infinite<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isnormal checks if the given number is normal<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
isunordered checks if two floating-point values are unordered<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i> </p>
