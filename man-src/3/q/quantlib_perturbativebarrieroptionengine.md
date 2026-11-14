---
title: "quantlib_perturbativebarrieroptionengine(3)"
name: "quantlib_perturbativebarrieroptionengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_perturbativebarrieroptionengine/"
description: "QuantLib::PerturbativeBarrierOptionEngine – perturbative barrier-option engine"
---

<p>QuantLib::PerturbativeBarrierOptionEngine &#8211; perturbative barrier-option engine </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/barrieroption/perturbativebarrieroptionengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::BarrierOption::engine</code>. </p>
<h3>Public Member Functions</h3>
<p><code>PerturbativeBarrierOptionEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;, <code>Natural</code> order=1, bool zeroGamma=false) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>perturbative barrier-option engine </p>
<p> This engine implements the approach described in &lt;<a rel="nofollow" href="http://www.econ.univpm.it/recchioni/finance/w3/">http://www.econ.univpm.it/recchioni/finance/w3/</a>&gt;. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
