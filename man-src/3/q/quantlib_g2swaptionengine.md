---
title: "quantlib_g2swaptionengine(3)"
name: "quantlib_g2swaptionengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_g2swaptionengine/"
description: "QuantLib::G2SwaptionEngine – Swaption priced by means of the Black formula"
---

<p>QuantLib::G2SwaptionEngine &#8211; Swaption priced by means of the Black formula </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/swaption/g2swaptionengine.hpp&gt; </p>
<p> Inherits <code>GenericModelEngine&lt; G2, Swaption::arguments, Swaption::results &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>G2SwaptionEngine</code> (const boost::shared_ptr&lt; <code>G2</code> &gt; &amp;model, <code>Real</code> range, Size intervals) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Swaption priced by means of the Black formula </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>The engine assumes that the exercise date equals the start date of the passed swap.</dl>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
