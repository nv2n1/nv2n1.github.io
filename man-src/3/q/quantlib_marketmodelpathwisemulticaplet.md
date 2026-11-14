---
title: "quantlib_marketmodelpathwisemulticaplet(3)"
name: "quantlib_marketmodelpathwisemulticaplet"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_marketmodelpathwisemulticaplet/"
description: "QuantLib::MarketModelPathwiseMultiCaplet – market-model pathwise caplet"
---

<p>QuantLib::MarketModelPathwiseMultiCaplet &#8211; market-model pathwise caplet </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/products/pathwise/pathwiseproductcaplet.hpp&gt; </p>
<p> Inherits <code>QuantLib::MarketModelPathwiseMultiProduct</code>. </p>
<h3>Public Member Functions</h3>
<p><code>MarketModelPathwiseMultiCaplet</code> (const std::vector&lt; <code>Time</code> &gt; &amp;rateTimes, const std::vector&lt; <code>Real</code> &gt; &amp;accruals, const std::vector&lt; <code>Time</code> &gt; &amp;paymentTimes, const std::vector&lt; <code>Rate</code> &gt; &amp;strikes) </p>
<p> virtual std::vector&lt; Size &gt; <code>suggestedNumeraires</code> () const </p>
<p> virtual const <code>EvolutionDescription</code> &amp; <code>evolution</code> () const </p>
<p> virtual std::vector&lt; <code>Time</code> &gt; <code>possibleCashFlowTimes</code> () const </p>
<p> virtual Size <code>numberOfProducts</code> () const </p>
<p> virtual Size <code>maxNumberOfCashFlowsPerProductPerStep</code> () const </p>
<p> virtual bool <code>alreadyDeflated</code> () const </p>
<p> virtual void <code>reset</code> ()<br />
 <i>during simulation put product at start of path </i><br />
 virtual bool <code>nextTimeStep</code> (const <code>CurveState</code> &amp;currentState, std::vector&lt; Size &gt; &amp;numberCashFlowsThisStep, std::vector&lt; std::vector&lt; MarketModelPathwiseMultiProduct::CashFlow &gt; &gt; &amp;cashFlowsGenerated)<br />
 <i>return value indicates whether path is finished, TRUE means done </i><br />
 virtual std::auto_ptr&lt; <code>MarketModelPathwiseMultiProduct</code> &gt; <code>clone</code> () const<br />
 <i>returns a newly-allocated copy of itself </i></p>
<h2>Detailed Description</h2>
<p>market-model pathwise caplet </p>
<p> implementation of path wise methodology for caplets, essentially a test class since we have better ways of computing <code>Greeks</code> of caplets </p>
<p> used in MarketModelTest::testPathwiseVegas and MarketModelTest::testPathwiseGreeks </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
