---
title: "quantlib_syntheticcdo_engine(3)"
name: "quantlib_syntheticcdo_engine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_syntheticcdo_engine/"
description: "QuantLib::SyntheticCDO::engine – CDO base engine."
---

<p>QuantLib::SyntheticCDO::engine &#8211; <code>CDO</code> base <code>engine</code>. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/syntheticcdoengines.hpp&gt; </p>
<p> Inherits <code>GenericEngine&lt; SyntheticCDO::arguments, SyntheticCDO::results &gt;</code>. </p>
<p> Inherited by <code>IntegralCDOEngine</code>, <code>MidPointCDOEngine</code>, and <code>MonteCarloCDOEngine2</code>. </p>
<h3>Protected Member Functions</h3>
<p>virtual <code>Real</code> <code>expectedTrancheLoss</code> (const <code>Date</code> &amp;) const =0 </p>
<p> virtual void <code>initialize</code> () const </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>Basket</code> &gt; <code>remainingBasket_</code> </p>
<h2>Detailed Description</h2>
<p><code>CDO</code> base <code>engine</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
