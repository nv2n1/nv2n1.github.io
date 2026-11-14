---
title: "euriborswapisdafixb(3)"
name: "euriborswapisdafixb"
section: "3"
letter: "e"
url: "/docs/linux/man/3-euriborswapisdafixb/"
description: "QuantLib::EuriborSwapIsdaFixB – EuriborSwapIsdaFixB index base class"
---

<p>QuantLib::EuriborSwapIsdaFixB &#8211; EuriborSwapIsdaFixB index base class </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/swap/euriborswap.hpp&gt; </p>
<p> Inherits <code>QuantLib::SwapIndex</code>. </p>
<h3>Public Member Functions</h3>
<p><code>EuriborSwapIsdaFixB</code> (const <code>Period</code> &amp;tenor, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>EuriborSwapIsdaFixB index base class </p>
<p> Euribor Swap indexes fixed by ISDA in cooperation with Reuters and Intercapital Brokers at 12am Frankfurt. Annual 30/360 vs 6M <code>Euribor</code>, 1Y vs 3M <code>Euribor</code>. Reuters page ISDAFIX2 or EURSFIXB=. </p>
<p> Further info can be found at &lt;<a rel="nofollow" href="http://www.isda.org/fix/isdafix.html">http://www.isda.org/fix/isdafix.html</a>&gt; or Reuters page ISDAFIX. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
