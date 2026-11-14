---
title: "stdweibull_distributionweibull_distribution(3)"
name: "stdweibull_distributionweibull_distribution"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdweibull_distributionweibull_distribution/"
description: "std::weibull_distribution<RealType>::weibull_distribution – std::weibull_distribution<RealType>::weibull_distribution"
---

<p>std::weibull_distribution&lt;RealType&gt;::weibull_distribution &#8211; std::weibull_distribution&lt;RealType&gt;::weibull_distribution</p>
<h2>Synopsis</h2>
<pre><code>weibull_distribution()
    : weibull_distribution(1.0){}(1)(since C++ 11)

          explicit weibull_distribution(RealType a, RealType b = 1.0);
(2)(since C++ 11)

    explicit weibull_distribution(const param_type &amp;params);
(3)(since C++ 11)</code></pre>
<p>Constructs a new distribution object. <code>(2)</code> uses a and b as the distribution parameters. <code>(3)</code> uses params as the distribution parameters. </p>
<h2>Parameters</h2>
<p>a &#8211; the a distribution parameter (shape)<br />
b &#8211; the b distribution parameter (scale)<br />
params &#8211; the distribution parameter set </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
P0935R0 C++11 default constructor was explicit made implicit</p>
