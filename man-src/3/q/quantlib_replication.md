---
title: "quantlib_replication(3)"
name: "quantlib_replication"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_replication/"
description: "QuantLib::Replication – Digital option replication strategy."
---

<p>QuantLib::Replication &#8211; Digital option replication strategy. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/replication.hpp&gt; </p>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>Sub</code>, <code>Central</code>, <code>Super</code> } </p>
<h3>Related Functions</h3>
<p>(Note that these are not member functions.)<br />
 std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, Replication::Type) </p>
<h2>Detailed Description</h2>
<p>Digital option replication strategy. </p>
<p> Specification of replication strategies used to price the embedded digital option in a digital coupon.</p>
<h2>Friends And Related Function Documentation</h2>
<h3>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, Replication::Type) [related]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
