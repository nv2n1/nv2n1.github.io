---
title: "direct(3)"
name: "direct"
section: "3"
letter: "d"
url: "/docs/linux/man/3-direct/"
description: "QuantLib::ExchangeRate – exchange rate between two currencies"
---

<p>QuantLib::ExchangeRate &#8211; exchange rate between two currencies </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/exchangerate.hpp&gt; </p>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>Direct</code>, <code>Derived</code> } </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code> </p>
<p> <code>ExchangeRate</code> () </p>
<p> <code>ExchangeRate</code> (const <code>Currency</code> &amp;source, const <code>Currency</code> &amp;target, Decimal rate) </p>
<p> <code>Inspectors</code> </p>
<p> const <code>Currency</code> &amp; <code>source</code> () const<br />
 <i>the source currency. </i><br />
 const <code>Currency</code> &amp; <code>target</code> () const<br />
 <i>the target currency. </i><br />
 <code>Type</code> <code>type</code> () const<br />
 <i>the type </i><br />
 Decimal <code>rate</code> () const<br />
 <i>the exchange rate (when available) </i></p>
<h3>Utility methods</h3>
<p><code>Money</code> <code>exchange</code> (const <code>Money</code> &amp;amount) const<br />
 <i>apply the exchange rate to a cash amount </i><br />
 static <code>ExchangeRate</code> <code>chain</code> (const <code>ExchangeRate</code> &amp;r1, const <code>ExchangeRate</code> &amp;r2)<br />
 <i>chain two exchange rates </i></p>
<h2>Detailed Description</h2>
<p>exchange rate between two currencies </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>application of direct and derived exchange rate is tested against calculations.</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>Type</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>Direct </i></p>
<dd>given directly by the user</p>
<dt><i>Derived </i></p>
<dd>derived from exchange rates between other currencies</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>ExchangeRate</code> (const <code>Currency</code> &amp; source, const <code>Currency</code> &amp; target, Decimal rate)</h3>
<p>the rate $ r $ is given with the convention that a unit of the source is worth $ r $ units of the target. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
