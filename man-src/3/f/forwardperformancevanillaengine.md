---
title: "forwardperformancevanillaengine(3)"
name: "forwardperformancevanillaengine"
section: "3"
letter: "f"
url: "/docs/linux/man/3-forwardperformancevanillaengine/"
description: "QuantLib::ForwardPerformanceVanillaEngine – Forward performance engine for vanilla options"
---

<p>QuantLib::ForwardPerformanceVanillaEngine &#8211; Forward performance engine for vanilla options </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/forward/forwardperformanceengine.hpp&gt; </p>
<p> Inherits <code>ForwardVanillaEngine&lt; Engine &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ForwardPerformanceVanillaEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;) </p>
<p> void <code>calculate</code> () const </p>
<h3>Protected Member Functions</h3>
<p>void <code>getOriginalResults</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class Engine&gt; class QuantLib::ForwardPerformanceVanillaEngine&lt; Engine &gt;</h3>
<p>Forward performance engine for vanilla options </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</p>
<dt>*</p>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dl>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
