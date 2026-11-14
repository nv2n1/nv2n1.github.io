---
title: "stdabsstdcomplex(3)"
name: "stdabsstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdabsstdcomplex/"
---

std::abs(std::complex) - std::abs(std::complex)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;

    T abs(const complex&lt;T&gt; &amp;z);</code></pre> 
Returns the magnitude of the complex number z. 

<h2>Parameters</h2>

z - complex value

<h2>Return value</h2>

If no errors occur, returns the absolute value (also known as norm, modulus, or magnitude) of z. 
Errors and special cases are handled as if the function is implemented as std::hypot(std::real(z), std::imag(z)) 

<h2>Examples</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;complex&gt;
int main()

{
    std::complex&lt;double&gt; z(1, 1);
    std::cout &lt;&lt; z &lt;&lt; &quot; cartesian is rho = &quot; &lt;&lt; std::abs(z)
              &lt;&lt; &quot; theta = &quot; &lt;&lt; std::arg(z) &lt;&lt; &quot; polar\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;(1,1) cartesian is rho = 1.41421 theta = 0.785398 polar

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the phase angle 
arg <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a complex number from magnitude and phase angle 
polar <i>(function template)</i> 
abs(int) 
labs 
llabs computes absolute value of an integral value (|x|) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
abs(float) 
fabs 
fabsf 
fabsl absolute value of a floating point value (|x|) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
hypot computes square root of the sum of the squares of two given numbers ( 
hypotf √ 
hypotl x2 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;+y2 
<i>(C++11)</i> ) 
<i>(C++11)</i> <i>(function)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::abs to each element of valarray 
abs(std::valarray) <i>(function template)</i> 
