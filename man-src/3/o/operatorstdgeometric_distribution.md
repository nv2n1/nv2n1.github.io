---
title: "operatorstdgeometric_distribution(3)"
name: "operatorstdgeometric_distribution"
section: "3"
letter: "o"
url: "/docs/linux/man/3-operatorstdgeometric_distribution/"
---

operator==,!=(std::geometric_distribution) - operator==,!=(std::geometric_distribution)

<h2>Synopsis</h2>

<pre><code>template &lt;class ResultType&gt;

bool operator==(const geometric_distribution&lt;ResultType&gt; &amp;lhs, (1)

                                                                   const geometric_distribution&lt;ResultType&gt; &amp;rhs);

template &lt;class ResultType&gt;

bool operator!=(const geometric_distribution&lt;ResultType&gt; &amp;lhs, (2)

                                                                   const geometric_distribution&lt;ResultType&gt; &amp;rhs);</code></pre> 
Compares two distribution objects. Two distribution objects are equal when parameter values and internal state is the same. 
1) Compares two distribution objects for equality. 
2) Compares two distribution objects for inequality. 

<h2>Parameters</h2>

lhs, rhs - distribution objects to compare

<h2>Return value</h2>

1) true if the distribution objects are equal, false otherwise 
2) true if the distribution objects are not equal, false otherwise 

<h2>Complexity</h2>

Constant.
