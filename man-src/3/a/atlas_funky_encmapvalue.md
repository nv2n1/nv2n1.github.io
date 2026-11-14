---
title: "atlas_funky_encmapvalue(3)"
name: "atlas_funky_encmapvalue"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_funky_encmapvalue/"
description: "Atlas::Funky::EncMapValue – Encoder in map value state."
---

<p>Atlas::Funky::EncMapValue &#8211; Encoder in map value state. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/FEncoder.h">FEncoder.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>EncMapValue</code> (B &amp;<code>b</code>, const std::string &amp;<code>name</code>) </p>
<p> <code>EncMap</code>&lt; B, T &gt; <code>operator&lt;&lt;</code> (const <code>BeginMap</code> &amp;)<br />
 <i>Begin a map. </i><br />
 <code>EncList</code>&lt; B, T &gt; <code>operator&lt;&lt;</code> (const <code>BeginList</code> &amp;)<br />
 <i>Begin a list. </i><br />
 T <code>operator&lt;&lt;</code> (long i)<br />
 <i>Send an integer value. </i><br />
 T <code>operator&lt;&lt;</code> (double d)<br />
 <i>Send a double value. </i><br />
 T <code>operator&lt;&lt;</code> (const std::string &amp;s)<br />
 <i>Send a string value. </i><br />
 template&lt;typename Arg &gt; T <code>operator&lt;&lt;</code> (const Arg &amp;a)<br />
 <i>If the encoder supports it, send any kind of value. </i></p>
<h3>Protected Attributes</h3>
<p>B &amp; <code>b</code><br />
 <i>The bridge or encoder that is written to. </i><br />
 std::string <code>name</code><br />
 <i>The name of this item. </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;class B, class T&gt; class Atlas::Funky::EncMapValue&lt; B, T &gt;</h3>
<p>Encoder in map value state. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Atlas Funky Encoder</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
