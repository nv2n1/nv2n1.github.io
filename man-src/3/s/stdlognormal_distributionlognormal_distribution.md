---
title: "stdlognormal_distributionlognormal_distribution(3)"
name: "stdlognormal_distributionlognormal_distribution"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlognormal_distributionlognormal_distribution/"
description: "std::lognormal_distribution<RealType>::lognormal_distribution – std::lognormal_distribution<RealType>::lognormal_distribution"
---

<p>std::lognormal_distribution&lt;RealType&gt;::lognormal_distribution &#8211; std::lognormal_distribution&lt;RealType&gt;::lognormal_distribution</p>
<h2>Synopsis</h2>
<pre><code>lognormal_distribution()
    : lognormal_distribution(0.0){}(1)(since C++ 11)

          explicit lognormal_distribution(RealType m, RealType s = 1.0);
(2)(since C++ 11)

    explicit lognormal_distribution(const param_type &amp;params);
(3)(since C++ 11)</code></pre>
<p>Constructs a new distribution object. <code>(2)</code> uses m and s as the distribution parameters. <code>(3)</code> uses params as the distribution parameters. </p>
<h2>Parameters</h2>
<p>m &#8211; the m distribution parameter (log-scale)<br />
s &#8211; the s distribution parameter (shape)<br />
params &#8211; the distribution parameter set </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
P0935R0 C++11 default constructor was explicit made implicit</p>
