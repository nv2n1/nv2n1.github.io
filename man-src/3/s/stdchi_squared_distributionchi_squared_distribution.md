---
title: "stdchi_squared_distributionchi_squared_distribution(3)"
name: "stdchi_squared_distributionchi_squared_distribution"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchi_squared_distributionchi_squared_distribution/"
description: "std::chi_squared_distribution<RealType>::chi_squared_distribution – std::chi_squared_distribution<RealType>::chi_squared_distribution"
---

<p>std::chi_squared_distribution&lt;RealType&gt;::chi_squared_distribution &#8211; std::chi_squared_distribution&lt;RealType&gt;::chi_squared_distribution</p>
<h2>Synopsis</h2>
<p>chi_squared_distribution() : chi_squared_distribution(1.0) {} <code>(1)</code> <i>(since C++11)</i><br />
explicit chi_squared_distribution( RealType n ); <code>(2)</code> <i>(since C++11)</i><br />
explicit chi_squared_distribution( const param_type&amp; params ); <code>(3)</code> <i>(since C++11)</i><br />
Constructs a new distribution object. <code>(2)</code> uses n as the distribution parameter. <code>(3)</code> uses params as the distribution parameter. </p>
<h2>Parameters</h2>
<p>n &#8211; the n distribution parameter (degrees of freedom)<br />
params &#8211; the distribution parameter set </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
P0935R0 C++11 default constructor was explicit made implicit</p>
