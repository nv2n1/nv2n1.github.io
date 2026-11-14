---
title: "stdtruncstdtruncfstdtruncl(3)"
name: "stdtruncstdtruncfstdtruncl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtruncstdtruncfstdtruncl/"
description: "std::trunc,std::truncf,std::truncl – std::trunc,std::truncf,std::truncl"
---

<p>std::trunc,std::truncf,std::truncl &#8211; std::trunc,std::truncf,std::truncl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float trunc ( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
float truncf( float arg );<br />
double trunc ( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
long double trunc ( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
long double truncl( long double arg );<br />
double trunc ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the nearest integer not greater in magnitude than arg.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; floating point value</p>
<h2>Return value</h2>
<p>If no errors occur, the nearest integer value not greater in magnitude than arg (in other words, arg rounded towards zero) is returned.</p>
<h2>Return value</h2>
<p>&nbsp;math-trunc.svg<br />
Argument </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* The current rounding_mode has no effect.<br />
* If arg is ±∞, it is returned, unmodified<br />
* If arg is ±0, it is returned, unmodified<br />
* If arg is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>FE_INEXACT may be (but isn&#8217;t required to be) raised when truncating a non-integer finite value.<br />
The largest representable floating-point values are exact integers in all standard floating-point formats, so this function never overflows on its own; however the result may overflow any integer type (including std::intmax_t), when stored in an integer variable.<br />
The implicit_conversion from floating-point to integral types also rounds towards zero, but is limited to the values that can be represented by the target type. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cmath&gt;

#include &lt;iostream&gt;

int main()

{
    std::cout &lt;&lt; std::fixed
              &lt;&lt; &quot;trunc(+2.7) = &quot; &lt;&lt; std::trunc(+2.7) &lt;&lt; '
'
              &lt;&lt; &quot;trunc(-2.9) = &quot; &lt;&lt; std::trunc(-2.9) &lt;&lt; '
'
              &lt;&lt; &quot;trunc(-0.0) = &quot; &lt;&lt; std::trunc(-0.0) &lt;&lt; '
'
              &lt;&lt; &quot;trunc(-Inf) = &quot; &lt;&lt; std::trunc(-INFINITY) &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;trunc(+2.7) = 2.000000<br />
&nbsp;<wbr>&nbsp;trunc(-2.9) = -2.000000<br />
&nbsp;<wbr>&nbsp;trunc(-0.0) = -0.000000<br />
&nbsp;<wbr>&nbsp;trunc(-Inf) = -inf</p>
<h2>See also</h2>
<p>floor<br />
floorf<br />
floorl nearest integer not greater than the given value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
ceil<br />
ceilf<br />
ceill nearest integer not less than the given value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
round<br />
roundf<br />
roundl<br />
lround<br />
lroundf<br />
lroundl<br />
llround<br />
llroundf<br />
llroundl nearest integer, rounding away from zero in halfway cases<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
