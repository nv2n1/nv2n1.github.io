---
title: "quantlib_relativedateratehelper(3)"
name: "quantlib_relativedateratehelper"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_relativedateratehelper/"
description: "QuantLib::RelativeDateRateHelper – Rate helper with date schedule relative to the global evaluation date."
---

<p>QuantLib::RelativeDateRateHelper &#8211; Rate helper with date schedule relative to the global evaluation date. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/ratehelpers.hpp&gt; </p>
<p> Inherits <code>QuantLib::BootstrapHelper&lt; YieldTermStructure &gt;</code>. </p>
<p> Inherited by <code>BMASwapRateHelper</code>, <code>DepositRateHelper</code>, <code>FraRateHelper</code>, and <code>SwapRateHelper</code>. </p>
<h3>Public Member Functions</h3>
<p><code>RelativeDateRateHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;quote) </p>
<p> <code>RelativeDateRateHelper</code> (<code>Real</code> quote) </p>
<p> <code>Observer interface</code> </p>
<p> void <code>update</code> () </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>initializeDates</code> ()=0 </p>
<h3>Protected Attributes</h3>
<p><code>Date</code> <code>evaluationDate_</code> </p>
<h2>Detailed Description</h2>
<p>Rate helper with date schedule relative to the global evaluation date. </p>
<p> This class takes care of rebuilding the date schedule when the global evaluation date changes</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>BootstrapHelper&lt; TS &gt;</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
