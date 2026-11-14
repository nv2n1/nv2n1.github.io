---
title: "fddividendamericanenginemerton73(3)"
name: "fddividendamericanenginemerton73"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fddividendamericanenginemerton73/"
description: "ql/pricingengines/vanilla/fddividendamericanengine.hpp – american engine with discrete deterministic dividends"
---

<p>ql/pricingengines/vanilla/fddividendamericanengine.hpp &#8211; american engine with discrete deterministic dividends </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/dividendvanillaoption.hpp&gt;<br />
 #include &lt;ql/pricingengines/vanilla/fddividendengine.hpp&gt;<br />
 #include &lt;ql/pricingengines/vanilla/fdconditions.hpp&gt; </p>
<h3>Typedefs</h3>
<p>typedef FDEngineAdapter&lt; FDAmericanCondition&lt; FDDividendEngine &gt;, DividendVanillaOption::engine &gt; <code>FDDividendAmericanEngine</code><br />
 <i>Finite-differences pricing engine for dividend American options. </i><br />
 typedef FDEngineAdapter&lt; FDAmericanCondition&lt; FDDividendEngineMerton73 &gt;, DividendVanillaOption::engine &gt; <code>FDDividendAmericanEngineMerton73</code> </p>
<p> typedef FDEngineAdapter&lt; FDAmericanCondition&lt; FDDividendEngineShiftScale &gt;, DividendVanillaOption::engine &gt; <code>FDDividendAmericanEngineShiftScale</code> </p>
<h2>Detailed Description</h2>
<p>american engine with discrete deterministic dividends </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
