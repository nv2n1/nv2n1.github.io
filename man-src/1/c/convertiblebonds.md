---
title: "convertiblebonds(1)"
name: "convertiblebonds"
section: "1"
letter: "c"
url: "/docs/linux/man/1-convertiblebonds/"
description: "ConvertibleBonds – Example of using QuantLib to value convertible bonds"
---

<p>ConvertibleBonds &#8211; Example of using QuantLib to value convertible bonds</p>
<h2>Synopsis</h2>
<p><code>ConvertibleBonds</code></p>
<h2>Description</h2>
<p><code>ConvertibleBonds</code> is an example of using <i>QuantLib</i>. </p>
<p> For a given set of option parameters, it computes the value of a convertible bond with an embedded put option for two different equity options types (with european and american exercise features) using the Tsiveriotis-Fernandes method with different implied tree algorithms. </p>
<p> The tree types are Jarrow-Rudd, Cox-Ross-Rubinstein, Additive equiprobabilities, Trigeorgis, Tian and Leisen-Reimer. </p>
<h2>See Also</h2>
<p>The source code <i>ConvertibleBonds.cpp</i>, <code><a href="/docs/linux/man/1-bermudanswaption/">BermudanSwaption</a></code>(1), <code><a href="/docs/linux/man/1-discretehedging/">DiscreteHedging</a></code>(1), <code><a href="/docs/linux/man/1-equityoption/">EquityOption</a></code>(1), <code><a href="/docs/linux/man/1-fra/">FRA</a></code>(1), <code><a href="/docs/linux/man/1-replication/">Replication</a></code>(1), <code><a href="/docs/linux/man/1-repo/">Repo</a></code>(1), <code><a href="/docs/linux/man/1-swapvaluation/">SwapValuation</a></code>(1), the QuantLib documentation and website at <i><a rel="nofollow" href="http://quantlib.org">http://quantlib.org</a></i>. </p>
<h2>Authors</h2>
<p>The QuantLib Group (see <i>Authors.txt</i>). </p>
<p> This manual page was added by Dirk Eddelbuettel &lt;edd [at] debian.org&gt;, the Debian GNU/Linux maintainer for <code>QuantLib</code>.</p>
