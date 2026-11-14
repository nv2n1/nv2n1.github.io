---
title: "atlas_net_negotiatehelper(3)"
name: "atlas_net_negotiatehelper"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_net_negotiatehelper/"
description: "Atlas::Net::NegotiateHelper – Negotiation of codecs and filters for an Atlas connection."
---

<p>Atlas::Net::NegotiateHelper &#8211; Negotiation of codecs and filters for an <code>Atlas</code> connection. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Stream.h">Stream.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>NegotiateHelper</code> (std::list&lt; std::string &gt; &amp;names) </p>
<p> bool <code>get</code> (std::string &amp;buf, const std::string &amp;header) </p>
<p> void <code>put</code> (std::string &amp;buf, const std::string &amp;header) </p>
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
