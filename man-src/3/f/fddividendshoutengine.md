---
title: "fddividendshoutengine(3)"
name: "fddividendshoutengine"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fddividendshoutengine/"
description: "ql/pricingengines/vanilla/fddividendshoutengine.hpp – base class for shout engine with dividends"
---

<h2 class="name">NAME</h2>
<p> ql/pricingengines/vanilla/fddividendshoutengine.hpp &#8211; base class for shout engine with dividends </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/instruments/dividendvanillaoption.hpp&gt;<br />
 #include &lt;ql/pricingengines/vanilla/fddividendengine.hpp&gt;<br />
 #include &lt;ql/pricingengines/vanilla/fdconditions.hpp&gt;<br />
 #include &lt;ql/methods/finitedifferences/shoutcondition.hpp&gt; </p>
<h3>Typedefs</h3>
<p> typedef FDEngineAdapter&lt; FDShoutCondition&lt; FDDividendEngine &gt;, DividendVanillaOption::engine &gt; <code>FDDividendShoutEngine</code><br />
 <i>Finite-differences shout engine with dividends. </i><br />
 typedef FDEngineAdapter&lt; FDShoutCondition&lt; FDDividendEngineMerton73 &gt;, DividendVanillaOption::engine &gt; <code>FDDividendShoutEngineMerton73</code> </p>
<p> typedef FDEngineAdapter&lt; FDShoutCondition&lt; FDDividendEngineShiftScale &gt;, DividendVanillaOption::engine &gt; <code>FDDividendShoutEngineShiftScale</code> </p>
<h2>Detailed Description</h2>
<p> base class for shout engine with dividends </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
