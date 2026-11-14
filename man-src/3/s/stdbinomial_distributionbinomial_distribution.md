---
title: "stdbinomial_distributionbinomial_distribution(3)"
name: "stdbinomial_distributionbinomial_distribution"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbinomial_distributionbinomial_distribution/"
description: "std::binomial_distribution<IntType>::binomial_distribution – std::binomial_distribution<IntType>::binomial_distribution"
---

<p>std::binomial_distribution&lt;IntType&gt;::binomial_distribution &#8211; std::binomial_distribution&lt;IntType&gt;::binomial_distribution</p>
<h2>Synopsis</h2>
<pre><code>binomial_distribution()
    : binomial_distribution(1){}(1)(since C++ 11)

          explicit binomial_distribution(IntType t, double p = 0.5);
(2)(since C++ 11)

    explicit binomial_distribution(const param_type &amp;params);
(3)(since C++ 11)</code></pre>
<p>Constructs a new distribution object. <code>(2)</code> uses t and p as the distribution parameters. <code>(3)</code> uses params as the distribution parameters. </p>
<h2>Parameters</h2>
<p>t &#8211; the t distribution parameter (number of trials)<br />
p &#8211; the p distribution parameter (probability of a trial generating true)<br />
params &#8211; the distribution parameter set</p>
<h2>Notes</h2>
<p>Requires that 0 ≤ p ≤ 1 and 0 ≤ t.<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
P0935R0 C++11 default constructor was explicit made implicit </p>
