---
title: "atlas_message_encoder(3)"
name: "atlas_message_encoder"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_message_encoder/"
description: "Atlas::Message::Encoder – Encoder that transmits Atlas::Message::Element."
---

<p>Atlas::Message::Encoder &#8211; <code>Encoder</code> that transmits <code>Atlas::Message::Element</code>. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/MEncoder.h">MEncoder.h</a>&gt; </p>
<p> Inherits <code>Atlas::EncoderBase</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Encoder</code> (<code>Atlas::Bridge</code> &amp;) </p>
<p> void <code>streamMessageElement</code> (const MapType &amp;obj)<br />
 <i>Send a message (must be a map!) in stream state. </i><br />
 void <code>mapElementItem</code> (const std::string &amp;, const <code>Element</code> &amp;)<br />
 <i>Send an object as a map item. </i><br />
 void <code>mapElementMapItem</code> (const std::string &amp;, const MapType &amp;) </p>
<p> void <code>mapElementListItem</code> (const std::string &amp;, const ListType &amp;) </p>
<p> void <code>listElementItem</code> (const <code>Element</code> &amp;)<br />
 <i>Send an object as a list item. </i><br />
 void <code>listElementMapItem</code> (const MapType &amp;) </p>
<p> void <code>listElementListItem</code> (const ListType &amp;) </p>
<h2>Detailed Description</h2>
<p><code>Encoder</code> that transmits <code>Atlas::Message::Element</code>. </p>
<p> This encoder can be used to send <code>Atlas::Message::Element</code> objects representing full atlas messages. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Element</code> </p>
<p> <code>Atlas::Bridge</code> </p>
<p> <code>Atlas::EncoderBase</code></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Stefanus Du Toit &lt;sdt [at] gmx.net&gt;</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
