---
title: "atlas_message_decoderbase(3)"
name: "atlas_message_decoderbase"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_message_decoderbase/"
description: "Atlas::Message::DecoderBase – Base class for decoders that take Atlas::Message::Object."
---

<p>Atlas::Message::DecoderBase &#8211; Base class for decoders that take Atlas::Message::Object. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/DecoderBase.h">DecoderBase.h</a>&gt; </p>
<p> Inherits <code>Atlas::Bridge</code>. </p>
<p> Inherited by <code>Atlas::Message::QueuedDecoder</code>, and <code>Atlas::Objects::ObjectsDecoder</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual void <code>streamBegin</code> ()<br />
 <i>Begin an </i><code>Atlas</code> stream.<br />
 virtual void <code>streamMessage</code> ()<br />
 <i>Start a message in an </i><code>Atlas</code> stream.<br />
 virtual void <code>streamEnd</code> ()<br />
 <i>Ends the </i><code>Atlas</code> stream.<br />
 virtual void <code>mapMapItem</code> (const std::string &amp;name)<br />
 <i>Starts a map object to the currently streamed map. </i><br />
 virtual void <code>mapListItem</code> (const std::string &amp;name)<br />
 <i>Starts a list object to the currently streamed map. </i><br />
 virtual void <code>mapIntItem</code> (const std::string &amp;name, long)<br />
 <i>Adds an integer to the currently streames map. </i><br />
 virtual void <code>mapFloatItem</code> (const std::string &amp;name, double)<br />
 <i>Adds a float to the currently streamed map. </i><br />
 virtual void <code>mapStringItem</code> (const std::string &amp;name, const std::string &amp;)<br />
 <i>Adds a string to the currently streamed map. </i><br />
 virtual void <code>mapEnd</code> ()<br />
 <i>Ends the currently streamed map. </i><br />
 virtual void <code>listMapItem</code> ()<br />
 <i>Starts a map object in the currently streamed list. </i><br />
 virtual void <code>listListItem</code> ()<br />
 <i>Starts a list object in the currently streamed list. </i><br />
 virtual void <code>listIntItem</code> (long)<br />
 <i>Adds an integer to the currently streames list. </i><br />
 virtual void <code>listFloatItem</code> (double)<br />
 <i>Adds a float to the currently streamed list. </i><br />
 virtual void <code>listStringItem</code> (const std::string &amp;)<br />
 <i>Adds a string to the currently streamed list. </i><br />
 virtual void <code>listEnd</code> ()<br />
 <i>Ends the currently streamed list. </i></p>
<h3>Protected Types</h3>
<p>enum <code>State</code> { <code>STATE_STREAM</code>, <code>STATE_MAP</code>, <code>STATE_LIST</code> }<br />
 <i>Our current decoding state. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>messageArrived</code> (const MapType &amp;obj)=0<br />
 <i>Override this &#8211; called when an object was received. </i></p>
<h3>Protected Attributes</h3>
<p>std::stack&lt; <code>State</code> &gt; <code>m_state</code><br />
 <i>The state stack. </i><br />
 std::stack&lt; MapType &gt; <code>m_maps</code><br />
 <i>The map stack. </i><br />
 std::stack&lt; ListType &gt; <code>m_lists</code><br />
 <i>The list stack. </i><br />
 std::stack&lt; std::string &gt; <code>m_names</code><br />
 <i>Names for maps and lists. </i></p>
<h2>Detailed Description</h2>
<p>Base class for decoders that take Atlas::Message::Object. </p>
<p> This class is passed to a codec as receiver bridge. It decodes a stream into Message::Object objects, and after completion calls the abstract <code>messageArrived()</code> method. This is to be overridden by base classes, which might, for instance, provide an object queue or a callback method for arrived messages. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Atlas::Bridge</code> </p>
<p> <code>Atlas::Codec</code> </p>
<p> Object</dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Stefanus Du Toit &lt;sdt [at] gmx.net&gt;</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
