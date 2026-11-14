---
title: "stdacosstdcomplex(3)"
name: "stdacosstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdacosstdcomplex/"
---

std::acos(std::complex) - std::acos(std::complex)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;
    (since C++ 11)

        complex&lt;T&gt; acos(const complex&lt;T&gt; &amp;z);</code></pre> 
Computes complex arc cosine of a complex value z. Branch cuts exist outside the interval [−1 ; +1] along the real axis. 

<h2>Parameters</h2>

z - complex value

<h2>Return value</h2>

If no errors occur, complex arc cosine of z is returned, in the range [0 ; ∞) along the real axis and in the range [−iπ ; iπ] along the imaginary axis. 
Error handling and special values 
Errors are reported consistent with math_errhandling 
If the implementation supports IEEE floating-point arithmetic, 
* std::acos(std::conj(z)) == std::conj(std::acos(z)) 
* If z is (±0,+0), the result is (π/2,-0) 
* If z is (±0,NaN), the result is (π/2,NaN) 
* If z is (x,+∞) (for any finite x), the result is (π/2,-∞) 
* If z is (x,NaN) (for any nonzero finite x), the result is (NaN,NaN) and FE_INVALID may be raised. 
* If z is (-∞,y) (for any positive finite y), the result is (π,-∞) 
* If z is (+∞,y) (for any positive finite y), the result is (+0,-∞) 
* If z is (-∞,+∞), the result is (3π/4,-∞) 
* If z is (+∞,+∞), the result is (π/4,-∞) 
* If z is (±∞,NaN), the result is (NaN,±∞) (the sign of the imaginary part is unspecified) 
* If z is (NaN,y) (for any finite y), the result is (NaN,NaN) and FE_INVALID may be raised 
* If z is (NaN,+∞), the result is (NaN,-∞) 
* If z is (NaN,NaN), the result is (NaN,NaN) 

<h2>Notes</h2>

Inverse cosine (or arc cosine) is a multivalued function and requires a branch cut on the complex plane. The branch cut is conventionally placed at the line segments (-∞,-1) and (1,∞) of the real axis. 
The mathematical definition of the principal value of arc cosine is acos z = 
1 
2 π + iln(iz +

√

1-z2

)

For any z, acos(z) = π - acos(-z)


<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;complex&gt;
int main()

{
    std::cout &lt;&lt; std::fixed;
    std::complex&lt;double&gt; z1(-2, 0);
    std::cout &lt;&lt; &quot;acos&quot; &lt;&lt; z1 &lt;&lt; &quot; = &quot; &lt;&lt; std::acos(z1) &lt;&lt; '\n';
    std::complex&lt;double&gt; z2(-2, -0.0);
    std::cout &lt;&lt; &quot;acos&quot; &lt;&lt; z2 &lt;&lt; &quot; (the other side of the cut) = &quot;
              &lt;&lt; std::acos(z2) &lt;&lt; '\n';
    // for any z, acos(z) = pi - acos(-z)
    const double pi = std::acos(-1);
    std::complex&lt;double&gt; z3 = pi - std::acos(z2);
    std::cout &lt;&lt; &quot;cos(pi - acos&quot; &lt;&lt; z2 &lt;&lt; &quot;) = &quot; &lt;&lt; std::cos(z3) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;acos(-2.000000,0.000000) = (3.141593,-1.316958) 
&nbsp;<wbr>&nbsp;acos(-2.000000,-0.000000) (the other side of the cut) = (3.141593,1.316958) 
&nbsp;<wbr>&nbsp;cos(pi - acos(-2.000000,-0.000000)) = (2.000000,0.000000)

<h2>See also</h2>

asin(std::complex) computes arc sine of a complex number (arcsin(z)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
atan(std::complex) computes arc tangent of a complex number (arctan(z)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes cosine of a complex number (cos(z)) 
cos(std::complex) <i>(function template)</i> 
acos 
acosf 
acosl computes arc cosine (arccos(x)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::acos to each element of valarray 
acos(std::valarray) <i>(function template)</i> 
