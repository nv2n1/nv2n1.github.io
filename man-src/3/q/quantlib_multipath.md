---
title: "quantlib_multipath(3)"
name: "quantlib_multipath"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_multipath/"
description: "QuantLib::MultiPath – Correlated multiple asset paths."
---

<p>QuantLib::MultiPath &#8211; Correlated multiple asset paths. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/montecarlo/multipath.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>MultiPath</code> (Size nAsset, const <code>TimeGrid</code> &amp;timeGrid) </p>
<p> <code>MultiPath</code> (const std::vector&lt; <code>Path</code> &gt; &amp;multiPath) </p>
<p> <code>inspectors</code> </p>
<p> Size <code>assetNumber</code> () const </p>
<p> Size <code>pathSize</code> () const </p>
<p> <code>read/write access to components</code> </p>
<p> const <code>Path</code> &amp; <code>operator[]</code> (Size j) const </p>
<p> const <code>Path</code> &amp; <code>at</code> (Size j) const </p>
<p> <code>Path</code> &amp; <code>operator[]</code> (Size j) </p>
<p> <code>Path</code> &amp; <code>at</code> (Size j) </p>
<h2>Detailed Description</h2>
<p>Correlated multiple asset paths. </p>
<p> <code>MultiPath</code> contains the list of paths for each asset, i.e., multipath[j] is the path followed by the j-th asset. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
