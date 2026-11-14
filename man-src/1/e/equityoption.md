---
title: "equityoption(1)"
name: "equityoption"
section: "1"
letter: "e"
url: "/docs/linux/man/1-equityoption/"
description: "EquityOption – Example of using QuantLib to value equity options"
---

<p>EquityOption &#8211; Example of using QuantLib to value equity options</p>
<h2>Synopsis</h2>
<p><code>EquityOption</code></p>
<h2>Description</h2>
<p><code>EquityOption</code> is an example of using <i>QuantLib</i>. </p>
<p> For a given set of option parameters, it computes the value of three different equity options types (with european, bermudan and american exercise features) using different valuation algorithms. </p>
<p> The calculation methods are Black-Scholes (for european options only), Barone-Adesi/Whaley (american-only), Bjerksund/Stensland (american), Integral (european), Finite differences, Binomial Jarrow-Rudd, Binomial Cox-Ross-Rubinstein, Additive equiprobabilities, Binomial Trigeorgis, Binomial Tian, Binomial Leisen-Reimer, crude Monte Carlo (european-only) and Sobol-sequence Monte Carlo (european-only). </p>
<h2>See Also</h2>
<p>The source code <i>EquityOption.cpp</i>, <code><a href="/docs/linux/man/1-bermudanswaption/">BermudanSwaption</a></code>(1), <code><a href="/docs/linux/man/1-convertiblebonds/">ConvertibleBonds</a></code>(1), <code><a href="/docs/linux/man/1-discretehedging/">DiscreteHedging</a></code>(1), <code><a href="/docs/linux/man/1-fra/">FRA</a></code>(1), <code><a href="/docs/linux/man/1-replication/">Replication</a></code>(1), <code><a href="/docs/linux/man/1-repo/">Repo</a></code>(1), <code><a href="/docs/linux/man/1-swapvaluation/">SwapValuation</a></code>(1), the QuantLib documentation and website at <i><a rel="nofollow" href="http://quantlib.org">http://quantlib.org</a></i>. </p>
<h2>Authors</h2>
<p>The QuantLib Group (see <i>Authors.txt</i>). </p>
<p> This manual page was added by Dirk Eddelbuettel &lt;edd [at] debian.org&gt;, the Debian GNU/Linux maintainer for <code>QuantLib</code>.</p>
