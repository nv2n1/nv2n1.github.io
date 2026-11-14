---
title: "stdasinstdcomplex(3)"
name: "stdasinstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdasinstdcomplex/"
---

std::asin(std::complex) - std::asin(std::complex)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;
    (since C++ 11)

        complex&lt;T&gt; asin(const complex&lt;T&gt; &amp;z);</code></pre> 
Computes complex arc sine of a complex value z. Branch cut exists outside the interval [−1 ; +1] along the real axis. 

<h2>Parameters</h2>

z - complex value

<h2>Return value</h2>

If no errors occur, complex arc sine of z is returned, in the range of a strip unbounded along the imaginary axis and in the interval [−π/2; +π/2] along the real axis. 
Errors and special cases are handled as if the operation is implemented by -i * std::asinh(i*z), where i is the imaginary unit. 

<h2>Notes</h2>

Inverse sine (or arc sine) is a multivalued function and requires a branch cut on the complex plane. The branch cut is conventionally placed at the line segments (-∞,-1) and (1,∞) of the real axis.

The mathematical definition of the principal value of arc sine is asin z = -iln(iz +

√

1-z2

)

For any z, asin(z) = acos(-z) - 
π 
2 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;complex&gt;
int main()

{
    std::cout &lt;&lt; std::fixed;
    std::complex&lt;double&gt; z1(-2, 0);
    std::cout &lt;&lt; &quot;acos&quot; &lt;&lt; z1 &lt;&lt; &quot; = &quot; &lt;&lt; std::acos(z1) &lt;&lt; '\n';
    std::complex&lt;double&gt; z2(-2, -0.0);
    std::cout &lt;&lt; &quot;acos&quot; &lt;&lt; z2 &lt;&lt; &quot; (the other side of the cut) = &quot;
              &lt;&lt; std::acos(z2) &lt;&lt; '\n';
    // for any z, acos(z) = pi - acos(-z)
    const double pi = std::acos(-1);
    std::complex&lt;double&gt; z3 = pi - std::acos(z2);
    std::cout &lt;&lt; &quot;cos(pi - acos&quot; &lt;&lt; z2 &lt;&lt; &quot;) = &quot; &lt;&lt; std::cos(z3) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;asin(-2.000000,0.000000) = (-1.570796,1.316958) 
&nbsp;<wbr>&nbsp;asin(-2.000000,-0.000000) (the other side of the cut) = (-1.570796,-1.316958) 
&nbsp;<wbr>&nbsp;sin(acos(-2.000000,-0.000000) - pi/2) = (-2.000000,-0.000000)

<h2>See also</h2>

acos(std::complex) computes arc cosine of a complex number (arccos(z)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
atan(std::complex) computes arc tangent of a complex number (arctan(z)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes sine of a complex number (sin(z)) 
sin(std::complex) <i>(function template)</i> 
asin 
asinf 
asinl computes arc sine (arcsin(x)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::asin to each element of valarray 
asin(std::valarray) <i>(function template)</i> 
