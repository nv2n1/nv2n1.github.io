---
title: "binomialengine(3)"
name: "binomialengine"
section: "3"
letter: "b"
url: "/docs/linux/man/3-binomialengine/"
description: "ql/pricingengines/vanilla/binomialengine.hpp – Binomial option engine."
---

<h2 class="name">NAME</h2>
<p> ql/pricingengines/vanilla/binomialengine.hpp &#8211; Binomial option engine. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/methods/lattices/binomialtree.hpp&gt;<br />
 #include &lt;ql/methods/lattices/bsmlattice.hpp&gt;<br />
 #include &lt;ql/math/distributions/normaldistribution.hpp&gt;<br />
 #include &lt;ql/pricingengines/vanilla/discretizedvanillaoption.hpp&gt;<br />
 #include &lt;ql/pricingengines/greeks.hpp&gt;<br />
 #include &lt;ql/processes/blackscholesprocess.hpp&gt;<br />
 #include &lt;ql/termstructures/yield/flatforward.hpp&gt;<br />
 #include &lt;ql/termstructures/volatility/equityfx/blackconstantvol.hpp&gt; </p>
<h3>Classes</h3>
<p> class <code>BinomialVanillaEngine&lt; T &gt;</code><br />
 <i>Pricing engine for vanilla options using binomial trees. </i></p>
<h2>Detailed Description</h2>
<p> Binomial option engine. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
