---
title: "quantlib_extendedbinomialtree(3)"
name: "quantlib_extendedbinomialtree"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_extendedbinomialtree/"
description: "QuantLib::ExtendedBinomialTree – Binomial tree base class."
---

<p>QuantLib::ExtendedBinomialTree &#8211; Binomial tree base class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/lattices/extendedbinomialtree.hpp&gt; </p>
<p> Inherits <code>Tree&lt; T &gt;</code>. </p>
<h3>Public Types</h3>
<p>enum <code>Branches</code> { <code>branches</code> = 2 } </p>
<h3>Public Member Functions</h3>
<p><code>ExtendedBinomialTree</code> (const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp;process, <code>Time</code> end, Size steps) </p>
<p> Size <code>size</code> (Size i) const </p>
<p> Size <code>descendant</code> (Size, Size index, Size branch) const </p>
<h3>Protected Member Functions</h3>
<p><code>Real</code> <code>driftStep</code> (<code>Time</code> driftTime) const </p>
<h3>Protected Attributes</h3>
<p><code>Real</code> <code>x0_</code> </p>
<p> <code>Real</code> <code>driftPerStep_</code> </p>
<p> <code>Time</code> <code>dt_</code> </p>
<p> boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; <code>treeProcess_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class QuantLib::ExtendedBinomialTree&lt; T &gt;</h3>
<p>Binomial tree base class. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
