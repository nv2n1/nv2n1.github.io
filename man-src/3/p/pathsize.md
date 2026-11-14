---
title: "pathsize(3)"
name: "pathsize"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pathsize/"
description: "QuantLib::MultiPath – Correlated multiple asset paths."
---

<p>QuantLib::MultiPath &#8211; Correlated multiple asset paths. </p>
<h2>Synopsis</h2>
<pre><code>const Path &amp; operator[] (Size j) const



const Path &amp; at (Size j) const



Path &amp; operator[] (Size j)



Path &amp; at (Size j)</code></pre>
<h3>Public Member Functions</h3>
<p><code>MultiPath</code> (Size nAsset, const <code>TimeGrid</code> &amp;timeGrid) </p>
<p> <code>MultiPath</code> (const std::vector&lt; <code>Path</code> &gt; &amp;multiPath)<br />
 <code>inspectors</code> </p>
<p> Size <code>assetNumber</code> () const </p>
<p> Size <code>pathSize</code> () const<br />
 <code>read/write access to components</code> </p>
<pre><code>const Path &amp; operator[] (Size j) const



const Path &amp; at (Size j) const



Path &amp; operator[] (Size j)



Path &amp; at (Size j)</code></pre>
<h2>Detailed Description</h2>
<p>Correlated multiple asset paths. </p>
<p> <code>MultiPath</code> contains the list of paths for each asset, i.e., multipath[j] is the path followed by the j-th asset.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
