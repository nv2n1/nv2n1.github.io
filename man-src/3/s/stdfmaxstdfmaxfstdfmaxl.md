---
title: "stdfmaxstdfmaxfstdfmaxl(3)"
name: "stdfmaxstdfmaxfstdfmaxl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfmaxstdfmaxfstdfmaxl/"
description: "std::fmax,std::fmaxf,std::fmaxl – std::fmax,std::fmaxf,std::fmaxl"
---

<p>std::fmax,std::fmaxf,std::fmaxl &#8211; std::fmax,std::fmaxf,std::fmaxl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float fmax ( float x, float y ); <code>(1)</code> <i>(since C++11)</i><br />
float fmaxf( float x, float y );<br />
double fmax ( double x, double y ); <code>(2)</code> <i>(since C++11)</i><br />
long double fmax ( long double x, long double y ); <code>(3)</code> <i>(since C++11)</i><br />
long double fmaxl( long double x, long double y );<br />
Promoted fmax ( Arithmetic1 x, Arithmetic2 y ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Returns the larger of two floating point arguments, treating NaNs as missing data (between a NaN and a numeric value, the numeric value is chosen)<br />
4) A set of overloads or a function template for all combinations of arguments of arithmetic_type not covered by 1-3). If any argument has integral_type, it is cast to double. If any other argument is long double, then the return type is long double, otherwise it is double. </p>
<h2>Parameters</h2>
<p>x, y &#8211; values of floating-point or integral_types</p>
<h2>Return value</h2>
<p>If successful, returns the larger of two floating point values. The value returned is exact and does not depend on any rounding modes. </p>
<h2>Error handling</h2>
<p>This function is not subject to any of the error conditions specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If one of the two arguments is NaN, the value of the other argument is returned<br />
* Only if both arguments are NaN, NaN is returned</p>
<h2>Notes</h2>
<p>This function is not required to be sensitive to the sign of zero, although some implementations additionally enforce that if one argument is +0 and the other is -0, then +0 is returned. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;
int main()

{
    std::cout &lt;&lt; &quot;fmax(2,1)    = &quot; &lt;&lt; std::fmax(2, 1) &lt;&lt; '
'
              &lt;&lt; &quot;fmax(-Inf,0) = &quot; &lt;&lt; std::fmax(-INFINITY, 0) &lt;&lt; '
'
              &lt;&lt; &quot;fmax(NaN,-1) = &quot; &lt;&lt; std::fmax(NAN, -1) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;fmax(2,1) = 2<br />
&nbsp;<wbr>&nbsp;fmax(-Inf,0) = 0<br />
&nbsp;<wbr>&nbsp;fmax(NaN,-1) = -1</p>
<h2>See also</h2>
<p>isgreater checks if the first floating-point argument is greater than the second<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
fmin<br />
fminf<br />
fminl smaller of two floating point values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the greater of the given values<br />
max <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the largest element in a range<br />
max_element <i>(function template)</i><br />
minmax returns the smaller and larger of two elements<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
minmax_element returns the smallest and the largest elements in a range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i> </p>
