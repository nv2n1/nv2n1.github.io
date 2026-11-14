---
title: "atlas_encoderbase(3)"
name: "atlas_encoderbase"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_encoderbase/"
description: "Atlas::EncoderBase – Base class forwarding to Atlas::Bridge as skeleton for other encoders."
---

<p>Atlas::EncoderBase &#8211; Base class forwarding to <code>Atlas::Bridge</code> as skeleton for other encoders. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/EncoderBase.h">EncoderBase.h</a>&gt; </p>
<p> Inherited by <code>Atlas::Message::Encoder</code>, and <code>Atlas::Objects::ObjectsEncoder</code>. </p>
<h3>Public Member Functions</h3>
<p><code>EncoderBase</code> (<code>Atlas::Bridge</code> &amp;b)<br />
 <i>You will need to implement this in subclasses. </i><br />
 void <code>streamBegin</code> () </p>
<p> void <code>streamMessage</code> () </p>
<p> void <code>streamEnd</code> () </p>
<p> void <code>mapMapItem</code> (const std::string &amp;name) </p>
<p> void <code>mapListItem</code> (const std::string &amp;name) </p>
<p> void <code>mapIntItem</code> (const std::string &amp;name, long i) </p>
<p> void <code>mapFloatItem</code> (const std::string &amp;name, double d) </p>
<p> void <code>mapStringItem</code> (const std::string &amp;name, const std::string &amp;s) </p>
<p> void <code>mapEnd</code> () </p>
<p> void <code>listMapItem</code> () </p>
<p> void <code>listListItem</code> () </p>
<p> void <code>listIntItem</code> (long i) </p>
<p> void <code>listFloatItem</code> (double d) </p>
<p> void <code>listStringItem</code> (const std::string &amp;s) </p>
<p> void <code>listEnd</code> () </p>
<h3>Protected Attributes</h3>
<p><code>Atlas::Bridge</code> &amp; <code>m_b</code><br />
 <i>The bridge that requests are forwarded to. </i></p>
<h2>Detailed Description</h2>
<p>Base class forwarding to <code>Atlas::Bridge</code> as skeleton for other encoders. </p>
<p> This class is useful when building your own encoders that work on top of <code>Bridge</code> (hence taking one as an argument). </p>
<p> It forwards all requests to a protected <code>Bridge</code> b, hence you can inherit from it and your encoder can be used as a <code>Bridge</code> (for instance, as argument to another encoder) without you needing to implement all these forwarding requests. </p>
<p> Of course your encoder does not have to inherit from <code>EncoderBase</code> &#8211; you could offer a completely different interface from that of bridge. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Bridge</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
