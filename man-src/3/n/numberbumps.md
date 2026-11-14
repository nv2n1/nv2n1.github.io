---
title: "numberbumps(3)"
name: "numberbumps"
section: "3"
letter: "n"
url: "/docs/linux/man/3-numberbumps/"
---

QuantLib::VegaBumpCollection -

<h2>Synopsis</h2>

<pre><code>
#include &lt;ql/models/marketmodels/pathwisegreeks/vegabumpcluster.hpp&gt;</code></pre>

<h3>Public Member Functions</h3>

<pre><code>VegaBumpCollection (const boost::shared_ptr&lt; MarketModel &gt; &amp;volStructure, bool allowFactorwiseBumping=true)



VegaBumpCollection (const std::vector&lt; VegaBumpCluster &gt; &amp;allBumps, const boost::shared_ptr&lt; MarketModel &gt; &amp;volStructure)



Size numberBumps () const



const boost::shared_ptr&lt; MarketModel &gt; &amp; associatedModel () const



const std::vector&lt; VegaBumpCluster &gt; &amp; allBumps () const



bool isFull () const



bool isNonOverlapping () const



bool isSensible () const</code></pre>

<h2>Detailed Description</h2>

There are too many pseudo-root elements to allow bumping them all independently so we cluster them together and then divide all elements into a collection of such clusters.

<h2>Author</h2>

Generated automatically by Doxygen for QuantLib from the source code.
