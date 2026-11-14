---
title: "stdlognormal_distributionms(3)"
name: "stdlognormal_distributionms"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlognormal_distributionms/"
description: "std::lognormal_distribution<RealType>::m,s – std::lognormal_distribution<RealType>::m,s"
---

<p>std::lognormal_distribution&lt;RealType&gt;::m,s &#8211; std::lognormal_distribution&lt;RealType&gt;::m,s</p>
<h2>Synopsis</h2>
<p>RealType m() const; <code>(1)</code> <i>(since C++11)</i><br />
RealType s() const; <code>(2)</code> <i>(since C++11)</i><br />
Returns the parameters the distribution was constructed with.<br />
1) Returns the log-mean m distribution parameter. It defines the location of the peak. The default value is 0.0.<br />
2) Returns the log-deviation s distribution parameter. The default value is 1.0. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1) The log-mean m distribution parameter.<br />
2) The log-deviation s distribution parameter. </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets or sets the distribution parameter object<br />
param <i>(public member function)</i> </p>
