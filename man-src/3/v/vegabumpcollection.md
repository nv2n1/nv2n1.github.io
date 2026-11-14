---
title: "vegabumpcollection(3)"
name: "vegabumpcollection"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vegabumpcollection/"
description: "QuantLib::VegaBumpCollection –"
---

<p>QuantLib::VegaBumpCollection &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/pathwisegreeks/vegabumpcluster.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>VegaBumpCollection</code> (const boost::shared_ptr&lt; <code>MarketModel</code> &gt; &amp;volStructure, bool allowFactorwiseBumping=true) </p>
<p> <code>VegaBumpCollection</code> (const std::vector&lt; VegaBumpCluster &gt; &amp;allBumps, const boost::shared_ptr&lt; <code>MarketModel</code> &gt; &amp;volStructure) </p>
<p> Size <code>numberBumps</code> () const </p>
<p> const boost::shared_ptr&lt; <code>MarketModel</code> &gt; &amp; <code>associatedModel</code> () const </p>
<p> const std::vector&lt; VegaBumpCluster &gt; &amp; <code>allBumps</code> () const </p>
<p> bool <code>isFull</code> () const </p>
<p> bool <code>isNonOverlapping</code> () const </p>
<p> bool <code>isSensible</code> () const </p>
<h2>Detailed Description</h2>
<p>There are too many pseudo-root elements to allow bumping them all independently so we cluster them together and then divide all elements into a collection of such clusters. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
