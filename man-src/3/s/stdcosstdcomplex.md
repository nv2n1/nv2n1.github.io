---
title: "stdcosstdcomplex(3)"
name: "stdcosstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcosstdcomplex/"
description: "std::cos(std::complex) – std::cos(std::complex)"
---

<p>std::cos(std::complex) &#8211; std::cos(std::complex)</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;

    complex&lt;T&gt; cos(const complex&lt;T&gt; &amp;z);</code></pre>
<p>Computes complex cosine of a complex value z. </p>
<h2>Parameters</h2>
<p>z &#8211; complex value</p>
<h2>Return value</h2>
<p>If no errors occur, the complex cosine of z is returned.<br />
Errors and special cases are handled as if the operation is implemented by std::cosh(i*z), where i is the imaginary unit. </p>
<h2>Notes</h2>
<p>The cosine is an entire function on the complex plane, and has no branch cuts.<br />
Mathematical definition of the cosine is cos z =<br />
eiz<br />
+e-iz<br />
2 </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;complex&gt;
int main()

{
    std::cout &lt;&lt; std::fixed;
    std::complex&lt;double&gt; z(1, 0); // behaves like real cosine along the real line
    std::cout &lt;&lt; &quot;cos&quot; &lt;&lt; z &lt;&lt; &quot; = &quot; &lt;&lt; std::cos(z)
              &lt;&lt; &quot; ( cos(1) = &quot; &lt;&lt; std::cos(1) &lt;&lt; &quot;)
&quot;;
    std::complex&lt;double&gt; z2(0, 1); // behaves like real cosh along the imaginary line
    std::cout &lt;&lt; &quot;cos&quot; &lt;&lt; z2 &lt;&lt; &quot; = &quot; &lt;&lt; std::cos(z2)
              &lt;&lt; &quot; (cosh(1) = &quot; &lt;&lt; std::cosh(1) &lt;&lt; &quot;)
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;cos(1.000000,0.000000) = (0.540302,-0.000000) ( <a href="/docs/linux/man/1-cos/">cos</a><code>(1)</code> = 0.540302)<br />
&nbsp;<wbr>&nbsp;cos(0.000000,1.000000) = (1.543081,-0.000000) (<a href="/docs/linux/man/1-cosh/">cosh</a><code>(1)</code> = 1.543081)</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes sine of a complex number (sin(z))<br />
sin(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes tangent of a complex number (tan(z))<br />
tan(std::complex) <i>(function template)</i><br />
acos(std::complex) computes arc cosine of a complex number (arccos(z))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
cos<br />
cosf<br />
cosl computes cosine (cos(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::cos to each element of valarray<br />
cos(std::valarray) <i>(function template)</i> </p>
