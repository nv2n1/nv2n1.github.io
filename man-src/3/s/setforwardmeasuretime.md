---
title: "setforwardmeasuretime(3)"
name: "setforwardmeasuretime"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setforwardmeasuretime/"
description: "QuantLib::ForwardMeasureProcess – forward-measure stochastic process"
---

<p>QuantLib::ForwardMeasureProcess &#8211; forward-measure stochastic process </p>
<h2>Synopsis</h2>
<pre><code>void setForwardMeasureTime (Time)



Time getForwardMeasureTime () const



Protected Member Functions</code></pre>
<p> Inherits <code>QuantLib::StochasticProcess</code>. Inherited by <code>G2ForwardProcess</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>void setForwardMeasureTime (Time)



Time getForwardMeasureTime () const



Protected Member Functions</code></pre>
<p> <code>ForwardMeasureProcess</code> (<code>Time</code> T) </p>
<p> <code>ForwardMeasureProcess</code> (const boost::shared_ptr&lt; <code>discretization</code> &gt; &amp;)</p>
<h3>Protected Attributes</h3>
<p><code>Time</code> <code>T_</code></p>
<h2>Detailed Description</h2>
<p>forward-measure stochastic process </p>
<p> stochastic process whose dynamics are expressed in the forward measure.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
