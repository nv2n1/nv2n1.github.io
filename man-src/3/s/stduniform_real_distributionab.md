---
title: "stduniform_real_distributionab(3)"
name: "stduniform_real_distributionab"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stduniform_real_distributionab/"
description: "std::uniform_real_distribution<RealType>::a,b – std::uniform_real_distribution<RealType>::a,b"
---

<p>std::uniform_real_distribution&lt;RealType&gt;::a,b &#8211; std::uniform_real_distribution&lt;RealType&gt;::a,b</p>
<h2>Synopsis</h2>
<p>result_type a() const; <code>(1)</code> <i>(since C++11)</i><br />
result_type b() const; <code>(2)</code> <i>(since C++11)</i><br />
Returns the parameters the distribution has been constructed with.<br />
1) Returns the a distribution parameter. It defines the minimum possibly generated value. The default value is 0.0.<br />
2) Returns the b distribution parameter. It defines the maximum possibly generated value. The default value is 1.0 </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1) The a distribution parameter.<br />
2) The b distribution parameter. </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets or sets the distribution parameter object<br />
param <i>(public member function)</i> </p>
