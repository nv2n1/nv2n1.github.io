---
title: "stock(3)"
name: "stock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stock/"
description: "QuantLib::Stock – Simple stock class."
---

<p>QuantLib::Stock &#8211; Simple stock class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/stock.hpp&gt; </p>
<p> Inherits <code>QuantLib::Instrument</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Stock</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;quote) </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i></p>
<h3>Protected Member Functions</h3>
<p>void <code>performCalculations</code> () const </p>
<h2>Detailed Description</h2>
<p>Simple stock class. </p>
<h2>Member Function Documentation</h2>
<h3>void performCalculations () const [protected, virtual]</h3>
<p>In case a pricing engine is <code>not</code> used, this method must be overridden to perform the actual calculations and set any needed results. In case a pricing engine is used, the default implementation can be used. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
