---
title: "atlas_message_queueddecoder(3)"
name: "atlas_message_queueddecoder"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_message_queueddecoder/"
description: "Atlas::Message::QueuedDecoder – Decoder that presents a queue of Atlas::Message::Element."
---

<p>Atlas::Message::QueuedDecoder &#8211; Decoder that presents a queue of <code>Atlas::Message::Element</code>. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/QueuedDecoder.h">QueuedDecoder.h</a>&gt; </p>
<p> Inherits <code>Atlas::Message::DecoderBase</code>. </p>
<h3>Public Member Functions</h3>
<p>size_t <code>queueSize</code> ()<br />
 <i>Retrieve the current size of the message queue. </i><br />
 const MapType <code>popMessage</code> ()<br />
 <i>Pop an object from the front of the message queue. </i><br />
 const MapType <code>frontMessage</code> ()<br />
 <i>Peek at the object at the front of the queue. </i><br />
 void <code>clearQueue</code> ()<br />
 <i>Clear the message queue. </i></p>
<h3>Protected Member Functions</h3>
<p>void <code>messageArrived</code> (const MapType &amp;obj)<br />
 <i>This adds a message to the queue. </i></p>
<h2>Detailed Description</h2>
<p>Decoder that presents a queue of <code>Atlas::Message::Element</code>. </p>
<p> This message decoder puts arrived objects into a queue and allows the application to pop them off the front of the queue, peek at the front of the queue, as well as checking to see how many objects are currently in the queue. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>DecoderBase</code> </p>
<p> <code>Element</code></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Stefanus Du Toit &lt;sdt [at] gmx.net&gt;</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
