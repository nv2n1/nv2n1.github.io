---
title: "atlas_funky_enclist(3)"
name: "atlas_funky_enclist"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_funky_enclist/"
description: "Atlas::Funky::EncList – Encoder in List state."
---

<p>Atlas::Funky::EncList &#8211; Encoder in List state. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/FEncoder.h">FEncoder.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>EncList</code> (B &amp;<code>b</code>) </p>
<p> <code>EncMap</code>&lt; B, <code>EncList</code>&lt; B, T &gt; &gt; <code>operator&lt;&lt;</code> (const <code>BeginMap</code> &amp;)<br />
 <i>Start a map. </i><br />
 <code>EncList</code>&lt; B, <code>EncList</code>&lt; B, T &gt; &gt; <code>operator&lt;&lt;</code> (const <code>BeginList</code> &amp;)<br />
 <i>Start a list. </i><br />
 <code>EncList</code>&lt; B, T &gt; <code>operator&lt;&lt;</code> (long i)<br />
 <i>Send an integer value. </i><br />
 <code>EncList</code>&lt; B, T &gt; <code>operator&lt;&lt;</code> (double d)<br />
 <i>Send a double value. </i><br />
 <code>EncList</code>&lt; B, T &gt; <code>operator&lt;&lt;</code> (const std::string &amp;s)<br />
 <i>Send a string value. </i><br />
 template&lt;typename Arg &gt; <code>EncList</code>&lt; B, T &gt; <code>operator&lt;&lt;</code> (const Arg &amp;a)<br />
 <i>If the encoder supports it, send any kind of value. </i><br />
 T <code>operator&lt;&lt;</code> (<code>EndList</code>)<br />
 <i>End this list. </i></p>
<h3>Protected Attributes</h3>
<p>B &amp; <code>b</code><br />
 <i>The bridge or encoder that is written to. </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;class B, class T&gt; class Atlas::Funky::EncList&lt; B, T &gt;</h3>
<p>Encoder in List state. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Atlas Funky Encoder</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
