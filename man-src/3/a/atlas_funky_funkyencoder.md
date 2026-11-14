---
title: "atlas_funky_funkyencoder(3)"
name: "atlas_funky_funkyencoder"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atlas_funky_funkyencoder/"
description: "Atlas::Funky::FunkyEncoder – The root encoder in ‘stream’ state."
---

<p>Atlas::Funky::FunkyEncoder &#8211; The root encoder in &#8216;stream&#8217; state. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/FEncoder.h">FEncoder.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>FunkyEncoder</code> (B &amp;<code>b</code>) </p>
<p> <code>EncMap</code>&lt; B, <code>FunkyEncoder</code> &gt; <code>operator&lt;&lt;</code> (const <code>BeginMap</code> &amp;)<br />
 <i>Start a message (as a map). </i><br />
 template&lt;typename Arg &gt; <code>FunkyEncoder</code>&lt; B &gt; <code>operator&lt;&lt;</code> (const Arg &amp;a)<br />
 <i>If the encoder supports it, send a different kind of message. </i></p>
<h3>Protected Attributes</h3>
<p>B &amp; <code>b</code><br />
 <i>The bridge or encoder that is written to. </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;class B&gt; class Atlas::Funky::FunkyEncoder&lt; B &gt;</h3>
<p>The root encoder in &#8216;stream&#8217; state. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>Atlas Funky Encoder</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Atlas-C++ from the source code.</p>
