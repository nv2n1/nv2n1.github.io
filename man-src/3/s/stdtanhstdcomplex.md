---
title: "stdtanhstdcomplex(3)"
name: "stdtanhstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtanhstdcomplex/"
description: "std::tanh(std::complex) – std::tanh(std::complex)"
---

<p>std::tanh(std::complex) &#8211; std::tanh(std::complex)</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;
    (since C++ 11)

        complex&lt;T&gt; tanh(const complex&lt;T&gt; &amp;z);</code></pre>
<p>Computes complex hyperbolic tangent of a complex value z. </p>
<h2>Parameters</h2>
<p>z &#8211; complex value</p>
<h2>Return value</h2>
<p>If no errors occur, complex hyperbolic tangent of z is returned<br />
Error handling and special values<br />
Errors are reported consistent with math_errhandling<br />
If the implementation supports IEEE floating-point arithmetic,<br />
* std::tanh(std::conj(z)) == std::conj(std::tanh(z))<br />
* std::tanh(-z) == -std::tanh(z)<br />
* If z is (+0,+0), the result is (+0,+0)<br />
* If z is (x,+∞) (for any[1] finite x), the result is (NaN,NaN) and FE_INVALID is raised<br />
* If z is (x,NaN) (for any[2] finite x), the result is (NaN,NaN) and FE_INVALID may be raised<br />
* If z is (+∞,y) (for any finite positive y), the result is (1,+0)<br />
* If z is (+∞,+∞), the result is (1,±0) (the sign of the imaginary part is unspecified)<br />
* If z is (+∞,NaN), the result is (1,±0) (the sign of the imaginary part is unspecified)<br />
* If z is (NaN,+0), the result is (NaN,+0)<br />
* If z is (NaN,y) (for any non-zero y), the result is (NaN,NaN) and FE_INVALID may be raised<br />
* If z is (NaN,NaN), the result is (NaN,NaN)<br />
&nbsp;<wbr>&nbsp;1. ↑ per C11_DR471, this only holds for non-zero x. If z is (0,∞), the result should be (0,NaN)<br />
&nbsp;<wbr>&nbsp;2. ↑ per C11_DR471, this only holds for non-zero x. If z is (0,NaN), the result should be (0,NaN) </p>
<h2>Notes</h2>
<p>Mathematical definition of hyperbolic tangent is tanh z =<br />
ez<br />
-e-z<br />
ez<br />
+e-z<br />
Hyperbolic tangent is an analytical function on the complex plain and has no branch cuts. It is periodic with respect to the imaginary component, with period πi, and has poles of the first order along the imaginary line, at coordinates (0, π(1/2 + n)). However no common floating-point representation is able to represent π/2 exactly, thus there is no value of the argument for which a pole error occurs. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;complex&gt;
int main()

{
    std::cout &lt;&lt; std::fixed;
    std::complex&lt;double&gt; z(1, 0); // behaves like real tanh along the real line
    std::cout &lt;&lt; &quot;tanh&quot; &lt;&lt; z &lt;&lt; &quot; = &quot; &lt;&lt; std::tanh(z)
              &lt;&lt; &quot; (tanh(1) = &quot; &lt;&lt; std::tanh(1) &lt;&lt; &quot;)
&quot;;
    std::complex&lt;double&gt; z2(0, 1); // behaves like tangent along the imaginary line
    std::cout &lt;&lt; &quot;tanh&quot; &lt;&lt; z2 &lt;&lt; &quot; = &quot; &lt;&lt; std::tanh(z2)
              &lt;&lt; &quot; ( tan(1) = &quot; &lt;&lt; std::tan(1) &lt;&lt; &quot;)
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;tanh(1.000000,0.000000) = (0.761594,0.000000) (<a href="/docs/linux/man/1-tanh/">tanh</a><code>(1)</code> = 0.761594)<br />
&nbsp;<wbr>&nbsp;tanh(0.000000,1.000000) = (0.000000,1.557408) ( <a href="/docs/linux/man/1-tan/">tan</a><code>(1)</code> = 1.557408)</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes hyperbolic sine of a complex number (sh(z))<br />
sinh(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes hyperbolic cosine of a complex number (ch(z))<br />
cosh(std::complex) <i>(function template)</i><br />
atanh(std::complex) computes area hyperbolic tangent of a complex number<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
tanh<br />
tanhf<br />
tanhl hyperbolic tangent<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::tanh to each element of valarray<br />
tanh(std::valarray) <i>(function template)</i> </p>
