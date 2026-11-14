---
title: "stdfisher_f_distributionfisher_f_distribution(3)"
name: "stdfisher_f_distributionfisher_f_distribution"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfisher_f_distributionfisher_f_distribution/"
description: "std::fisher_f_distribution<RealType>::fisher_f_distribution – std::fisher_f_distribution<RealType>::fisher_f_distribution"
---

<p>std::fisher_f_distribution&lt;RealType&gt;::fisher_f_distribution &#8211; std::fisher_f_distribution&lt;RealType&gt;::fisher_f_distribution</p>
<h2>Synopsis</h2>
<pre><code>fisher_f_distribution()
    : fisher_f_distribution(1.0){}(1)(since C++ 11)

          explicit fisher_f_distribution(RealType m, RealType n = 1.0);
(2)(since C++ 11)

    explicit fisher_f_distribution(const param_type &amp;params);
(3)(since C++ 11)</code></pre>
<p>Constructs a new distribution object. <code>(2)</code> uses m and n as the distribution parameters. <code>(3)</code> uses params as the distribution parameters. </p>
<h2>Parameters</h2>
<p>m &#8211; the m distribution parameter (degrees of freedom)<br />
n &#8211; the n distribution parameter (degrees of freedom)<br />
params &#8211; the distribution parameter set </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
P0935R0 C++11 default constructor was explicit made implicit</p>
