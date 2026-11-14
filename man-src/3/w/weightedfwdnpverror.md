---
title: "weightedfwdnpverror(3)"
name: "weightedfwdnpverror"
section: "3"
letter: "w"
url: "/docs/linux/man/3-weightedfwdnpverror/"
description: "QuantLib::CmsMarket – set of CMS quotes"
---

<p>QuantLib::CmsMarket &#8211; set of CMS quotes </p>
<h2>Synopsis</h2>
<pre><code>void update ()</code></pre>
<p> Inherits <code>QuantLib::LazyObject</code>.</p>
<h3>Public Member Functions</h3>
<p><code>CmsMarket</code> (const std::vector&lt; <code>Period</code> &gt; &amp;swapLengths, const std::vector&lt; boost::shared_ptr&lt; <code>SwapIndex</code> &gt; &gt; &amp;swapIndexes, const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;iborIndex, const std::vector&lt; std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &gt; &amp;bidAskSpreads, const std::vector&lt; boost::shared_ptr&lt; <code>HaganPricer</code> &gt; &gt; &amp;pricers, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;discountingTS) </p>
<p> void <code>reprice</code> (const <code>Handle</code>&lt; <code>SwaptionVolatilityStructure</code> &gt; &amp;volStructure, <code>Real</code> meanReversion) </p>
<p> const std::vector&lt; <code>Period</code> &gt; &amp; <code>swapTenors</code> () const </p>
<p> const <code>Matrix</code> &amp; <code>impliedCmsSpreads</code> () </p>
<p> const <code>Matrix</code> &amp; <code>spreadErrors</code> () </p>
<p> <code>Matrix</code> <code>browse</code> () const </p>
<p> <code>Real</code> <code>weightedSpreadError</code> (const <code>Matrix</code> &amp;weights) </p>
<p> <code>Real</code> <code>weightedSpotNpvError</code> (const <code>Matrix</code> &amp;weights) </p>
<p> <code>Real</code> <code>weightedFwdNpvError</code> (const <code>Matrix</code> &amp;weights) </p>
<p> <code>Disposable</code>&lt; <code>Array</code> &gt; <code>weightedSpreadErrors</code> (const <code>Matrix</code> &amp;weights) </p>
<p> <code>Disposable</code>&lt; <code>Array</code> &gt; <code>weightedSpotNpvErrors</code> (const <code>Matrix</code> &amp;weights) </p>
<p> <code>Disposable</code>&lt; <code>Array</code> &gt; <code>weightedFwdNpvErrors</code> (const <code>Matrix</code> &amp;weights)<br />
 <code>LazyObject interface</code> </p>
<pre><code>void update ()</code></pre>
<h2>Detailed Description</h2>
<p>set of CMS quotes</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>LazyObject</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
