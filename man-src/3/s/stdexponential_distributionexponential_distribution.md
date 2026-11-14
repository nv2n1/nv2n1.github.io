---
title: "stdexponential_distributionexponential_distribution(3)"
name: "stdexponential_distributionexponential_distribution"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexponential_distributionexponential_distribution/"
description: "std::exponential_distribution<RealType>::exponential_distribution – std::exponential_distribution<RealType>::exponential_distribution"
---

<p>std::exponential_distribution&lt;RealType&gt;::exponential_distribution &#8211; std::exponential_distribution&lt;RealType&gt;::exponential_distribution</p>
<h2>Synopsis</h2>
<p>exponential_distribution() : exponential_distribution(1.0) {} <code>(1)</code> <i>(since C++11)</i><br />
explicit exponential_distribution( RealType lambda ); <code>(2)</code> <i>(since C++11)</i><br />
explicit exponential_distribution( const param_type&amp; params ); <code>(3)</code> <i>(since C++11)</i><br />
Constructs a new distribution object. <code>(2)</code> uses lambda as the distribution parameter. <code>(3)</code> uses params as the distribution parameter. </p>
<h2>Parameters</h2>
<p>lambda &#8211; the λ distribution parameter (the rate parameter)<br />
params &#8211; the distribution parameter set</p>
<h2>Notes</h2>
<p>Requires that 0 &lt; lambda.<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
P0935R0 C++11 default constructor was explicit made implicit </p>
