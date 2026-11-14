---
title: "quantlib_usdliborswapisdafixpm(3)"
name: "quantlib_usdliborswapisdafixpm"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_usdliborswapisdafixpm/"
description: "QuantLib::UsdLiborSwapIsdaFixPm – UsdLiborSwapIsdaFixPm index base class"
---

<p>QuantLib::UsdLiborSwapIsdaFixPm &#8211; UsdLiborSwapIsdaFixPm index base class </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/swap/usdliborswap.hpp&gt; </p>
<p> Inherits <code>QuantLib::SwapIndex</code>. </p>
<h3>Public Member Functions</h3>
<p><code>UsdLiborSwapIsdaFixPm</code> (const <code>Period</code> &amp;tenor, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>UsdLiborSwapIsdaFixPm index base class </p>
<p> USD Libor Swap indexes fixed by ISDA in cooperation with Reuters and Intercapital Brokers at 3pm New York. Semiannual 30/360 vs 3M <code>Libor</code>. Reuters page ISDAFIX1 or USDSFIXP=. </p>
<p> Further info can be found at &lt;<a rel="nofollow" href="http://www.isda.org/fix/isdafix.html">http://www.isda.org/fix/isdafix.html</a>&gt; or Reuters page ISDAFIX. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
