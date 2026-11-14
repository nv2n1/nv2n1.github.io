---
title: "stdsqrtstdcomplex(3)"
name: "stdsqrtstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsqrtstdcomplex/"
---

std::sqrt(std::complex) - std::sqrt(std::complex)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;

    complex&lt;T&gt; sqrt(const complex&lt;T&gt; &amp;z);</code></pre> 
Computes the square root of the complex number z with a branch cut along the negative real axis. 

<h2>Parameters</h2>

z - complex number to take the square root of

<h2>Return value</h2>

If no errors occur, returns the square root of z, in the range of the right half-plane, including the imaginary axis ([0; +∞) along the real axis and (−∞; +∞) along the imaginary axis.) 
Error handling and special values 
Errors are reported consistent with math_errhandling 
If the implementation supports IEEE floating-point arithmetic, 
* The function is continuous onto the branch cut taking into account the sign of imaginary part 
* std::sqrt(std::conj(z)) == std::conj(std::sqrt(z)) 
* If z is (±0,+0), the result is (+0,+0) 
* If z is (x,+∞), the result is (+∞,+∞) even if x is NaN 
* If z is (x,NaN), the result is (NaN,NaN) (unless x is ±∞) and FE_INVALID may be raised 
* If z is (-∞,y), the result is (+0,+∞) for finite positive y 
* If z is (+∞,y), the result is (+∞,+0) for finite positive y 
* If z is (-∞,NaN), the result is (NaN,∞) (sign of imaginary part unspecified) 
* If z is (+∞,NaN), the result is (+∞,NaN) 
* If z is (NaN,y), the result is (NaN,NaN) and FE_INVALID may be raised 
* If z is (NaN,NaN), the result is (NaN,NaN) 

<h2>Notes</h2>

The semantics of this function are intended to be consistent with the C function csqrt. 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_2597 C++98 specification mishandles signed zero imaginary parts erroneous requirement removed 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;complex&gt;
int main()

{
    std::cout &lt;&lt; &quot;Square root of -4 is &quot;
              &lt;&lt; std::sqrt(std::complex&lt;double&gt;(-4, 0)) &lt;&lt; '\n'
              &lt;&lt; &quot;Square root of (-4,-0), the other side of the cut, is &quot;
              &lt;&lt; std::sqrt(std::complex&lt;double&gt;(-4, -0.0)) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Square root of -4 is (0,2) 
&nbsp;<wbr>&nbsp;Square root of (-4,-0), the other side of the cut, is (0,-2)

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;complex power, one or both arguments may be a complex number 
pow(std::complex) <i>(function template)</i> 
sqrt 
sqrtf computes square root ( 
sqrtl √ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::sqrt to each element of valarray 
sqrt(std::valarray) <i>(function template)</i> 
