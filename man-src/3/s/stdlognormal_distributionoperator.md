---
title: "stdlognormal_distributionoperator(3)"
name: "stdlognormal_distributionoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlognormal_distributionoperator/"
---

std::lognormal_distribution&lt;RealType&gt;::operator() - std::lognormal_distribution&lt;RealType&gt;::operator()

<h2>Synopsis</h2>

<pre><code>template &lt;class Generator&gt;
(1)(since C++ 11)

    result_type
    operator()(Generator &amp;g);

template &lt;class Generator&gt;
(2)(since C++ 11)

    result_type
    operator()(Generator &amp;g, const param_type &amp;params);</code></pre> 
Generates random numbers that are distributed according to the associated probability function. The entropy is acquired by calling g.operator(). 
The first version uses the associated parameter set, the second version uses params. The associated parameter set is not modified. 

<h2>Parameters</h2>

g - an uniform random bit generator object 
params - distribution parameter set to use instead of the associated one

<h2>Type requirements</h2>

- 
Generator must meet the requirements of UniformRandomBitGenerator.

<h2>Return value</h2>

The generated random number. 

<h2>Complexity</h2>

Amortized constant number of invocations of g.operator().
