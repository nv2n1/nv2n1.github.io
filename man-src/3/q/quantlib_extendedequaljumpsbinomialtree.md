---
title: "quantlib_extendedequaljumpsbinomialtree(3)"
name: "quantlib_extendedequaljumpsbinomialtree"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_extendedequaljumpsbinomialtree/"
description: "QuantLib::ExtendedEqualJumpsBinomialTree – Base class for equal jumps binomial tree."
---

<p>QuantLib::ExtendedEqualJumpsBinomialTree &#8211; Base class for equal jumps binomial tree. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/lattices/extendedbinomialtree.hpp&gt; </p>
<p> Inherits <code>ExtendedBinomialTree&lt; T &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ExtendedEqualJumpsBinomialTree</code> (const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp;process, <code>Time</code> end, Size steps) </p>
<p> <code>Real</code> <code>underlying</code> (Size i, Size index) const </p>
<p> <code>Real</code> <code>probability</code> (Size i, Size, Size branch) const </p>
<h3>Protected Member Functions</h3>
<p>virtual <code>Real</code> <code>probUp</code> (<code>Time</code> stepTime) const =0 </p>
<p> virtual <code>Real</code> <code>dxStep</code> (<code>Time</code> stepTime) const =0 </p>
<h3>Protected Attributes</h3>
<p><code>Real</code> <code>dx_</code> </p>
<p> <code>Real</code> <code>pu_</code> </p>
<p> <code>Real</code> <code>pd_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class QuantLib::ExtendedEqualJumpsBinomialTree&lt; T &gt;</h3>
<p>Base class for equal jumps binomial tree. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
