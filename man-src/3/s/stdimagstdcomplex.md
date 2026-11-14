---
title: "stdimagstdcomplex(3)"
name: "stdimagstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdimagstdcomplex/"
---

std::imag(std::complex) - std::imag(std::complex)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;
    (until C++ 14)

        T imag(const std::complex&lt;T&gt; &amp;z);

template &lt;class T&gt;
(since C++ 14)

    constexpr T imag(const std::complex&lt;T&gt; &amp;z);

float imag(float z);

template &lt;class DoubleOrInteger&gt;
(1)(since C++ 11)

    double imag(DoubleOrInteger z);
(until C++ 14)

    long double imag(long double z);
(2)

    constexpr float imag(float z);

template &lt;class DoubleOrInteger&gt;
(since C++ 14)

    constexpr double imag(DoubleOrInteger z);

constexpr long double imag(long double z);</code></pre> 
1) Returns the imaginary component of the complex number z, i.e. z.imag(). 
2) Additional overloads are provided for float, double, long double, and all integer types, which are treated as complex numbers with zero imaginary component. <i>(since C++11)</i> 

<h2>Parameters</h2>

z - complex value

<h2>Return value</h2>

the imaginary component of z 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;accesses the imaginary part of the complex number 
imag <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the real component 
real <i>(function template)</i> 
