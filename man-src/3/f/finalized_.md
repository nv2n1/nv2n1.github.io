---
title: "finalized_(3)"
name: "finalized_"
section: "3"
letter: "f"
url: "/docs/linux/man/3-finalized_/"
description: "QuantLib::MarketModelComposite – Composition of two or more market-model products."
---

<h2 class="name">NAME</h2>
<p> QuantLib::MarketModelComposite &#8211; Composition of two or more market-model products. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/models/marketmodels/products/compositeproduct.hpp&gt; </p>
<p> Inherits <code>QuantLib::MarketModelMultiProduct</code>. </p>
<p> Inherited by <code>MultiProductComposite</code>, and <code>SingleProductComposite</code>. </p>
<h3>Public Member Functions</h3>
<p> <code>MarketModelMultiProduct interface</code> </p>
<p> const <code>EvolutionDescription</code> &amp; <code>evolution</code> () const </p>
<p> std::vector&lt; Size &gt; <code>suggestedNumeraires</code> () const </p>
<p> std::vector&lt; <code>Time</code> &gt; <code>possibleCashFlowTimes</code> () const </p>
<p> void <code>reset</code> ()<br />
 <i>during simulation put product at start of path </i> </p>
<p> <code>Composite facilities</code> </p>
<p> void <code>add</code> (const <code>Clone</code>&lt; <code>MarketModelMultiProduct</code> &gt; &amp;, <code>Real</code> multiplier=1.0) </p>
<p> void <code>subtract</code> (const <code>Clone</code>&lt; <code>MarketModelMultiProduct</code> &gt; &amp;, <code>Real</code> multiplier=1.0) </p>
<p> void <code>finalize</code> () </p>
<p> Size <code>size</code> () const </p>
<p> const <code>MarketModelMultiProduct</code> &amp; <code>item</code> (Size i) const </p>
<p> <code>MarketModelMultiProduct</code> &amp; <code>item</code> (Size i) </p>
<p> <code>Real</code> <code>multiplier</code> (Size i) const </p>
<h3>Protected Types</h3>
<p> typedef std::vector&lt; SubProduct &gt;::iterator <code>iterator</code> </p>
<p> typedef std::vector&lt; SubProduct &gt;::const_iterator <code>const_iterator</code> </p>
<h3>Protected Attributes</h3>
<p> std::vector&lt; SubProduct &gt; <code>components_</code> </p>
<p> std::vector&lt; <code>Time</code> &gt; <code>rateTimes_</code> </p>
<p> std::vector&lt; <code>Time</code> &gt; <code>evolutionTimes_</code> </p>
<p> <code>EvolutionDescription</code> <code>evolution_</code> </p>
<p> bool <code>finalized_</code> </p>
<p> Size <code>currentIndex_</code> </p>
<p> std::vector&lt; <code>Time</code> &gt; <code>cashflowTimes_</code> </p>
<p> std::vector&lt; std::vector&lt; <code>Time</code> &gt; &gt; <code>allEvolutionTimes_</code> </p>
<p> std::vector&lt; std::vector&lt; bool &gt; &gt; <code>isInSubset_</code> </p>
<h2>Detailed Description</h2>
<p> Composition of two or more market-model products. </p>
<p> Instances of this class build a market-model product by composing one or more subproducts. </p>
<p> <code>Precondition:</code></p>
<dl>
<dt>
<dd> All subproducts must have the same rate times.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
