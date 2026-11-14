---
title: "stdbinomial_distributionreset(3)"
name: "stdbinomial_distributionreset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbinomial_distributionreset/"
---

std::binomial_distribution&lt;IntType&gt;::reset - std::binomial_distribution&lt;IntType&gt;::reset

<h2>Synopsis</h2>

<pre><code>void reset();
(since C++ 11)</code></pre> 
Resets the internal state of the distribution object. After a call to this function, the next call to operator() on the distribution object will not be dependent on previous calls to operator(). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

Constant.
