---
title: "multiproductonestep(3)"
name: "multiproductonestep"
section: "3"
letter: "m"
url: "/docs/linux/man/3-multiproductonestep/"
description: "QuantLib::MultiProductOneStep – Single-step market-model product."
---

<p>QuantLib::MultiProductOneStep &#8211; Single-step market-model product. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/products/multiproductonestep.hpp&gt; </p>
<p> Inherits <code>QuantLib::MarketModelMultiProduct</code>. </p>
<p> Inherited by OneStepCoinitialSwaps, OneStepCoterminalSwaps, OneStepForwards, and OneStepOptionlets. </p>
<h3>Public Member Functions</h3>
<p><code>MultiProductOneStep</code> (const std::vector&lt; <code>Time</code> &gt; &amp;rateTimes) </p>
<p> <code>MarketModelMultiProduct interface</code> </p>
<p> const <code>EvolutionDescription</code> &amp; <code>evolution</code> () const </p>
<p> std::vector&lt; Size &gt; <code>suggestedNumeraires</code> () const </p>
<h3>Protected Attributes</h3>
<p>std::vector&lt; <code>Time</code> &gt; <code>rateTimes_</code> </p>
<p> <code>EvolutionDescription</code> <code>evolution_</code> </p>
<h2>Detailed Description</h2>
<p>Single-step market-model product. </p>
<p> This is the abstract base class that encapsulates the notion of a <code>MarketModelMultiProduct</code> which can be evaluated in one step (aka Rebonato&#8217;s very long jump). </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
