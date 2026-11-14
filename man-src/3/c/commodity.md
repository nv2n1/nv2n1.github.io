---
title: "commodity(3)"
name: "commodity"
section: "3"
letter: "c"
url: "/docs/linux/man/3-commodity/"
description: "ql/experimental/commodities/commodity.hpp – Commodity base class."
---

<h2 class="name">NAME</h2>
<p> ql/experimental/commodities/commodity.hpp &#8211; Commodity base class. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/instrument.hpp&gt;<br />
 #include &lt;ql/money.hpp&gt;<br />
 #include &lt;vector&gt;<br />
 #include &lt;ostream&gt; </p>
<h3>Classes</h3>
<p> class <code>Commodity</code><br />
 <i></i><code>Commodity</code> base class.</p>
<h3>Typedefs</h3>
<p> typedef std::map&lt; std::string, boost::any &gt; <code>SecondaryCosts</code> </p>
<p> typedef std::map&lt; std::string, Money &gt; <code>SecondaryCostAmounts</code> </p>
<p> typedef std::vector&lt; PricingError &gt; <code>PricingErrors</code> </p>
<h3>Functions</h3>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;out, const SecondaryCostAmounts &amp;secondaryCostAmounts) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;out, const PricingError &amp;error) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;out, const PricingErrors &amp;errors) </p>
<h2>Detailed Description</h2>
<p> Commodity base class. </p>
<p> commodity type</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
