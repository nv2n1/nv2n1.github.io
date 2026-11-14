---
title: "stdnegative_binomial_distributionnegative_binomial_distribution(3)"
name: "stdnegative_binomial_distributionnegative_binomial_distribution"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnegative_binomial_distributionnegative_binomial_distribution/"
description: "std::negative_binomial_distribution<IntType>::negative_binomial_distribution – std::negative_binomial_distribution<IntType>::negative_binomial_distribution"
---

<p>std::negative_binomial_distribution&lt;IntType&gt;::negative_binomial_distribution &#8211; std::negative_binomial_distribution&lt;IntType&gt;::negative_binomial_distribution</p>
<h2>Synopsis</h2>
<pre><code>negative_binomial_distribution()
    : negative_binomial_distribution(1){}(1)(since C++ 11)

          explicit negative_binomial_distribution(IntType k, double p = 0.5);
(2)(since C++ 11)

    explicit negative_binomial_distribution(const param_type &amp;params);
(3)(since C++ 11)</code></pre>
<p>Constructs a new distribution object. <code>(2)</code> uses k and p as the distribution parameters. <code>(3)</code> uses params as the distribution parameters. </p>
<h2>Parameters</h2>
<p>k &#8211; the k distribution parameter (number of trial successes)<br />
p &#8211; the p distribution parameter (probability of a trial generating true)<br />
params &#8211; the distribution parameter set</p>
<h2>Notes</h2>
<p>Requires that 0 &lt; p ≤ 1 and 0 &lt; k.<br />
If p == 1, subsequent calls to the operator() overload that does not accept a param_type object will cause undefined behavior.<br />
The default-constructed std::negative_binomial_distribution is equivalent to the default-constructed std::geometric_distribution.<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
P0935R0 C++11 default constructor was explicit made implicit </p>
