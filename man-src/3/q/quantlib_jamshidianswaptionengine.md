---
title: "quantlib_jamshidianswaptionengine(3)"
name: "quantlib_jamshidianswaptionengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_jamshidianswaptionengine/"
description: "QuantLib::JamshidianSwaptionEngine – Jamshidian swaption engine."
---

<p>QuantLib::JamshidianSwaptionEngine &#8211; Jamshidian swaption engine. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/swaption/jamshidianswaptionengine.hpp&gt; </p>
<p> Inherits <code>GenericModelEngine&lt; OneFactorAffineModel, Swaption::arguments, Swaption::results &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>JamshidianSwaptionEngine</code> (const boost::shared_ptr&lt; <code>OneFactorAffineModel</code> &gt; &amp;model, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<p> void <code>calculate</code> () const </p>
<h3>Friends</h3>
<p>class <code>rStarFinder</code> </p>
<h2>Detailed Description</h2>
<p>Jamshidian swaption engine. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>The engine assumes that the exercise date equals the start date of the passed swap.</dl>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>JamshidianSwaptionEngine</code> (const boost::shared_ptr&lt; <code>OneFactorAffineModel</code> &gt; &amp; model, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; termStructure = <code>Handle</code>&lt;<code>YieldTermStructure</code>&gt;())</h3>
<p><code>Note:</code></p>
<dl COMPACT>
<dd>the term structure is only needed when the short-rate model cannot provide one itself.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
