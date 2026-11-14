---
title: "up_(3)"
name: "up_"
section: "3"
letter: "u"
url: "/docs/linux/man/3-up_/"
description: "QuantLib::ExtendedEqualProbabilitiesBinomialTree – Base class for equal probabilities binomial tree."
---

<p>QuantLib::ExtendedEqualProbabilitiesBinomialTree &#8211; Base class for equal probabilities binomial tree. </p>
<h2>Synopsis</h2>
<pre><code>virtual Real upStep (Time stepTime) const =0



Protected Attributes</code></pre>
<p> Inherits <code>ExtendedBinomialTree&lt; T &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ExtendedEqualProbabilitiesBinomialTree</code> (const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp;process, <code>Time</code> end, Size steps) </p>
<p> <code>Real</code> <code>underlying</code> (Size i, Size index) const </p>
<p> <code>Real</code> <code>probability</code> (Size, Size, Size) const</p>
<h3>Protected Member Functions</h3>
<pre><code>virtual Real upStep (Time stepTime) const =0



Protected Attributes</code></pre>
<p> <code>Real</code> <code>up_</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class QuantLib::ExtendedEqualProbabilitiesBinomialTree&lt; T &gt;</h3>
<p>Base class for equal probabilities binomial tree.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
