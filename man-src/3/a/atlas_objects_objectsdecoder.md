---
title: "atlas_objects_objectsdecoder(3)"
name: "atlas_objects_objectsdecoder"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_objectsdecoder/"
description: "Atlas::Objects::ObjectsDecoder – Objects hierarchy decoder."
---

<p>Atlas::Objects::ObjectsDecoder &#8211; <code>Objects</code> hierarchy decoder. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Decoder.h">Decoder.h</a>&gt; </p>
<p> Inherits <code>Atlas::Message::DecoderBase</code>. </p>
<p> Inherited by <code>Atlas::Objects::Dispatcher</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ObjectsDecoder</code> (Factories *f=0)<br />
 <i>Constructor. </i><br />
 virtual <code>~ObjectsDecoder</code> ()<br />
 <i>Default destructor. </i><br />
 Factories * <code>factories</code> () const<br />
 <i>Factories accessor. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>messageArrived</code> (const Atlas::Message::MapType &amp;)<br />
 <i>Overridden by to retrieve the message from DecoderBase. </i><br />
 virtual void <code>objectArrived</code> (const Root &amp;obj)=0<br />
 <i>call right object*Arrived method </i></p>
<h3>Protected Attributes</h3>
<p>Factories * <code>m_factories</code> </p>
<h2>Detailed Description</h2>
<p><code>Objects</code> hierarchy decoder. </p>
<p> This decoder can be bound to a codec, will assemble incoming messages, check their type, convert them into the appropriate instance in the <code>Objects</code> hierarchy and call the relevant member functions, which subclasses can conveniently override to pick up the object. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd>Atlas::Objects::Encoder</dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Stefanus Du Toit &lt;sdt [at] gmx.net&gt;</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
