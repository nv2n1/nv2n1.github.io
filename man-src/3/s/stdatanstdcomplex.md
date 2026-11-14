---
title: "stdatanstdcomplex(3)"
name: "stdatanstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatanstdcomplex/"
---

std::atan(std::complex) - std::atan(std::complex)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;
    (since C++ 11)

        complex&lt;T&gt; atan(const complex&lt;T&gt; &amp;z);</code></pre> 
Computes complex arc tangent of a complex value z. Branch cut exists outside the interval [−i ; +i] along the imaginary axis. 

<h2>Parameters</h2>

z - complex value

<h2>Return value</h2>

If no errors occur, complex arc tangent of z is returned, in the range of a strip unbounded along the imaginary axis and in the interval [−π/2; +π/2] along the real axis. 
Errors and special cases are handled as if the operation is implemented by -i * std::atanh(i*z), where i is the imaginary unit. 

<h2>Notes</h2>

Inverse tangent (or arc tangent) is a multivalued function and requires a branch cut on the complex plane. The branch cut is conventionally placed at the line segments (-∞i,-i) and (+i,+∞i) of the imaginary axis.

The mathematical definition of the principal value of inverse tangent is atan z = - 
1 
2 
i [ln(1 - iz) - ln (1 + iz)] 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;complex&gt;

#include &lt;cmath&gt;

int main()

{
    std::cout &lt;&lt; std::fixed;
    std::complex&lt;double&gt; z1(0, 2);
    std::cout &lt;&lt; &quot;atan&quot; &lt;&lt; z1 &lt;&lt; &quot; = &quot; &lt;&lt; std::atan(z1) &lt;&lt; '\n';
    std::complex&lt;double&gt; z2(-0.0, 2);
    std::cout &lt;&lt; &quot;atan&quot; &lt;&lt; z2 &lt;&lt; &quot; (the other side of the cut) = &quot;
              &lt;&lt; std::atan(z2) &lt;&lt; '\n';
    std::complex&lt;double&gt; z3(0, INFINITY);
    std::cout &lt;&lt; &quot;2*atan&quot; &lt;&lt; z3 &lt;&lt; &quot; = &quot; &lt;&lt; 2.0 * std::atan(z3) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;atan(0.000000,2.000000) = (1.570796,0.549306) 
&nbsp;<wbr>&nbsp;atan(-0.000000,2.000000) (the other side of the cut) = (-1.570796,0.549306) 
&nbsp;<wbr>&nbsp;2*atan(0.000000,inf) = (3.141593,0.000000)

<h2>See also</h2>

asin(std::complex) computes arc sine of a complex number (arcsin(z)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
acos(std::complex) computes arc cosine of a complex number (arccos(z)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes tangent of a complex number (tan(z)) 
tan(std::complex) <i>(function template)</i> 
atan 
atanf 
atanl computes arc tangent (arctan(x)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::atan to each element of valarray 
atan(std::valarray) <i>(function template)</i> 
