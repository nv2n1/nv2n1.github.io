---
title: "atlas_bridge(3)"
name: "atlas_bridge"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_bridge/"
description: "Atlas::Bridge – Atlas stream bridge."
---

<p>Atlas::Bridge &#8211; <code>Atlas</code> stream bridge. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Bridge.h">Bridge.h</a>&gt; </p>
<p> Inherited by <code>Atlas::Codec</code>, <code>Atlas::Formatter</code>, <code>Atlas::Message::DecoderBase</code>, DebugBridge, and DebugBridge. </p>
<h3>Public Member Functions</h3>
<p>virtual void <code>streamBegin</code> ()=0<br />
 <i>Begin an </i><code>Atlas</code> stream.<br />
 virtual void <code>streamMessage</code> ()=0<br />
 <i>Start a message in an </i><code>Atlas</code> stream.<br />
 virtual void <code>streamEnd</code> ()=0<br />
 <i>Ends the </i><code>Atlas</code> stream.<br />
 virtual void <code>mapMapItem</code> (const std::string &amp;name)=0<br />
 <i>Starts a map object to the currently streamed map. </i><br />
 virtual void <code>mapListItem</code> (const std::string &amp;name)=0<br />
 <i>Starts a list object to the currently streamed map. </i><br />
 virtual void <code>mapIntItem</code> (const std::string &amp;name, long)=0<br />
 <i>Adds an integer to the currently streames map. </i><br />
 virtual void <code>mapFloatItem</code> (const std::string &amp;name, double)=0<br />
 <i>Adds a float to the currently streamed map. </i><br />
 virtual void <code>mapStringItem</code> (const std::string &amp;name, const std::string &amp;)=0<br />
 <i>Adds a string to the currently streamed map. </i><br />
 virtual void <code>mapEnd</code> ()=0<br />
 <i>Ends the currently streamed map. </i><br />
 virtual void <code>listMapItem</code> ()=0<br />
 <i>Starts a map object in the currently streamed list. </i><br />
 virtual void <code>listListItem</code> ()=0<br />
 <i>Starts a list object in the currently streamed list. </i><br />
 virtual void <code>listIntItem</code> (long)=0<br />
 <i>Adds an integer to the currently streames list. </i><br />
 virtual void <code>listFloatItem</code> (double)=0<br />
 <i>Adds a float to the currently streamed list. </i><br />
 virtual void <code>listStringItem</code> (const std::string &amp;)=0<br />
 <i>Adds a string to the currently streamed list. </i><br />
 virtual void <code>listEnd</code> ()=0<br />
 <i>Ends the currently streamed list. </i></p>
<h2>Detailed Description</h2>
<p><code>Atlas</code> stream bridge. </p>
<p> This class presents an interface that accepts an <code>Atlas</code> stream. The stream begins with a call to <code>streamBegin()</code> and finishes with <code>streamEnd()</code>. While the <code>Bridge</code> is in this stream context, a message can be sent using <code>streamMessage()</code>. This puts the <code>Bridge</code> into a map context, allowing various map*Item() calls. </p>
<p> Several classes are derived from <code>Bridge</code>, the most notable of which is <code>Codec</code>, which accepts an <code>Atlas</code> stream for encoding and transmission. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Codec</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
