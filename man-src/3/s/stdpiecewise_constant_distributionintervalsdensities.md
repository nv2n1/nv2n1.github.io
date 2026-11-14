---
title: "stdpiecewise_constant_distributionintervalsdensities(3)"
name: "stdpiecewise_constant_distributionintervalsdensities"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpiecewise_constant_distributionintervalsdensities/"
description: "std::piecewise_constant_distribution<RealType>::intervals,densities – std::piecewise_constant_distribution<RealType>::intervals,densities"
---

<p>std::piecewise_constant_distribution&lt;RealType&gt;::intervals,densities &#8211; std::piecewise_constant_distribution&lt;RealType&gt;::intervals,densities</p>
<h2>Synopsis</h2>
<p>std::vector&lt;RealType&gt; intervals() const; <code>(1)</code> <i>(since C++11)</i><br />
std::vector&lt;RealType&gt; densities() const; <code>(2)</code> <i>(since C++11)</i><br />
Returns the distribution parameters.<br />
1) Returns the list of boundaries of the intervals.<br />
2) Returns the list of probability densities of the intervals. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>The distribution parameters:<br />
1) The list of boundaries of the intervals.<br />
2) The list of probability densities of the intervals. </p>
<h2>Complexity</h2>
<p>Constant.</p>
