---
title: "stduniform_real_distributionuniform_real_distribution(3)"
name: "stduniform_real_distributionuniform_real_distribution"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stduniform_real_distributionuniform_real_distribution/"
description: "std::uniform_real_distribution<RealType>::uniform_real_distribution – std::uniform_real_distribution<RealType>::uniform_real_distribution"
---

<p>std::uniform_real_distribution&lt;RealType&gt;::uniform_real_distribution &#8211; std::uniform_real_distribution&lt;RealType&gt;::uniform_real_distribution</p>
<h2>Synopsis</h2>
<pre><code>uniform_real_distribution()
    : uniform_real_distribution(0.0){}(1)(since C++ 11)

          explicit uniform_real_distribution(RealType a, RealType b = 1.0);
(1)(since C++ 11)

    explicit uniform_real_distribution(const param_type &amp;params);
(2)(since C++ 11)</code></pre>
<p>Constructs a new distribution object. <code>(2)</code> uses a and b as the distribution parameters, <code>(3)</code> uses params as the distribution parameters. </p>
<h2>Parameters</h2>
<p>a &#8211; the a distribution parameter (minimum value)<br />
b &#8211; the b distribution parameter (maximum value)<br />
params &#8211; the distribution parameter set</p>
<h2>Notes</h2>
<p>Requires that a ≤ b and b-a ≤ std::numeric_limits&lt;RealType&gt;::max()<br />
If a == b, subsequent calls to the operator() overload that does not accept a param_type object will cause undefined behavior.<br />
To create a distribution over the closed interval [a,b], std::nextafter(b, std::numeric_limits&lt;RealType&gt;::max()) may be used as the second parameter.<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
P0935R0 C++11 default constructor was explicit made implicit </p>
