---
title: "swapindex(3)"
name: "swapindex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-swapindex/"
description: "QuantLib::CmsCoupon – CMS coupon class."
---

<p>QuantLib::CmsCoupon &#8211; CMS coupon class. </p>
<h2>Synopsis</h2>
<pre><code>const boost::shared_ptr&lt; SwapIndex &gt; &amp; swapIndex () const</code></pre>
<p> Inherits <code>QuantLib::FloatingRateCoupon</code>.</p>
<h3>Public Member Functions</h3>
<p>const boost::shared_ptr&lt; SwapIndex &gt; &amp; swapIndex () const <code>Inspectors</code> </p>
<pre><code>const boost::shared_ptr&lt; SwapIndex &gt; &amp; swapIndex () const</code></pre>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;)</p>
<h2>Detailed Description</h2>
<p>CMS coupon class. </p>
<p> <code>Warning</code></p>
<dl>
<dd>This class does not perform any date adjustment, i.e., the start and end date passed upon construction should be already rolled to a business day.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
