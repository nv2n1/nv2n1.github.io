---
title: "quantlib_bivariatecumulativenormaldistributionwe04dp(3)"
name: "quantlib_bivariatecumulativenormaldistributionwe04dp"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_bivariatecumulativenormaldistributionwe04dp/"
description: "QuantLib::BivariateCumulativeNormalDistributionWe04DP – Cumulative bivariate normal distibution function (West 2004)."
---

<p>QuantLib::BivariateCumulativeNormalDistributionWe04DP &#8211; Cumulative bivariate normal distibution function (West 2004). </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/distributions/bivariatenormaldistribution.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>BivariateCumulativeNormalDistributionWe04DP</code> (<code>Real</code> rho) </p>
<p> <code>Real</code> <code>operator()</code> (<code>Real</code> a, <code>Real</code> b) const </p>
<h2>Detailed Description</h2>
<p>Cumulative bivariate normal distibution function (West 2004). </p>
<p> The implementation derives from the article &#8216;Better Approximations To Cumulative Normal Distibutions&#8217;, Graeme West, Dec 2004 available at <a rel="nofollow" href="http://www.finmod.co.za">www.finmod.co.za</a>. Also available in Wilmott Magazine, 2005, (May), 70-76, The main code is a port of the C++ code at <a href="http://www.finmod.co.za">www.finmod.co.za</a>/cumfunctions.zip. </p>
<p> The algorithm is based on the near double-precision algorithm described in &#8216;Numerical Computation of Rectangular Bivariate an Trivariate Normal and t Probabilities&#8217;, Genz (2004), Statistics and Computing 14, 151-160. (available at <a rel="nofollow" href="http://www.sci.wsu.edu">www.sci.wsu.edu</a>/math/faculty/henz/homepage) </p>
<p> The QuantLib implementation mainly differs from the original code in two regards;</p>
<dl COMPACT>
<dt>*</p>
<dd>The implementation of the cumulative normal distribution is <code>QuantLib::CumulativeNormalDistribution</code></p>
<dt>*</p>
<dd>The arrays XX and W are zero-based</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by checking it against known good results.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
