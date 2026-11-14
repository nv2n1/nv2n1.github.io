---
title: "stdbernoulli_distributionbernoulli_distribution(3)"
name: "stdbernoulli_distributionbernoulli_distribution"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbernoulli_distributionbernoulli_distribution/"
description: "std::bernoulli_distribution::bernoulli_distribution – std::bernoulli_distribution::bernoulli_distribution"
---

<p>std::bernoulli_distribution::bernoulli_distribution &#8211; std::bernoulli_distribution::bernoulli_distribution</p>
<h2>Synopsis</h2>
<p>bernoulli_distribution() : bernoulli_distribution(0.5) { } <code>(1)</code> <i>(since C++11)</i><br />
explicit bernoulli_distribution( double p ); <code>(2)</code> <i>(since C++11)</i><br />
explicit bernoulli_distribution( const param_type&amp; params ); <code>(3)</code> <i>(since C++11)</i><br />
Constructs new distribution object. <code>(2)</code> uses p as the distribution parameter. <code>(3)</code> uses params as the distribution parameter. </p>
<h2>Parameters</h2>
<p>p &#8211; the p distribution parameter (probability of generating true)<br />
params &#8211; the distribution parameter set </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
P0935R0 C++11 default constructor was explicit made implicit</p>
