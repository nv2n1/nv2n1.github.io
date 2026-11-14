---
title: "stdcomplexoperatorunaryoperator-unary(3)"
name: "stdcomplexoperatorunaryoperator-unary"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcomplexoperatorunaryoperator-unary/"
---

std::complex&lt;T&gt;::operator+(unary),operator-(unary) - std::complex&lt;T&gt;::operator+(unary),operator-(unary)

<h2>Synopsis</h2>

<pre><code>template &lt;class T&gt;
(until C++ 20)

    std::complex&lt;T&gt;
    operator+(const std::complex&lt;T&gt; &amp;val);

template &lt;class T&gt;
(since C++ 20)

    constexpr std::complex&lt;T&gt;
    operator+(const std::complex&lt;T&gt; &amp;val);
(1)

    template &lt;class T&gt;
    (until C++ 20)

        std::complex&lt;T&gt;
        operator-(const std::complex&lt;T&gt; &amp;val);
(2)

    template &lt;class T&gt;
    (since C++ 20)

        constexpr std::complex&lt;T&gt;
        operator-(const std::complex&lt;T&gt; &amp;val);</code></pre> 
Implements the analogs of the unary arithmetic operators for complex numbers. 
1) Returns the value of its argument 
2) Negates the argument 

<h2>Parameters</h2>

val - the complex number argument

<h2>Return value</h2>

1) a copy of the argument, std::complex&lt;T&gt;(val) 
2) negated argument, std::complex&lt;T&gt;(-val.real(), -val.imag()) 

<h2>See also</h2>

operator+ performs complex number arithmetics on two complex values or a complex and a scalar 
operator- <i>(function template)</i> 
operator* 
operator/ 
