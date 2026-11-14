---
title: "quantlib_claim(3)"
name: "quantlib_claim"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_claim/"
description: "QuantLib::Claim – Claim associated to a default event."
---

<p>QuantLib::Claim &#8211; <code>Claim</code> associated to a default event. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/claim.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observable</code>, and <code>QuantLib::Observer</code>. </p>
<p> Inherited by <code>FaceValueAccrualClaim</code>, and <code>FaceValueClaim</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual Real <code>amount</code> (const <code>Date</code> &amp;defaultDate, Real notional, Real recoveryRate) const =0 </p>
<p> void <code>update</code> () </p>
<h2>Detailed Description</h2>
<p><code>Claim</code> associated to a default event.</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
