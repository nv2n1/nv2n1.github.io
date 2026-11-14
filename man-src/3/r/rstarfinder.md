---
title: "rstarfinder(3)"
name: "rstarfinder"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rstarfinder/"
description: "QuantLib::JamshidianSwaptionEngine – Jamshidian swaption engine."
---

<p>QuantLib::JamshidianSwaptionEngine &#8211; Jamshidian swaption engine. </p>
<h2>Synopsis</h2>
<pre><code>JamshidianSwaptionEngine (const boost::shared_ptr&lt; OneFactorAffineModel &gt; &amp;model, const Handle&lt; YieldTermStructure &gt; &amp;termStructure=Handle&lt; YieldTermStructure &gt;())



void calculate () const



Friends</code></pre>
<p> Inherits <code>GenericModelEngine&lt; OneFactorAffineModel, Swaption::arguments, Swaption::results &gt;</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>JamshidianSwaptionEngine (const boost::shared_ptr&lt; OneFactorAffineModel &gt; &amp;model, const Handle&lt; YieldTermStructure &gt; &amp;termStructure=Handle&lt; YieldTermStructure &gt;())



void calculate () const



Friends</code></pre>
<p> class <code>rStarFinder</code></p>
<h2>Detailed Description</h2>
<p>Jamshidian swaption engine. </p>
<p> <code>Warning</code></p>
<dl>
<dd>The engine assumes that the exercise date equals the start date of the passed swap.</dl>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>JamshidianSwaptionEngine</code> (const boost::shared_ptr&lt; <code>OneFactorAffineModel</code> &gt; &amp; model, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; termStructure = <code>Handle</code>&lt;<code>YieldTermStructure</code>&gt;())</h3>
<p><code>Note:</code></p>
<dl>
<dd>the term structure is only needed when the short-rate model cannot provide one itself.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
