---
title: "makeswaption(3)"
name: "makeswaption"
section: "3"
letter: "m"
url: "/docs/linux/man/3-makeswaption/"
description: "QuantLib::MakeSwaption – helper class"
---

<p>QuantLib::MakeSwaption &#8211; helper class </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/makeswaption.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>MakeSwaption</code> (const boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &amp;swapIndex, const <code>Period</code> &amp;optionTenor, <code>Rate</code> strike=<code>Null</code>&lt; <code>Rate</code> &gt;()) </p>
<p> <code>operator Swaption</code> () const </p>
<p> <code>operator boost::shared_ptr&lt; Swaption &gt;</code> () const </p>
<p> <code>MakeSwaption</code> &amp; <code>withSettlementType</code> (Settlement::Type delivery) </p>
<p> <code>MakeSwaption</code> &amp; <code>withOptionConvention</code> (<code>BusinessDayConvention</code> bdc) </p>
<p> <code>MakeSwaption</code> &amp; <code>withExerciseDate</code> (const <code>Date</code> &amp;) </p>
<p> <code>MakeSwaption</code> &amp; <code>withPricingEngine</code> (const boost::shared_ptr&lt; <code>PricingEngine</code> &gt; &amp;engine) </p>
<h2>Detailed Description</h2>
<p>helper class </p>
<p> This class provides a more comfortable way to instantiate standard market swaption. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
