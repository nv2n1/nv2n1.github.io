---
title: "quantlib_discretizeddiscountbond(3)"
name: "quantlib_discretizeddiscountbond"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_discretizeddiscountbond/"
description: "QuantLib::DiscretizedDiscountBond – Useful discretized discount bond asset."
---

<p>QuantLib::DiscretizedDiscountBond &#8211; Useful discretized discount bond asset. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/discretizedasset.hpp&gt; </p>
<p> Inherits <code>QuantLib::DiscretizedAsset</code>. </p>
<h3>Public Member Functions</h3>
<p>void <code>reset</code> (Size size) </p>
<p> std::vector&lt; <code>Time</code> &gt; <code>mandatoryTimes</code> () const </p>
<h2>Detailed Description</h2>
<p>Useful discretized discount bond asset.</p>
<h2>Member Function Documentation</h2>
<h3>void reset (Size size) [virtual]</h3>
<p>This method should initialize the asset values to an <code>Array</code> of the given size and with values depending on the particular asset. </p>
<p> Implements <code>DiscretizedAsset</code>.</p>
<h3>std::vector&lt;<code>Time</code>&gt; mandatoryTimes () const [virtual]</h3>
<p>This method returns the times at which the numerical method should stop while rolling back the asset. Typical examples include payment times, exercise times and such. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The returned values are not guaranteed to be sorted.</dl>
<p> Implements <code>DiscretizedAsset</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
