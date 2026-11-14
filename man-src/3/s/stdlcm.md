---
title: "stdlcm(3)"
name: "stdlcm"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlcm/"
---

std::lcm - std::lcm

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;numeric&gt;

template&lt; class M, class N&gt;                        (since C++17)

constexpr std::common_type_t&lt;M, N&gt; lcm(M m, N n);</code></pre> 
Computes the least common multiple of the integers m and n. 

<h2>Parameters</h2>

m, n - integer values

<h2>Return value</h2>

If either m or n is zero, returns zero. Otherwise, returns the least common multiple of |m| and |n|. 
Remarks 
If either M or N is not an integer type, or if either is (possibly cv-qualified) bool, the program is ill-formed. 
The behavior is undefined if |m|, |n|, or the least common multiple of |m| and |n| is not representable as a value of type std::common_type_t&lt;M, N&gt;. 

<h2>Exceptions</h2>

Throws no exceptions.

<h2>See also</h2>

gcd constexpr function template returning the greatest common divisor of two integers 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
