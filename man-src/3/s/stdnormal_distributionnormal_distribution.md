---
title: "stdnormal_distributionnormal_distribution(3)"
name: "stdnormal_distributionnormal_distribution"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnormal_distributionnormal_distribution/"
description: "std::normal_distribution<RealType>::normal_distribution – std::normal_distribution<RealType>::normal_distribution"
---

<p>std::normal_distribution&lt;RealType&gt;::normal_distribution &#8211; std::normal_distribution&lt;RealType&gt;::normal_distribution</p>
<h2>Synopsis</h2>
<pre><code>normal_distribution()
    : normal_distribution(0.0){}(1)(since C++ 11)

          explicit normal_distribution(RealType mean, RealType stddev = 1.0);
(2)(since C++ 11)

    explicit normal_distribution(const param_type &amp;params);
(3)(since C++ 11)</code></pre>
<p>Constructs a new distribution object. <code>(2)</code> uses mean and stddev as the distribution parameters. <code>(3)</code> uses params as the distribution parameters. </p>
<h2>Parameters</h2>
<p>mean &#8211; the μ distribution parameter (mean)<br />
stddev &#8211; the σ distribution parameter (standard deviation)<br />
params &#8211; the distribution parameter set </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
P0935R0 C++11 default constructor was explicit made implicit</p>
