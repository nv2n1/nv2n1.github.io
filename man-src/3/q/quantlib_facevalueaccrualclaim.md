---
title: "quantlib_facevalueaccrualclaim(3)"
name: "quantlib_facevalueaccrualclaim"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_facevalueaccrualclaim/"
description: "QuantLib::FaceValueAccrualClaim – Claim on the notional of a reference security, including accrual."
---

<p>QuantLib::FaceValueAccrualClaim &#8211; <code>Claim</code> on the notional of a reference security, including accrual. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/claim.hpp&gt; </p>
<p> Inherits <code>QuantLib::Claim</code>. </p>
<h3>Public Member Functions</h3>
<p><code>FaceValueAccrualClaim</code> (const boost::shared_ptr&lt; <code>Bond</code> &gt; &amp;referenceSecurity) </p>
<p> Real <code>amount</code> (const <code>Date</code> &amp;d, Real notional, Real recoveryRate) const </p>
<h2>Detailed Description</h2>
<p><code>Claim</code> on the notional of a reference security, including accrual. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
