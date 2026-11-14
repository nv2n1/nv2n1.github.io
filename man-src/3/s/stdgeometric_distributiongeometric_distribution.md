---
title: "stdgeometric_distributiongeometric_distribution(3)"
name: "stdgeometric_distributiongeometric_distribution"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdgeometric_distributiongeometric_distribution/"
description: "std::geometric_distribution<IntType>::geometric_distribution – std::geometric_distribution<IntType>::geometric_distribution"
---

<p>std::geometric_distribution&lt;IntType&gt;::geometric_distribution &#8211; std::geometric_distribution&lt;IntType&gt;::geometric_distribution</p>
<h2>Synopsis</h2>
<p>geometric_distribution() : geometric_distribution(0.5) {} <code>(1)</code> <i>(since C++11)</i><br />
explicit geometric_distribution( double p ); <code>(2)</code> <i>(since C++11)</i><br />
explicit geometric_distribution( const param_type&amp; params ); <code>(3)</code> <i>(since C++11)</i><br />
Constructs a new distribution object. <code>(2)</code> uses p as the distribution parameter. <code>(3)</code> uses params as the distribution parameter. </p>
<h2>Parameters</h2>
<p>p &#8211; the p distribution parameter (probability of a trial generating true)<br />
params &#8211; the distribution parameter set</p>
<h2>Notes</h2>
<p>Requires that 0 &lt; p &lt; 1<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
P0935R0 C++11 default constructor was explicit made implicit </p>
