---
title: "stdnextafterstdnextafterfstdnextafterlstdnexttowardstdnexttowardfstdnexttowardl(3)"
name: "stdnextafterstdnextafterfstdnextafterlstdnexttowardstdnexttowardfstdnexttowardl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnextafterstdnextafterfstdnextafterlstdnexttowardstdnexttowardfstdnexttowardl/"
description: "std::nextafter,std::nextafterf,std::nextafterl,std::nexttoward,std::nexttowardf,std::nexttowardl – std::nextafter,std::nextafterf,std::nextafterl,std::nexttoward,std::nexttowardf,std::nexttowardl"
---

<p>std::nextafter,std::nextafterf,std::nextafterl,std::nexttoward,std::nexttowardf,std::nexttowardl &#8211; std::nextafter,std::nextafterf,std::nextafterl,std::nexttoward,std::nexttowardf,std::nexttowardl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float nextafter ( float from, float to ); <code>(1)</code> <i>(since C++11)</i><br />
float nextafterf( float from, float to );<br />
double nextafter ( double from, double to ); <code>(2)</code> <i>(since C++11)</i><br />
long double nextafter ( long double from, long double to ); <code>(3)</code> <i>(since C++11)</i><br />
long double nextafterl( long double from, long double to );<br />
Promoted nextafter ( Arithmetic1 from, Arithmetic2 to ); <code>(4)</code> <i>(since C++11)</i><br />
float nexttoward ( float from, long double to ); <code>(5)</code> <i>(since C++11)</i><br />
float nexttowardf( float from, long double to );<br />
double nexttoward ( double from, long double to ); <code>(6)</code> <i>(since C++11)</i><br />
long double nexttoward ( long double from, long double to ); <code>(7)</code> <i>(since C++11)</i><br />
long double nexttowardl( long double from, long double to );<br />
double nexttoward ( IntegralType from, long double to ); <code>(8)</code> <i>(since C++11)</i> </p>
<pre><code>Returns the next representable value of from in the direction of to.

1-3) If from equals to to, to is returned.

5-7) If from equals to to, to is returned, converted from long double to the return type of the function without loss of range or precision.

4) A set of overloads or a function template for all combinations of arguments of arithmetic type not covered by (1-3). If any argument has integral_type, it is cast to double. If any argument is long double, then the return type Promoted is also long double, otherwise the return type is always double.

8) A set of overloads or a function template accepting the from argument of any integral_type. Equivalent to (6) (the argument is cast to double).
</code></pre>
<h2>Parameters</h2>
<p>from, to &#8211; floating point values</p>
<h2>Return value</h2>
<p>If no errors occur, the next representable value of from in the direction of to. is returned. If from equals to, then to is returned.<br />
If a range error due to overflow occurs, ±HUGE_VAL, ±HUGE_VALF, or ±HUGE_VALL is returned (with the same sign as from)<br />
If a range error occurs due to underflow, the correct result is returned. </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* if from is finite, but the expected result is an infinity, raises FE_INEXACT and FE_OVERFLOW<br />
* if from does not equal to and the result is subnormal or zero, raises FE_INEXACT and FE_UNDERFLOW<br />
* in any case, the returned value is independent of the current rounding mode<br />
* if either from or to is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>POSIX_specifies that the overflow and the underflow conditions are range errors (errno may be set)<br />
IEC 60559 recommends that from is returned whenever from==to. These functions return to instead, which makes the behavior around zero consistent: std::nextafter(-0.0, +0.0) returns +0.0 and std::nextafter(+0.0, -0.0) returns –0.0. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cmath&gt;

#include &lt;iomanip&gt;

#include &lt;iostream&gt;

#include &lt;cfloat&gt;

#include &lt;cfenv&gt;
int main()

{
    float from1 = 0, to1 = std::nextafter(from1, 1.f);
    std::cout &lt;&lt; &quot;The next representable float after &quot; &lt;&lt; std::setprecision(20) &lt;&lt; from1
              &lt;&lt; &quot; is &quot; &lt;&lt; to1
              &lt;&lt; std::hexfloat &lt;&lt; &quot; (&quot; &lt;&lt; to1 &lt;&lt; &quot;)
&quot;
              &lt;&lt; std::defaultfloat;
    float from2 = 1, to2 = std::nextafter(from2, 2.f);
    std::cout &lt;&lt; &quot;The next representable float after &quot; &lt;&lt; from2 &lt;&lt; &quot; is &quot; &lt;&lt; to2
              &lt;&lt; std::hexfloat &lt;&lt; &quot; (&quot; &lt;&lt; to2 &lt;&lt; &quot;)
&quot;
              &lt;&lt; std::defaultfloat;
    double from3 = std::nextafter(0.1, 0), to3 = 0.1;
    std::cout &lt;&lt; &quot;The number 0.1 lies between two valid doubles:
&quot;
              &lt;&lt; std::setprecision(56) &lt;&lt; &quot;    &quot; &lt;&lt; from3
              &lt;&lt; std::hexfloat &lt;&lt; &quot; (&quot; &lt;&lt; from3 &lt;&lt; ')' &lt;&lt; std::defaultfloat
              &lt;&lt; &quot;
and &quot; &lt;&lt; to3 &lt;&lt; std::hexfloat &lt;&lt; &quot; (&quot; &lt;&lt; to3 &lt;&lt; &quot;)
&quot;
              &lt;&lt; std::defaultfloat &lt;&lt; std::setprecision(20);
    // difference between nextafter and nexttoward:
    long double dir = std::nextafter(from1, 1.0L); // first subnormal long double
    float x = nextafter(from1, dir);               // first converts dir to float, giving 0
    std::cout &lt;&lt; &quot;With nextafter, next float after &quot; &lt;&lt; from1 &lt;&lt; &quot; is &quot; &lt;&lt; x &lt;&lt; '
';
    x = std::nexttoward(from1, dir);
    std::cout &lt;&lt; &quot;With nexttoward, next float after &quot; &lt;&lt; from1 &lt;&lt; &quot; is &quot; &lt;&lt; x &lt;&lt; '
';
    // special values
    {
#pragma STDC FENV_ACCESS ON
        std::feclearexcept(FE_ALL_EXCEPT);
        double from4 = DBL_MAX, to4 = std::nextafter(from4, INFINITY);
        std::cout &lt;&lt; &quot;The next representable double after &quot; &lt;&lt; std::setprecision(6)
                  &lt;&lt; from4 &lt;&lt; std::hexfloat &lt;&lt; &quot; (&quot; &lt;&lt; from4 &lt;&lt; ')'
                  &lt;&lt; std::defaultfloat &lt;&lt; &quot; is &quot; &lt;&lt; to4
                  &lt;&lt; std::hexfloat &lt;&lt; &quot; (&quot; &lt;&lt; to4 &lt;&lt; &quot;)
&quot;
                  &lt;&lt; std::defaultfloat;
        if (std::fetestexcept(FE_OVERFLOW))
            std::cout &lt;&lt; &quot;   raised FE_OVERFLOW
&quot;;
        if (std::fetestexcept(FE_INEXACT))
            std::cout &lt;&lt; &quot;   raised FE_INEXACT
&quot;;
    } // end FENV_ACCESS block
    float from5 = 0.0, to5 = std::nextafter(from5, -0.0);
    std::cout &lt;&lt; &quot;std::nextafter(+0.0, -0.0) gives &quot; &lt;&lt; std::fixed &lt;&lt; to5 &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;The next representable float after 0 is 1.4012984643248170709e-45 (0x1p-149)<br />
&nbsp;<wbr>&nbsp;The next representable float after 1 is 1.0000001192092895508 (0x1.000002p+0)<br />
&nbsp;<wbr>&nbsp;The number 0.1 lies between two valid doubles:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0.09999999999999999167332731531132594682276248931884765625 (0x1.9999999999999p-4)<br />
&nbsp;<wbr>&nbsp;and 0.1000000000000000055511151231257827021181583404541015625 (0x1.999999999999ap-4)<br />
&nbsp;<wbr>&nbsp;With nextafter, next float after 0 is 0<br />
&nbsp;<wbr>&nbsp;With nexttoward, next float after 0 is 1.4012984643248170709e-45<br />
&nbsp;<wbr>&nbsp;The next representable double after 1.79769e+308 (0x1.fffffffffffffp+1023) is inf (inf)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;raised FE_OVERFLOW<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;raised FE_INEXACT<br />
&nbsp;<wbr>&nbsp;std::nextafter(+0.0, -0.0) gives -0.000000</p>
<h2>See also</h2>
