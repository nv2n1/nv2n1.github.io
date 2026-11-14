---
title: "stdtanstdcomplex(3)"
name: "stdtanstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtanstdcomplex/"
description: "std::tan(std::complex) – std::tan(std::complex)"
---

<p>std::tan(std::complex) &#8211; std::tan(std::complex)</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;

    complex&lt;T&gt; tan(const complex&lt;T&gt; &amp;z);</code></pre>
<p>Computes complex tangent of a complex value z. </p>
<h2>Parameters</h2>
<p>z &#8211; complex value</p>
<h2>Return value</h2>
<p>If no errors occur, the complex tangent of z is returned.<br />
Errors and special cases are handled as if the operation is implemented by -i * std::tanh(i*z), where i is the imaginary unit. </p>
<h2>Notes</h2>
<p>Tangent is an analytical function on the complex plain and has no branch cuts. It is periodic with respect to the real component, with period πi, and has poles of the first order along the real line, at coordinates (π(1/2 + n), 0). However no common floating-point representation is able to represent π/2 exactly, thus there is no value of the argument for which a pole error occurs.<br />
Mathematical definition of the tangent is tan z =<br />
i(e-iz<br />
-eiz<br />
)<br />
e-iz<br />
+eiz </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;complex&gt;
int main()

{
    std::cout &lt;&lt; std::fixed;
    std::complex&lt;double&gt; z(1, 0); // behaves like real tangent along the real line
    std::cout &lt;&lt; &quot;tan&quot; &lt;&lt; z &lt;&lt; &quot; = &quot; &lt;&lt; std::tan(z)
              &lt;&lt; &quot; ( tan(1) = &quot; &lt;&lt; std::tan(1) &lt;&lt; &quot;)
&quot;;
    std::complex&lt;double&gt; z2(0, 1); // behaves like tanh along the imaginary line
    std::cout &lt;&lt; &quot;tan&quot; &lt;&lt; z2 &lt;&lt; &quot; = &quot; &lt;&lt; std::tan(z2)
              &lt;&lt; &quot; (tanh(1) = &quot; &lt;&lt; std::tanh(1) &lt;&lt; &quot;)
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;tan(1.000000,0.000000) = (1.557408,0.000000) ( <a href="/docs/linux/man/1-tan/">tan</a><code>(1)</code> = 1.557408)<br />
&nbsp;<wbr>&nbsp;tan(0.000000,1.000000) = (0.000000,0.761594) (<a href="/docs/linux/man/1-tanh/">tanh</a><code>(1)</code> = 0.761594)</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes sine of a complex number (sin(z))<br />
sin(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes cosine of a complex number (cos(z))<br />
cos(std::complex) <i>(function template)</i><br />
atan(std::complex) computes arc tangent of a complex number (arctan(z))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
tan<br />
tanf<br />
tanl computes tangent (tan(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::tan to each element of valarray<br />
tan(std::valarray) <i>(function template)</i> </p>
