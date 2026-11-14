---
title: "equalprobabilitiesbinomialtree(3)"
name: "equalprobabilitiesbinomialtree"
section: "3"
letter: "e"
url: "/docs/linux/man/3-equalprobabilitiesbinomialtree/"
description: "QuantLib::EqualProbabilitiesBinomialTree – Base class for equal probabilities binomial tree."
---

<p>QuantLib::EqualProbabilitiesBinomialTree &#8211; Base class for equal probabilities binomial tree. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/lattices/binomialtree.hpp&gt; </p>
<p> Inherits <code>BinomialTree&lt; T &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>EqualProbabilitiesBinomialTree</code> (const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp;process, <code>Time</code> end, Size steps) </p>
<p> <code>Real</code> <code>underlying</code> (Size i, Size index) const </p>
<p> <code>Real</code> <code>probability</code> (Size, Size, Size) const </p>
<h3>Protected Attributes</h3>
<p><code>Real</code> <code>up_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class QuantLib::EqualProbabilitiesBinomialTree&lt; T &gt;</h3>
<p>Base class for equal probabilities binomial tree. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
