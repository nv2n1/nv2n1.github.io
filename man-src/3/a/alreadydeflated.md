---
title: "alreadydeflated(3)"
name: "alreadydeflated"
section: "3"
letter: "a"
url: "/docs/linux/man/3-alreadydeflated/"
description: "QuantLib::MarketModelPathwiseMultiProduct – market-model pathwise product"
---

<p>QuantLib::MarketModelPathwiseMultiProduct &#8211; market-model pathwise product </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/pathwisemultiproduct.hpp&gt; </p>
<p> Inherited by <code>MarketModelPathwiseCoterminalSwaptionsDeflated</code>, <code>MarketModelPathwiseCoterminalSwaptionsNumericalDeflated</code>, <code>MarketModelPathwiseMultiCaplet</code>, <code>MarketModelPathwiseMultiDeflatedCap</code>, and MarketModelPathwiseMultiDeflatedCaplet. </p>
<h3>Public Member Functions</h3>
<p>virtual std::vector&lt; Size &gt; <code>suggestedNumeraires</code> () const =0 </p>
<p> virtual const <code>EvolutionDescription</code> &amp; <code>evolution</code> () const =0 </p>
<p> virtual std::vector&lt; <code>Time</code> &gt; <code>possibleCashFlowTimes</code> () const =0 </p>
<p> virtual Size <code>numberOfProducts</code> () const =0 </p>
<p> virtual Size <code>maxNumberOfCashFlowsPerProductPerStep</code> () const =0 </p>
<p> virtual bool <code>alreadyDeflated</code> () const =0 </p>
<p> virtual void <code>reset</code> ()=0<br />
 <i>during simulation put product at start of path </i><br />
 virtual bool <code>nextTimeStep</code> (const <code>CurveState</code> &amp;currentState, std::vector&lt; Size &gt; &amp;numberCashFlowsThisStep, std::vector&lt; std::vector&lt; MarketModelPathwiseMultiProduct::CashFlow &gt; &gt; &amp;cashFlowsGenerated)=0<br />
 <i>return value indicates whether path is finished, TRUE means done </i><br />
 virtual std::auto_ptr&lt; <code>MarketModelPathwiseMultiProduct</code> &gt; <code>clone</code> () const =0<br />
 <i>returns a newly-allocated copy of itself </i></p>
<h2>Detailed Description</h2>
<p>market-model pathwise product </p>
<p> This is the abstract base class that encapsulates the notion of a product: it contains the information that would be in the termsheet of the product. </p>
<p> It&#8217;s useful to have it be able to do several products simultaneously. The products would have to have the same underlying rate times of course. The class is therefore really encapsulating the notion of a multi-product. </p>
<p> For each time evolved to, it generates the cash flows associated to that time for the state of the yield curve. If one was doing a callable product then this would encompass the product and its exercise strategy. </p>
<p> This class differs from market-model multi-product in that it also returns the derivative of the pay-off with respect to each forward rate </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
