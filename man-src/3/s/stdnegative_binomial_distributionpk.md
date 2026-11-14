---
title: "stdnegative_binomial_distributionpk(3)"
name: "stdnegative_binomial_distributionpk"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnegative_binomial_distributionpk/"
---

std::negative_binomial_distribution&lt;IntType&gt;::p,k - std::negative_binomial_distribution&lt;IntType&gt;::p,k

<h2>Synopsis</h2>

<pre><code>double p() const;
(1)(since C++ 11)

    IntType k() const;
(2)(since C++ 11)</code></pre> 
Returns the parameters the distribution was constructed with. 
1) Returns the p distribution parameter. It defines the probability of a trial generating true. The default value is 0.5. 
2) Returns the k distribution parameter. It defines the number of desired outcomes. The default value is 1. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

1) The p distribution parameter. 
2) The k distribution parameter. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets or sets the distribution parameter object 
param <i>(public member function)</i> 
