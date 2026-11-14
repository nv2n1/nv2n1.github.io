---
title: "analyticcapfloorengine-2(3)"
name: "analyticcapfloorengine-2"
section: "3"
letter: "a"
url: "/docs/linux/man/3-analyticcapfloorengine-2/"
description: "QuantLib::AnalyticCapFloorEngine – Analytic engine for cap/floor."
---

<p>QuantLib::AnalyticCapFloorEngine &#8211; Analytic engine for cap/floor. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/capfloor/analyticcapfloorengine.hpp&gt; </p>
<p> Inherits <code>GenericModelEngine&lt; AffineModel, CapFloor::arguments, CapFloor::results &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>AnalyticCapFloorEngine</code> (const boost::shared_ptr&lt; <code>AffineModel</code> &gt; &amp;model, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Analytic engine for cap/floor. </p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>AnalyticCapFloorEngine</code> (const boost::shared_ptr&lt; <code>AffineModel</code> &gt; &amp; model, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; termStructure = <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;())</h3>
<p><code>Note:</code></p>
<dl COMPACT>
<dd>the term structure is only needed when the short-rate model cannot provide one itself.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
