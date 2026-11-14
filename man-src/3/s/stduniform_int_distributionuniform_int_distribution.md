---
title: "stduniform_int_distributionuniform_int_distribution(3)"
name: "stduniform_int_distributionuniform_int_distribution"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stduniform_int_distributionuniform_int_distribution/"
description: "std::uniform_int_distribution<IntType>::uniform_int_distribution – std::uniform_int_distribution<IntType>::uniform_int_distribution"
---

<p>std::uniform_int_distribution&lt;IntType&gt;::uniform_int_distribution &#8211; std::uniform_int_distribution&lt;IntType&gt;::uniform_int_distribution</p>
<h2>Synopsis</h2>
<pre><code>uniform_int_distribution()
    : uniform_int_distribution(0){}(1)(since C++ 11)

          explicit uniform_int_distribution(IntType a, (2)(since C++ 11)

                                                           IntType b = std::numeric_limits&lt;IntType&gt;::max());

explicit uniform_int_distribution(const param_type &amp;params);
(3)(since C++ 11)</code></pre>
<p>Constructs new distribution object. <code>(2)</code> uses a and b as the distribution parameters, <code>(3)</code> uses params as the distribution parameters.<br />
The behavior is undefined if a&gt;b. </p>
<h2>Parameters</h2>
<p>a &#8211; the a distribution parameter (minimum value)<br />
b &#8211; the b distribution parameter (maximum value)<br />
params &#8211; the distribution parameter set </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
P0935R0 C++11 default constructor was explicit made implicit</p>
