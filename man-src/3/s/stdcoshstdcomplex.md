---
title: "stdcoshstdcomplex(3)"
name: "stdcoshstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcoshstdcomplex/"
description: "std::cosh(std::complex) – std::cosh(std::complex)"
---

<p>std::cosh(std::complex) &#8211; std::cosh(std::complex)</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;
    (since C++ 11)

        complex&lt;T&gt; cosh(const complex&lt;T&gt; &amp;z);</code></pre>
<p>Computes complex hyperbolic cosine of a complex value z. </p>
<h2>Parameters</h2>
<p>z &#8211; complex value</p>
<h2>Return value</h2>
<p>If no errors occur, complex hyperbolic cosine of z is returned<br />
Error handling and special values<br />
Errors are reported consistent with math_errhandling<br />
If the implementation supports IEEE floating-point arithmetic,<br />
* std::cosh(std::conj(z)) == std::conj(std::cosh(z))<br />
* std::cosh(z) == std::cosh(-z)<br />
* If z is (+0,+0), the result is (1,+0)<br />
* If z is (+0,+∞), the result is (NaN,±0) (the sign of the imaginary part is unspecified) and FE_INVALID is raised<br />
* If z is (+0,NaN), the result is (NaN,±0) (the sign of the imaginary part is unspecified)<br />
* If z is (x,+∞) (for any finite non-zero x), the result is (NaN,NaN) and FE_INVALID is raised<br />
* If z is (x,NaN) (for any finite non-zero x), the result is (NaN,NaN) and FE_INVALID may be raised<br />
* If z is (+∞,+0), the result is (+∞,+0)<br />
* If z is (+∞,y) (for any finite non-zero y), the result is +∞cis(y)<br />
* If z is (+∞,+∞), the result is (±∞,NaN) (the sign of the real part is unspecified) and FE_INVALID is raised<br />
* If z is (+∞,NaN), the result is (+∞,NaN)<br />
* If z is (NaN,+0), the result is (NaN,±0) (the sign of the imaginary part is unspecified)<br />
* If z is (NaN,+y) (for any finite non-zero y), the result is (NaN,NaN) and FE_INVALID may be raised<br />
* If z is (NaN,NaN), the result is (NaN,NaN)<br />
where cis(y) is cos(y) + i sin(y) </p>
<h2>Notes</h2>
<p>Mathematical definition of hyperbolic cosine is cosh z =<br />
ez<br />
+e-z<br />
2<br />
Hyperbolic cosine is an entire function in the complex plane and has no branch cuts. It is periodic with respect to the imaginary component, with period 2πi </p>
<h2>Examples</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;complex&gt;
int main()

{
    std::cout &lt;&lt; std::fixed;
    std::complex&lt;double&gt; z(1, 0); // behaves like real cosh along the real line
    std::cout &lt;&lt; &quot;cosh&quot; &lt;&lt; z &lt;&lt; &quot; = &quot; &lt;&lt; std::cosh(z)
              &lt;&lt; &quot; (cosh(1) = &quot; &lt;&lt; std::cosh(1) &lt;&lt; &quot;)
&quot;;
    std::complex&lt;double&gt; z2(0, 1); // behaves like real cosine along the imaginary line
    std::cout &lt;&lt; &quot;cosh&quot; &lt;&lt; z2 &lt;&lt; &quot; = &quot; &lt;&lt; std::cosh(z2)
              &lt;&lt; &quot; ( cos(1) = &quot; &lt;&lt; std::cos(1) &lt;&lt; &quot;)
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;cosh(1.000000,0.000000) = (1.543081,0.000000) (<a href="/docs/linux/man/1-cosh/">cosh</a><code>(1)</code> = 1.543081)<br />
&nbsp;<wbr>&nbsp;cosh(0.000000,1.000000) = (0.540302,0.000000) ( <a href="/docs/linux/man/1-cos/">cos</a><code>(1)</code> = 0.540302)</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes hyperbolic sine of a complex number (sh(z))<br />
sinh(std::complex) <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes hyperbolic tangent of a complex number<br />
tanh(std::complex) <i>(function template)</i><br />
acosh(std::complex) computes area hyperbolic cosine of a complex number<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
cosh<br />
coshf<br />
coshl computes hyperbolic cosine (ch(x))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::cosh to each element of valarray<br />
cosh(std::valarray) <i>(function template)</i> </p>
