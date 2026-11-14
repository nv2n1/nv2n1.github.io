---
title: "stderfcstderfcfstderfcl(3)"
name: "stderfcstderfcfstderfcl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderfcstderfcfstderfcl/"
description: "std::erfc,std::erfcf,std::erfcl – std::erfc,std::erfcf,std::erfcl"
---

<p>std::erfc,std::erfcf,std::erfcl &#8211; std::erfc,std::erfcf,std::erfcl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float erfc ( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
float erfcf( float arg );<br />
double erfc ( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
long double erfc ( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
long double erfcl( long double arg );<br />
double erfc ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the complementary_error_function of arg, that is 1.0-erf(arg), but without loss of precision for large arg<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, value of the complementary error function of arg, that is<br />
2<br />
√<br />
π<br />
∫∞<br />
arge-t2<br />
dt or 1-erf(arg), is returned.<br />
If a range error occurs due to underflow, the correct result (after rounding) is returned </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If the argument is +∞, +0 is returned<br />
* If the argument is -∞, 2 is returned<br />
* If the argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>For the IEEE-compatible type double, underflow is guaranteed if arg &gt; 26.55. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;iomanip&gt;

double normalCDF(double x) // Phi(-∞, x) aka N(x)

{
    return std::erfc(-x / std::sqrt(2)) / 2;
}

int main()

{
    std::cout &lt;&lt; &quot;normal cumulative distribution function:
&quot;
              &lt;&lt; std::fixed &lt;&lt; std::setprecision(2);
    for (double n = 0; n &lt; 1; n += 0.1)
        std::cout &lt;&lt; &quot;normalCDF(&quot; &lt;&lt; n &lt;&lt; &quot;) &quot; &lt;&lt; 100 * normalCDF(n) &lt;&lt; &quot;%
&quot;;
    std::cout &lt;&lt; &quot;special values:
&quot;
              &lt;&lt; &quot;erfc(-Inf) = &quot; &lt;&lt; std::erfc(-INFINITY) &lt;&lt; '
'
              &lt;&lt; &quot;erfc(Inf) = &quot; &lt;&lt; std::erfc(INFINITY) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;normal cumulative distribution function:<br />
&nbsp;<wbr>&nbsp;normalCDF(0.00) 50.00%<br />
&nbsp;<wbr>&nbsp;normalCDF(0.10) 53.98%<br />
&nbsp;<wbr>&nbsp;normalCDF(0.20) 57.93%<br />
&nbsp;<wbr>&nbsp;normalCDF(0.30) 61.79%<br />
&nbsp;<wbr>&nbsp;normalCDF(0.40) 65.54%<br />
&nbsp;<wbr>&nbsp;normalCDF(0.50) 69.15%<br />
&nbsp;<wbr>&nbsp;normalCDF(0.60) 72.57%<br />
&nbsp;<wbr>&nbsp;normalCDF(0.70) 75.80%<br />
&nbsp;<wbr>&nbsp;normalCDF(0.80) 78.81%<br />
&nbsp;<wbr>&nbsp;normalCDF(0.90) 81.59%<br />
&nbsp;<wbr>&nbsp;normalCDF(1.00) 84.13%<br />
&nbsp;<wbr>&nbsp;special values:<br />
&nbsp;<wbr>&nbsp;erfc(-Inf) = 2.00<br />
&nbsp;<wbr>&nbsp;erfc(Inf) = 0.00</p>
<h2>See also</h2>
<p>erf<br />
erff<br />
erfl error function<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Erfc.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
