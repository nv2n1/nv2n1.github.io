---
title: "fittedbondcurve(1)"
name: "fittedbondcurve"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fittedbondcurve/"
description: "FittedBondCurve – Example of using QuantLib to fit discount curves"
---

<p>FittedBondCurve &#8211; Example of using QuantLib to fit discount curves</p>
<h2>Synopsis</h2>
<p><code>FittedBondCurve</code></p>
<h2>Description</h2>
<p><code>FittedBondCurve</code> is an example of using <i>QuantLib</i>. </p>
<p> For a given set of coupons and terms to maturity, it computes the value of a bond by fitting the yields to a curve using different methods. </p>
<p> The fitting methods are exponential splines, simple polynomials, Nelson-Siegel, and cubic B-splines. It then shifts the evaluation date into the future to compute implied forward par rates. It also computes yields after small price shifts. </p>
<h2>See Also</h2>
<p>The source code <i>FittedBondCurve.cpp</i>, <code><a href="/docs/linux/man/1-bermudanswaption/">BermudanSwaption</a></code>(1), <code><a href="/docs/linux/man/1-equityoption/">EquityOption</a></code>(1), <code><a href="/docs/linux/man/1-discretehedging/">DiscreteHedging</a></code>(1), <code><a href="/docs/linux/man/1-swapvaluation/">SwapValuation</a></code>(1), the QuantLib documentation and website at <i><a rel="nofollow" href="http://quantlib.org">http://quantlib.org</a></i>. </p>
<h2>Authors</h2>
<p>The QuantLib Group (see <i>Authors.txt</i>). </p>
<p> This manual page was added by Dirk Eddelbuettel &lt;edd [at] debian.org&gt;, the Debian GNU/Linux maintainer for <code>QuantLib</code>.</p>
