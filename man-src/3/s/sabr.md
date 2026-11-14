---
title: "sabr(3)"
name: "sabr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sabr/"
description: "ql/termstructures/volatility/sabr.hpp – SABR functions."
---

<p>ql/termstructures/volatility/sabr.hpp &#8211; SABR functions. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/types.hpp&gt;</code></pre>
<h3>Functions</h3>
<p>Real <code>unsafeSabrVolatility</code> (Rate strike, Rate forward, Time expiryTime, Real alpha, Real beta, Real nu, Real rho) </p>
<p> Real <code>sabrVolatility</code> (Rate strike, Rate forward, Time expiryTime, Real alpha, Real beta, Real nu, Real rho) </p>
<p> void <code>validateSabrParameters</code> (Real alpha, Real beta, Real nu, Real rho)</p>
<h2>Detailed Description</h2>
<p>SABR functions.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
