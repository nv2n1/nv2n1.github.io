---
title: "stdmodfstdmodffstdmodfl(3)"
name: "stdmodfstdmodffstdmodfl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmodfstdmodffstdmodfl/"
description: "std::modf,std::modff,std::modfl – std::modf,std::modff,std::modfl"
---

<p>std::modf,std::modff,std::modfl &#8211; std::modf,std::modff,std::modfl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float modf ( float x, float* iptr );<br />
float modff( float x, float* iptr ); <i>(since C++11)</i><br />
double modf ( double x, double* iptr ); <code>(1)</code> <code>(2)</code><br />
long double modf ( long double x, long double* iptr ); <code>(3)</code><br />
long double modfl( long double x, long double* iptr ); <i>(since C++11)</i><br />
1-3) Decomposes given floating point value x into integral and fractional parts, each having the same type and sign as x. The integral part (in floating-point format) is stored in the object pointed to by iptr. </p>
<h2>Parameters</h2>
<p>x &#8211; floating point value<br />
iptr &#8211; pointer to floating point value to store the integral part to</p>
<h2>Return value</h2>
<p>If no errors occur, returns the fractional part of x with the same sign as x. The integral part is put into the value pointed to by iptr.<br />
The sum of the returned value and the value stored in *iptr gives x (allowing for rounding) </p>
<h2>Error handling</h2>
<p>This function is not subject to any errors specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If x is ±0, ±0 is returned, and ±0 is stored in *iptr.<br />
* If x is ±∞, ±0 is returned, and ±∞ is stored in *iptr.<br />
* If x is NaN, NaN is returned, and NaN is stored in *iptr.<br />
* The returned value is exact, the_current_rounding_mode is ignored</p>
<h2>Notes</h2>
<p>This function behaves as if implemented as follows: </p>
<pre><code>double modf(double x, double *iptr)

{

#pragma STDC FENV_ACCESS ON
    int save_round = std::fegetround();
    std::fesetround(FE_TOWARDZERO);
    *iptr = std::nearbyint(x);
    std::fesetround(save_round);
    return std::copysign(std::isinf(x) ? 0.0 : x - (*iptr), x);
}
</code></pre>
<h2>Example</h2>
<p>Compares different floating-point decomposition functions<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;limits&gt;
int main()

{
    double f = 123.45;
    std::cout &lt;&lt; &quot;Given the number &quot; &lt;&lt; f &lt;&lt; &quot; or &quot; &lt;&lt; std::hexfloat
              &lt;&lt; f &lt;&lt; std::defaultfloat &lt;&lt; &quot; in hex,
&quot;;
    double f3;
    double f2 = std::modf(f, &amp;f3);
    std::cout &lt;&lt; &quot;modf() makes &quot; &lt;&lt; f3 &lt;&lt; &quot; + &quot; &lt;&lt; f2 &lt;&lt; '
';
    int i;
    f2 = std::frexp(f, &amp;i);
    std::cout &lt;&lt; &quot;frexp() makes &quot; &lt;&lt; f2 &lt;&lt; &quot; * 2^&quot; &lt;&lt; i &lt;&lt; '
';
    i = std::ilogb(f);
    std::cout &lt;&lt; &quot;logb()/ilogb() make &quot; &lt;&lt; f / std::scalbn(1.0, i) &lt;&lt; &quot; * &quot;
              &lt;&lt; std::numeric_limits&lt;double&gt;::radix
              &lt;&lt; &quot;^&quot; &lt;&lt; std::ilogb(f) &lt;&lt; '
';
    // special values
    f2 = std::modf(-0.0, &amp;f3);
    std::cout &lt;&lt; &quot;modf(-0) makes &quot; &lt;&lt; f3 &lt;&lt; &quot; + &quot; &lt;&lt; f2 &lt;&lt; '
';
    f2 = std::modf(-INFINITY, &amp;f3);
    std::cout &lt;&lt; &quot;modf(-Inf) makes &quot; &lt;&lt; f3 &lt;&lt; &quot; + &quot; &lt;&lt; f2 &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Given the number 123.45 or 0x1.edccccccccccdp+6 in hex,<br />
&nbsp;<wbr>&nbsp;modf() makes 123 + 0.45<br />
&nbsp;<wbr>&nbsp;frexp() makes 0.964453 * 2^7<br />
&nbsp;<wbr>&nbsp;logb()/ilogb() make 1.92891 * 2^6<br />
&nbsp;<wbr>&nbsp;modf(-0) makes -0 + -0<br />
&nbsp;<wbr>&nbsp;modf(-Inf) makes -INF + -0</p>
<h2>See also</h2>
<p>trunc<br />
truncf<br />
truncl nearest integer not greater in magnitude than the given value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
