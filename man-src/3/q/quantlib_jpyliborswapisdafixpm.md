---
title: "quantlib_jpyliborswapisdafixpm(3)"
name: "quantlib_jpyliborswapisdafixpm"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_jpyliborswapisdafixpm/"
description: "QuantLib::JpyLiborSwapIsdaFixPm – JpyLiborSwapIsdaFixPm index base class"
---

<p>QuantLib::JpyLiborSwapIsdaFixPm &#8211; JpyLiborSwapIsdaFixPm index base class </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/swap/jpyliborswap.hpp&gt; </p>
<p> Inherits <code>QuantLib::SwapIndex</code>. </p>
<h3>Public Member Functions</h3>
<p><code>JpyLiborSwapIsdaFixPm</code> (const <code>Period</code> &amp;tenor, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>JpyLiborSwapIsdaFixPm index base class </p>
<p> JPY Libor Swap indexes fixed by ISDA in cooperation with Reuters and Intercapital Brokers at 3pm Tokyo. Semiannual Act/365 vs 6M <code>Libor</code>. Reuters page ISDAFIX1 or JPYSFIXP=. </p>
<p> Further info can be found at &lt;<a rel="nofollow" href="http://www.isda.org/fix/isdafix.html">http://www.isda.org/fix/isdafix.html</a>&gt; or Reuters page ISDAFIX. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
