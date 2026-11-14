---
title: "quantlib_callability_price(3)"
name: "quantlib_callability_price"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_callability_price/"
description: "QuantLib::Callability::Price – amount to be paid upon callability"
---

<p>QuantLib::Callability::Price &#8211; amount to be paid upon callability </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/callabilityschedule.hpp&gt; </p>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>Dirty</code>, <code>Clean</code> } </p>
<h3>Public Member Functions</h3>
<p><code>Price</code> (<code>Real</code> amount, Type type) </p>
<p> <code>Real</code> <code>amount</code> () const </p>
<p> Type <code>type</code> () const </p>
<h2>Detailed Description</h2>
<p>amount to be paid upon callability </p>
<p> <code>Examples: </code> </p>
<p> <code>CallableBonds.cpp</code>, and <code>ConvertibleBonds.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
