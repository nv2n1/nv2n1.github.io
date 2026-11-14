---
title: "stdweibull_distributionab(3)"
name: "stdweibull_distributionab"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdweibull_distributionab/"
---

std::weibull_distribution&lt;RealType&gt;::a,b - std::weibull_distribution&lt;RealType&gt;::a,b

<h2>Synopsis</h2>

RealType a() const; <b>(1)</b> <i>(since C++11)</i> 
RealType b() const; <b>(2)</b> <i>(since C++11)</i> 
Returns the parameters the distribution was constructed with. 
1) Returns the a parameter. It defines the shape of the distribution. The default value is 1.0. 
2) Returns the b parameter. It defines the scale of the distribution. The default value is 1.0. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

1) The value of the a parameter. 
2) The value of the b parameter. 

<h2>Complexity</h2>

Constant.

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets or sets the distribution parameter object 
param <i>(public member function)</i> 
