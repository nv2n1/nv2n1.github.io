---
title: "bivariatecumulativenormaldistributiondr78(3)"
name: "bivariatecumulativenormaldistributiondr78"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bivariatecumulativenormaldistributiondr78/"
description: "QuantLib::BivariateCumulativeNormalDistributionDr78 – Cumulative bivariate normal distribution function."
---

<p>QuantLib::BivariateCumulativeNormalDistributionDr78 &#8211; Cumulative bivariate normal distribution function. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/distributions/bivariatenormaldistribution.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>BivariateCumulativeNormalDistributionDr78</code> (Real rho) </p>
<p> Real <code>operator()</code> (Real a, Real b) const </p>
<h2>Detailed Description</h2>
<p>Cumulative bivariate normal distribution function. </p>
<p> Drezner (1978) algorithm, six decimal places accuracy. </p>
<p> For this implementation see &#8216;Option pricing formulas&#8217;, E.G. Haug, McGraw-Hill 1998 </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>check accuracy of this algorithm and compare with: 1) Drezner, Z, (1978), Computation of the bivariate normal integral, Mathematics of Computation 32, pp. 277-279. 2) Drezner, Z. and Wesolowsky, G. O. (1990) `On the Computation of the Bivariate Normal Integral&#8217;, Journal of Statistical Computation and Simulation 35, pp. 101-107. 3) Drezner, Z (1992) Computation of the Multivariate Normal Integral, ACM Transactions on Mathematics Software 18, pp. 450-460. 4) Drezner, Z (1994) Computation of the Trivariate Normal Integral, Mathematics of Computation 62, pp. 289-294. 5) Genz, A. (1992) `Numerical Computation of the Multivariate Normal Probabilities&#8217;, J. Comput. Graph. Stat. 1, pp. 141-150.</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by checking it against known good results.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
