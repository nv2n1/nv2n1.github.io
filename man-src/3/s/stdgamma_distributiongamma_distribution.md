---
title: "stdgamma_distributiongamma_distribution(3)"
name: "stdgamma_distributiongamma_distribution"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdgamma_distributiongamma_distribution/"
description: "std::gamma_distribution<RealType>::gamma_distribution – std::gamma_distribution<RealType>::gamma_distribution"
---

<p>std::gamma_distribution&lt;RealType&gt;::gamma_distribution &#8211; std::gamma_distribution&lt;RealType&gt;::gamma_distribution</p>
<h2>Synopsis</h2>
<pre><code>gamma_distribution()
    : gamma_distribution(1.0){}(1)(since C++ 11)

          explicit gamma_distribution(RealType alpha, RealType beta = 1.0);
(2)(since C++ 11)

    explicit gamma_distribution(const param_type &amp;params);
(3)(since C++ 11)</code></pre>
<p>Constructs a new distribution object. <code>(2)</code> uses alpha and beta as the distribution parameters. <code>(3)</code> uses params as the distribution parameters. </p>
<h2>Parameters</h2>
<p>alpha &#8211; the α distribution parameter (shape)<br />
beta &#8211; the β distribution parameter (scale)<br />
params &#8211; the distribution parameter set </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
P0935R0 C++11 default constructor was explicit made implicit</p>
