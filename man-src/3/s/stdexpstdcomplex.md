---
title: "stdexpstdcomplex(3)"
name: "stdexpstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexpstdcomplex/"
---

std::exp(std::complex) - std::exp(std::complex)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;

    complex&lt;T&gt; exp(const complex&lt;T&gt; &amp;z);</code></pre> 
Compute base-e exponential of z, that is e (Euler's number, 2.7182818) raised to the z power. 

<h2>Parameters</h2>

z - complex value

<h2>Return value</h2>

If no errors occur, e raised to the power of z, ez 
, is returned. 
Error handling and special values 
Errors are reported consistent with math_errhandling 
If the implementation supports IEEE floating-point arithmetic, 
* std::exp(std::conj(z)) == std::conj(std::exp(z)) 
* If z is (±0,+0), the result is (1,+0) 
* If z is (x,+∞) (for any finite x), the result is (NaN,NaN) and FE_INVALID is raised. 
* If z is (x,NaN) (for any finite x), the result is (NaN,NaN) and FE_INVALID may be raised. 
* If z is (+∞,+0), the result is (+∞,+0) 
* If z is (-∞,y) (for any finite y), the result is +0cis(y) 
* If z is (+∞,y) (for any finite nonzero y), the result is +∞cis(y) 
* If z is (-∞,+∞), the result is (±0,±0) (signs are unspecified) 
* If z is (+∞,+∞), the result is (±∞,NaN) and FE_INVALID is raised (the sign of the real part is unspecified) 
* If z is (-∞,NaN), the result is (±0,±0) (signs are unspecified) 
* If z is (+∞,NaN), the result is (±∞,NaN) (the sign of the real part is unspecified) 
* If z is (NaN,+0), the result is (NaN,+0) 
* If z is (NaN,y) (for any nonzero y), the result is (NaN,NaN) and FE_INVALID may be raised 
* If z is (NaN,NaN), the result is (NaN,NaN) 
where cis(y) is cos(y) + i sin(y) 

<h2>Notes</h2>

The complex exponential function ez 
for z = x+iy equals ex 
cis(y), or, ex 
(cos(y) + i sin(y)) 
The exponential function is an entire function in the complex plane and has no branch cuts. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;complex&gt;

#include &lt;iostream&gt;
int main()

{
    const double pi = std::acos(-1);
    const std::complex&lt;double&gt; i(0, 1);
    std::cout &lt;&lt; std::fixed &lt;&lt; &quot; exp(i*pi) = &quot; &lt;&lt; std::exp(i * pi) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;exp(i*pi) = (-1.000000,0.000000)

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;complex natural logarithm with the branch cuts along the negative real axis 
log(std::complex) <i>(function template)</i> 
exp 
expf 
expl returns e raised to the given power (ex) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::exp to each element of valarray 
exp(std::valarray) <i>(function template)</i> 
