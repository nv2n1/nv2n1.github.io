---
title: "stdprojstdcomplex(3)"
name: "stdprojstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdprojstdcomplex/"
description: "std::proj(std::complex) – std::proj(std::complex)"
---

<p>std::proj(std::complex) &#8211; std::proj(std::complex)</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;complex&gt;<br />
template&lt; class T &gt; <code>(1)</code> <i>(since C++11)</i><br />
complex&lt;T&gt; proj( const complex&lt;T&gt;&amp; z );<br />
std::complex&lt;long double&gt; proj( long double z ); <code>(2)</code> <i>(since C++11)</i><br />
template&lt; class DoubleOrInteger &gt; <code>(3)</code> <i>(since C++11)</i><br />
std::complex&lt;double&gt; proj( DoubleOrInteger z );<br />
std::complex&lt;float&gt; proj( float z ); <code>(4)</code> <i>(since C++11)</i><br />
Returns the projection of the complex number z onto the Riemann sphere.<br />
For most z, std::proj(z)==z, but all complex infinities, even the numbers where one component is infinite and the other is NaN, become positive real infinity, (INFINITY, 0) or (INFINITY, -0). The sign of the imaginary (zero) component is the sign of std::imag(z).<br />
Additional overloads are provided for float, double, long double, and all integer types, which are treated as complex numbers with zero imaginary component. </p>
<h2>Parameters</h2>
<p>z &#8211; complex value</p>
<h2>Return value</h2>
<p>the projection of z onto the Riemann sphere </p>
<h2>Notes</h2>
<p>The proj function helps model the Riemann sphere by mapping all infinities to one (give or take the sign of the imaginary zero), and should be used just before any operation, especially comparisons, that might give spurious results for any of the other infinities. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;complex&gt;
int main()

{
    std::complex&lt;double&gt; c1(1, 2);
    std::cout &lt;&lt; &quot;proj&quot; &lt;&lt; c1 &lt;&lt; &quot; = &quot; &lt;&lt; std::proj(c1) &lt;&lt; '
';
    std::complex&lt;double&gt; c2(INFINITY, -1);
    std::cout &lt;&lt; &quot;proj&quot; &lt;&lt; c2 &lt;&lt; &quot; = &quot; &lt;&lt; std::proj(c2) &lt;&lt; '
';
    std::complex&lt;double&gt; c3(0, -INFINITY);
    std::cout &lt;&lt; &quot;proj&quot; &lt;&lt; c3 &lt;&lt; &quot; = &quot; &lt;&lt; std::proj(c3) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;proj(1,2) = (1,2)<br />
&nbsp;<wbr>&nbsp;proj(inf,-1) = (inf,-0)<br />
&nbsp;<wbr>&nbsp;proj(0,-inf) = (inf,-0)</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the magnitude of a complex number<br />
abs(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the squared magnitude<br />
norm <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a complex number from magnitude and phase angle<br />
polar <i>(function template)</i> </p>
