---
title: "remainingbasket_(3)"
name: "remainingbasket_"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remainingbasket_/"
description: "QuantLib::SyntheticCDO::engine – CDO base engine."
---

<p>QuantLib::SyntheticCDO::engine &#8211; <code>CDO</code> base <code>engine</code>. </p>
<h2>Synopsis</h2>
<pre><code>virtual Real expectedTrancheLoss (const Date &amp;) const =0



virtual void initialize () const



Protected Attributes</code></pre>
<p> Inherits <code>GenericEngine&lt; SyntheticCDO::arguments, SyntheticCDO::results &gt;</code>. Inherited by <code>IntegralCDOEngine</code>, <code>MidPointCDOEngine</code>, and <code>MonteCarloCDOEngine2</code>.</p>
<h3>Protected Member Functions</h3>
<pre><code>virtual Real expectedTrancheLoss (const Date &amp;) const =0



virtual void initialize () const



Protected Attributes</code></pre>
<p> boost::shared_ptr&lt; <code>Basket</code> &gt; <code>remainingBasket_</code></p>
<h2>Detailed Description</h2>
<p><code>CDO</code> base <code>engine</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
