---
title: "stdexperimentallcm(3)"
name: "stdexperimentallcm"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentallcm/"
---

std::experimental::lcm - std::experimental::lcm

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/numeric&gt;

template&lt; class M, class N&gt;                        (library fundamentals TS v2)

constexpr std::common_type_t&lt;M, N&gt; lcm(M m, N n);</code></pre> 
Computes the least common multiple of the integers m and n. 

<h2>Parameters</h2>

m, n - integer values

<h2>Return value</h2>

If either m or n is zero, returns zero. Otherwise, return the least common multiple of |m| and |n|. 
Remarks 
If either M or N is not an integer type, or if either is (possibly cv-qualified) bool, the program is ill-formed. 
The behavior is undefined if |m|, |n| or the least common multiple of |m| and |n| is not representable as a value of type std::common_type_t&lt;M,N&gt;. 

<h2>Exceptions</h2>

Throws no exceptions.

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constexpr function template returning the greatest common divisor of two integers 
gcd <i>(function template)</i> 
