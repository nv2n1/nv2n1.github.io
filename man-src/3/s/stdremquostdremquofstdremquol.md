---
title: "stdremquostdremquofstdremquol(3)"
name: "stdremquostdremquofstdremquol"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdremquostdremquofstdremquol/"
description: "std::remquo,std::remquof,std::remquol – std::remquo,std::remquof,std::remquol"
---

<p>std::remquo,std::remquof,std::remquol &#8211; std::remquo,std::remquof,std::remquol</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float remquo ( float x, float y, int* quo ); <code>(1)</code> <i>(since C++11)</i><br />
float remquof( float x, float y, int* quo );<br />
double remquo ( double x, double y, int* quo ); <code>(2)</code> <i>(since C++11)</i><br />
long double remquo ( long double x, long double y, int* quo ); <code>(3)</code> <i>(since C++11)</i><br />
long double remquol( long double x, long double y, int* quo );<br />
Promoted remquo ( Arithmetic1 x, Arithmetic2 y, int* quo ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the floating-point remainder of the division operation x/y as the std::remainder() function does. Additionally, the sign and at least the three of the last bits of x/y will be stored in quo, sufficient to determine the octant of the result within a period.<br />
4) A set of overloads or a function template for all combinations of arguments of arithmetic_type not covered by (1-3). If any non-pointer argument has integral_type, it is cast to double. If any other non-pointer argument is long double, then the return type is long double, otherwise it is double. </p>
<h2>Parameters</h2>
<p>x, y &#8211; floating point values<br />
quo &#8211; pointer to an integer value to store the sign and some bits of x/y</p>
<h2>Return value</h2>
<p>If successful, returns the floating-point remainder of the division x/y as defined in std::remainder, and stores, in *quo, the sign and at least three of the least significant bits of x/y (formally, stores a value whose sign is the sign of x/y and whose magnitude is congruent modulo 2n<br />
to the magnitude of the integral quotient of x/y, where n is an implementation-defined integer greater than or equal to 3).<br />
If y is zero, the value stored in *quo is unspecified.<br />
If a domain error occurs, an implementation-defined value is returned (NaN where supported)<br />
If a range error occurs due to underflow, the correct result is returned if subnormals are supported.<br />
If y is zero, but the domain error does not occur, zero is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
Domain error may occur if y is zero.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* The current rounding_mode has no effect.<br />
* FE_INEXACT is never raised<br />
* If x is ±∞ and y is not NaN, NaN is returned and FE_INVALID is raised<br />
* If y is ±0 and x is not NaN, NaN is returned and FE_INVALID is raised<br />
* If either x or y is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>POSIX_requires that a domain error occurs if x is infinite or y is zero.<br />
This function is useful when implementing periodic functions with the period exactly representable as a floating-point value: when calculating sin(πx) for a very large x, calling std::sin directly may result in a large error, but if the function argument is first reduced with std::remquo, the low-order bits of the quotient may be used to determine the sign and the octant of the result within the period, while the remainder may be used to calculate the value with high precision.<br />
On some platforms this operation is supported by hardware (and, for example, on Intel CPUs, FPREM1 leaves exactly 3 bits of precision in the quotient when complete). </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cfenv&gt;
#pragma STDC FENV_ACCESS ON

const double pi = std::acos(-1);

double cos_pi_x_naive(double x)
{
    return std::cos(pi * x);
}

// the period is 2, values are (0;0.5) positive, (0.5;1.5) negative, (1.5,2) positive

double cos_pi_x_smart(double x)

{
    int quadrant;
    double rem = std::remquo(x, 1, &amp;quadrant);
    quadrant = (unsigned)quadrant % 2; // The period is 2.
    switch (quadrant) {
    case 0:
        return std::cos(pi * rem);
    case 1:
        return -std::cos(pi * rem);
    };
}

int main()

{
    std::cout &lt;&lt; &quot;cos(pi * 0.25) = &quot; &lt;&lt; cos_pi_x_naive(0.25) &lt;&lt; '
'
              &lt;&lt; &quot;cos(pi * 1.25) = &quot; &lt;&lt; cos_pi_x_naive(1.25) &lt;&lt; '
'
              &lt;&lt; &quot;cos(pi * 2.25) = &quot; &lt;&lt; cos_pi_x_naive(2.25) &lt;&lt; '
'
              &lt;&lt; &quot;cos(pi * 0.25) = &quot; &lt;&lt; cos_pi_x_smart(0.25) &lt;&lt; '
'
              &lt;&lt; &quot;cos(pi * 1.25) = &quot; &lt;&lt; cos_pi_x_smart(1.25) &lt;&lt; '
'
              &lt;&lt; &quot;cos(pi * 2.25) = &quot; &lt;&lt; cos_pi_x_smart(2.25) &lt;&lt; '
'
              &lt;&lt; &quot;cos(pi * 1000000000000.25) = &quot;
              &lt;&lt; cos_pi_x_naive(1000000000000.25) &lt;&lt; '
'
              &lt;&lt; &quot;cos(pi * 1000000000001.25) = &quot;
              &lt;&lt; cos_pi_x_naive(1000000000001.25) &lt;&lt; '
'
              &lt;&lt; &quot;cos(pi * 1000000000000.25) = &quot;
              &lt;&lt; cos_pi_x_smart(1000000000000.25) &lt;&lt; '
'
              &lt;&lt; &quot;cos(pi * 1000000000001.25) = &quot;
              &lt;&lt; cos_pi_x_smart(1000000000001.25) &lt;&lt; '
';
    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);
    int quo;
    std::cout &lt;&lt; &quot;remquo(+Inf, 1) = &quot; &lt;&lt; std::remquo(INFINITY, 1, &amp;quo) &lt;&lt; '
';
    if (fetestexcept(FE_INVALID))
        std::cout &lt;&lt; &quot;    FE_INVALID raised
&quot;;
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;cos(pi * 0.25) = 0.707107<br />
&nbsp;<wbr>&nbsp;cos(pi * 1.25) = -0.707107<br />
&nbsp;<wbr>&nbsp;cos(pi * 2.25) = 0.707107<br />
&nbsp;<wbr>&nbsp;cos(pi * 0.25) = 0.707107<br />
&nbsp;<wbr>&nbsp;cos(pi * 1.25) = -0.707107<br />
&nbsp;<wbr>&nbsp;cos(pi * 2.25) = 0.707107<br />
&nbsp;<wbr>&nbsp;cos(pi * 1000000000000.25) = 0.707123<br />
&nbsp;<wbr>&nbsp;cos(pi * 1000000000001.25) = -0.707117<br />
&nbsp;<wbr>&nbsp;cos(pi * 1000000000000.25) = 0.707107<br />
&nbsp;<wbr>&nbsp;cos(pi * 1000000000001.25) = -0.707107<br />
&nbsp;<wbr>&nbsp;remquo(+Inf, 1) = -nan<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INVALID raised</p>
<h2>See also</h2>
<p>div(int)<br />
ldiv<br />
lldiv computes quotient and remainder of integer division<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
fmod<br />
fmodf<br />
fmodl remainder of the floating point division operation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
remainder<br />
remainderf<br />
remainderl signed remainder of the division operation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
