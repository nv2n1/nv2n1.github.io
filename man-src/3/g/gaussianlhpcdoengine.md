---
title: "gaussianlhpcdoengine(3)"
name: "gaussianlhpcdoengine"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gaussianlhpcdoengine/"
description: "QuantLib::GaussianLHPCDOEngine –"
---

<p>QuantLib::GaussianLHPCDOEngine &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/syntheticcdoengines.hpp&gt; </p>
<p> Inherits CDOEngine. </p>
<h3>Public Member Functions</h3>
<p><code>GaussianLHPCDOEngine</code> (const <code>Handle</code>&lt; <code>OneFactorCopula</code> &gt; copula, <code>Period</code> stepSize=1 *Days) </p>
<h2>Detailed Description</h2>
<h3>template&lt;class CDOEngine&gt; class QuantLib::GaussianLHPCDOEngine&lt; CDOEngine &gt;</h3>
<p><code>CDO</code> engine with analytical expected tranche loss for a large homogeneous pool with Gaussian one-factor copula. See for example &#8216;The Normal Inverse Gaussian Distribution for Synthetic CDO pricing.&#8217;, Anna Kalemanova, Bernd Schmid, Ralf Werner, Journal of Derivatives, Vol. 14, No. 3, (Spring 2007), pp. 80-93. <a rel="nofollow" href="http://www.defaultrisk.com/pp_crdrv_91.htm">http://www.defaultrisk.com/pp_crdrv_91.htm</a> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
