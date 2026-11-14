---
title: "stderfstderffstderfl(3)"
name: "stderfstderffstderfl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderfstderffstderfl/"
description: "std::erf,std::erff,std::erfl – std::erf,std::erff,std::erfl"
---

<p>std::erf,std::erff,std::erfl &#8211; std::erf,std::erff,std::erfl</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cmath&gt;<br />
float erf ( float arg ); <code>(1)</code> <i>(since C++11)</i><br />
float erff( float arg );<br />
double erf ( double arg ); <code>(2)</code> <i>(since C++11)</i><br />
long double erf ( long double arg ); <code>(3)</code> <i>(since C++11)</i><br />
long double erfl( long double arg );<br />
double erf ( IntegralType arg ); <code>(4)</code> <i>(since C++11)</i><br />
1-3) Computes the error_function of arg.<br />
4) A set of overloads or a function template accepting an argument of any integral_type. Equivalent to 2) (the argument is cast to double). </p>
<h2>Parameters</h2>
<p>arg &#8211; value of a floating-point or Integral_type</p>
<h2>Return value</h2>
<p>If no errors occur, value of the error function of arg, that is<br />
2<br />
√<br />
π<br />
∫arg<br />
0e-t2<br />
dt, is returned.<br />
If a range error occurs due to underflow, the correct result (after rounding), that is<br />
2*arg<br />
√<br />
π<br />
is returned </p>
<h2>Error handling</h2>
<p>Errors are reported as specified in math_errhandling.<br />
If the implementation supports IEEE floating-point arithmetic (IEC 60559), </p>
<p>* If the argument is ±0, ±0 is returned<br />
* If the argument is ±∞, ±1 is returned<br />
* If the argument is NaN, NaN is returned</p>
<h2>Notes</h2>
<p>Underflow is guaranteed if |arg| &lt; DBL_MIN*(sqrt(π)/2)<br />
erf(<br />
x<br />
σ<br />
√<br />
2<br />
) is the probability that a measurement whose errors are subject to a normal distribution with standard deviation σ is less than x away from the mean value. </p>
<h2>Example</h2>
<p>The following example calculates the probability that a normal variate is on the interval (x1, x2)<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;iomanip&gt;

double phi(double x1, double x2)

{
    return (std::erf(x2 / std::sqrt(2)) - std::erf(x1 / std::sqrt(2))) / 2;
}

int main()

{
    std::cout &lt;&lt; &quot;normal variate probabilities:
&quot;
              &lt;&lt; std::fixed &lt;&lt; std::setprecision(2);
    for (int n = -4; n &lt; 4; ++n)
        std::cout &lt;&lt; &quot;[&quot; &lt;&lt; std::setw(2) &lt;&lt; n &lt;&lt; &quot;:&quot; &lt;&lt; std::setw(2) &lt;&lt; n + 1 &lt;&lt; &quot;]: &quot;
                  &lt;&lt; std::setw(5) &lt;&lt; 100 * phi(n, n + 1) &lt;&lt; &quot;%
&quot;;
    std::cout &lt;&lt; &quot;special values:
&quot;
              &lt;&lt; &quot;erf(-0) = &quot; &lt;&lt; std::erf(-0.0) &lt;&lt; '
'
              &lt;&lt; &quot;erf(Inf) = &quot; &lt;&lt; std::erf(INFINITY) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;normal variate probabilities:<br />
&nbsp;<wbr>&nbsp;[-4:-3]: 0.13%<br />
&nbsp;<wbr>&nbsp;[-3:-2]: 2.14%<br />
&nbsp;<wbr>&nbsp;[-2:-1]: 13.59%<br />
&nbsp;<wbr>&nbsp;[-1: 0]: 34.13%<br />
&nbsp;<wbr>&nbsp;[ 0: 1]: 34.13%<br />
&nbsp;<wbr>&nbsp;[ 1: 2]: 13.59%<br />
&nbsp;<wbr>&nbsp;[ 2: 3]: 2.14%<br />
&nbsp;<wbr>&nbsp;[ 3: 4]: 0.13%<br />
&nbsp;<wbr>&nbsp;special values:<br />
&nbsp;<wbr>&nbsp;erf(-0) = -0.00<br />
&nbsp;<wbr>&nbsp;erf(Inf) = 1.00</p>
<h2>See also</h2>
<p>erfc<br />
erfcf<br />
erfcl complementary error function<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Erf.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
