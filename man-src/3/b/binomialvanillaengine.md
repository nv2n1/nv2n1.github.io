---
title: "binomialvanillaengine(3)"
name: "binomialvanillaengine"
section: "3"
letter: "b"
url: "/docs/linux/man/3-binomialvanillaengine/"
description: "QuantLib::BinomialVanillaEngine – Pricing engine for vanilla options using binomial trees."
---

<p>QuantLib::BinomialVanillaEngine &#8211; Pricing engine for vanilla options using binomial trees. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/binomialengine.hpp&gt; </p>
<p> Inherits QuantLib::OneAssetOption::engine. </p>
<h3>Public Member Functions</h3>
<p><code>BinomialVanillaEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, Size timeSteps) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class QuantLib::BinomialVanillaEngine&lt; T &gt;</h3>
<p>Pricing engine for vanilla options using binomial trees. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned values is tested by checking it against analytic results.</dl>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd><code>Greeks</code> are not overly accurate. They could be improved by building a tree so that it has three points at the current time. The value would be fetched from the middle one, while the two side points would be used for estimating partial derivatives.</dl>
<p> <code>Examples: </code> </p>
<p> <code>EquityOption.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
