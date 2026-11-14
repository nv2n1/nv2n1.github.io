---
title: "extraterminbermudan(3)"
name: "extraterminbermudan"
section: "3"
letter: "e"
url: "/docs/linux/man/3-extraterminbermudan/"
description: "QuantLib::FDBermudanEngine – Finite-differences Bermudan engine."
---

<p>QuantLib::FDBermudanEngine &#8211; Finite-differences Bermudan engine. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/fdbermudanengine.hpp&gt; </p>
<p> Inherits VanillaOption::engine, and QuantLib::FDMultiPeriodEngine. </p>
<h3>Public Member Functions</h3>
<p><code>FDBermudanEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, Size timeSteps=100, Size gridPoints=100, bool timeDependent=false) </p>
<p> void <code>calculate</code> () const </p>
<h3>Protected Member Functions</h3>
<p>void <code>initializeStepCondition</code> () const </p>
<p> void <code>executeIntermediateStep</code> (Size) const </p>
<h3>Protected Attributes</h3>
<p><code>Real</code> <code>extraTermInBermudan</code> </p>
<h2>Detailed Description</h2>
<p>Finite-differences Bermudan engine. </p>
<p> <code>Examples: </code> </p>
<p> <code>EquityOption.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
