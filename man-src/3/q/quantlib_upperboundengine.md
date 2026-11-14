---
title: "quantlib_upperboundengine(3)"
name: "quantlib_upperboundengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_upperboundengine/"
description: "QuantLib::UpperBoundEngine – Market-model engine for upper-bound estimation."
---

<p>QuantLib::UpperBoundEngine &#8211; Market-model engine for upper-bound estimation. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/callability/upperboundengine.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>UpperBoundEngine</code> (const boost::shared_ptr&lt; <code>MarketModelEvolver</code> &gt; &amp;evolver, const std::vector&lt; boost::shared_ptr&lt; <code>MarketModelEvolver</code> &gt; &gt; &amp;innerEvolvers, const <code>MarketModelMultiProduct</code> &amp;underlying, const MarketModelExerciseValue &amp;rebate, const <code>MarketModelMultiProduct</code> &amp;hedge, const MarketModelExerciseValue &amp;hedgeRebate, const ExerciseStrategy&lt; <code>CurveState</code> &gt; &amp;hedgeStrategy, <code>Real</code> initialNumeraireValue) </p>
<p> void <code>multiplePathValues</code> (<code>Statistics</code> &amp;stats, Size outerPaths, Size innerPaths) </p>
<p> std::pair&lt; <code>Real</code>, <code>Real</code> &gt; <code>singlePathValue</code> (Size innerPaths) </p>
<h2>Detailed Description</h2>
<p>Market-model engine for upper-bound estimation. </p>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>product and hedge must have the same rate times and exercise times</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
