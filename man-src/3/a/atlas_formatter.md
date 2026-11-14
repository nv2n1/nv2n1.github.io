---
title: "atlas_formatter(3)"
name: "atlas_formatter"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_formatter/"
description: "Atlas::Formatter – Atlas stream formatter."
---

<p>Atlas::Formatter &#8211; <code>Atlas</code> stream formatter. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/Formatter.h">Formatter.h</a>&gt; </p>
<p> Inherits <code>Atlas::Bridge</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Formatter</code> (std::iostream &amp;s, <code>Atlas::Bridge</code> &amp;b) </p>
<p> virtual void <code>streamBegin</code> ()<br />
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
 <i>Ends the currently streamed list. </i><br />
 void <code>setSpacing</code> (int s) </p>
<h3>Protected Attributes</h3>
<p>std::iostream &amp; <code>m_stream</code> </p>
<p> <code>Bridge</code> &amp; <code>m_bridge</code> </p>
<p> int <code>m_indent</code> </p>
<p> int <code>m_spacing</code> </p>
<h2>Detailed Description</h2>
<p><code>Atlas</code> stream formatter. </p>
<p> This class implements the <code>Bridge</code> interface that accepts an <code>Atlas</code> stream. It copies the input stream to an output bridge, inserting formatting characters according to settings defined at construction time. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Codec</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
