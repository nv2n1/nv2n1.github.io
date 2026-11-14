---
title: "quantlib_squarerootandersen(3)"
name: "quantlib_squarerootandersen"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_squarerootandersen/"
description: "QuantLib::SquareRootAndersen –"
---

<p>QuantLib::SquareRootAndersen &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/evolvers/volprocesses/squarerootandersen.hpp&gt; </p>
<p> Inherits <code>QuantLib::MarketModelVolProcess</code>. </p>
<h3>Public Member Functions</h3>
<p><code>SquareRootAndersen</code> (Real meanLevel, Real reversionSpeed, Real volVar, Real v0, const std::vector&lt; Real &gt; &amp;evolutionTimes, Size numberSubSteps_, Real w1, Real w2, Real cutPoint=1.5) </p>
<p> virtual Size <code>variatesPerStep</code> () </p>
<p> virtual Size <code>numberSteps</code> () </p>
<p> virtual void <code>nextPath</code> () </p>
<p> virtual Real <code>nextstep</code> (const std::vector&lt; Real &gt; &amp;variates) </p>
<p> virtual Real <code>stepSd</code> () const </p>
<p> virtual std::vector&lt; Real &gt; &amp; <code>stateVariables</code> () const </p>
<p> virtual Size <code>numberStateVariables</code> () const </p>
<h2>Detailed Description</h2>
<p>Displaced diffusion LMM with uncorrelated vol process. Called &#8216;Shifted BGM&#8217; with Heston vol by Brace in &#8216;Engineering BGM.&#8217; Vol process is an external input. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
