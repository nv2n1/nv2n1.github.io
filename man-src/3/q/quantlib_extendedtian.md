---
title: "quantlib_extendedtian(3)"
name: "quantlib_extendedtian"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_extendedtian/"
description: "QuantLib::ExtendedTian – Tian tree: third moment matching, multiplicative approach"
---

<p>QuantLib::ExtendedTian &#8211; Tian tree: third moment matching, multiplicative approach </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/lattices/extendedbinomialtree.hpp&gt; </p>
<p> Inherits <code>ExtendedBinomialTree&lt; ExtendedTian &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ExtendedTian</code> (const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp;, <code>Time</code> end, Size steps, Real strike) </p>
<p> Real <code>underlying</code> (Size i, Size index) const </p>
<p> Real <code>probability</code> (Size, Size, Size branch) const </p>
<h3>Protected Attributes</h3>
<p>Real <code>up_</code> </p>
<p> Real <code>down_</code> </p>
<p> Real <code>pu_</code> </p>
<p> Real <code>pd_</code> </p>
<h2>Detailed Description</h2>
<p>Tian tree: third moment matching, multiplicative approach </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
