---
title: "stdacoshstdcomplex(3)"
name: "stdacoshstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdacoshstdcomplex/"
---

std::acosh(std::complex) - std::acosh(std::complex)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;
    (since C++ 11)

        complex&lt;T&gt; acosh(const complex&lt;T&gt; &amp;z);</code></pre> 
Computes complex arc hyperbolic cosine of a complex value z with branch cut at values less than 1 along the real axis. 

<h2>Parameters</h2>

z - complex value

<h2>Return value</h2>

If no errors occur, the complex arc hyperbolic cosine of z is returned, in the range of a half-strip of nonnegative values along the real axis and in the interval [−iπ; +iπ] along the imaginary axis. 
Error handling and special values 
Errors are reported consistent with math_errhandling 
If the implementation supports IEEE floating-point arithmetic, 
* std::acosh(std::conj(z)) == std::conj(std::acosh(z)) 
* If z is (±0,+0), the result is (+0,π/2) 
* If z is (x,+∞) (for any finite x), the result is (+∞,π/2) 
* If z is (x,NaN) (for any[1] finite x), the result is (NaN,NaN) and FE_INVALID may be raised. 
* If z is (-∞,y) (for any positive finite y), the result is (+∞,π) 
* If z is (+∞,y) (for any positive finite y), the result is (+∞,+0) 
* If z is (-∞,+∞), the result is (+∞,3π/4) 
* If z is (±∞,NaN), the result is (+∞,NaN) 
* If z is (NaN,y) (for any finite y), the result is (NaN,NaN) and FE_INVALID may be raised. 
* If z is (NaN,+∞), the result is (+∞,NaN) 
* If z is (NaN,NaN), the result is (NaN,NaN) 
&nbsp;<wbr>&nbsp;1. ↑ per C11_DR471, this holds for non-zero x only. If z is (0,NaN), the result should be (NaN,π/2) 

<h2>Notes</h2>

Although the C++ standard names this function &quot;complex arc hyperbolic cosine&quot;, the inverse functions of the hyperbolic functions are the area functions. Their argument is the area of a hyperbolic sector, not an arc. The correct name is &quot;complex inverse hyperbolic cosine&quot;, and, less common, &quot;complex area hyperbolic cosine&quot;. 
Inverse hyperbolic cosine is a multivalued function and requires a branch cut on the complex plane. The branch cut is conventionally placed at the line segment (-∞,+1) of the real axis. 
The mathematical definition of the principal value of the inverse hyperbolic cosine is acosh z = ln(z + 
√ 
z+1 
√ 
z-1) 
For any z, acosh(z) = 
√ 
z-1 
√ 
1-z 
acos(z), or simply i acos(z) in the upper half of the complex plane. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;complex&gt;
int main()

{
    std::cout &lt;&lt; std::fixed;
    std::complex&lt;double&gt; z1(0.5, 0);
    std::cout &lt;&lt; &quot;acosh&quot; &lt;&lt; z1 &lt;&lt; &quot; = &quot; &lt;&lt; std::acosh(z1) &lt;&lt; '\n';
    std::complex&lt;double&gt; z2(0.5, -0.0);
    std::cout &lt;&lt; &quot;acosh&quot; &lt;&lt; z2 &lt;&lt; &quot; (the other side of the cut) = &quot;
              &lt;&lt; std::acosh(z2) &lt;&lt; '\n';
    // in upper half-plane, acosh = i acos
    std::complex&lt;double&gt; z3(1, 1), i(0, 1);
    std::cout &lt;&lt; &quot;acosh&quot; &lt;&lt; z3 &lt;&lt; &quot; = &quot; &lt;&lt; std::acosh(z3) &lt;&lt; '\n'
              &lt;&lt; &quot;i*acos&quot; &lt;&lt; z3 &lt;&lt; &quot; = &quot; &lt;&lt; i * std::acos(z3) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;acosh(0.500000,0.000000) = (0.000000,-1.047198) 
&nbsp;<wbr>&nbsp;acosh(0.500000,-0.000000) (the other side of the cut) = (0.000000,1.047198) 
&nbsp;<wbr>&nbsp;acosh(1.000000,1.000000) = (1.061275,0.904557) 
&nbsp;<wbr>&nbsp;i*acos(1.000000,1.000000) = (1.061275,0.904557)

<h2>See also</h2>

acos(std::complex) computes arc cosine of a complex number (arccos(z)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
asinh(std::complex) computes area hyperbolic sine of a complex number 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
atanh(std::complex) computes area hyperbolic tangent of a complex number 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes hyperbolic cosine of a complex number (ch(z)) 
cosh(std::complex) <i>(function template)</i> 
acosh 
acoshf 
acoshl computes the inverse hyperbolic cosine (arcosh(x)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
