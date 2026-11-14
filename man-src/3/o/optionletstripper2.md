---
title: "optionletstripper2(3)"
name: "optionletstripper2"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optionletstripper2/"
description: "QuantLib::OptionletStripper2 –"
---

<p>QuantLib::OptionletStripper2 &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/optionlet/optionletstripper2.hpp&gt; </p>
<p> Inherits QuantLib::OptionletStripper. </p>
<h3>Public Member Functions</h3>
<p><code>OptionletStripper2</code> (const boost::shared_ptr&lt; <code>OptionletStripper1</code> &gt; &amp;optionletStripper1, const <code>Handle</code>&lt; <code>CapFloorTermVolCurve</code> &gt; &amp;atmCapFloorTermVolCurve) </p>
<p> std::vector&lt; <code>Rate</code> &gt; <code>atmCapFloorStrikes</code> () const </p>
<p> std::vector&lt; <code>Real</code> &gt; <code>atmCapFloorPrices</code> () const </p>
<p> std::vector&lt; <code>Volatility</code> &gt; <code>spreadsVol</code> () const </p>
<p> <code>LazyObject interface</code> </p>
<p> void <code>performCalculations</code> () const </p>
<h2>Detailed Description</h2>
<p>Helper class to extend an <code>OptionletStripper1</code> object stripping additional optionlet (i.e. caplet/floorlet) volatilities (a.k.a. forward-forward volatilities) from the (cap/floor) At-The-Money term volatilities of a <code>CapFloorTermVolCurve</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void performCalculations () const [virtual]</h3>
<p>This method must implement any calculations which must be (re)done in order to calculate the desired results. </p>
<p> Implements <code>LazyObject</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
