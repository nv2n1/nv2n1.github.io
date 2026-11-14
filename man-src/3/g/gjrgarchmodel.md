---
title: "gjrgarchmodel(3)"
name: "gjrgarchmodel"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gjrgarchmodel/"
description: "QuantLib::GJRGARCHModel – GJR-GARCH model for the stochastic volatility of an asset."
---

<p>QuantLib::GJRGARCHModel &#8211; GJR-GARCH model for the stochastic volatility of an asset. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/equity/gjrgarchmodel.hpp&gt; </p>
<p> Inherits <code>QuantLib::CalibratedModel</code>. </p>
<h3>Public Member Functions</h3>
<p><code>GJRGARCHModel</code> (const boost::shared_ptr&lt; <code>GJRGARCHProcess</code> &gt; &amp;process) </p>
<p> <code>Real</code> <code>omega</code> () const </p>
<p> <code>Real</code> <code>alpha</code> () const </p>
<p> <code>Real</code> <code>beta</code> () const </p>
<p> <code>Real</code> <code>gamma</code> () const </p>
<p> <code>Real</code> <code>lambda</code> () const </p>
<p> <code>Real</code> <code>v0</code> () const </p>
<p> boost::shared_ptr&lt; <code>GJRGARCHProcess</code> &gt; <code>process</code> () const </p>
<h3>Protected Member Functions</h3>
<p>void <code>generateArguments</code> () </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>GJRGARCHProcess</code> &gt; <code>process_</code> </p>
<h2>Detailed Description</h2>
<p>GJR-GARCH model for the stochastic volatility of an asset. </p>
<p> References: </p>
<p> Glosten, L., Jagannathan, R., Runkle, D., 1993. Relationship between the expected value and the volatility of the nominal excess return on stocks. Journal of Finance 48, 1779-1801 </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>calibration is not implemented for GJR-GARCH</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
