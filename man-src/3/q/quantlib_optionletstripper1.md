---
title: "quantlib_optionletstripper1(3)"
name: "quantlib_optionletstripper1"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_optionletstripper1/"
description: "QuantLib::OptionletStripper1 –"
---

<p>QuantLib::OptionletStripper1 &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/optionlet/optionletstripper1.hpp&gt; </p>
<p> Inherits QuantLib::OptionletStripper. </p>
<h3>Public Member Functions</h3>
<p><code>OptionletStripper1</code> (const boost::shared_ptr&lt; <code>CapFloorTermVolSurface</code> &gt; &amp;, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;index, <code>Rate</code> switchStrikes=<code>Null</code>&lt; <code>Rate</code> &gt;(), Real accuracy=1.0e-6, Natural maxIter=100) </p>
<p> const <code>Matrix</code> &amp; <code>capFloorPrices</code> () const </p>
<p> const <code>Matrix</code> &amp; <code>capFloorVolatilities</code> () const </p>
<p> const <code>Matrix</code> &amp; <code>optionletPrices</code> () const </p>
<p> <code>Rate</code> <code>switchStrike</code> () const </p>
<p> <code>LazyObject interface</code> </p>
<p> void <code>performCalculations</code> () const </p>
<h2>Detailed Description</h2>
<p>Helper class to strip optionlet (i.e. caplet/floorlet) volatilities (a.k.a. forward-forward volatilities) from the (cap/floor) term volatilities of a <code>CapFloorTermVolSurface</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void performCalculations () const [virtual]</h3>
<p>This method must implement any calculations which must be (re)done in order to calculate the desired results. </p>
<p> Implements <code>LazyObject</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
