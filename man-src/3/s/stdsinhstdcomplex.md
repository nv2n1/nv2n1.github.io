---
title: "stdsinhstdcomplex(3)"
name: "stdsinhstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsinhstdcomplex/"
description: "std::sinh(std::complex) – std::sinh(std::complex)"
---

<p>std::sinh(std::complex) &#8211; std::sinh(std::complex)</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;
    (since C++ 11)

        complex&lt;T&gt; sinh(const complex&lt;T&gt; &amp;z);</code></pre>
<p>Computes complex hyperbolic sine of a complex value z. </p>
<h2>Parameters</h2>
<p>z &#8211; complex value</p>
<h2>Return value</h2>
<p>If no errors occur, complex hyperbolic sine of z is returned<br />
Error handling and special values<br />
Errors are reported consistent with math_errhandling<br />
If the implementation supports IEEE floating-point arithmetic,<br />
* std::sinh(std::conj(z)) == std::conj(std::sinh(z))<br />
* std::sinh(z) == -std::sinh(-z)<br />
* If z is (+0,+0), the result is (+0,+0)<br />
* If z is (+0,+∞), the result is (±0,NaN) (the sign of the real part is unspecified) and FE_INVALID is raised<br />
* If z is (+0,NaN), the result is (±0,NaN)<br />
* If z is (x,+∞) (for any positive finite x), the result is (NaN,NaN) and FE_INVALID is raised<br />
* If z is (x,NaN) (for any positive finite x), the result is (NaN,NaN) and FE_INVALID may be raised<br />
* If z is (+∞,+0), the result is (+∞,+0)<br />
* If z is (+∞,y) (for any positive finite y), the result is +∞cis(y)<br />
* If z is (+∞,+∞), the result is (±∞,NaN) (the sign of the real part is unspecified) and FE_INVALID is raised<br />
* If z is (+∞,NaN), the result is (±∞,NaN) (the sign of the real part is unspecified)<br />
* If z is (NaN,+0), the result is (NaN,+0)<br />
* If z is (NaN,y) (for any finite nonzero y), the result is (NaN,NaN) and FE_INVALID may be raised<br />
* If z is (NaN,NaN), the result is (NaN,NaN)<br />
where cis(y) is cos(y) + i sin(y) </p>
<h2>Notes</h2>
<p>Mathematical definition of hyperbolic sine is sinh z =<br />
ez<br />
-e-z<br />
2<br />
Hyperbolic sine is an entire function in the complex plane and has no branch cuts. It is periodic with respect to the imaginary component, with period 2πi </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;complex&gt;
int main()

{
    std::cout &lt;&lt; std::fixed;
    std::complex&lt;double&gt; z(1, 0); // behaves like real sinh along the real line
    std::cout &lt;&lt; &quot;sinh&quot; &lt;&lt; z &lt;&lt; &quot; = &quot; &lt;&lt; std::sinh(z)
              &lt;&lt; &quot; (sinh(1) = &quot; &lt;&lt; std::sinh(1) &lt;&lt; &quot;)
&quot;;
    std::complex&lt;double&gt; z2(0, 1); // behaves like sine along the imaginary line
    std::cout &lt;&lt; &quot;sinh&quot; &lt;&lt; z2 &lt;&lt; &quot; = &quot; &lt;&lt; std::sinh(z2)
              &lt;&lt; &quot; ( sin(1) = &quot; &lt;&lt; std::sin(1) &lt;&lt; &quot;)
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;sinh(1.000000,0.000000) = (1.175201,0.000000) (<a href="/docs/linux/man/1-sinh/">sinh</a><code>(1)</code> = 1.175201)<br />
&nbsp;<wbr>&nbsp;sinh(0.000000,1.000000) = (0.000000,0.841471) ( <a href="/docs/linux/man/1-sin/">sin</a><code>(1)</code> = 0.841471)</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes hyperbolic cosine of a complex number (ch(z))<br />
cosh(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes hyperbolic tangent of a complex number<br />
tanh(std::complex) <i>(function template)</i><br />
asinh(std::complex) computes area hyperbolic sine of a complex number<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
sinh<br />
sinhf<br />
sinhl computes hyperbolic sine (sh(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::sinh to each element of valarray<br />
sinh(std::valarray) <i>(function template)</i> </p>
