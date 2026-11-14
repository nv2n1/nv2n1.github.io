---
title: "quantlib_forwardmeasureprocess1d(3)"
name: "quantlib_forwardmeasureprocess1d"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_forwardmeasureprocess1d/"
description: "QuantLib::ForwardMeasureProcess1D – forward-measure 1-D stochastic process"
---

<p>QuantLib::ForwardMeasureProcess1D &#8211; forward-measure 1-D stochastic process </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/processes/forwardmeasureprocess.hpp&gt; </p>
<p> Inherits <code>QuantLib::StochasticProcess1D</code>. </p>
<p> Inherited by <code>HullWhiteForwardProcess</code>. </p>
<h3>Public Member Functions</h3>
<p>void <code>setForwardMeasureTime</code> (<code>Time</code>) </p>
<p> <code>Time</code> <code>getForwardMeasureTime</code> () const </p>
<h3>Protected Member Functions</h3>
<p><code>ForwardMeasureProcess1D</code> (<code>Time</code> T) </p>
<p> <code>ForwardMeasureProcess1D</code> (const boost::shared_ptr&lt; <code>discretization</code> &gt; &amp;) </p>
<h3>Protected Attributes</h3>
<p><code>Time</code> <code>T_</code> </p>
<h2>Detailed Description</h2>
<p>forward-measure 1-D stochastic process </p>
<p> 1-D stochastic process whose dynamics are expressed in the forward measure. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
