---
title: "stdpowstdcomplex(3)"
name: "stdpowstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpowstdcomplex/"
---

std::pow(std::complex) - std::pow(std::complex)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;
    (1)

        complex&lt;T&gt; pow(const complex&lt;T&gt; &amp;x, const complex&lt;T&gt; &amp;y);

template &lt;class T&gt;
(2)

    complex&lt;T&gt; pow(const complex&lt;T&gt; &amp;x, const T &amp;y);

template &lt;class T&gt;
(3)

    complex&lt;T&gt; pow(const T &amp;x, const complex&lt;T&gt; &amp;y);

template &lt;class T, class U&gt;
(4)(since C++ 11)

    complex&lt;/*Promoted*/&gt; pow(const complex&lt;T&gt; &amp;x, const complex&lt;U&gt; &amp;y);

template &lt;class T, class U&gt;
(5)(since C++ 11)

    complex&lt;/*Promoted*/&gt; pow(const complex&lt;T&gt; &amp;x, const U &amp;y);

template &lt;class T, class U&gt;
(6)(since C++ 11)

    complex&lt;/*Promoted*/&gt; pow(const T &amp;x, const complex&lt;U&gt; &amp;y);</code></pre> 
1-3) Computes complex x raised to a complex power y with a branch cut along the negative real axis for the first argument. 
4-6) Additional overloads are provided for all arithmetic types, such that 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1. If either argument is long double or std::complex&lt;long double&gt;, then both arguments are cast to std::complex&lt;long double&gt; <i>(since C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2. Otherwise, if either argument is double, std::complex&lt;double&gt; or integer type, then both arguments are cast to std::complex&lt;double&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3. Otherwise, if either argument is float or std::complex&lt;float&gt;, then both arguments are cast to std::complex&lt;float&gt; 

<h2>Parameters</h2>

x - base as a complex value 
y - exponent as a complex value

<h2>Return value</h2>

If no errors occur, the complex power xy 
, is returned. 
Errors and special cases are handled as if the operation is implemented by std::exp(y*std::log(x)) 
The result of std::pow(0, 0) is implementation-defined. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;complex&gt;
int main()

{
    std::cout &lt;&lt; std::fixed;
    std::complex&lt;double&gt; z(1, 2);
    std::cout &lt;&lt; &quot;(1,2)^2 = &quot; &lt;&lt; std::pow(z, 2) &lt;&lt; '\n';
    std::complex&lt;double&gt; z2(-1, 0); // square root of -1
    std::cout &lt;&lt; &quot;-1^0.5 = &quot; &lt;&lt; std::pow(z2, 0.5) &lt;&lt; '\n';
    std::complex&lt;double&gt; z3(-1, -0.0); // other side of the cut
    std::cout &lt;&lt; &quot;(-1, -0)^0.5 = &quot; &lt;&lt; std::pow(z3, 0.5) &lt;&lt; '\n';
    std::complex&lt;double&gt; i(0, 1); // i^i = exp(-pi/2)
    std::cout &lt;&lt; &quot;i^i = &quot; &lt;&lt; std::pow(i, i) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;(1,2)^2 = (-3.000000,4.000000) 
&nbsp;<wbr>&nbsp;-1^0.5 = (0.000000,1.000000) 
&nbsp;<wbr>&nbsp;(-1, -0)^0.5 = (0.000000,-1.000000) 
&nbsp;<wbr>&nbsp;i^i = (0.207880,0.000000)

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;complex square root in the range of the right half-plane 
sqrt(std::complex) <i>(function template)</i> 
pow 
powf 
powl raises a number to the given power (xy) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;applies the function std::pow to two valarrays or a valarray and a value 
pow(std::valarray) <i>(function template)</i> 
