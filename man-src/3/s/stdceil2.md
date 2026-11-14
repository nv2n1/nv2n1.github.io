---
title: "stdceil2(3)"
name: "stdceil2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdceil2/"
---

std::ceil2 - std::ceil2

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;bit&gt;

template&lt; class T &gt;               (since C++20)

constexpr T ceil2(T x) noexcept;</code></pre> 
Calculates the smallest integral power of two that is not smaller than x. If that value is not representable in T, the result is unspecified. 
This overload only participates in overload resolution if T is an unsigned integer type (that is, unsigned char, unsigned short, unsigned int, unsigned long, unsigned long long, or an extended unsigned integer type). 

<h2>Return value</h2>

The smallest integral power of two that is not smaller than x, or an unspecified value if the result cannot be represented in T. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
