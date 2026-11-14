---
title: "fdamericanengine(3)"
name: "fdamericanengine"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fdamericanengine/"
description: "ql/pricingengines/vanilla/fdamericanengine.hpp – Finite-differences American option engine."
---

<h2 class="name">NAME</h2>
<p> ql/pricingengines/vanilla/fdamericanengine.hpp &#8211; Finite-differences American option engine. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/instruments/oneassetoption.hpp&gt;<br />
 #include &lt;ql/pricingengines/vanilla/fdstepconditionengine.hpp&gt;<br />
 #include &lt;ql/pricingengines/vanilla/fdconditions.hpp&gt;<br />
 #include &lt;ql/methods/finitedifferences/fdtypedefs.hpp&gt; </p>
<h3>Typedefs</h3>
<p> typedef FDEngineAdapter&lt; FDAmericanCondition&lt; FDStepConditionEngine &gt;, OneAssetOption::engine &gt; <code>FDAmericanEngine</code><br />
 <i>Finite-differences pricing engine for American one asset options. </i></p>
<h2>Detailed Description</h2>
<p> Finite-differences American option engine. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
