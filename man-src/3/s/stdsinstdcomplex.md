---
title: "stdsinstdcomplex(3)"
name: "stdsinstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsinstdcomplex/"
description: "std::sin(std::complex) – std::sin(std::complex)"
---

<p>std::sin(std::complex) &#8211; std::sin(std::complex)</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;

    complex&lt;T&gt; sin(const complex&lt;T&gt; &amp;z);</code></pre>
<p>Computes complex sine of a complex value z. </p>
<h2>Parameters</h2>
<p>z &#8211; complex value</p>
<h2>Return value</h2>
<p>If no errors occur, the complex sine of z is returned.<br />
Errors and special cases are handled as if the operation is implemented by -i * std::sinh(i*z), where i is the imaginary unit. </p>
<h2>Notes</h2>
<p>The sine is an entire function on the complex plane, and has no branch cuts.<br />
Mathematical definition of the sine is sin z =<br />
eiz<br />
-e-iz<br />
2i </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;complex&gt;
int main()

{
    std::cout &lt;&lt; std::fixed;
    std::complex&lt;double&gt; z(1, 0); // behaves like real sine along the real line
    std::cout &lt;&lt; &quot;sin&quot; &lt;&lt; z &lt;&lt; &quot; = &quot; &lt;&lt; std::sin(z)
              &lt;&lt; &quot; ( sin(1) = &quot; &lt;&lt; std::sin(1) &lt;&lt; &quot;)
&quot;;
    std::complex&lt;double&gt; z2(0, 1); // behaves like sinh along the imaginary line
    std::cout &lt;&lt; &quot;sin&quot; &lt;&lt; z2 &lt;&lt; &quot; = &quot; &lt;&lt; std::sin(z2)
              &lt;&lt; &quot; (sinh(1) = &quot; &lt;&lt; std::sinh(1) &lt;&lt; &quot;)
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;sin(1.000000,0.000000) = (0.841471,0.000000) ( <a href="/docs/linux/man/1-sin/">sin</a><code>(1)</code> = 0.841471)<br />
&nbsp;<wbr>&nbsp;sin(0.000000,1.000000) = (0.000000,1.175201) (<a href="/docs/linux/man/1-sinh/">sinh</a><code>(1)</code> = 1.175201)</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes cosine of a complex number (cos(z))<br />
cos(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes tangent of a complex number (tan(z))<br />
tan(std::complex) <i>(function template)</i><br />
asin(std::complex) computes arc sine of a complex number (arcsin(z))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
sin<br />
sinf<br />
sinl computes sine (sin(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::sin to each element of valarray<br />
sin(std::valarray) <i>(function template)</i> </p>
