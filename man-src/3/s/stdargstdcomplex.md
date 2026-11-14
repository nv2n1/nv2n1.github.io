---
title: "stdargstdcomplex(3)"
name: "stdargstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdargstdcomplex/"
description: "std::arg(std::complex) – std::arg(std::complex)"
---

<p>std::arg(std::complex) &#8211; std::arg(std::complex)</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;complex&gt;<br />
template&lt; class T &gt; <code>(1)</code><br />
T arg( const complex&lt;T&gt;&amp; z );<br />
long double arg( long double z ); <code>(2)</code> <i>(since C++11)</i><br />
template&lt; class DoubleOrInteger &gt; <code>(3)</code> <i>(since C++11)</i><br />
double arg( DoubleOrInteger z );<br />
float arg( float z ); <code>(4)</code> <i>(since C++11)</i><br />
Calculates the phase angle (in radians) of the complex number z<br />
<i>(since C++11)</i>Additional overloads are provided for float, double, long double, and all integer types, which are treated as complex numbers with zero imaginary component. </p>
<h2>Parameters</h2>
<p>z &#8211; complex value</p>
<h2>Return value</h2>
<p>If no errors occur, returns the phase angle of z in the interval [−π; π].<br />
Errors and special cases are handled as if the function is implemented as std::atan2(std::imag(z), std::real(z)). </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;complex&gt;
int main()

{
    std::complex&lt;double&gt; z1(1, 0);
    std::cout &lt;&lt; &quot;phase angle of &quot; &lt;&lt; z1 &lt;&lt; &quot; is &quot; &lt;&lt; std::arg(z1) &lt;&lt; '
';
    std::complex&lt;double&gt; z2(0, 1);
    std::cout &lt;&lt; &quot;phase angle of &quot; &lt;&lt; z2 &lt;&lt; &quot; is &quot; &lt;&lt; std::arg(z2) &lt;&lt; '
';
    std::complex&lt;double&gt; z3(-1, 0);
    std::cout &lt;&lt; &quot;phase angle of &quot; &lt;&lt; z3 &lt;&lt; &quot; is &quot; &lt;&lt; std::arg(z3) &lt;&lt; '
';
    std::complex&lt;double&gt; z4(-1, -0.0);
    std::cout &lt;&lt; &quot;phase angle of &quot; &lt;&lt; z4 &lt;&lt; &quot; (the other side of the cut) is &quot;
              &lt;&lt; std::arg(z4) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;phase angle of (1,0) is 0<br />
&nbsp;<wbr>&nbsp;phase angle of (0,1) is 1.5708<br />
&nbsp;<wbr>&nbsp;phase angle of (-1,0) is 3.14159<br />
&nbsp;<wbr>&nbsp;phase angle of (-1,-0) (the other side of the cut) is -3.14159</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the magnitude of a complex number<br />
abs(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a complex number from magnitude and phase angle<br />
polar <i>(function template)</i><br />
atan2<br />
atan2f<br />
atan2l arc tangent, using signs to determine quadrants<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::atan2 to a valarray and a value<br />
atan2(std::valarray) <i>(function template)</i> </p>
