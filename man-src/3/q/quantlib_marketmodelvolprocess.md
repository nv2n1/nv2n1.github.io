---
title: "quantlib_marketmodelvolprocess(3)"
name: "quantlib_marketmodelvolprocess"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_marketmodelvolprocess/"
description: "QuantLib::MarketModelVolProcess –"
---

<p>QuantLib::MarketModelVolProcess &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/evolvers/marketmodelvolprocess.hpp&gt; </p>
<p> Inherited by <code>SquareRootAndersen</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual Size <code>variatesPerStep</code> ()=0 </p>
<p> virtual Size <code>numberSteps</code> ()=0 </p>
<p> virtual void <code>nextPath</code> ()=0 </p>
<p> virtual Real <code>nextstep</code> (const std::vector&lt; Real &gt; &amp;variates)=0 </p>
<p> virtual Real <code>stepSd</code> () const =0 </p>
<p> virtual std::vector&lt; Real &gt; &amp; <code>stateVariables</code> () const =0 </p>
<p> virtual Size <code>numberStateVariables</code> () const =0 </p>
<h2>Detailed Description</h2>
<p>Displaced diffusion LMM with uncorrelated vol process. Called &#8216;Shifted BGM&#8217; with Heston vol by Brace in &#8216;Engineering BGM.&#8217; Vol process is an external input. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
