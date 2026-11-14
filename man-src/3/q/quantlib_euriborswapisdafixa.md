---
title: "quantlib_euriborswapisdafixa(3)"
name: "quantlib_euriborswapisdafixa"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_euriborswapisdafixa/"
description: "QuantLib::EuriborSwapIsdaFixA – EuriborSwapIsdaFixA index base class"
---

<p>QuantLib::EuriborSwapIsdaFixA &#8211; EuriborSwapIsdaFixA index base class </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/swap/euriborswap.hpp&gt; </p>
<p> Inherits <code>QuantLib::SwapIndex</code>. </p>
<h3>Public Member Functions</h3>
<p><code>EuriborSwapIsdaFixA</code> (const <code>Period</code> &amp;tenor, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h=<code>Handle</code>&lt; <code>YieldTermStructure</code> &gt;()) </p>
<h2>Detailed Description</h2>
<p>EuriborSwapIsdaFixA index base class </p>
<p> Euribor Swap indexes fixed by ISDA in cooperation with Reuters and Intercapital Brokers at 11am Frankfurt. Annual 30/360 vs 6M <code>Euribor</code>, 1Y vs 3M <code>Euribor</code>. Reuters page ISDAFIX2 or EURSFIXA=. </p>
<p> Further info can be found at &lt;<a rel="nofollow" href="http://www.isda.org/fix/isdafix.html">http://www.isda.org/fix/isdafix.html</a>&gt; or Reuters page ISDAFIX. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
