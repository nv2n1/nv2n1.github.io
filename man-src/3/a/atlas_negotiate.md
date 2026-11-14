---
title: "atlas_negotiate(3)"
name: "atlas_negotiate"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_negotiate/"
description: "Atlas::Negotiate – Negotiation of codecs and filters for an Atlas connection."
---

<p>Atlas::Negotiate &#8211; Negotiation of codecs and filters for an <code>Atlas</code> connection. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Negotiate.h">Negotiate.h</a>&gt; </p>
<p> Inherited by <code>Atlas::Net::StreamAccept</code>, and <code>Atlas::Net::StreamConnect</code>. </p>
<h3>Public Types</h3>
<p>enum <code>State</code> { <code>IN_PROGRESS</code>, <code>SUCCEEDED</code>, <code>FAILED</code> } </p>
<h3>Public Member Functions</h3>
<p>virtual State <code>getState</code> ()=0 </p>
<p> virtual <code>Codec</code> * <code>getCodec</code> (<code>Bridge</code> &amp;)=0 </p>
<p> virtual void <code>poll</code> (bool can_get=true)=0 </p>
<h2>Detailed Description</h2>
<p>Negotiation of codecs and filters for an <code>Atlas</code> connection. </p>
<p> non blocking negotiation of Codecs and Filters requires a list of avalable Codecs and Filters, along with the name of sender and a Socket </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd>Connection </p>
<p> <code>Codec</code> </p>
<p> <code>Filter</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
