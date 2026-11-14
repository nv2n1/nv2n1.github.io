---
title: "suggestednumeraires(3)"
name: "suggestednumeraires"
section: "3"
letter: "s"
url: "/docs/linux/man/3-suggestednumeraires/"
description: "QuantLib::MarketModelMultiProduct – market-model product"
---

<p>QuantLib::MarketModelMultiProduct &#8211; market-model product </p>
<h2>Synopsis</h2>
<pre><code>virtual std::vector&lt; Size &gt; suggestedNumeraires () const =0



virtual const EvolutionDescription &amp; evolution () const =0



virtual std::vector&lt; Time &gt; possibleCashFlowTimes () const =0



virtual Size numberOfProducts () const =0



virtual Size maxNumberOfCashFlowsPerProductPerStep () const =0



virtual void reset ()=0


during simulation put product at start of path


virtual bool nextTimeStep (const CurveState &amp;currentState, std::vector&lt; Size &gt; &amp;numberCashFlowsThisStep, std::vector&lt; std::vector&lt; CashFlow &gt; &gt; &amp;cashFlowsGenerated)=0


return value indicates whether path is finished, TRUE means done


virtual std::auto_ptr&lt; MarketModelMultiProduct &gt; clone () const =0


returns a newly-allocated copy of itself</code></pre>
<p> Inherited by CallSpecifiedMultiProduct, MarketModelCashRebate, <code>MarketModelComposite</code>, <code>MultiProductMultiStep</code>, and <code>MultiProductOneStep</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>virtual std::vector&lt; Size &gt; suggestedNumeraires () const =0



virtual const EvolutionDescription &amp; evolution () const =0



virtual std::vector&lt; Time &gt; possibleCashFlowTimes () const =0



virtual Size numberOfProducts () const =0



virtual Size maxNumberOfCashFlowsPerProductPerStep () const =0



virtual void reset ()=0


during simulation put product at start of path


virtual bool nextTimeStep (const CurveState &amp;currentState, std::vector&lt; Size &gt; &amp;numberCashFlowsThisStep, std::vector&lt; std::vector&lt; CashFlow &gt; &gt; &amp;cashFlowsGenerated)=0


return value indicates whether path is finished, TRUE means done


virtual std::auto_ptr&lt; MarketModelMultiProduct &gt; clone () const =0


returns a newly-allocated copy of itself</code></pre>
<h2>Detailed Description</h2>
<p>market-model product </p>
<p> This is the abstract base class that encapsulates the notion of a product: it contains the information that would be in the termsheet of the product. </p>
<p> It&#8217;s useful to have it be able to do several products simultaneously. The products would have to have the same underlying rate times of course. The class is therefore really encapsulating the notion of a multi-product. </p>
<p> For each time evolved to, it generates the cash flows associated to that time for the state of the yield curve. If one was doing a callable product then this would encompass the product and its exercise strategy.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
