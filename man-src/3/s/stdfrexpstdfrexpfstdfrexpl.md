---
title: "stdfrexpstdfrexpfstdfrexpl(3)"
name: "stdfrexpstdfrexpfstdfrexpl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfrexpstdfrexpfstdfrexpl/"
description: "std::frexp,std::frexpf,std::frexpl – std::frexp,std::frexpf,std::frexpl"
---

<p>std::frexp,std::frexpf,std::frexpl &#8211; std::frexp,std::frexpf,std::frexpl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float frexp ( float arg, int* exp );<br />
float frexpf( float arg, int* exp ); <i>(since C++11)</i><br />
double frexp ( double arg, int* exp ); <code>(1)</code> <code>(2)</code><br />
long double frexp ( long double arg, int* exp );<br />
long double frexpl( long double arg, int* exp ); <code>(3)</code> <i>(since C++11)</i><br />
double frexp ( IntegralType arg, int* exp ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Decomposes given floating point value arg into a normalized fraction and an integral power of two.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to <code>(2)</code> (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; floating point value<br />
exp &#8211; pointer to integer value to store the exponent to</p>
<h2>Return value</h2>
<p>If arg is zero, returns zero and stores zero in *exp.<br />
Otherwise (if arg is not zero), if no errors occur, returns the value x in the range (-1;-0.5], [0.5; 1) and stores an integer value in *exp such that x×2(*exp)<br />
=arg<br />
If the value to be stored in *exp is outside the range of int, the behavior is unspecified.<br />
If arg is not a floating-point number, the behavior is unspecified. </p>
<h2>Error handling</h2>
<p>This function is not subject to any errors specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If arg is ±0, it is returned, unmodified, and 0 is stored in *exp.<br />
* If arg is ±∞, it is returned, and an unspecified value is stored in *exp.<br />
* If arg is NaN, NaN is returned, and an unspecified value is stored in *exp.<br />
* No floating-point exceptions are raised.<br />
* If FLT_RADIX is 2 (or a power of 2), the returned value is exact, the_current_rounding_mode is ignored</p>
<h2>Notes</h2>
<p>On a binary system (where FLT_RADIX is 2), frexp may be implemented as </p>
<pre><code>{
    *exp = (value == 0) ? 0 : (int)(1 + std::logb(value));
    return std::scalbn(value, -(*exp));
}</code></pre>
<p>The function std::frexp, together with its dual, std::ldexp, can be used to manipulate the representation of a floating-point number without direct bit manipulations. </p>
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
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Given the number 123.45 or 0x1.edccccccccccdp+6 in hex,<br />
&nbsp;<wbr>&nbsp;modf() makes 123 + 0.45<br />
&nbsp;<wbr>&nbsp;frexp() makes 0.964453 * 2^7<br />
&nbsp;<wbr>&nbsp;logb()/ilogb() make 1.92891 * 2^6</p>
<h2>See also</h2>
<p>ldexp<br />
ldexpf<br />
ldexpl multiplies a number by 2 raised to a power<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
logb<br />
logbf<br />
logbl extracts exponent of the number<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
ilogb<br />
ilogbf<br />
ilogbl extracts exponent of the number<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
modf<br />
modff<br />
modfl decomposes a number into integer and fractional parts<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
