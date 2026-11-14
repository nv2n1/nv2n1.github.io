---
title: "nextstep(3)"
name: "nextstep"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nextstep/"
description: "QuantLib::MarketModelVolProcess –"
---

<p>QuantLib::MarketModelVolProcess &#8211;</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/models/marketmodels/evolvers/marketmodelvolprocess.hpp&gt;</code></pre>
<p> Inherited by <code>SquareRootAndersen</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>virtual Size variatesPerStep ()=0



virtual Size numberSteps ()=0



virtual void nextPath ()=0



virtual Real nextstep (const std::vector&lt; Real &gt; &amp;variates)=0



virtual Real stepSd () const =0



virtual std::vector&lt; Real &gt; &amp; stateVariables () const =0



virtual Size numberStateVariables () const =0</code></pre>
<h2>Detailed Description</h2>
<p>Displaced diffusion LMM with uncorrelated vol process. Called &#8216;Shifted BGM&#8217; with Heston vol by Brace in &#8216;Engineering BGM.&#8217; Vol process is an external input.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
