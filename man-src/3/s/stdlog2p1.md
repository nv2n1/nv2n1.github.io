---
title: "stdlog2p1(3)"
name: "stdlog2p1"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlog2p1/"
---

std::log2p1 - std::log2p1

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;bit&gt;

template&lt; class T &gt;                (since C++20)

constexpr T log2p1(T x) noexcept;</code></pre> 
If x is not zero, calculates the number of bits needed to store the value x, that is, \(1 + \lfloor log_2(x) \rfloor\)1 + floor(log 
2(x)). If x is zero, returns zero. 
This overload only participates in overload resolution if T is an unsigned integer type (that is, unsigned char, unsigned short, unsigned int, unsigned long, unsigned long long, or an extended unsigned integer type). 

<h2>Return value</h2>

Zero if x is zero; otherwise, one plus the base-2 logarithm of x, with any fractional part discarded. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
