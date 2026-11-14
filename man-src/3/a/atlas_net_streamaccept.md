---
title: "atlas_net_streamaccept(3)"
name: "atlas_net_streamaccept"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_net_streamaccept/"
description: "Atlas::Net::StreamAccept – Negotiation of servers accepting a connection from a remote system."
---

<p>Atlas::Net::StreamAccept &#8211; Negotiation of servers accepting a connection from a remote system. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Stream.h">Stream.h</a>&gt; </p>
<p> Inherits <code>Atlas::Negotiate</code>. </p>
<h3>Public Member Functions</h3>
<p><code>StreamAccept</code> (const std::string &amp;name, std::iostream &amp;) </p>
<p> virtual void <code>poll</code> (bool can_read=true) </p>
<p> virtual State <code>getState</code> () </p>
<p> virtual <code>Atlas::Codec</code> * <code>getCodec</code> (<code>Atlas::Bridge</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Negotiation of servers accepting a connection from a remote system. </p>
<p> Used once a stream connection has been established by a client. This class listens to the list of <code>Atlas::Codec</code> types that the client offers, and then responds with the name of the <code>Atlas::Codec</code> which it thinks is most suitable. Once the server has told the client which <code>Atlas::Codec</code> to use, negotiation is flagged as complete, and this object can be deleted. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
