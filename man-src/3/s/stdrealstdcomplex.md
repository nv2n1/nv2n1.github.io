---
title: "stdrealstdcomplex(3)"
name: "stdrealstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrealstdcomplex/"
---

std::real(std::complex) - std::real(std::complex)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;
    (until C++ 14)

        T real(const std::complex&lt;T&gt; &amp;z);

template &lt;class T&gt;
(since C++ 14)

    constexpr T real(const std::complex&lt;T&gt; &amp;z);

float real(float z);

template &lt;class DoubleOrInteger&gt;
(1)(since C++ 11)

    double real(DoubleOrInteger z);
(until C++ 14)

    long double real(long double z);
(2)

    constexpr float real(float z);

template &lt;class DoubleOrInteger&gt;
(since C++ 14)

    constexpr double real(DoubleOrInteger z);

constexpr long double real(long double z);</code></pre> 
1) Returns the real component of the complex number z, i.e. z.real(). 
2) Additional overloads are provided for float, double, long double, and all integer types, which are treated as complex numbers with zero imaginary component. <i>(since C++11)</i> 

<h2>Parameters</h2>

z - complex value

<h2>Return value</h2>

the real component of z 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the real part of the complex number 
real <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the imaginary component 
imag <i>(function template)</i> 
