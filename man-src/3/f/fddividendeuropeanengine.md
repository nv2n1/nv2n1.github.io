---
title: "fddividendeuropeanengine(3)"
name: "fddividendeuropeanengine"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fddividendeuropeanengine/"
description: "ql/pricingengines/vanilla/fddividendeuropeanengine.hpp – finite-differences engine for European option with dividends"
---

<h2 class="name">NAME</h2>
<p> ql/pricingengines/vanilla/fddividendeuropeanengine.hpp &#8211; finite-differences engine for European option with dividends </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/instruments/dividendvanillaoption.hpp&gt;<br />
 #include &lt;ql/pricingengines/vanilla/fddividendengine.hpp&gt; </p>
<h3>Typedefs</h3>
<p> typedef FDEngineAdapter&lt; FDDividendEngine, DividendVanillaOption::engine &gt; <code>FDDividendEuropeanEngine</code><br />
 <i>Finite-differences pricing engine for dividend European options. </i><br />
 typedef FDEngineAdapter&lt; FDDividendEngineMerton73, DividendVanillaOption::engine &gt; <code>FDDividendEuropeanEngineMerton73</code> </p>
<p> typedef FDEngineAdapter&lt; FDDividendEngineShiftScale, DividendVanillaOption::engine &gt; <code>FDDividendEuropeanEngineShiftScale</code> </p>
<h2>Detailed Description</h2>
<p> finite-differences engine for European option with dividends </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
