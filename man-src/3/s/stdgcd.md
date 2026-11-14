---
title: "stdgcd(3)"
name: "stdgcd"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdgcd/"
---

std::gcd - std::gcd

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;numeric&gt;

template&lt; class M, class N&gt;                        (since C++17)

constexpr std::common_type_t&lt;M, N&gt; gcd(M m, N n);</code></pre> 
Computes the greatest common divisor of the integers m and n. 

<h2>Parameters</h2>

m, n - integer values

<h2>Return value</h2>

If both m and n are zero, returns zero. Otherwise, returns the greatest common divisor of |m| and |n|. 
Remarks 
If either M or N is not an integer type, or if either is (possibly cv-qualified) bool, the program is ill-formed. 
If either |m| or |n| is not representable as a value of type std::common_type_t&lt;M, N&gt;, the behavior is undefined. 

<h2>Exceptions</h2>

Throws no exceptions.

<h2>See also</h2>

lcm constexpr function template returning the least common multiple of two integers 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
