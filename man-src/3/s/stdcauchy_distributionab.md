---
title: "stdcauchy_distributionab(3)"
name: "stdcauchy_distributionab"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcauchy_distributionab/"
description: "std::cauchy_distribution<RealType>::a,b – std::cauchy_distribution<RealType>::a,b"
---

<p>std::cauchy_distribution&lt;RealType&gt;::a,b &#8211; std::cauchy_distribution&lt;RealType&gt;::a,b</p>
<h2>Synopsis</h2>
<p>RealType a() const; <code>(1)</code> <i>(since C++11)</i><br />
RealType b() const; <code>(2)</code> <i>(since C++11)</i><br />
Returns the distribution parameters with which the distribution was constructed.<br />
1) Returns the a parameter. It specifies the location of the peak and is also called location parameter. The default value is 0.0.<br />
2) Returns the b parameter. It represents the half-width at half-maximum (HWHM) and is also called scale parameter. The default value is 1.0. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1) The value of the a parameter.<br />
2) The value of the b parameter. </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets or sets the distribution parameter object<br />
param <i>(public member function)</i> </p>
<h2>External links</h2>
<p>* Scale_parameter. From Wikipedia.<br />
* Location_parameter. From Wikipedia.</p>
