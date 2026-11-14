---
title: "stdlogstdcomplex(3)"
name: "stdlogstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlogstdcomplex/"
---

std::log(std::complex) - std::log(std::complex)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;

    complex&lt;T&gt; log(const complex&lt;T&gt; &amp;z);</code></pre> 
Computes complex natural (base e) logarithm of a complex value z with a branch cut along the negative real axis. 

<h2>Parameters</h2>

z - complex value

<h2>Return value</h2>

If no errors occur, the complex natural logarithm of z is returned, in the range of a strip in the interval [−iπ, +iπ] along the imaginary axis and mathematically unbounded along the real axis. 
Error handling and special values 
Errors are reported consistent with math_errhandling 
If the implementation supports IEEE floating-point arithmetic, 
* The function is continuous onto the branch cut taking into account the sign of imaginary part 
* std::log(std::conj(z)) == std::conj(std::log(z)) 
* If z is (-0,+0), the result is (-∞,π) and FE_DIVBYZERO is raised 
* If z is (+0,+0), the result is (-∞,+0) and FE_DIVBYZERO is raised 
* If z is (x,+∞) (for any finite x), the result is (+∞,π/2) 
* If z is (x,NaN) (for any finite x), the result is (NaN,NaN) and FE_INVALID may be raised 
* If z is (-∞,y) (for any finite positive y), the result is (+∞,π) 
* If z is (+∞,y) (for any finite positive y), the result is (+∞,+0) 
* If z is (-∞,+∞), the result is (+∞,3π/4) 
* If z is (+∞,+∞), the result is (+∞,π/4) 
* If z is (±∞,NaN), the result is (+∞,NaN) 
* If z is (NaN,y) (for any finite y), the result is (NaN,NaN) and FE_INVALID may be raised 
* If z is (NaN,+∞), the result is (+∞,NaN) 
* If z is (NaN,NaN), the result is (NaN,NaN) 

<h2>Notes</h2>

The natural logarithm of a complex number z with polar coordinate components (r,θ) equals ln r + i(θ+2nπ), with the principal value ln r + iθ 
The semantics of this function are intended to be consistent with the C function clog. 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_2597 C++98 specification mishandles signed zero imaginary parts erroneous requirement removed 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;complex&gt;
int main()

{
    std::complex&lt;double&gt; z(0, 1); // // r = 1, θ = pi/2
    std::cout &lt;&lt; &quot;2*log&quot; &lt;&lt; z &lt;&lt; &quot; = &quot; &lt;&lt; 2. * std::log(z) &lt;&lt; '\n';
    std::complex&lt;double&gt; z2(sqrt(2) / 2, sqrt(2) / 2); // r = 1, θ = pi/4
    std::cout &lt;&lt; &quot;4*log&quot; &lt;&lt; z2 &lt;&lt; &quot; = &quot; &lt;&lt; 4. * std::log(z2) &lt;&lt; '\n';
    std::complex&lt;double&gt; z3(-1, 0); // r = 1, θ = pi
    std::cout &lt;&lt; &quot;log&quot; &lt;&lt; z3 &lt;&lt; &quot; = &quot; &lt;&lt; std::log(z3) &lt;&lt; '\n';
    std::complex&lt;double&gt; z4(-1, -0.0); // the other side of the cut
    std::cout &lt;&lt; &quot;log&quot; &lt;&lt; z4 &lt;&lt; &quot; (the other side of the cut) = &quot; &lt;&lt; std::log(z4) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;2*log(0,1) = (0,3.14159) 
&nbsp;<wbr>&nbsp;4*log(0.707107,0.707107) = (0,3.14159) 
&nbsp;<wbr>&nbsp;log(-1,0) = (0,3.14159) 
&nbsp;<wbr>&nbsp;log(-1,-0) (the other side of the cut) = (0,-3.14159)

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;complex common logarithm with the branch cuts along the negative real axis 
log10(std::complex) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;complex base e exponential 
exp(std::complex) <i>(function template)</i> 
log 
logf 
logl computes natural (base e) logarithm (ln(x)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::log to each element of valarray 
log(std::valarray) <i>(function template)</i> 
