---
title: "stdextreme_value_distributionreset(3)"
name: "stdextreme_value_distributionreset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdextreme_value_distributionreset/"
---

std::extreme_value_distribution&lt;RealType&gt;::reset - std::extreme_value_distribution&lt;RealType&gt;::reset

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
