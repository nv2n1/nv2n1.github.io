---
title: "stdnormstdcomplex(3)"
name: "stdnormstdcomplex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnormstdcomplex/"
---

std::norm(std::complex) - std::norm(std::complex)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;complex&gt;

    template &lt;class T&gt;
    (until C++ 20)

        T norm(const std::complex&lt;T&gt; &amp;z);

template &lt;class T&gt;
(since C++ 20)

    constexpr T norm(const std::complex&lt;T&gt; &amp;z);

float norm(float z);

template &lt;class DoubleOrInteger&gt;
(1)(since C++ 11)

    double norm(DoubleOrInteger z);
(until C++ 20)

    long double norm(long double z);
(2)

    constexpr float norm(float z);

template &lt;class DoubleOrInteger&gt;
(since C++ 20)

    constexpr double norm(DoubleOrInteger z);

constexpr long double norm(long double z);</code></pre> 
1) Returns the squared magnitude of the complex number z. 
2) Additional overloads are provided for float, double, long double, and all integer types, which are treated as complex numbers with zero imaginary component. <i>(since C++11)</i> 

<h2>Parameters</h2>

z - complex value

<h2>Return value</h2>

the squared magnitude of z 

<h2>Notes</h2>

The norm calculated by this function is also known as field_norm or absolute_square. 
The Euclidean norm of a complex number is provided by std::abs, which is more costly to compute. In some situations, it may be replaced by std::norm, for example, if abs(z1) &gt; abs(z2) then norm(z1) &gt; norm(z2). 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the magnitude of a complex number 
abs(std::complex) <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the complex conjugate 
conj <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a complex number from magnitude and phase angle 
polar <i>(function template)</i> 
