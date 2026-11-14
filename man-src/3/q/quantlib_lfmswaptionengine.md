---
title: "quantlib_lfmswaptionengine(3)"
name: "quantlib_lfmswaptionengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_lfmswaptionengine/"
description: "QuantLib::LfmSwaptionEngine – Libor forward model swaption engine based on Black formula"
---

<p>QuantLib::LfmSwaptionEngine &#8211; Libor forward model swaption engine based on Black formula </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/legacy/libormarketmodels/lfmswaptionengine.hpp&gt; </p>
<p> Inherits <code>GenericModelEngine&lt; LiborForwardModel, Swaption::arguments, Swaption::results &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LfmSwaptionEngine</code> (const boost::shared_ptr&lt; <code>LiborForwardModel</code> &gt; &amp;model, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountCurve) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Libor forward model swaption engine based on Black formula </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
