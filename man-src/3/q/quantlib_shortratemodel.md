---
title: "quantlib_shortratemodel(3)"
name: "quantlib_shortratemodel"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_shortratemodel/"
description: "QuantLib::ShortRateModel – Abstract short-rate model class."
---

<p>QuantLib::ShortRateModel &#8211; Abstract short-rate model class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/model.hpp&gt; </p>
<p> Inherits <code>QuantLib::CalibratedModel</code>. </p>
<p> Inherited by <code>OneFactorModel</code>, and <code>TwoFactorModel</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ShortRateModel</code> (Size nArguments) </p>
<p> virtual boost::shared_ptr&lt; <code>Lattice</code> &gt; <code>tree</code> (const <code>TimeGrid</code> &amp;) const =0 </p>
<h2>Detailed Description</h2>
<p>Abstract short-rate model class. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
