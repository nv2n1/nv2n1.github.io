---
title: "stdatanhstdcomplex(3)"
name: "stdatanhstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatanhstdcomplex/"
---

std::atanh(std::complex) - std::atanh(std::complex)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;
    (since C++ 11)

        complex&lt;T&gt; atanh(const complex&lt;T&gt; &amp;z);</code></pre> 
Computes the complex arc hyperbolic tangent of z with branch cuts outside the interval [−1; +1] along the real axis. 

<h2>Parameters</h2>

z - complex value

<h2>Return value</h2>

If no errors occur, the complex arc hyperbolic tangent of z is returned, in the range of a half-strip mathematically unbounded along the real axis and in the interval [−iπ/2; +iπ/2] along the imaginary axis. 
Error handling and special values 
Errors are reported consistent with math_errhandling 
If the implementation supports IEEE floating-point arithmetic, 
* std::atanh(std::conj(z)) == std::conj(std::atanh(z)) 
* std::atanh(-z) == -std::atanh(z) 
* If z is (+0,+0), the result is (+0,+0) 
* If z is (+0,NaN), the result is (+0,NaN) 
* If z is (+1,+0), the result is (+∞,+0) and FE_DIVBYZERO is raised 
* If z is (x,+∞) (for any finite positive x), the result is (+0,π/2) 
* If z is (x,NaN) (for any finite nonzero x), the result is (NaN,NaN) and FE_INVALID may be raised 
* If z is (+∞,y) (for any finite positive y), the result is (+0,π/2) 
* If z is (+∞,+∞), the result is (+0,π/2) 
* If z is (+∞,NaN), the result is (+0,NaN) 
* If z is (NaN,y) (for any finite y), the result is (NaN,NaN) and FE_INVALID may be raised 
* If z is (NaN,+∞), the result is (±0,π/2) (the sign of the real part is unspecified) 
* If z is (NaN,NaN), the result is (NaN,NaN) 

<h2>Notes</h2>

Although the C++ standard names this function &quot;complex arc hyperbolic tangent&quot;, the inverse functions of the hyperbolic functions are the area functions. Their argument is the area of a hyperbolic sector, not an arc. The correct name is &quot;complex inverse hyperbolic tangent&quot;, and, less common, &quot;complex area hyperbolic tangent&quot;. 
Inverse hyperbolic tangent is a multivalued function and requires a branch cut on the complex plane. The branch cut is conventionally placed at the line segmentd (-∞,-1] and [+1,+∞) of the real axis. 
The mathematical definition of the principal value of the inverse hyperbolic tangent is atanh z = 
ln(1+z)-ln(1-z) 
2 
. 
For any z, atanh(z) = 
atan(iz) 
i 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;complex&gt;
int main()

{
    std::cout &lt;&lt; std::fixed;
    std::complex&lt;double&gt; z1(2, 0);
    std::cout &lt;&lt; &quot;atanh&quot; &lt;&lt; z1 &lt;&lt; &quot; = &quot; &lt;&lt; std::atanh(z1) &lt;&lt; '\n';
    std::complex&lt;double&gt; z2(2, -0.0);
    std::cout &lt;&lt; &quot;atanh&quot; &lt;&lt; z2 &lt;&lt; &quot; (the other side of the cut) = &quot;
              &lt;&lt; std::atanh(z2) &lt;&lt; '\n';
    // for any z, atanh(z) = atanh(iz)/i
    std::complex&lt;double&gt; z3(1, 2);
    std::complex&lt;double&gt; i(0, 1);
    std::cout &lt;&lt; &quot;atanh&quot; &lt;&lt; z3 &lt;&lt; &quot; = &quot; &lt;&lt; std::atanh(z3) &lt;&lt; '\n'
              &lt;&lt; &quot;atan&quot; &lt;&lt; z3 * i &lt;&lt; &quot;/i = &quot; &lt;&lt; std::atan(z3 * i) / i &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;atanh(2.000000,0.000000) = (0.549306,1.570796) 
&nbsp;<wbr>&nbsp;atanh(2.000000,-0.000000) (the other side of the cut) = (0.549306,-1.570796) 
&nbsp;<wbr>&nbsp;atanh(1.000000,2.000000) = (0.173287,1.178097) 
&nbsp;<wbr>&nbsp;atan(-2.000000,1.000000)/i = (0.173287,1.178097)

<h2>See also</h2>

asinh(std::complex) computes area hyperbolic sine of a complex number 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
acosh(std::complex) computes area hyperbolic cosine of a complex number 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes hyperbolic tangent of a complex number 
tanh(std::complex) <i>(function template)</i> 
atanh 
atanhf 
atanhl computes the inverse hyperbolic tangent (artanh(x)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
