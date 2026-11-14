---
title: "stdbinomial_distributionpt(3)"
name: "stdbinomial_distributionpt"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbinomial_distributionpt/"
---

std::binomial_distribution&lt;IntType&gt;::p,t - std::binomial_distribution&lt;IntType&gt;::p,t

<h2>Synopsis</h2>

<pre><code>double p() const;
(1)(since C++ 11)

    IntType t() const;
(2)(since C++ 11)</code></pre> 
Returns the parameters the distribution was constructed with. 
1) Returns the p distribution parameter. It defines the probability of a trial generating true. The default value is 0.5. 
2) Returns the t distribution parameter. It identifies the number of trials. The default value is 1. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

1) The p distribution parameter. 
2) The t distribution parameter. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets or sets the distribution parameter object 
param <i>(public member function)</i> 
