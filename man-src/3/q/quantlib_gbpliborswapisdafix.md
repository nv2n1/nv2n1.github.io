---
title: "quantlib_gbpliborswapisdafix(3)"
name: "quantlib_gbpliborswapisdafix"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_gbpliborswapisdafix/"
description: "QuantLib::GbpLiborSwapIsdaFix – GbpLiborSwapIsdaFix index base class"
---

<p>QuantLib::GbpLiborSwapIsdaFix &#8211; GbpLiborSwapIsdaFix index base class </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/swap/gbpliborswap.hpp&gt; </p>
<p> Inherits <code>QuantLib::SwapIndex</code>. </p>
<h3>Public Member Functions</h3>
<p><code>GbpLiborSwapIsdaFix</code> (const <code>Period</code> &amp;tenor, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>GbpLiborSwapIsdaFix index base class </p>
<p> GBP Libor Swap indexes fixed by ISDA in cooperation with Reuters and Intercapital Brokers at 11am London. Semiannual Actual/365F vs 6M <code>Libor</code>, 1Y Annual vs 3M <code>Libor</code>. Reuters page ISDAFIX4 or GBPSFIX=. </p>
<p> Further info can be found at &lt;<a rel="nofollow" href="http://www.isda.org/fix/isdafix.html">http://www.isda.org/fix/isdafix.html</a>&gt; or Reuters page ISDAFIX. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
