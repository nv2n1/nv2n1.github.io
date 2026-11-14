---
title: "atlas_codec(3)"
name: "atlas_codec"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_codec/"
description: "Atlas::Codec – Atlas stream codec."
---

<p>Atlas::Codec &#8211; <code>Atlas</code> stream codec. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Codec.h">Codec.h</a>&gt; </p>
<p> Inherits <code>Atlas::Bridge</code>. </p>
<p> Inherited by Atlas::Codecs::Bach, Atlas::Codecs::Packed, and Atlas::Codecs::XML. </p>
<h3>Public Member Functions</h3>
<p>virtual void <code>poll</code> (bool can_get=true)=0 </p>
<h2>Detailed Description</h2>
<p><code>Atlas</code> stream codec. </p>
<p> This class presents an interface for sending and receiving <code>Atlas</code> messages. Each outgoing message is converted to a byte stream and piped through an optional chain of filters for compression or other transformations, then passed to a socket for transmission. Incoming messages are read from the socket, piped through the filters in the opposite direction and passed to a user specified <code>Bridge</code> callback class. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Bridge</code> </p>
<p> <code>Negotiate</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
