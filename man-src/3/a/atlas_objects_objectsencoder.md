---
title: "atlas_objects_objectsencoder(3)"
name: "atlas_objects_objectsencoder"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_objects_objectsencoder/"
description: "Atlas::Objects::ObjectsEncoder – Objects hierarchy encoder."
---

<p>Atlas::Objects::ObjectsEncoder &#8211; <code>Objects</code> hierarchy encoder. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Encoder.h">Encoder.h</a>&gt; </p>
<p> Inherits <code>Atlas::EncoderBase</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ObjectsEncoder</code> (<code>Atlas::Bridge</code> &amp;b)<br />
 <i>The default constructor. </i><br />
 <code>~ObjectsEncoder</code> ()<br />
 <i>The default destructor. </i><br />
 template&lt;class ObjectData &gt; void <code>streamObjectsMessage</code> (const Atlas::Objects::SmartPtr&lt; ObjectData &gt; &amp;o)<br />
 <i>Send an object to the bridge. </i></p>
<h2>Detailed Description</h2>
<p><code>Objects</code> hierarchy encoder. </p>
<p> This Encoder can be used to send objects in the <code>Atlas::Objects</code> hierarchy to a certain <code>Bridge</code> (e.g. a codec). </p>
<p> Simply call the streamMessage member with a pointer to the object to be sent. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd>Atlas::Objects::Decoder</dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Stefanus Du Toit &lt;sdt [at] gmx.net&gt;</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>Atlas::Objects::ObjectsEncoder::ObjectsEncoder (<code>Atlas::Bridge</code> &amp; b) [inline, explicit]</h3>
<p>The default constructor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>b</i> The <code>Bridge</code> to which objects are to be sent.</dl>
<h2>Member Function Documentation</h2>
<h3>template&lt;class ObjectData &gt; void Atlas::Objects::ObjectsEncoder::streamObjectsMessage (const Atlas::Objects::SmartPtr&lt; ObjectData &gt; &amp; o) [inline]</h3>
<p>Send an object to the bridge. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>o</i> The object that is to be sent.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
