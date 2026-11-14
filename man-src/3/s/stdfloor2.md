---
title: "stdfloor2(3)"
name: "stdfloor2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfloor2/"
---

std::floor2 - std::floor2

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;bit&gt;

template&lt; class T &gt;                (since C++20)

constexpr T floor2(T x) noexcept;</code></pre> 
If x is not zero, calculates the largest integral power of two that is not greater than x. If x is zero, returns zero. 
This overload only participates in overload resolution if T is an unsigned integer type (that is, unsigned char, unsigned short, unsigned int, unsigned long, unsigned long long, or an extended unsigned integer type). 

<h2>Return value</h2>

Zero if x is zero; otherwise, the largest integral power of two that is not greater than x. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
