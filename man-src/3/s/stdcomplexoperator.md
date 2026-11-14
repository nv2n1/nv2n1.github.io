---
title: "stdcomplexoperator(3)"
name: "stdcomplexoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcomplexoperator/"
---

std::complex&lt;T&gt;::operator= - std::complex&lt;T&gt;::operator=

<h2>Synopsis</h2>

<pre><code>primary template complex&lt;T&gt;

    complex &amp;operator=(const T &amp;x);
(until C++ 20)

    constexpr complex &amp;
    operator=(const T &amp;x);
(since C++ 20)

    specialization complex&lt;float&gt;

    complex &amp;operator=(float x);
(until C++ 20)

    constexpr complex &amp;
    operator=(float x);
(since C++ 20)

    specialization complex&lt;double&gt;

    complex &amp;operator=(double x);
(until C++ 20)

    constexpr complex &amp;
    operator=(double x);
(since C++ 20)

    specialization complex&lt;long double&gt;(1)

        complex &amp;
        operator=(long double x);
(until C++ 20)

    constexpr complex &amp;
    operator=(long double x);
(1)(since C++ 20)

    all specializations(1)

        complex &amp;
        operator=(const complex &amp;cx);
(until C++ 20)

    constexpr complex &amp;
    operator=(const complex &amp;cx);
(1)(since C++ 20)

    template &lt;class X&gt;
    (2)(until C++ 20)

        complex &amp;
        operator=(const std::complex&lt;X&gt; &amp;cx);
(3)

    template &lt;class X&gt;
    (since C++ 20)

        constexpr complex &amp;
        operator=(const std::complex&lt;X&gt; &amp;cx);</code></pre> 
Assigns new values to the contents. 
1) Assigns x to the real part of the complex number. Imaginary part is set to zero. 
2,3) Assigns cx.real() and cx.imag() to the real and the imaginary parts of the complex number respectively. 

<h2>Parameters</h2>

x - value to assign 
cx - complex value to assign

<h2>Return value</h2>

*this 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a complex number 
constructor <i>(public member function)</i> 
operator&quot;&quot;if 
operator&quot;&quot;i A std::complex literal representing pure imaginary number 
operator&quot;&quot;il <i>(function)</i> 
<i>(C++14)</i> 
