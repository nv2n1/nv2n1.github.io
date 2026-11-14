---
title: "quantlib_callability(3)"
name: "quantlib_callability"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_callability/"
description: "QuantLib::Callability – instrument callability"
---

<p>QuantLib::Callability &#8211; instrument callability </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/callabilityschedule.hpp&gt; </p>
<p> Inherits <code>QuantLib::Event</code>. </p>
<p> Inherited by <code>SoftCallability</code>. </p>
<h3>Classes</h3>
<p>class <code>Price</code><br />
 <i>amount to be paid upon callability </i></p>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>Call</code>, <code>Put</code> }<br />
 <i>type of the callability </i></p>
<h3>Public Member Functions</h3>
<p><code>Callability</code> (const <code>Price</code> &amp;price, <code>Type</code> type, const <code>Date</code> &amp;date) </p>
<p> const <code>Price</code> &amp; <code>price</code> () const </p>
<p> <code>Type</code> <code>type</code> () const </p>
<p> <code>Date</code> <code>date</code> () const<br />
 <i>returns the date at which the event occurs </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>instrument callability </p>
<p> <code>Examples: </code> </p>
<p> <code>CallableBonds.cpp</code>, and <code>ConvertibleBonds.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
