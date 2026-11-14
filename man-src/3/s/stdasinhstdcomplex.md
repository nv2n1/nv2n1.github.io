---
title: "stdasinhstdcomplex(3)"
name: "stdasinhstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdasinhstdcomplex/"
---

std::asinh(std::complex) - std::asinh(std::complex)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;
    (since C++ 11)

        complex&lt;T&gt; asinh(const complex&lt;T&gt; &amp;z);</code></pre> 
Computes complex arc hyperbolic sine of a complex value z with branch cuts outside the interval [−i; +i] along the imaginary axis. 

<h2>Parameters</h2>

z - complex value

<h2>Return value</h2>

If no errors occur, the complex arc hyperbolic sine of z is returned, in the range of a strip mathematically unbounded along the real axis and in the interval [−iπ/2; +iπ/2] along the imaginary axis. 
Error handling and special values 
Errors are reported consistent with math_errhandling 
If the implementation supports IEEE floating-point arithmetic, 
* std::asinh(std::conj(z)) == std::conj(std::asinh(z)) 
* std::asinh(-z) == -std::asinh(z) 
* If z is (+0,+0), the result is (+0,+0) 
* If z is (x,+∞) (for any positive finite x), the result is (+∞,π/2) 
* If z is (x,NaN) (for any finite x), the result is (NaN,NaN) and FE_INVALID may be raised 
* If z is (+∞,y) (for any positive finite y), the result is (+∞,+0) 
* If z is (+∞,+∞), the result is (+∞,π/4) 
* If z is (+∞,NaN), the result is (+∞,NaN) 
* If z is (NaN,+0), the result is (NaN,+0) 
* If z is (NaN,y) (for any finite nonzero y), the result is (NaN,NaN) and FE_INVALID may be raised 
* If z is (NaN,+∞), the result is (±∞,NaN) (the sign of the real part is unspecified) 
* If z is (NaN,NaN), the result is (NaN,NaN) 

<h2>Notes</h2>

Although the C++ standard names this function &quot;complex arc hyperbolic sine&quot;, the inverse functions of the hyperbolic functions are the area functions. Their argument is the area of a hyperbolic sector, not an arc. The correct name is &quot;complex inverse hyperbolic sine&quot;, and, less common, &quot;complex area hyperbolic sine&quot;. 
Inverse hyperbolic sine is a multivalued function and requires a branch cut on the complex plane. The branch cut is conventionally placed at the line segments (-i∞,-i) and (i,i∞) of the imaginary axis. 
The mathematical definition of the principal value of the inverse hyperbolic sine is asinh z = ln(z + 
√ 
1+z2 
) 
For any z, asinh(z) = 
asin(iz) 
i 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;complex&gt;
int main()

{
    std::cout &lt;&lt; std::fixed;
    std::complex&lt;double&gt; z1(0, -2);
    std::cout &lt;&lt; &quot;asinh&quot; &lt;&lt; z1 &lt;&lt; &quot; = &quot; &lt;&lt; std::asinh(z1) &lt;&lt; '\n';
    std::complex&lt;double&gt; z2(-0.0, -2);
    std::cout &lt;&lt; &quot;asinh&quot; &lt;&lt; z2 &lt;&lt; &quot; (the other side of the cut) = &quot;
              &lt;&lt; std::asinh(z2) &lt;&lt; '\n';
    // for any z, asinh(z) = asin(iz)/i
    std::complex&lt;double&gt; z3(1, 2);
    std::complex&lt;double&gt; i(0, 1);
    std::cout &lt;&lt; &quot;asinh&quot; &lt;&lt; z3 &lt;&lt; &quot; = &quot; &lt;&lt; std::asinh(z3) &lt;&lt; '\n'
              &lt;&lt; &quot;asin&quot; &lt;&lt; z3 * i &lt;&lt; &quot;/i = &quot; &lt;&lt; std::asin(z3 * i) / i &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;asinh(0.000000,-2.000000) = (1.316958,-1.570796) 
&nbsp;<wbr>&nbsp;asinh(-0.000000,-2.000000) (the other side of the cut) = (-1.316958,-1.570796) 
&nbsp;<wbr>&nbsp;asinh(1.000000,2.000000) = (1.469352,1.063440) 
&nbsp;<wbr>&nbsp;asin(-2.000000,1.000000)/i = (1.469352,1.063440)

<h2>See also</h2>

acosh(std::complex) computes area hyperbolic cosine of a complex number 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
atanh(std::complex) computes area hyperbolic tangent of a complex number 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes hyperbolic sine of a complex number (sh(z)) 
sinh(std::complex) <i>(function template)</i> 
asinh 
asinhf 
asinhl computes the inverse hyperbolic sine (arsinh(x)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
