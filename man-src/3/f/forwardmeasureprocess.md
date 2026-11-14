---
title: "forwardmeasureprocess(3)"
name: "forwardmeasureprocess"
section: "3"
letter: "f"
url: "/docs/linux/man/3-forwardmeasureprocess/"
description: "QuantLib::ForwardMeasureProcess – forward-measure stochastic process"
---

<p>QuantLib::ForwardMeasureProcess &#8211; forward-measure stochastic process </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/processes/forwardmeasureprocess.hpp&gt; </p>
<p> Inherits <code>QuantLib::StochasticProcess</code>. </p>
<p> Inherited by <code>G2ForwardProcess</code>. </p>
<h3>Public Member Functions</h3>
<p>void <code>setForwardMeasureTime</code> (<code>Time</code>) </p>
<p> <code>Time</code> <code>getForwardMeasureTime</code> () const </p>
<h3>Protected Member Functions</h3>
<p><code>ForwardMeasureProcess</code> (<code>Time</code> T) </p>
<p> <code>ForwardMeasureProcess</code> (const boost::shared_ptr&lt; <code>discretization</code> &gt; &amp;) </p>
<h3>Protected Attributes</h3>
<p><code>Time</code> <code>T_</code> </p>
<h2>Detailed Description</h2>
<p>forward-measure stochastic process </p>
<p> stochastic process whose dynamics are expressed in the forward measure. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
