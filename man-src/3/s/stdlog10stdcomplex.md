---
title: "stdlog10stdcomplex(3)"
name: "stdlog10stdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlog10stdcomplex/"
description: "std::log10(std::complex) – std::log10(std::complex)"
---

<p>std::log10(std::complex) &#8211; std::log10(std::complex)</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;

    complex&lt;T&gt; log10(const complex&lt;T&gt; &amp;z);</code></pre>
<p>Computes complex common (base 10) logarithm of a complex value z with a branch cut along the negative real axis.<br />
The behavior of this function is equivalent to std::log(z)/std::log(T<code>(10)</code>). </p>
<h2>Parameters</h2>
<p>z &#8211; complex value</p>
<h2>Return value</h2>
<p>Complex common logarithm of z </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;complex&gt;
int main()

{
    std::complex&lt;double&gt; z(0, 1); // // r = 0, θ = pi/2
    std::cout &lt;&lt; &quot;2*log10&quot; &lt;&lt; z &lt;&lt; &quot; = &quot; &lt;&lt; 2. * std::log10(z) &lt;&lt; '
';
    std::complex&lt;double&gt; z2(sqrt(2) / 2, sqrt(2) / 2); // r = 1, θ = pi/4
    std::cout &lt;&lt; &quot;4*log10&quot; &lt;&lt; z2 &lt;&lt; &quot; = &quot; &lt;&lt; 4. * std::log10(z2) &lt;&lt; '
';
    std::complex&lt;double&gt; z3(-100, 0); // r = 100, θ = pi
    std::cout &lt;&lt; &quot;log10&quot; &lt;&lt; z3 &lt;&lt; &quot; = &quot; &lt;&lt; std::log10(z3) &lt;&lt; '
';
    std::complex&lt;double&gt; z4(-100, -0.0); // the other side of the cut
    std::cout &lt;&lt; &quot;log10&quot; &lt;&lt; z4 &lt;&lt; &quot; (the other side of the cut) = &quot;
              &lt;&lt; std::log10(z4) &lt;&lt; '
'
              &lt;&lt; &quot;(note: pi/log(10) = &quot; &lt;&lt; acos(-1) / log(10) &lt;&lt; &quot;)
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;2*log10(0,1) = (0,1.36438)<br />
&nbsp;<wbr>&nbsp;4*log10(0.707107,0.707107) = (0,1.36438)<br />
&nbsp;<wbr>&nbsp;log10(-100,0) = (2,1.36438)<br />
&nbsp;<wbr>&nbsp;log10(-100,-0) (the other side of the cut) = (2,-1.36438)<br />
&nbsp;<wbr>&nbsp;(note: pi/log<code>(10)</code> = 1.36438)</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;complex natural logarithm with the branch cuts along the negative real axis<br />
log(std::complex) <i>(function template)</i><br />
log10<br />
log10f<br />
log10l computes common (base 10) logarithm (log10(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::log10 to each element of valarray<br />
log10(std::valarray) <i>(function template)</i> </p>
