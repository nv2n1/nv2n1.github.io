---
title: "stdfdimstdfdimfstdfdiml(3)"
name: "stdfdimstdfdimfstdfdiml"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfdimstdfdimfstdfdiml/"
description: "std::fdim,std::fdimf,std::fdiml – std::fdim,std::fdimf,std::fdiml"
---

<p>std::fdim,std::fdimf,std::fdiml &#8211; std::fdim,std::fdimf,std::fdiml</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float fdim ( float x, float y ); <code>(1)</code> <i>(since C++11)</i><br />
float fdimf( float x, float y );<br />
double fdim ( double x, double y ); <code>(2)</code> <i>(since C++11)</i><br />
long double fdim ( long double x, long double y ); <code>(3)</code> <i>(since C++11)</i><br />
long double fdiml( long double x, long double y );<br />
Promoted fdim ( Arithmetic1 x, Arithmetic2 y ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Returns the positive difference between x and y, that is, if x&gt;y, returns x-y, otherwise (if x≤y), returns +0.<br />
4) A set of overloads or a function template for all combinations of arguments of arithmetic_type not covered by 1-3). If any argument has integral_type, it is cast to double. If any argument is long double, then the return type Promoted is also long double, otherwise the return type is always double. </p>
<h2>Parameters</h2>
<p>x, y &#8211; values of floating-point or integral_types</p>
<h2>Return value</h2>
<p>If successful, returns the positive difference between x and y.<br />
If a range error due to overflow occurs, +HUGE_VAL, +HUGE_VALF, or +HUGE_VALL is returned.<br />
If a range error due to underflow occurs, the correct value (after rounding) is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If either argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>Equivalent to std::fmax(x-y, 0), except for the NaN handling requirements. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cerrno&gt;

#include &lt;cstring&gt;

#include &lt;cfenv&gt;

#pragma STDC FENV_ACCESS ON

int main()

{
    std::cout &lt;&lt; &quot;fdim(4, 1) = &quot; &lt;&lt; std::fdim(4, 1)
              &lt;&lt; &quot; fdim(1, 4) = &quot; &lt;&lt; std::fdim(1, 4) &lt;&lt; '
'
              &lt;&lt; &quot;fdim(4,-1) = &quot; &lt;&lt; std::fdim(4, -1)
              &lt;&lt; &quot; fdim(1,-4) = &quot; &lt;&lt; std::fdim(1, -4) &lt;&lt; '
';
    // error handling
    errno = 0;
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;fdim(1e308, -1e308) = &quot; &lt;&lt; std::fdim(1e308, -1e308) &lt;&lt; '
';
    if (errno == ERANGE)
        std::cout &lt;&lt; &quot;    errno == ERANGE: &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '
';
    if (std::fetestexcept(FE_OVERFLOW))
        std::cout &lt;&lt; &quot;    FE_OVERFLOW raised
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;fdim(4, 1) = 3 fdim(1, 4) = 0<br />
&nbsp;<wbr>&nbsp;fdim(4,-1) = 5 fdim(1,-4) = 5<br />
&nbsp;<wbr>&nbsp;fdim(1e308, -1e308) = inf<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errno == ERANGE: Numerical result out of range<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_OVERFLOW raised</p>
<h2>See also</h2>
<p>abs(int)<br />
labs<br />
llabs computes absolute value of an integral value (|x|)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
fmax<br />
fmaxf<br />
fmaxl larger of two floating point values<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
